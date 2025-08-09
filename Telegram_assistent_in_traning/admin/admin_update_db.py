import asyncio
from datetime import datetime
import logging
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import text

engine = create_async_engine("postgresql+asyncpg://postgres:123Qwezxcasd@localhost/my_assistant_in_training")

async def get_db_session():
    """Создает асинхронную сессию для работы с БД"""
    return AsyncSession(engine)


async def update_data_in_db():
    async with await get_db_session() as session:
        today = datetime.now().date()
        try:
            result = await session.execute(
                text("""   
                        UPDATE questions
                        SET question_data = NULL
                    """),
            )
            # updated_count = len(result.all())
            await session.commit()
            # logging.info(f"Успешно обновлено {updated_count} записей")
            await session.commit()
        except Exception as e:
            await session.rollback()
            logging.error(f"Ошибка при обновлении данных: {e}")
            raise
        finally:
            print('все')

if __name__ == '__main__':
    asyncio.run(update_data_in_db())