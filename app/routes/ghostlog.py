from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/write")
async def write_log(request: Request):
    log_entry = await request.json()
    return {"status": "logged", "entry": log_entry}
