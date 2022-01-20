import requests

from bs4 import BeautifulSoup

try:
    num = int(input())
except ValueError:
    print("Should enter number first")

try:
    link = input()
    r = requests.get(link)
except Exception:
    print("Should enter valid link")

soup = BeautifulSoup(r.content, 'html.parser')
all_subtitles = soup.find_all('h2')
print(all_subtitles[num].text)
