class User:

 def __init__(self, username , password):
     self.username = username
     self.password = password





class Buyer(User):
    def __init__(self,address ,codemeli,username , password):
        self.address = address
        self.codemeli = codemeli
        self.username = username
        self.password = password



        
        
