import os
from fastapi import FastAPI

app = FastAPI()

# load environment variables
MY_PROJECT = os.getenv("MY_PROJECT") or "This is my default project"
API_KEY = os.getenv("API_KEY") 
if not API_KEY:
    raise ValueError("API_KEY is not set")

@app.get("/")
def read_index():
    return {"message": "Welcome to my project: " + MY_PROJECT, "api_key": API_KEY}


#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8000)