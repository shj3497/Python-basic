from pip._vendor import requests

urls = ["https://www.naver.com/", "https://www.python.org/"]
filename = "robots.txt"

# 각 사이트 url 주소의 robots.txt 라는 파일을 가져온다라는것 같은데..
# resp.text 에서의 
#   request.get(url) 는 요청 url의 응답 코드 반환
#   .text는 resp의 응답 코드에 따른 html 코드 출력
for url in urls:
    file_path = url + filename
    print("file_path : ", file_path)
    resp = requests.get(file_path)
    print("resp >>> : ", resp)
    print("#### resp.text ####", "\n", resp.text)
    print("\n")

"""
위키피디아 작성일시 : 2020.12.12 20:15
로봇 배제 표준(robots exclusion standard), 로봇 배제 프로토콜(robots exclusion protocol)은
웹 사이트에 로봇이 접근하는 것을 방지하기 위한 규약으로,
일반적으로 접근 제한에 대한 설명을 robots.txt 에 기술한다.

이 규약은 1994.6월에 처음 만들어졌고, 아직 이 규약에 대한 RFC는 없다.

이 규약은 권고안이며, 로봇이 robots.txt 파일을 읽고 접근을 중지하는 것을 목적으로한다.
하지만 접근 방지 설정을 하였다고 해도, 다른 사람들이 그 파일에 접근할 수는 있다.
robots.txt 파일은 항상 사이트의 루트 디렉토리에 위치해야 한다.

-- https://ko.wikipedia.org/wiki/  로봇 배제 표준

만약 모든 로봇에게 문서 접근을 허락하려면, robots.txt에 다음과 같이 입력하면 된다.
User-agent : *
Allow : /(루트 디렉토리)

모든 로봇을 차단하려면, robots.txt에 다음과 같이 입력하면 된다.
User-agent : *
Disallow : /

모든 로봇에 새 디렉토리 접근을 차단하려면, robots.txt에 다음과 같이 입력하면 된다.
User-agent : *
Disallow : /cgi-bin/
Disallow : /tmp/
Disallow : /junk/

모든 로봇에 특정 파일 접근을 차단하려면, robots.txt에 다음과 같이 입력하면 된다.
User-agent : *
Disallow : /directory/file.html
"""