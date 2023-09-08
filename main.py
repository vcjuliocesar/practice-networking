from fastapi import status,FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

app.title = "Docker FastAPI Mongodb"
app.version = "0.0.1"

@app.get("/",tags=["Home"])
def index():
    return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"Hello world"})