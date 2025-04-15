from services.authorize import Authorize


class BaseApi(Authorize):
    def __init__(self,name):
        self.token = self.authorize(name)
        self.url = 'http://167.172.172.115:52355/'
        self.headers = {'Authorization': f"{self.token}"}
        self.response = None
        self.json = None


