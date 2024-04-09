from fastapi import APIRouter
from app import endpoints

api = APIRouter()


api.include_router(endpoints.routes, prefix="/api")
