import pytest
from pageObjects.yatra_launch_page import launchPage 
from pageObjects.search_flights_result_page import *
from testCases.conftest import setup
import time
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class Test005_searchFlights():
    
    # def test_launch_page_title(self):
        
    #     title = self.driver.title
    #     print(f"{title=}")
        
        
    def test_launch_page_url(self):
        
        url = self.driver.current_url
        print(f"{url=}")
        
        lp = launchPage(self.driver)
        lp.depart_from()
        lp.going_to()
        lp.calender("22/04/2024")
        lp.click_search()
        lp.page_scroll()
        
        
        sf = SearchFlightsResultPage(self.driver)
        sf.filter_flight()
        
        all_stops1 = lp.wait_for_presence_of_all_elements(By.XPATH, 
                                             "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")
        print(f"{len(all_stops1)=}")
        
        ut = Utils()
        ut.assert_list_item_txt(all_stops1, "1 Stop")