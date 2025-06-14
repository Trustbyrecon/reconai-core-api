from fastapi import FastAPI
from app.routes import reflex, ghostlog

app = FastAPI()

# Include route files
app.include_router(reflex.router, prefix="/reflex-score")
app.include_router(ghostlog.router, prefix="/ghostlog")
