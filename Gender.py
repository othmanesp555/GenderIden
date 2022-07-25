import requests

print("put a name")
name = input()
url = "https://api.genderize.io/?name=" + name
response = requests.request("GET", url)
u = response.json()
print(u["gender"])