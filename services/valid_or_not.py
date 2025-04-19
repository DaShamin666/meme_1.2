import requests
from services.authorize import Authorize

class ValidOrNot(Authorize):
    @classmethod
    def validation_token(cls, token):
        response = requests.get(f'http://167.172.172.115:52355/authorize/{token}')
        return response.status_code