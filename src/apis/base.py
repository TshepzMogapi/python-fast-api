from apis.v1 import route_auth
from apis.v1 import route_products
from apis.v1 import route_users
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_products.router, prefix="/products", tags=["products"])
