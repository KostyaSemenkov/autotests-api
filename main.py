import httpx
data = {
  "id": 1,
  "category": {
    "id": 1,
    "name": "string"
  },
  "name": "tim",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
poste = httpx.post('https://petstore.swagger.io/v2/pet', json=data)
print(poste.text)
print(poste.status_code)
print(poste.json()['category']['id'])
# req = httpx.get('https://petstore.swagger.io/')
# print(req.status_code)  # Проверить статус
# print(req.json())         # Распечатать HTML