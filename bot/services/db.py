import aiomysql

from config import Config

class DataBase:
    def __init__(self) -> None:
        self.db_config = Config.DataBase.db_config

    async def table_create(self):
        pool = await aiomysql.create_pool(**self.db_config)

        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users(
                        user_id BIGINT PRIMARY KEY,
                        token TEXT,
                        id BIGINT,
                        password TEXT,
                        is_admin INTEGER
                    )
                ''')
                await conn.commit()

                await cursor.execute('''
                    CREATE TABLE IF NOT EXISTS favorites(
                        user_id BIGINT PRIMARY KEY,
                        cams TEXT
                    )
                ''')
                await conn.commit()

        pool.close()
        await pool.wait_closed()

    async def get_user_info(self, user_id: int):
        async with aiomysql.create_pool(**self.db_config) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    await cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
                    return await cursor.fetchone()

    async def delete_user_data(self, user_id: int):
        async with aiomysql.create_pool(**self.db_config) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    await cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
                    await cursor.execute("DELETE FROM favorites WHERE user_id = %s", (user_id,))
                    await conn.commit()

    async def update_token(self, user_id: int, token: str):
        async with aiomysql.create_pool(**self.db_config) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    await cursor.execute("UPDATE users SET token = %s WHERE user_id = %s", (token, user_id))
                    await conn.commit()

    async def update_password(self, user_id: int, password: str):
        async with aiomysql.create_pool(**self.db_config) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    await cursor.execute("UPDATE users SET password = %s WHERE user_id = %s", (password, user_id))
                    await conn.commit()

    async def update_admin(self, user_id: int, admin: int):
        async with aiomysql.create_pool(**self.db_config) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    await cursor.execute("UPDATE users SET is_admin = %s WHERE user_id = %s", (admin, user_id))
                    await conn.commit()

    async def add_user(self, user_id: int, token: str, id: int, password: str, is_admin: int):
        async with aiomysql.create_pool(**self.db_config) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    await cursor.execute(
                        'INSERT INTO users (user_id, token, id, password, is_admin) VALUES (%s, %s, %s, %s, %s)', 
                        (user_id, token, id, password, is_admin)
                    )
                    await cursor.execute(
                        'INSERT INTO favorites (user_id, cams) VALUES (%s, %s)', 
                        (user_id, '[]')
                    )
                    await conn.commit()

    async def get_cams(self, user_id: int):
        async with aiomysql.create_pool(**self.db_config) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    await cursor.execute("SELECT cams FROM favorites WHERE user_id = %s", (user_id,))
                    return await cursor.fetchone()

    async def cam_update(self, user_id: int, dump: dict):
        async with aiomysql.create_pool(**self.db_config) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    await cursor.execute("REPLACE INTO favorites (user_id, cams) VALUES (%s, %s)", (user_id, dump))
                    await conn.commit()

    async def get_all_user_id(self):
        async with aiomysql.create_pool(**self.db_config) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    await cursor.execute("SELECT user_id FROM users")
                    return await cursor.fetchall()
