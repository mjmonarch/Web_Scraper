import requests

from bs4 import BeautifulSoup

letter = 'S'

url = input()

search_list = []
try:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    all_a = soup.find_all('a')
    for a in all_a:
        if a.text.startswith(letter) and len(a.text) > 1 and \
                ('topic' in a.get('href') or 'entity' in a.get('href')):
            search_list.append(a.text)
    print(search_list)
except Exception:
    print("Something went wrong")
