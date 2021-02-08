from selenium import webdriver

driver = webdriver.Chrome('./driver/chromedriver')
driver.implicitly_wait(3)
driver.get("https://map.naver.com/")

keyword = "헬스장"

