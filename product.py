class Product:
    #Initialize the Object
    def __init__(self, ip, ep, stock):
        self.obj = self.create(ip, ep, stock)
    #Function to create the object in the form of a dictionary
    def create(self, ip, ep, stock):
        return{
        "export_price": ep,
        "import_price": ip,
        "stock": stock,
        "shipped": 0
        }   
    #Function to get value of a specific key
    def get(self, key):
        return self.obj.get(key)
    #Function to update value of a specific key
    def update(self, key, value):
        self.obj[key] = value