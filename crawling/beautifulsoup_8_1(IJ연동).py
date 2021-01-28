
import urllib.request as req

from bs4 import BeautifulSoup

url = "http://localhost:8088/testVue_war/python/beausoup_books.html"
fp = req.urlopen(url)
soup = BeautifulSoup(fp, "html.parser")

sel = lambda q: print(soup.select_one(q))
sel("#nu")
sel("li#nu")
sel("ul > li#nu")
sel("#bible #nu")
sel("#bible > #nu")
sel("ul#bible > #nu")
sel("li[id='nu']")
sel("li:nth-of-type(4)")

print(soup.select("li")[3].string)
print(soup.find_all("li")[3].string)
