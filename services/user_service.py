from database.db import get_pool

async def get_or_create_user(tg_id, username):
    pool = await get_pool()

    async with pool.acquire() as conn:
        user = await conn.fetchrow(
            "SELECT * FROM users WHERE id=$1", tg_id
        )

        if user:
            return user

        await conn.execute(
            """
            INSERT INTO users(id, username, role, gold, army, dragons, scorpions)
            VALUES($1, $2, 'member', 100, 0, 0, 0)
            """,
            tg_id, username
        )

        return await conn.fetchrow(
            "SELECT * FROM users WHERE id=$1", tg_id
        )
