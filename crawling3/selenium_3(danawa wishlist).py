import re

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("./driver/chromedriver")
driver.implicitly_wait(3)
driver.get("https://www.danawa.com/")

# 다나와 메인화면에 로그인 버튼을 누르는 작업 실행
login = driver.find_element_by_css_selector('li.my_page_service > a')
login.click()
driver.implicitly_wait(3)

# 아이디/비밀번호를 입력하고 로그인하기 버튼을 누르는 작업 실행
my_id = "shj3497"
my_pw = "rkawkrhrnak1!"

# 아이디를 입력하는 칸의 id값 : danawa-member-login-input-id
# .send_keys()로 파이썬에서 작성한 값을 보낸다.
driver.find_element_by_id('danawa-member-login-input-id').send_keys(my_id)
driver.implicitly_wait(2)
# driver.find_element_by_name('password').send_keys(my_pw)
driver.find_element_by_id('danawa-member-login-input-pwd').send_keys(my_pw)
driver.implicitly_wait(2)

# 나는 id로 찾아갔지만 css_selector로 <button>태그에 class 속성값이 btn_login 인
# 태그로 찾아서 들어갈 수도 있다.
driver.find_element_by_id('danawa-member-login-loginButton').click()
# driver.find_element_by_css_selector('button.btn_login').click()

# 관심상품 목록 html 페이지 가져오기
wishlist = driver.find_element_by_css_selector('li.interest_goods_service > a')
wishlist.click()
driver.implicitly_wait(2)

# page_source : 해당 페이지의 .html 긁어 오는듯
html_src = driver.page_source
driver.close()
print(html_src[:500]) # 500글자까지 제한
print("\n")

# 관심상품 목록 HTML 페이지를 BeautifulSoup으로 파싱하기
soup = BeautifulSoup(html_src, 'html.parser')
wish_table = soup.select('table[class="tbl wish_tbl"]')[0]
wish_items = wish_table.select('tbody > tr')

for item in wish_items:
    # <div>태그의 class 속성값이 tit인 .text를 가져온다.
    title = item.find('div', {'class' : 'tit'}).text
    # <span> 태그의 class 속성값이 price인 .text를 가져온다.
    price = item.find('span', {'class': 'price'}).text
    link = item.find('a', href=re.compile('prod.danawa.com/info/')).get('href')
    print(title)
    print(price)
    print(link)
    print("\n")