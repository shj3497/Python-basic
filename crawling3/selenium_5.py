import time

from bs4 import BeautifulSoup
from selenium import webdriver


def download_bok_statistics_by_keyword():
    item_found = 0
    # 0이 아니라는 소리니까 true로 진행한다는건가?
    while not item_found:
        # 검색어 초기화
        keyword = ""
        # 키워드가 초기화 되어있으면 0이니까 true
        while len(keyword) == 0:
            keyword = str(input("검색할 항목을 입력하세요 : "))

        # 웹드라이버 실행
        driver = webdriver.Chrome("./driver/chromedriver")
        driver.implicitly_wait(3)
        driver.get("http://ecos.bok.or.kr/jsp/vis/keystat/#/key")
        time.sleep(5)

        # 맨위 타이틀 100대 통계지표
        # elements >> s 꼭 확인하셈
        # 같은 이름의 class 명이 반복되니까 elements 인듯?
        items1 = driver.find_elements_by_css_selector('a[class="ng-binding"]')
        items2 = driver.find_elements_by_css_selector('a[class="a-c1-list ng-binding"]')
        items3 = driver.find_elements_by_css_selector('a[class="a-c4-list ng-binding"]')
        driver.implicitly_wait(3)

        # item1은 배열이니까 [1]에 따라 item2 + item3이 되는건가?
        items = items1[1:] + items2 + items3
        print(items)

        # enumerate : 리스트가 있는경우 순서와 리스트의 값을 전달하는 기능
        # 이 함수는 순서가 있는 자료형(list, set ..)을 입력으로 받아서 인덱스 값을 포함하는 
        # enumerate 객체를 리턴한다.
        # idx라는 인덱스 값을 포함하기 위해서 enumerate 함수를 써줌
        for idx, item in enumerate(items):
            # 입력받은 키워드가 item에 포함된다면
            if keyword in item.text:
                # %s %s >> %(keyword, item.text)
                print("검색어 '%s'에 매칭되는 '%s' 통계지표를 검색중 ..." %(keyword, item.text))
                item.click()
                item_found = 1
                time.sleep(5)
                break
            # 인덱스번호로 검색리스트의 최대개수의 -1이 도달할 동안
            # 키워드에 따른 자료가 검색되지 않으면
            elif idx == (len(items) -1):
                print("검색어 '%s'에 대한 통계 지표가 존재하지 않습니다." %(keyword))
                driver.close()
                continue
            else:
                pass

    # 검색결과 로딩 HTML 웹 페이지를 파싱 -- 통계지표 테이블 양식을 정리
    html_src = driver.page_source
    soup = BeautifulSoup(html_src,'html.parser')
    driver.close()

    table_items = soup.find_all('td', {'class':'ng-binding'})
    date = [t.text for i, t in enumerate(table_items) if i % 3 == 0]
    value = [t.text for i, t in enumerate(table_items) if i % 3 == 1]
    change = [t.text for i, t in enumerate(table_items) if i % 3 == 2]

    # CSV 파일로 저장
    result_file = open('./data/bok_statistic_%s.csv' %(keyword), 'w')

    for i in range(len(date)):
        result_file.write("%s, %s, %s" %(date[i], value[i], change[i]))
        result_file.write("\n")

    result_file.close()
    print("키워드 '%s' 에 대한 통계 지표를 저장하였습니다." %keyword)

    return date, value, change

#함수 실행 - 'CD수익률' 통계지표를 별도로 검색, CSV 파일로 저장
result = download_bok_statistics_by_keyword()
print(result)