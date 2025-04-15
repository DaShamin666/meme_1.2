import requests
from services.authorize import Authorize

class GetOneMeme:
    def __init__(self, name):
        self.token = Authorize.get_token(name)
        self.url = 'http://167.172.172.115:52355/'
        self.headers = {'Authorization': f"{self.token}"}

    def execute(self, meme_id):
        response = requests.get(f'{self.url}meme/{meme_id}', headers=self.headers)
        return response.status_code
