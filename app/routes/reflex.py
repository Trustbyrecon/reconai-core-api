from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/")
async def score_reflex(request: Request):
    payload = await request.json()
    return {"reflex_score": 0.82, "input": payload}
