from selenium import webdriver

driver = webdriver.Chrome("./driver/chromedriver")
driver.get("https://google.com")

# execute_script : 자바스크립트 사용가능
r = driver.execute_script("return 100+50")
print(r)