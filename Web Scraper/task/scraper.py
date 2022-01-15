# ------------------------------- STAGE 1 -------------------------------
import requests
import json

print("Input the URL:")
user_request = input()
try:
    r = requests.get(user_request)
    if r.status_code == 200:
        user_response = json.loads(r.text)
        try:
            print(user_response['content'])
        except KeyError:
            print("Invalid quote resource!")
    else:
        print("Invalid quote resource!")
except ValueError:
    print("Invalid quote resource!")

