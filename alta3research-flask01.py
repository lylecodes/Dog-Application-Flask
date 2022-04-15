import requests

URL = "http://127.0.0.1:2224/"

response = requests.get(f"{URL}/dog-info").json()

print(response)
