# import requests, json
# from bot_config import API_key
#
# r = requests.get(f"https://v6.exchangerate-api.com/v6/{API_key}/pair/EUR/RUB/100")
# d = json.loads(r.content)
# val = float(d.get("conversion_rate"))
# sval = float(d.get("conversion_result"))
#
# print(val)
# print(sval)

# r = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
# d = json.loads(r.content)
# val = d.get("Valute")
# vUSD = val.get("USD")
# vsUSD = vUSD.get("Value")
# print(vsUSD)

r = "1.2"

print(not r.isdigit())