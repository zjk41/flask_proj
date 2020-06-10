import requests


x = {'name': 'Claire Chance', 'id': 103}
r = requests.post("http://127.0.0.1:5000/new_patient", json=x)
print(r.status_code)
print(r.text)