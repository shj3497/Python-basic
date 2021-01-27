import urllib.request

url = "http://api.aoikujira.com/ip/ini"
print("url >>> : ", url)
res = urllib.request.urlopen(url)
print("res >>> : ", res)
data = res.read()
print("data >>> : ", data)

text = data.decode("UTF-8")
print(text)