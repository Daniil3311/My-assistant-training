from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from datetime import date
from sqlalchemy import select
import asyncio
from models import Questions,Variants
from Telegram_assistent_in_traning.questions_data import QUESTIONS_Django, QUESTIONS_base

async def seed_database(session: AsyncSession):
#     # try:
#         # Проверяем, есть ли уже данные
#         result = await session.execute(select(Questions))
#         if result.scalars().first():
#             print("Данные уже существуют")
#             # return
#
#         # Создаем тестовые вопросы
#         question1 = Questions(
#             current_question=1,
#             text="Как объявить список в Python?",
#             options="list = {}, list = [], list = (), list = set()",
#             correct=0,
#             question_data=date.today(),
#             variants=[
#                 Variants(text="list = {}"),
#                 Variants(text="list = []"),
#                 Variants(text="list = ()"),
#                 Variants(text="list = set()")
#             ]
#         )
#
#         question2 = Questions(
#             current_question=2,
#             text="Что выведет `print(2 + 2 * 2)`?",
#             options="6, 8, 4, Ошибку",
#             correct=0,
#             question_data=date.today(),
#             variants=[
#                 Variants(text="6"),
#                 Variants(text="8"),
#                 Variants(text="4"),
#                 Variants(text="Ошибку")
#             ]
#         )
#
#         question3 = Questions(
#             correct_answers=0,
#             current_question=2,
#             text="Какой тип данных изменяемый в Python?",
#             options='"tuple", "str", "list", "int"',
#             correct=0,
#             question_data=date.today(),
#             variants=[
#                 Variants(text="tuple"),
#                 Variants(text="str"),
#                 Variants(text="list"),
#                 Variants(text="int")
#             ]
#         )
#         session.add_all([question3])
#         await session.commit()
#         print("Данные успешно добавлены")
#     #
#     # except Exception as e:
#     #     await session.rollback()
#     #     print(f"Ошибка при добавлении данных: {e}")
#     #     raise
    try:
        # for i, v in enumerate(QUESTIONS_Django):
        #     text = QUESTIONS_Django[i + 1]['text']
        #     correct = QUESTIONS_Django[i + 1]['correct']
        #     options = f'"{','.join(QUESTIONS_Django[i + 1]['options'])}"'
        #     print(options)
        #
        #     question = Questions(
        #             correct_answers=0,
        #             current_question=0,
        #             text=text,
        #             options=options,
        #             correct=correct,
                    # question_data=date.today(),
                    # variants=[
                    #     Variants(text=v) for v in QUESTIONS_Django[i+1]['options']
                    # ]
                 # )
                    question3 = Questions(
                        correct_answers=0,
                        current_question=2,
                        text="test",
                        options='"test"',
                        correct=0,
                        question_data=None,
                        variants=[
                            Variants(text="tuple"),
                            Variants(text="str"),
                            Variants(text="list"),
                            Variants(text="int")
                        ]
                    )
            #         session.add_all([question3])
            #         await session.commit()
            #         print("Данные успешно добавлены")
                    session.add_all([question3])
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
