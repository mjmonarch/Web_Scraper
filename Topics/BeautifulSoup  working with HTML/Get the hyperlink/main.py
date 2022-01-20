import requests

from bs4 import BeautifulSoup

try:
    num = int(input())
except ValueError:
    print("Should enter number of the act")

try:
    link = input()
    r = requests.get(link)
except Exception:
    print("Should enter valid link")

soup = BeautifulSoup(r.content, 'html.parser')
all_a = soup.find_all('a')
for a in all_a:
    if f"ACT {num}" in a.text:
        print(a.get('href'))
        break
