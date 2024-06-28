import requests
from requests.auth import HTTPBasicAuth

response = requests.get(
    url="https://petstore.swagger.io/v2/pet/findByStatus",  # Endpoint
    # auth=HTTPBasicAuth("username", "password") если используется авторизация
    headers={
        "api_key": "special-key"
    },
    params={
        "status": "sold"
    },  # передача query параметров
    #verify=False,  # проверка SSL-сертификата, False/True игнорирует/выполняет проверку сертификата
)

print(response.json())

