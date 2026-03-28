import asyncpg
from config import DB_URL

pool = None

async def connect_db():
    global pool
    pool = await asyncpg.create_pool(DB_URL)

async def get_pool():
    return pool
