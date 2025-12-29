from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AziRequest(BaseModel):
    input: str

@app.post("/azi")
def azi(req: AziRequest):
    return {
        "response": f"Azi online. You said: {req.input}"
    }
