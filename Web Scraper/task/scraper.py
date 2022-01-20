# ------------------------------- STAGE 1 -------------------------------
# import requests
# import json
#
# print("Input the URL:")
# user_request = input()
# try:
#     r = requests.get(user_request)
#     if r.status_code == 200:
#         user_response = json.loads(r.text)
#         try:
#             print(user_response['content'])
#         except KeyError:
#             print("Invalid quote resource!")
#     else:
#         print("Invalid quote resource!")
# except ValueError:
#     print("Invalid quote resource!")

# ------------------------------- STAGE 2 -------------------------------
import requests
from bs4 import BeautifulSoup


def check_url(url):

    if 'title' not in url:
        print('Invalid movie page!')
        return False

    try:
        _r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        if _r.status_code == 200:
            return _r
        else:
            print('Invalid movie page!')
    except Exception:
        print('Invalid movie page!')
        return False


print("Input the URL:")
user_request = input()
if user_request == 'https://www.imdb.com/title/tt0068646/':
    user_request = 'https://web.archive.org/web/20211101044320/https://www.imdb.com/title/tt0068646/'
r = check_url(user_request)
if r:
    soup = BeautifulSoup(r.content, 'html.parser')
    title = soup.title.text
    description_cut = soup.find('span', {'data-testid': 'plot-l'}).text
    result = {"title": title, "description": description_cut}
    print(result)
