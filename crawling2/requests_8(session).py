from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

USER = "shj3497"
PASS = "rkawkrhrnak1!"

session = requests.session()
login_info = {
    "m_id":USER,
    "m_passwd":PASS
}

# hanbit.co.kr에 회원가입을 하고 회원가입한 id와 pw를 입력해야한다.

url_login = "https://www.hanbit.co.kr/member/login_proc.php"
# post방식일때 session 받아오기
res = session.post(url_login, data=login_info)
res.raise_for_status() # 오류가 발생하면 예외가 발생한다.

url_mypage = "https://www.hanbit.co.kr/myhanbit/myhanbit.html"
# get방식일때 session 받아오기
res = session.get(url_mypage)
res.raise_for_status() # 오류가 발생하면 예외가 발생한다.

soup = BeautifulSoup(res.text, 'html.parser')
mileage = soup.select_one('.mileage_section1 span').get_text()
ecoin = soup.select_one('.mileage_section2 span').get_text()
print("마일리지 >>> : ", mileage)
print("이코인 >>> : ", ecoin)
