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
        lp.searchFlights("singap", "duba", "22/04/2024")
        time.sleep(5)
        
        lp.page_scroll()
        
        
        sf = SearchFlightsResultPage(self.driver)
        sf.filter_flight_by_stop(by_stop="1 Stop")
        
        
        all_stops1 = sf.get_search_flights_result()
        
        print(f"{len(all_stops1)=}")
        
        ut = Utils()
        ut.assert_list_item_txt(all_stops1, "1 Stop")