from fastapi import status,FastAPI
from fastapi.responses import JSONResponse
from configs.database import client

app = FastAPI()

app.title = "Docker FastAPI Mongodb"
app.version = "0.0.1"

@app.get("/",tags=["Home"])
async def index():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"Hello world"})
    except Exception as error:
        print(f"error :{str(error)}")
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message":str(error)})
