from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1>스크레이핑이란?</h1>
        <p>웹 페이지를 분석하는 것</p>
        <p>원하는 부분을 추출하는 것</p>
    </body>
</html>
"""
# 그러니까 한마디로 html페이지에서 태그를 기준으로 데이터를 긁어올수 있다는 소리인데..
# 그렇다면 태그들을 알기 위해서 urllib에서 데이터를 확인해서 태그들을 확인해야겠네
soup = BeautifulSoup(html, 'html.parser')
print(soup)
h1 = soup.html.body.h1
print("h1 >>> : ", h1)
# p1 = h1.next_sibling.next_sibling : <h1>태그 다음을 불러왔음 형제호출하는것처럼 해서
p1 = soup.html.body.p # 최상위 부모태그로부터 자식태그를 지정해서 불러왔는데 <p>태그는 두개인데 첫번째 <p>태그만 호출되는듯
print("p1 >>> : ", p1)
p2 = p1.next_sibling.next_sibling
print("p2 >>> : ", p2)
# 첫 번째의 next_sibling 에서는 </p> 뒤에 이있는 줄 바꿈 또는
# 공백이 추출되는 데 이것도 하난의 노드(엘리먼트)로 보기 때문에
# next_sibling을 한 번 더 사용해서 추출 한다.
# 그러니까 <p></p> 하고 끝났는데 h1, p1과는 다르게 p2는 next_sibling 으로 불렀는데
# <p>태그는 자동으로 줄바꿈 기능이 있으므로
# 눈에 보이진 않지만 <br>이 들어가있다라고 생각을 하고 next_sibling 을 두번 써주라는건데

print()

# 태그별로 데이터를 긁어와서 h1.string 을 해주면 태그는 없어지고 string 값만 출력된다?
print("h1 >>> : " + h1.string)
print("p1 >>> : " + p1.string)
print("p2 >>> : " + p2.string)