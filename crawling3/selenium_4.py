import time

from selenium import webdriver


def download_bok_statistic():
    driver = webdriver.Chrome("./driver/chromedriver")
    driver.implicitly_wait(3)
    
    # 서버 연결
    driver.get("http://ecos.bok.or.kr/jsp/vis/keystat/#/key")

    # 해당 페이지의 버튼을 선택
    # <a href data-ng-click=""><img src=".." alt="download"></a>
    # data-ng-click : Angular 에서 동작하는 click 이벤트 명인건가..
    excel_download = driver.find_element_by_css_selector("img[alt='download']")
    driver.implicitly_wait(3)

    # 버튼을 클릭하는 동작 실행
    excel_download.click()
    time.sleep(5)

    driver.close()
    print()

    return None

# 함수 실행 -- 100대 통계 지표 엑셀 다운로드
download_bok_statistic()