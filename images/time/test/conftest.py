import docker     # http://docker-py.readthedocs.io/en/stable/
import pytest     # http://pytest.readthedocs.io/en/stable/
import testinfra  # http://testinfra.readthedocs.io/en/stable/


def pytest_addoption(parser):
  parser.addoption('--image',
                   action = 'store',
                   default = None,
                   help = 'Default:  cs/time:latest')


@pytest.fixture(scope = 'session')
def image(request, defaultimage):
  image = request.config.getoption('--image')
  return image if image is not None else defaultimage


@pytest.fixture(scope = 'session')
def host(image):
  dockerclient = docker.from_env()
  container = dockerclient.containers.run(image,
                                          publish_all_ports = True,
                                          detach = True)
  yield testinfra.get_host("docker://" + container.id)
  container.remove(force = True)


@pytest.fixture(scope = 'session')
def hostcolonport(host, port):
  containerid = host.backend.name
  apiclient = docker.from_env().api
  d = apiclient.port(containerid, port)[0]
  ret = '%s:%s' % ( d['HostIp'], d['HostPort'] )
  return ret
