import requests
from bs4 import BeautifulSoup

req1 = requests.get("https://www.geeksforgeeks.org/")

soup1 = BeautifulSoup(req1.content, "html.parser")

res1 = soup1.title.string
print(res1)

for i in range(0, 101):
    res2 = soup1.find_all('a')[i]
    print(res2.text)
    print(" ")


