import requests
from services.authorize import Authorize

class PutMeme:
    def __init__(self, name):
        self.token = Authorize.get_token(name)
        self.url = 'http://167.172.172.115:52355/'
        self.headers = {'Authorization': f"{self.token}"}

    def execute(self, meme_id, data):
        if isinstance(meme_id, tuple):
            meme_id = meme_id[0]  # Извлекаем ID из кортежа
        response = requests.put(f'{self.url}meme/{meme_id}', headers=self.headers, json=data)
        return response.status_code
