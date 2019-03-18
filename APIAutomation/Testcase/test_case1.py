import pytest
import allure
from API_Automation.Common import Request as br
from API_Automation.Config import  Config

class TestBasic():
    @allure.feature('登陆测试方法1')
    @pytest.mark.parametrize("das", [{'q': 'python'}, {'q': 'c'}])
    def test_douban_01(self,das):
    #conf=Config()
    #data=Basic()
        host=Config.test_get_hostConfig()
        data=Config.test_get_doubanhost()
        url='https://'+host+data
        getResponse = br.checkGetSubject(url, das)
