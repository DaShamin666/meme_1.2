import requests
from services.authorize import Authorize

class PostMeme:
    def __init__(self, name):
        self.token = Authorize.get_token(name)
        self.url = 'http://167.172.172.115:52355/'
        self.headers = {'Authorization': f"{self.token}"}

    def execute(self, data):
        response = requests.post(f'{self.url}meme', headers=self.headers, json=data)
        print(f"POST {self.url}meme with data: {data}")
        print(f"Response Code: {response.status_code}, Response Body: {response.text}")
        if response.status_code != 200:
            return None  # Или обработайте ошибку другим образом
        return response.json().get('id', None)
