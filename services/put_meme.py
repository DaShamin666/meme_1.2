import requests
from services.authorize import Authorize

class PutMeme:
    def __init__(self, name):
        self.token = Authorize.get_token(name)
        self.url = 'http://167.172.172.115:52355/'
        self.headers = {'Authorization': f"{self.token}"}

    def execute(self, meme_id, data):
        response = requests.put(f'{self.url}meme/{meme_id}', headers=self.headers, json=data)

        # Вывод информации для отладки
        print(f"PUT {self.url}meme/{meme_id} with data: {data}")
        print(f"Response Code: {response.status_code}, Response Body: {response.text}")

        return response.status_code
