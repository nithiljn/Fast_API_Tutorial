### Enum 
**Enum where used to pass the parameter to an url to get strict values type**
### Example
 you can pass whatever value use can passed through the parameter in path variable you want :
 **@app.get('/get/{model})**
 async def getvalues(model:EnumClass):
         you can get EnumClass.hr -> its will return the enum ojects 
         but if you want str you need to explicitly write the EnumClass.hr.value



from enum import Enum

class Department(str, Enum):
    hr = "hr"
    it = "it"
    sales = "sales"
