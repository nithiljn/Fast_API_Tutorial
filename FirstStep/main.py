from fastapi import FastAPI,HTTPException
from FirstStep.EmployeeData import EmployeeData
from FirstStep.EmployeeName import EmployeeName
'''
Browser
   ↓
Uvicorn (ASGI Server)
   ↓
FastAPI
   ↓
Starlette
   ↓
Python Code
'''
'''
openapi.json
      ↓
Swagger UI
      ↓
Interactive Docs
'''
app = FastAPI(
    title="My first APP",
    description="This is my first App where i have been Created it on fast API",
    version="1.2.0"
              )

@app.get('/')
async def root(name:str = "james"):
    return {"message":f"hello my first app{name}"}

"""
Path Paramters
"""
@app.get('/items/{item_id}', response_model=EmployeeData)
async def getProduct(item_id:int):
      datas = [
         {
           "item_id":1,
           "Name":"James Nithil",
           "Contact":8220173595
         },
         {
           "item_id":2,
           "Name":"Gokul Raj",
           "Contact":7384648383
         }
      ]
      for data in datas:
           if data["item_id"]==item_id:
                return {
                     "Name":data["Name"],
                     "Contact":data["Contact"]
                }
      raise HTTPException(
           status_code=400,
           detail="Data Not Found"
      )

@app.get('/username/{employee_name}')
async def getemployeeName(employee_name:EmployeeName):
      if employee_name in EmployeeName.JAMES:
           return {
                "Name":EmployeeName.JAMES.value,
                "status":"SUCCESSS"
           }
      raise HTTPException(
           status_code=400,
           detail="Invalid name you searched"
      )  