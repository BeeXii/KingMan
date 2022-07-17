
import requests

class _lineAPI:
    def __init__(self) -> None:
        self.BaseuRL = 'https://notify-api.line.me/api/notify'
        self.token = '3lCRgcVFMC2mnLw6PQqq8voNK9udGuqq9MZPo1O7jOe'
        self.headers  = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+ self.token }

        self.req = requests.session()
        
        self.req.headers = self.headers
       
    def SendMessage(self , m ):
        try:
            self.req.post(self.BaseuRL , data = {'message': m } )
        except:
            pass
    
LineAPI = _lineAPI()
