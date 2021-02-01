from selenium import webdriver

USER = "shj3497"
PASS = "fkspwm1!"

driver = webdriver.Chrome("./driver/chromedriver")
url_login = "https://nid.naver.com/nidlogin.login"
driver.get(url_login)
print("로그인 페이지에 접근")

e = driver.find_element_by_id("id")
e.clear()   # ?
e.send_keys(USER)
e = driver.find_element_by_id("pw")
e.clear()
e.send_keys(PASS)

form = driver.find_element_by_id("log.login")
# 얘는 로그인 버튼이 type="submit" 이라서 submit()을 해줌
# selenium_3 danawa사이트의 경우 <button>태그라서 .click()으로 로그인했음
form.submit()
print("로그인 버튼 클릭")

'''
driver.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")
products = driver.find_element_by_css_selector("ul.goods_group_list > li")
print(products)

for product in products:
    print("--", product.text)
'''