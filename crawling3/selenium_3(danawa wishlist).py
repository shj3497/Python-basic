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

""" 
    추가한 것!
    관심상품 전체를 클릭해주는 동작을 해줌
"""
wishlist1 = driver.find_element_by_id('myFolderMain_all')
wishlist1.click()
driver.implicitly_wait(2)

# page_source : 해당 페이지의 .html 긁어 오는듯
# page_source : 셀레늄이라는 패키지를 이용해서 해당 html을 긁어오는거고
# requests.get(url).text 로 해서 html을 긁어오는 방법이 있다.
# html코드를 긁어 왔다면 beautifulsoup을 이용해서 원하는 태그까지 찾아가는 과정을 하면 됨
html_src = driver.page_source
driver.close()
print(html_src[:500]) # 500글자까지 제한
print("\n")

# 관심상품 목록 HTML 페이지를 BeautifulSoup으로 파싱하기
soup = BeautifulSoup(html_src, 'html.parser')

# soup.select('원하는 정보')  # select('원하는 정보') -->  단 하나만 있더라도, 복수 가능한 형태로 되어있음
#   >> select() 를 사용할 경우 리스트로 담긴다.
# soup.select('태그명')
# soup.select('.클래스명')
# soup.select('상위태그명 > 하위태그명 > 하위태그명')
# soup.select('상위태그명.클래스명 > 하위태그명.클래스명')    # 바로 아래의(자식) 태그를 선택시에는 > 기호를 사용
# soup.select('상위태그명.클래스명 하~위태그명')              # 아래의(자손) 태그를 선택시에는   띄어쓰기 사용
# soup.select('상위태그명 > 바로아래태그명 하~위태그명')
# soup.select('.클래스명')
# soup.select('#아이디명')                  # 태그는 여러개에 사용 가능하나 아이디는 한번만 사용 가능함! ==> 선택하기 좋음
# soup.select('태그명.클래스명)
# soup.select('#아이디명 > 태그명.클래스명)
# soup.select('태그명[속성1=값1]')

# .select()를 사용할 경우 리스트로 담기기 때문에 리스의 순번 [0]을 붙여준거임
#wish_table = soup.select('table[class="tbl wish_tbl"]')[0]
""" 한번에 태그를 찾아가줌 """
wish_items = soup.select('div[id="wishProductListArea"] > table[class="tbl wish_tbl"] > tbody > tr')
# wish_items = wish_table.select('tbody > tr')
print(wish_items)

for item in wish_items:
    # <div>태그의 class 속성값이 tit인 .text를 가져온다.
    title = item.find('div', {'class' : 'tit'}).text
    # <span> 태그의 class 속성값이 price인 .text를 가져온다.
    # <span class="price">
    # <em class="num">48,000</em>원
    # </span>
    # em 태그로 안가져온 이유는 '원'이라는 글자가 em태그 바깥에 있음
    price = item.find('span', {'class': 'price'}).text
    link = item.find('a', href=re.compile('prod.danawa.com/info/')).get('href')
    print(title)
    print(price)
    print(link)
    print("\n")