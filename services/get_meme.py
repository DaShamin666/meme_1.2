import requests
from services.authorize import Authorize

class GetMeme:
    def __init__(self, name):
        self.token = Authorize.get_token(name)
        self.url = 'http://167.172.172.115:52355/'
        self.headers = {'Authorization': f"{self.token}"}

    def execute(self):
        response = requests.get(f'{self.url}meme', headers=self.headers)
        return response.status_code
