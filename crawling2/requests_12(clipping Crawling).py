import requests
from bs4 import BeautifulSoup

base_url = "https://news.google.com"
search_url = base_url + "/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&hl=ko&gl=KR&ceid=KR%3Ako"

resp = requests.get(search_url)
html_src = resp.text # .text html 코드로
soup = BeautifulSoup(html_src,'html.parser')

# 뉴스 아이템 블록을 선택
# div태그의 class 속성 값이 xrnccd인 것을 select 하여 배열로 저장
news_items = soup.select('div.xrnccd')
print("len >>> : ", len(news_items))
print(news_items[0])
print("\n")

# 각 뉴스 아이템에서 "링크, 제목, 내용, 출처, 등록일시" 데이터를 파싱(BeautifulSoup)
# div태그의 class 속성 값이 xrnccd인 것을 select 하여 배열로 저장한 것을
# [:3] 3개까지만 출력
for item in news_items[:3]:

    link = item.find('a', attrs={'class':'VDXfz'}).get('href')
    news_link = base_url + link[1:]
    print(news_link)

    news_content = item.find('span', attrs={'class': 'xBbh9'}).text
    print(news_content)

    news_agency = item.find('a', attrs={'class': 'wEwyrc AVN2gc uQIVzc Sksgp'}).text
    print(news_agency)

    news_reporting = item.find('time', attrs={'class':'WW6dff uQIVzc Sksgp'})
    # <time>태그의 datetime="2021-01-27T03:02:41+0000"
    # T를 기준으로 쪼개서 배열로 저장
    news_reporting_datetime = news_reporting.get('datetime').split('T')
    news_reporting_date = news_reporting_datetime[0] # 2021-01-27
    news_reporting_time = news_reporting_datetime[1][:-1] # 03:02:41 + 0000
    print(news_reporting_date, news_reporting_time)
    print("\n")

# 앞의 코드를 이용하여 구글 뉴스 클리핑 함수를 정의...
# 클리핑 : 특정 키워드를 포함하는 웹 크롤링
# 위에서 주석처리한 내용 중복됨
def google_new_clipping(url, limit=5):
    resp = requests.get(url)
    html_src = resp.text
    soup = BeautifulSoup(html_src,'html.parser')

    news_items = soup.select('div.xrnccd')

    # 각각의 변수명을 배열로 선언
    links=[]; titles=[]; contents=[]; agencies=[]; reporting_dates=[]; reporting_times=[];

    for item in news_items[:limit]:
        link = item.find('a', attrs={'class': 'VDXfz'}).get('href')
        news_link = base_url + link[1:]
        links.append(news_link)

        news_title = item.find('a', attrs={'class': 'DY5T1d'}).getText()
        titles.append(news_title)

        news_content = item.find('span', attrs={'class': 'xBbh9'}).text
        contents.append(news_content)

        news_agency = item.find('a', attrs={'class': 'wEwyrc AVN2gc uQIVzc Sksgp'}).text
        agencies.append(news_agency)

        news_reporting = item.find('time', attrs={'class': 'WW6dff uQIVzc Sksgp'})
        news_reporting_datetime = news_reporting.get('datetime').split('T')
        news_reporting_date = news_reporting_datetime[0]
        news_reporting_time = news_reporting_datetime[1][:-1]
        reporting_dates.append(news_reporting_date)
        reporting_times.append(news_reporting_time)

    result = {'link':links, 'title':titles, 'contents':contents, 'agency':agencies, 'date':reporting_dates, 'time':reporting_times}
    return result

# 함수를 실행하여 뉴스 목록 정리
news = google_new_clipping(search_url, 2)
print(news)