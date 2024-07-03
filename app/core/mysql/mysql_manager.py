import aiomysql
from aiomysql.cursors import DictCursor


async def connect_mysql():
    return await aiomysql.connect(host="127.0.0.1",
                                  port=3306,
                                  user="root",
                                  password="admin123#",
                                  db="user_management", cursorclass=DictCursor)


class MysqlConnectionManager:
    def __init__(self):
        self.conn = None

    async def __aenter__(self):
        self.conn = await connect_mysql()
        return self.conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
