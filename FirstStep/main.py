from fastapi import FastAPI

app = FastAPI(
    title="My first APP",
    description="This is my first App where i have been Created it on fast API",
    version="1.2.0"
              )

@app.get('/')
async def root():
    return {"message":"hello my first app"}