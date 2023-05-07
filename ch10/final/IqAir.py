import requests

class IqAir():

    def __init__(self):
        self.url = 'http://api.airvisual.com/v2/countries?key=70a235ba-dd25-441d-825f-2f4f3278a42b'
        #API Key (Air Quality) 70a235ba-dd25-441d-825f-2f4f3278a42b
    
    def get(self):
        r = requests.get(self.url)
        response = r.json()
        print(response)