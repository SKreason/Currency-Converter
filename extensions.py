import requests
import json
from bot_config import API_key, values


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):  # обработка и выполнение запроса конвертера
        if quote == base:
            raise APIException(f'Одинаковые валюты "{quote}"')

        if not amount.isdigit() or float(amount) <= 0:
            raise APIException(f'Неверное значение валюты для конвертирования "{amount}"')

        try:
            v1 = values[quote]  # валюта которую нужно конвертировать
        except KeyError:
            raise APIException(f'Неверное название валюты "{quote}"')

        try:
            v2 = values[base]  # валюта в которую нужно конвертировать
        except KeyError:
            raise APIException(f'Неверное название валюты "{base}"')

        v3 = float(amount)  # количество валюты для конвертирования
        r = requests.get(f"https://v6.exchangerate-api.com/v6/{API_key}/pair/{v1}/{v2}/{v3}")
        d = json.loads(r.content)
        con_val = float(d.get("conversion_result"))
        con_val = round(con_val, 2)
        text = f"Сумма {amount} {quote} в {base} = {con_val}"
        return text
