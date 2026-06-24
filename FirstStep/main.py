from fastapi import FastAPI

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