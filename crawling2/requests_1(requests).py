from pip._vendor import requests

url = "https://www.python.org/"
resp = requests.get(url)
print("1", resp)

url2 = "https://www.python.org/1"
resp2 = requests.get(url2)
print("2", resp2)