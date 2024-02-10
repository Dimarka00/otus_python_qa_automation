import pytest

from helpers import print_blue, print_green


@pytest.fixture(scope='session', autouse=True)
def start_stop_rest_service(start_db):
    print_blue('Start Rest Service')
    yield
    print_blue('Stop Rest Service')


@pytest.fixture(scope='session', autouse=True)
def start_db():
    print_blue('Start Database')
    yield
    print_blue('Stop Database')


@pytest.fixture(scope='function', autouse=True)
def clean_data():
    yield
    print_green('Cleanup data')
