import requests
from pprint import pprint as print

API_KEY = "Your API KEY here"

currency = "USD"
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

r = requests.get(url)
# print(r.status_code)
res = r.json()
# print(res)
# print(res["conversion_rate"])
kurs = res["conversion_rate"]
print(f"Buguni kurs: 1 AQSh dollari - {kurs} so'm")