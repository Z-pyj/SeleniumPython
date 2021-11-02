import pytest


@pytest.fixture(scope='function')
def login():
    print("开始连接数据库")


@pytest.fixture(scope="function")
def orderIm():
    return 2
