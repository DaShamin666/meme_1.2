import requests

class Authorize:
    _token = None

    @classmethod
    def get_token(cls, name):
        if cls._token is None:
            data = {"name": name}
            response = requests.post('http://167.172.172.115:52355/authorize', json=data)
            cls._token = response.json().get('token')
        return cls._token
