import pytest
from pageObjects.yatra_launch_page import launchPage 
from testCases.conftest import setup
import time

@pytest.mark.usefixtures("setup")
class Test001_LaunchPage():
    
    # def test_launch_page_title(self):
        
    #     title = self.driver.title
    #     print(f"{title=}")
        
        
    def test_launch_page_url(self):
        
        url = self.driver.current_url
        print(f"{url=}")
        
        lp = launchPage(self.driver, self.wait)
        lp.depart_from()
        lp.going_to()
        lp.calender("22/04/2024")
        lp.click_search()
        
        