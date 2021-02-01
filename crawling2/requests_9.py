import requests

r = requests.get("http://google.com")
print(r)
r1 = requests.get("https://wikibook.co.kr/wikibook.png")
print(r1)

text = r.text
print(text)

bin = r.content
print(bin)

with open("./data/test.png", "wb") as f:
    f.write(r.content)

print("save")
