from selenium import webdriver

driver = webdriver.Chrome('./driver/chromedriver')
driver.implicitly_wait(3)
driver.get("https://map.kakao.com/")

keyword = "헬스장"

driver.find_element_by_id("search.keyword.query").send_keys(keyword)
driver.implicitly_wait(2)
driver.find_element_by_id("search.keyword.submit").click()
driver.implicitly_wait(2)

#healthlist = driver.find_element_by_css_selector("ul#info.search.place.list > li")
#print(healthlist)