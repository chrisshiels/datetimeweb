import pytest     # http://pytest.readthedocs.io/en/stable/


def defaulttimeimage():
  return 'datetimeweb/time:latest'


def pytest_addoption(parser):
  parser.addoption('--timeimage',
                   action = 'store',
                   default = None,
                   help = 'Default:  %s' % ( defaulttimeimage() ))


@pytest.fixture(scope = 'session')
def timeimage(request):
  image = request.config.getoption('--timeimage')
  return image if image is not None else defaulttimeimage()
