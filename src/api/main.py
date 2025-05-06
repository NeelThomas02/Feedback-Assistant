from fastapi import FastAPI
from pydantic import BaseModel
from pipeline import run_pipeline
from fastapi.responses import JSONResponse
import traceback

class FeedbackRequest(BaseModel):
    text: str

app = FastAPI()

@app.post("/analyze")
def analyze(req: FeedbackRequest):
    return run_pipeline(req.text)

@app.exception_handler(Exception)
async def all_exceptions(request, exc):
    tb = traceback.format_exc()
    print(tb)  # still prints to console, for dev
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc), "trace": tb.splitlines()[-1]}
    )
