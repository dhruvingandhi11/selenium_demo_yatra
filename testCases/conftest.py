import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

# @pytest.fixture(scope="class")
@pytest.fixture(autouse=True, scope="class")
def setup(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-notifications")
    
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
                        options=chrome_options)
    # wait = WebDriverWait(driver, 10)
    
    driver.get("https://yatra.com/")
    driver.maximize_window()
    
    request.cls.driver = driver
    # request.cls.wait = wait
    yield
    driver.close()    
    