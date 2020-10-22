from selenium import webdriver
import pytest
from Config.config import  TestData
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(params=["chrome"],scope='class')
def init_driver(request):
    #web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    web_driver=webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver=web_driver
    yield
    web_driver.close()