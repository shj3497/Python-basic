from selenium import webdriver

driver = webdriver.Chrome('./driver/chromedriver')
driver.implicitly_wait(3)   # 3초 기다리세요
# driver.get('url')으로 url에 접속한다.
driver.get("https://www.danawa.com/")

# 다나와 메인화면의 로그인 버튼을 누르는 작업 실행
# find_element_by_css_selector로 찾는 이유가 있을까?
# >> <li>태그에는 class나 id값이 없기 때문에 css_selector로 태그를 찾아 들어간다.
# <li> 태그의 class속성 값 my_page_service의 자식태그중 <a> 태그를 지정
login = driver.find_element_by_css_selector('li.my_page_service > a')
print("html 요소 : ", login)
print("태그이름 : ", login.tag_name)
print("문자열 : ", login.text)
print("href 속성 : ", login.get_attribute('href'))

# click() 이벤트 동작하도록 버튼을 누른다.
login.click()
driver.implicitly_wait(3)

# 아이디/비밀번호를 입력하고 로그인하기 버튼을 누르는 작업을 실행한다.
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