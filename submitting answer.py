import requests

data = {"number": "190",
        "answer": "28",
        "user": "a.tonon"}
r = requests.post("http://34.163.196.38/", data=data)
print(r.text)
