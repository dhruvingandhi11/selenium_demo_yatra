
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_driver import BaseDriver

class SearchFlightsResultPage(BaseDriver):
    
    one_stop_filter_xpath = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    two_stop_filter_xpath = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    non_stop_filter_xpath = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    search_flights_result = "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]"
    
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver
        # self.wait = wait

    def get_filter_by_one_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.one_stop_filter_xpath)
    def get_filter_by_two_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.two_stop_filter_xpath)
    def get_filter_by_non_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.non_stop_filter_xpath)
        
    
    def filter_flight_by_stop(self,by_stop):
        print("filtering flight**************")
        if by_stop == "1 Stop":
            self.get_filter_by_one_stop_icon().click()
            print("1 stop clicked")
            time.sleep(3)
        elif by_stop == "2 Stop":
            self.get_filter_by_two_stop_icon().click()
            print("2 stop clicked")
            time.sleep(3)
        elif by_stop == "Non Stop":
            self.get_filter_by_non_stop_icon().click()
            print("Non stop clicked")
            time.sleep(3)
        else:
            print("Invalid filter option")
            
    def get_search_flights_result(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.search_flights_result)
            
            
            
            
       