from bs4 import BeautifulSoup

fp = open("beautifulsoup_frvege.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")


print(soup.select_one("ul:nth-of-type(2) > li:nth-of-type(4)").string)
# ul:nth-of-type(2) >> ul태그의 두번째를 가르키는듯한데..
# id값이나 클래스값으로 찾아가는게 좋지 않을까 싶다..

print(soup.select_one("#ve-list > li:nth-of-type(4)").string)
print(soup.select("#ve-list > li[data-lo='us']")[1].string)
print(soup.select("#ve-list > li.black")[1].string)

cond = {"data-lo":"us", "class":"black"}
print(soup.find("li", cond).string)

print(soup.find(id="ve-list").find("li", cond).string)