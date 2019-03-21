import configparser
import pytest

config = configparser.ConfigParser()

@pytest.fixture(scope='session')
def test_get_hostConfig():
    config.read("/Users/yuanyuan/PycharmProjects/pytest/API_Automation/Config/config.ini")
    # 获取它的所有section
    #sections = config.sections()
    hostconfig=config.get('qa-test','host')
    #print('\n--------------------\n',db)
    return hostconfig
