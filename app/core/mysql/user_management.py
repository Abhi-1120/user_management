import pymysql
from app.common import UserAlreadyExistException, UserNotExistException
from app.core import sql_scripts


async def add_user_in_db(conn, user) -> dict:
    try:
        async with conn.cursor() as cursor:
            add_user = {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "password": user.password,
                "mobile_no": user.mobile_no,
                "project_id": user.project_id,
                "date_of_birth": user.date_of_birth
            }
            await cursor.execute(sql_scripts["add_user_in_db"], add_user)
            user.id = cursor.lastrowid
        return user
    except pymysql.err.IntegrityError:
        raise UserAlreadyExistException


async def get_user_detail(conn, user_id) -> dict | None:
    async with conn.cursor() as cursor:
        user = {
            "user_id": user_id
        }
        await cursor.execute(sql_scripts["get_user_detail"], user)
        result = await cursor.fetchone()
        if result:
            return result
        raise UserNotExistException


async def update_user(conn, user, user_id) -> dict:
    user_info = {
        "id": user_id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "mobile_no": user.mobile_no,
        "project_id": user.project_id,
        "date_of_birth": user.date_of_birth
    }
    async with conn.cursor() as cursor:
        await cursor.execute(sql_scripts["update_user"], user_info)
    return user_info


async def delete_user(conn, user_id) -> bool:
    async with conn.cursor() as cursor:
        user = {
            "user_id": user_id
        }
        await cursor.execute(sql_scripts["delete_user"], user)
        return cursor.rowcount > 0
