from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from datetime import datetime

engine = create_async_engine("postgresql+asyncpg://postgres:123Qwezxcasd@localhost/my_assistant_in_training")


async def get_db_session():
    """Создает асинхронную сессию для работы с БД"""
    return AsyncSession(engine)


async def update_data():
    async with await get_db_session() as session:
        today = datetime.now().date()
        await session.execute(
            text("""
                    UPDATE questions
                    SET question_data = NULL
                    WHERE question_data < :today
                """),
            {"today": today}  # Передаём параметр
        )
        await session.commit()
    # return True


