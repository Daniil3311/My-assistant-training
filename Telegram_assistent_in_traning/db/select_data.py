from datetime import datetime
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

engine = create_async_engine("postgresql+asyncpg://postgres:123Qwezxcasd@localhost/my_assistant_in_training")


async def get_db_session():
    """Создает асинхронную сессию для работы с БД"""
    return AsyncSession(engine)


async def select_data():
    async with await get_db_session() as session:

        today = datetime.now().date()

        result = await session.execute(
            text("""SELECT * FROM questions 
                         WHERE question_data = :today 
                         OR question_data IS NULL
                         ORDER BY id"""),
            {"today": today}
        )
        res = result.mappings().all()
        res = [dict(row) for row in res]
    return res