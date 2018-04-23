import pytest     # http://pytest.readthedocs.io/en/stable/


def defaultdateimage():
  return 'datetimeweb/date:latest'


def pytest_addoption(parser):
  parser.addoption('--dateimage',
                   action = 'store',
                   default = None,
                   help = 'Default:  %s' % ( defaultdateimage() ))


@pytest.fixture(scope = 'session')
def dateimage(request):
  image = request.config.getoption('--dateimage')
  return image if image is not None else defaultdateimage()
