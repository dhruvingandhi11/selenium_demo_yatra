import pytest
from pageObjects.yatra_launch_page import launchPage 
from pageObjects.search_flights_result_page import *
from testCases.conftest import setup
import time
from utilities.utils import Utils
import softest

@pytest.mark.usefixtures("setup")
class Test005_searchFlights(softest.TestCase):
    
    # def test_launch_page_title(self):
        
    #     title = self.driver.title
    #     print(f"{title=}")
        
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = launchPage(self.driver)
        self.ut = Utils()
    
    def test_search_flights_one_stop(self):
        url = self.driver.current_url
        print(f"{url=}")
        search_flights_result = self.lp.searchFlights("singap", "duba", "22/04/2024")
        time.sleep(5)
        self.lp.page_scroll()
        search_flights_result.filter_flight_by_stop(by_stop="1 Stop")
        all_stops1 = search_flights_result.get_search_flights_result()
        print(f"{len(all_stops1)=}")
        self.ut.assert_list_item_txt(all_stops1, "1 Stop")
        
    def test_search_flights_two_stop(self):
        url = self.driver.current_url
        print(f"{url=}")
        search_flights_result = self.lp.searchFlights("singap", "Bangk", "26/04/2024")
        time.sleep(5)
        self.lp.page_scroll()
        search_flights_result.filter_flight_by_stop(by_stop="2 Stop")
        all_stops1 = search_flights_result.get_search_flights_result()
        print(f"{len(all_stops1)=}")
        self.ut.assert_list_item_txt(all_stops1, "2 Stops")