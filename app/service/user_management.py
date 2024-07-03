from passlib.context import CryptContext
from app.core import (MysqlConnectionManager)
from app.core.mysql.user_management import *

__all__ = ["UserService"]


class UserService:
    def __init__(self, user=None, user_id=None):
        self.user_id = user_id
        self.user = user
        self.user_detail = None

    async def create_user(self):
        async with MysqlConnectionManager() as conn:
            self.user.password = self.hash_password(self.user.password)
            self.user_detail = await add_user_in_db(conn, self.user)
            await conn.commit()
        return self.user_detail

    @staticmethod
    def hash_password(password):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.hash(password)

    async def get_user_details(self):
        async with MysqlConnectionManager() as conn:
            user_detail = await get_user_detail(conn, self.user_id)
            user_detail["date_of_birth"] = user_detail.get("date_of_birth").strftime('%Y-%m-%d')
        return user_detail

    async def update_user(self) -> dict:
        async with MysqlConnectionManager() as conn:
            self.user_detail = await update_user(conn, self.user, self.user_id)
            await conn.commit()
        return self.user_detail

    async def delete_user(self) -> bool:
        async with MysqlConnectionManager() as conn:
            user_delete = await delete_user(conn, self.user_id)
            await conn.commit()
            return user_delete
