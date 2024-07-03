from app import router
from app.common import UserRequestSchema, DefaultResponseSchema, UserSchema, UserNotExistException
from app.service import UserService
from app.common.constants import (API_V1_ADD_USER_ENDPOINT, API_V1_GET_USER_DETAIL_ENDPOINT,
                                  API_V1_UPDATE_USER_ENDPOINT, API_V1_DELETE_USER_ENDPOINT)

__all__ = ["create_user", "get_user_detail", "update_user", "delete_user"]


@router.post(API_V1_ADD_USER_ENDPOINT, response_model=UserSchema)
async def create_user(user: UserRequestSchema) -> dict:
    service = UserService(user)
    response = await service.create_user()
    return response


@router.get(API_V1_GET_USER_DETAIL_ENDPOINT, response_model=UserSchema)
async def get_user_detail(user_id: int) -> dict:
    service = UserService(user_id=user_id)
    response = await service.get_user_details()
    if response:
        return response
    raise UserNotExistException


@router.put(API_V1_UPDATE_USER_ENDPOINT, response_model=UserSchema)
async def update_user(user: UserSchema, user_id: int) -> dict:
    service = UserService(user=user, user_id=user_id)
    response = await service.update_user()
    if response:
        return response
    raise UserNotExistException


@router.delete(API_V1_DELETE_USER_ENDPOINT, response_model=DefaultResponseSchema)
async def delete_user(user_id: int):
    service = UserService(user_id=user_id)
    response = await service.delete_user()
    if response:
        return DefaultResponseSchema(ok=True)
    raise UserNotExistException
