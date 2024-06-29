#  POST запрос
import requests

response = requests.post(
    url="https://petstore.swagger.io/v2/pet",
    headers={
        "api_key": "special=key"
    },
    json={
      "id": 13,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": "Tison",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "dogs"
        }
      ],
      "status": "available"
    }
)
print(response.json())
petId = response.json()["id"]

get_pet_by_id = requests.get(f"https://petstore.swagger.io/v2/pet/{petId}")
print(get_pet_by_id.json())


post_uploads_an_image = requests.post(
    url=f"https://petstore.swagger.io/v2/pet/{petId}/uploadImage",
    headers={
            "api_key": "special=key"
        },
    files={
        "file": ("dog_ava.jpg", open("dog_ava.jpg", "rb"), "image/jpeg")
    }
)
print(post_uploads_an_image.status_code)
print(post_uploads_an_image.json())
