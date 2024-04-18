
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_driver import BaseDriver

class SearchFlightsResultPage(BaseDriver):
    
    stop_filter_xpath = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    # stop_filter_xpath = "//p[@class='font-lightgrey bold'][contains(text(),'1')]"
    
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver
        # self.wait = wait

    
    def filter_flight(self):
        print("filtering flight**************")
        self.driver.find_element(By.XPATH, self.stop_filter_xpath).click()
        time.sleep(4)