import requests


def dadata_search(query):
    url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address"
    api_key = "43d1f880e47e4e9b7f45d470beb41cc070a14d04"
    secret_key = "772d1eb87ce26c3fc4e9a6e31e3236f3d656d924"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token {api_key}"
    }
    data = {
        "query": query,
        "count": 10
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Это выбросит исключение для кода ответа != 200
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}


if __name__ == '__main__':
    query = input("Введите адрес для поиска: ")
    result = dadata_search(query)

    if 'error' in result:
        print(f"Error: {result['error']}")
    else:
        print("Результаты поиска:")
        for suggestion in result.get('suggestions', []):
            print(suggestion['value'])
