import requests
from django.conf import settings


class CladrService:
    def dadata_search(self, query):
        url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address"
        api_key = settings.DADATA_SEARCH_API_KEY

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
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}
