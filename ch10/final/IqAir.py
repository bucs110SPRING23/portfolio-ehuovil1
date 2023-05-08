import requests

class IqAir():

    def __init__(self):
        self.url = 'http://api.airvisual.com/v2/nearest_city?lat={}&lon={}&key=70a235ba-dd25-441d-825f-2f4f3278a42b'
        #API Key (Air Quality) 70a235ba-dd25-441d-825f-2f4f3278a42b
        
    def __str__(self):
        return f'IqAir({self.url})'
    

    def get(self, lat, long):
        personalIQ = self.url.format(lat, long)
        iqairrresponse = requests.get(personalIQ)
        response = iqairrresponse.json()

        return(response)

    
    def windcity(self, response):

        citydata = response['data']
        citylocation = citydata['city']
        #city = citylocation['latitude']
    
        wind1 = response['data']
        wind2 = wind1['current']
        wind3 = wind2['weather']
        wind4 = wind3['ws']
        ## unwrapping the json dictionary to find wind speed 

        
        print("City found from latitude and longitude: " + citylocation)
        print("The following is for any pilots or anyone thinking about throwing a kite outside:")
        print("Current wind speed in your area: " + str(wind4))
        return[wind4, citylocation]
    

        