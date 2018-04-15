import json

import pytest     # http://pytest.readthedocs.io/en/stable/
import requests   # http://docs.python-requests.org/en/master/


@pytest.fixture(scope = 'session')
def defaultimage():
  return 'cs/time:latest'


@pytest.fixture(scope = 'session')
def port():
  return '7002'


def test_systeminfo(host):
  systeminfo = host.system_info
  assert systeminfo.type == 'linux'
  assert systeminfo.distribution == 'alpine'
  assert systeminfo.release == '3.7.0'


def test_executable(host):
  f = host.file('/time')
  assert f.exists
  assert f.is_file
  assert f.user == 'root'
  assert f.group == 'root'
  assert f.mode == 0o775


def test_request_time(hostcolonport):
  url = 'http://%s/time' % ( hostcolonport )
  request = requests.get(url)
  assert request.status_code == 200
  assert request.headers['content-type'] == 'text/json'
  assert request.encoding == 'ISO-8859-1'
  d = json.loads(request.text)
  assert sorted(d.keys()) == [ 'hostname', 'time', 'version' ]


def test_request_status(hostcolonport):
  url = 'http://%s/status' % ( hostcolonport )
  request = requests.get(url)
  assert request.status_code == 200
  assert request.headers['content-type'] == 'text/json'
  assert request.encoding == 'ISO-8859-1'
  d = json.loads(request.text)
  assert sorted(d.keys()) == [ 'ok' ]
