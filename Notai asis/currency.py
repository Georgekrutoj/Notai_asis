import requests

def convert_currency():
    amount = float(input('Введите количество валюты: '))
    currency = input('Введите тип валюты (например, USD): ')

    url = f'https://api.exchangerate-api.com/v4/latest/{currency}'
    response = requests.get(url)
    if response.status_code == 404:
        return 'Ошибка: введенная валюта не поддерживается'
    exchange_rate = response.json()['rates']['RUB']

    converted_amount = round(amount * exchange_rate, 2)
    print(f'{amount} {currency} = {converted_amount} RUB')