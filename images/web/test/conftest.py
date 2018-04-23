import pytest     # http://pytest.readthedocs.io/en/stable/


def defaultdateimage():
  return 'datetimeweb/date:latest'


def defaulttimeimage():
  return 'datetimeweb/time:latest'


def defaultwebimage():
  return 'datetimeweb/web:latest'


def pytest_addoption(parser):
  parser.addoption('--dateimage',
                   action = 'store',
                   default = None,
                   help = 'Default:  %s' % ( defaultdateimage() ))
  parser.addoption('--timeimage',
                   action = 'store',
                   default = None,
                   help = 'Default:  %s' % ( defaulttimeimage() ))
  parser.addoption('--webimage',
                   action = 'store',
                   default = None,
                   help = 'Default:  %s' % ( defaultwebimage() ))


@pytest.fixture(scope = 'session')
def dateimage(request):
  image = request.config.getoption('--dateimage')
  return image if image is not None else defaultdateimage()


@pytest.fixture(scope = 'session')
def timeimage(request):
  image = request.config.getoption('--timeimage')
  return image if image is not None else defaulttimeimage()


@pytest.fixture(scope = 'session')
def webimage(request):
  image = request.config.getoption('--webimage')
  return image if image is not None else defaultwebimage()
