import requests
from services.authorize import Authorize
import requests

class PostMeme:
    def __init__(self, name):
        self.token = Authorize.get_token(name)
        self.url = 'http://167.172.172.115:52355/'
        self.headers = {'Authorization': f"{self.token}"}

    def execute(self, data):
        response = requests.post(f'{self.url}meme', headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json().get('id', None), response.status_code
        else:
            return None, response.status_code