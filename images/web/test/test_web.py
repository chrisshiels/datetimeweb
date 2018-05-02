import json
import os
import re

import docker     # http://docker-py.readthedocs.io/en/stable/
import pytest     # http://pytest.readthedocs.io/en/stable/
import requests   # http://docs.python-requests.org/en/master/
import testinfra  # http://testinfra.readthedocs.io/en/stable/


@pytest.fixture(scope = 'session')
def host(dateimage, timeimage, webimage):
  suffix = os.getpid()
  networkname = 'datetimeweb' + str(suffix)
  dateimagename = 'date' + str(suffix)
  timeimagename = 'time' + str(suffix)
  webimagename =  'web' + str(suffix)

  dockerclient = docker.from_env()
  dockernetwork = dockerclient.networks.create(networkname)
  datecontainer = \
    dockerclient.containers.run(dateimage,
                                name = dateimagename,
                                detach = True,
                                network = dockernetwork.name)
  timecontainer = \
    dockerclient.containers.run(timeimage,
                                name = timeimagename,
                                detach = True,
                                network = dockernetwork.name)
  webcontainer = \
    dockerclient.containers.run(webimage,
                                name = webimagename,
                                detach = True,
                                network = dockernetwork.name,
                                publish_all_ports = True,
                                environment = {
                                  'DATEENDPOINT': '%s:7001' % ( dateimagename ),
                                  'TIMEENDPOINT': '%s:7002' % ( timeimagename )
                                 })
  yield testinfra.get_host('docker://' + webcontainer.id)
  for container in (datecontainer, timecontainer, webcontainer):
    container.remove(force = True)
  dockernetwork.remove()


@pytest.fixture(scope = 'session')
def port():
  return '7000'


@pytest.fixture(scope = 'session')
def hostcolonport(host, port):
  containerid = host.backend.name
  apiclient = docker.from_env().api
  d = apiclient.port(containerid, port)[0]
  ret = '%s:%s' % ( d['HostIp'], d['HostPort'] )
  return ret


def test_systeminfo(host):
  systeminfo = host.system_info
  assert systeminfo.type == 'linux'
  assert systeminfo.distribution == 'alpine'
  assert systeminfo.release == '3.7.0'


def test_executable(host):
  f = host.file('/web')
  assert f.exists
  assert f.is_file
  assert f.user == 'root'
  assert f.group == 'root'
  assert f.mode == 0o755


def test_process(host):
  process = host.process.get(pid = 1)
  assert re.match('/web -p 7000 -dateendpoint date[0-9]+:7001 -timeendpoint time[0-9]+:7002',
                  process.args)


def test_request_home(hostcolonport):
  url = 'http://%s/' % ( hostcolonport )
  request = requests.get(url)
  assert request.status_code == 200
  assert request.headers['content-type'] == 'text/plain'
  assert request.encoding == 'ISO-8859-1'
  lines = request.text.splitlines()
  assert re.match('^[^ ]+ [^ ]+$', lines[0])
  assert re.match('^[0-9]{8} - [^ ]+ [0-9]+\.[0-9]+\.[0-9]$', lines[1])
  assert re.match('^[0-9:]{8} - [^ ]+ [0-9]+\.[0-9]+\.[0-9]$', lines[2])


def test_request_status(hostcolonport):
  url = 'http://%s/status' % ( hostcolonport )
  request = requests.get(url)
  assert request.status_code == 200
  assert request.headers['content-type'] == 'text/plain'
  assert request.encoding == 'ISO-8859-1'
  d = json.loads(request.text)
  assert d == { 'ok': True }
