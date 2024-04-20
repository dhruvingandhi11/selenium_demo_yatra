
# from testCases.conftest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver
import time

from pageObjects.search_flights_result_page import SearchFlightsResultPage

class launchPage(BaseDriver):
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_linktext = "Logout"
    
    button_depart_from_xpath =  "//input[@name='flight_origin']"   
    txt_depart_from_xpath = "//input[@class='required_field cityPadRight ac_input origin_ac']"# //input[@class='ac_input origin_ac']
    lst_seach_result_xpath =  "//div[@class='viewport']//div[1]//li"  #"//div[@class='viewport']//div[1]//li//p[@class='ac_airport']"
    
    button_going_to_xpath = "//input[@name='flight_destination']"
    
    # temp_from = "//li[@class='initial-tab flex1 safariFix__field activeBox safariFix__field--fifty']//div[@class='ac_results origin_ac']//div[@class='viewport']//div[1]//li"
    # temp_to = "//li[@class='flex1 destAutoSugestField safariFix__field activeBox safariFix__field--fifty']//div[@class='ac_results dest_ac']//div[@class='viewport']//div[1]//li"
    
    temp_from = "//div[@class='ac_results origin_ac']//div[@class='viewport']//div[1]//li"
    temp_to = "//div[@class='ac_results dest_ac']//div[@class='viewport']//div[1]//li"
    calender_click_xpath = "//input[@id='BE_flight_origin_date']"
    calender_dates_xpath = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    
    srch_btn_xpath = "//input[@id='BE_flight_flsearch_btn']"
    
    
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver
        # self.wait = wait

    def get_page_title(self):
        # return "Hello -**********************"
        return self.driver.title
        
        
    def depart_from(self,city_name="singa"):
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_depart_from_xpath))).click()
        depart_from_element = self.wait_until_element_is_clickable(By.XPATH, self.button_depart_from_xpath)
        depart_from_element.click()
        time.sleep(2)
        depart_from_element.send_keys(city_name)
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_depart_from_xpath))).send_keys(city_name)
        time.sleep(2)
        search_elements = self.wait_for_presence_of_all_elements(By.XPATH, self.temp_from)
        # search_elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.temp_from)))
        print(f"{len(search_elements)=}")
        # time.sleep(2)
        click_selected_city_element = search_elements[0].click()    
            
    def going_to(self, city_name="san"):
        going_to_element = self.wait_until_element_is_clickable(By.XPATH, self.button_going_to_xpath)
        going_to_element.click()
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_going_to_xpath))).click()
        time.sleep(3)
        going_to_element.send_keys(city_name)
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_going_to_xpath))).send_keys(city_name)
        time.sleep(2)
        search_elements = self.wait_for_presence_of_all_elements(By.XPATH, self.temp_to)
        # search_elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.temp_to)))
        print(f"{len(search_elements)=}")
        
        # time.sleep(1)
        # for element in search_elements:
        #     print('***')
        #     print(element.text)
        #     if "Bang" in element.text:
        #         element.click()
        #         break
        
        search_elements[0].click()  
        
    def calender(self,search_date):
        calender_element = self.wait_until_element_is_clickable(By.XPATH, self.calender_click_xpath)
        calender_element.click()
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, self.calender_click_xpath))).click()
        # all_dates = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.calender_dates_xpath)))
        # all_dates = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.calender_dates_xpath)))
        all_dates = self.wait_for_presence_of_all_elements(By.XPATH, self.calender_dates_xpath)
        print(f"{len(all_dates)=}")
        for date in all_dates:
            print(date.get_attribute("data-date"))
            if date.get_attribute("data-date") == search_date:
                date.click()
                break
        
    def click_search(self):
        time.sleep(2)
        click_search_element = self.wait_until_element_is_clickable(By.XPATH, self.srch_btn_xpath)
        click_search_element.click()
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, self.srch_btn_xpath))).click()
        
        
    def searchFlights(self, departlocation, gointolocation, departuredate):
        self.depart_from(departlocation)
        self.going_to(gointolocation)
        self.calender(departuredate)    
        self.click_search()
        search_flights_result = SearchFlightsResultPage(self.driver)
        return search_flights_result
        
        
        
        
          