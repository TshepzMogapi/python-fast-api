from fastapi import APIRouter

from apis.v1 import route_users
from apis.v1 import route_products


api_router = APIRouter()
api_router.include_router(route_users.router,prefix="/users",tags=["users"])
api_router.include_router(route_products.router,prefix="/products", tags=["products"])
