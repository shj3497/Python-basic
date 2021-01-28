from bs4 import BeautifulSoup

# 태그에 달린 id값(고유)으로도 내용을 찾을 수 있다.
html = """
<html>
    <body>
        <h1 id='title'>스크레핑이란?</h1>
        <p id="body">웹페이지를 분석하는것</p>
        <p>원하는 부분을 추출하는 것</p>
        <div id="table">
            <table>
                <tr>
                    <td>안녕하세요?</td>
                    <td>파이썬</td>
                </tr>
                <tr>
                    <td>안녕하세요?</td>
                    <td>자바</td>
                </tr>
            </table>
        </div>
    </body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
# html.parser
# "이 문자열은 단순한 텍스트가 아니라 html 구조에 맞게 작성되어있어.
# 그러니 너도 html 의 관점에서 이 문자열을 이해해줘" 라고 하는 것과 동일합니다.

title = soup.find(id='title')   # id값이 'title' 인 태그를 찾아라
body = soup.find(id='body')     # .find('body')라면 body 태그를 찾으라는 소리임
table = soup.find(id="table")   # .find(id='')으로 id를 찾으라고 지정해준거임
                                # .find(class_="")으로 class를 찾을 수 있다.
print('#title >>> : ',  title)
print('#body >>> : ', body)
print('#table >>> : ', table)

print()
print('.string') # .string은 태그를 제외하고 태그안에 담긴 내용을 보여준다.
print()

print('#title >>> : ', title.string)
print('#body >>> : ', body.string)
print('#table >>> : ', table.string) # table은 안됨