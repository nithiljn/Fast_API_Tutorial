from fastapi import FastAPI,HTTPException,Query
from FirstStep.EmployeeData import EmployeeData
from FirstStep.EmployeeName import EmployeeName
from pathlib import Path
from fastapi.responses import FileResponse
from FirstStep.Item import Item
import logging
from typing import Annotated
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
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
@app.get('/file/{file_path:path}')
async def getFile(file_path:str):
     path_area = Path(file_path)
     if not path_area.exists() or not path_area.is_file():
          raise HTTPException(
               status_code=400,
               detail="file not found"
          )
     return {
          "file":file_path
     }

employee_data = [
          {
               "Name":"James Nithil V",
               "Contact":8220173595,
               "Salary":23000
          },
          {
               "Name":"Gokul",
               "Contact":46843939,
               "Salary":24000
          }
     ]
@app.post('/user/salary')
async def getSalary(item:Item)->dict:
     response_data = None
     for res in employee_data:
       if res["Name"].lower() == item.Name.lower():
            response_data= res
            break
     if (response_data):
          logger.info(f"reponse {response_data}")
          return {
               "Name":response_data["Name"],
               "Salary":response_data["Salary"],
               "Contact":response_data["Contact"]
          }
     raise HTTPException(
          status_code=400,
          detail="No record Found"
     )

@app.post('/userdata/{item_id}')
async def updated_user_id(item:Item , item_id:int , q:Annotated[str | None , Query(min_length=3,max_length=10,description="for what uses !") ]= None):
     results = {
          "item_id":item_id,
          **item.model_dump()
     }
     if q:
          results.update({"q":q})
     
     return results