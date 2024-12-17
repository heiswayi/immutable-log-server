from fastapi.responses import JSONResponse, RedirectResponse
from blockchain import Blockchain
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import LogData

app = FastAPI(
    title="Immutable Log Server",
    description="A simple server to store logs in an immutable blockchain",
    version="1.0.0",
    docs_url="/api/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

blockchain = Blockchain()


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/api/docs")


@app.get("/healthcheck", tags=["Endpoints"], summary="Health Check")
async def health_check():
    return {"status": "healthy"}


@app.post(
    "/api/add_log",
    tags=["Endpoints"],
    summary="Add a log",
)
def add_log(data: LogData):
    try:
        if not data.metadata:
            data.metadata = {}
        if not data.message:
            return JSONResponse(
                status_code=400,
                content={"status": "Error", "details": "Message is required"},
            )
        blockchain.add_block(data.dict())
        return JSONResponse(
            status_code=201,
            content={"status": "Success", "details": data.dict()},
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "Error", "details": str(e)},
        )


@app.get(
    "/api/get_logs",
    tags=["Endpoints"],
    summary="Get all logs",
)
def get_logs():
    try:
        return blockchain.get_logs()
    except Exception as e:
        return {"status": "Error", "message": str(e)}


@app.get(
    "/api/validate_chain",
    tags=["Endpoints"],
    summary="Validate the blockchain",
    response_model=dict,
    status_code=200,
)
def validate_chain():
    return JSONResponse(
        content={
            "message": (
                "Blockchain is valid"
                if blockchain.validate_chain()
                else "Blockchain is invalid"
            ),
        }
    )
