from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from datetime import date
from sqlalchemy import select
import asyncio
from models import Questions,Variants
from Telegram_assistent_in_traning.questions_data import QUESTIONS_Django, QUESTIONS_base, QUESTIONS_new

async def seed_database(session: AsyncSession):

    try:
        for i, v in enumerate(QUESTIONS_base):
            text = QUESTIONS_base[i + 1]['text']
            correct = QUESTIONS_base[i + 1]['correct']
            options = QUESTIONS_base[i + 1]['options']
            print('","'.join(options))
            print('---------------')

            question = Questions(
                    correct_answers=0,
                    current_question=0,
                    text=text,
                    options='","'.join(options),
                    correct=correct,
                    question_data=None,
            )
            # variants = Variants(text=v)
            #         for v in QUESTIONS_Django[i + 1]['options']
            #         question3 = Questions(
            #             correct_answers=0,
            #             current_question=2,
            #             text="test",
            #             options='"test"',
            #             correct=0,
            #             question_data=None,
            #             variants=[
            #                 Variants(text="tuple"),
            #                 Variants(text="str"),
            #                 Variants(text="list"),
            #                 Variants(text="int")
            #             ]
            #         )
            # #         session.add_all([question3])
            # #         await session.commit()
            # #         print("Данные успешно добавлены")
            session.add_all([question])
            await session.commit()
            print("Данные успешно добавлены")
    except Exception as e:
        await session.rollback()
        print(f"Ошибка при добавлении данных: {e}")
        raise "Ошибочка молодой человек!"


async def main():
    engine = create_async_engine(
        "postgresql+asyncpg://postgres:123Qwezxcasd@localhost/my_assistant_in_training",
        echo=True
    )

    async with AsyncSession(engine) as session:
        await seed_database(session)

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
