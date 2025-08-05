import asyncio
from datetime import datetime, timedelta, date
import sys
from os.path import split
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
    CallbackQueryHandler
)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from questions_data import QUESTIONS_base, QUESTIONS_Django, knowledge_counter_base
from db.models import Questions, Variants
from sqlalchemy import text

class DataBot:
    pass
class TelegramBot:
    __slots__ = ['engine']
    TOKEN = "8339272645:AAH1suGtNCDkjY5owYT-sMtmF_VsoAEaLMo"
    def __init__(self):

        if sys.platform == "win32":
            asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

        self.engine = create_async_engine("postgresql+asyncpg://postgres:123Qwezxcasd@localhost/my_assistant_in_training")

    async def get_db_session(self):
        """Создает асинхронную сессию для работы с БД"""
        return AsyncSession(self.engine)


    async def start(self, u: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        # Начинаем тест с первого вопроса
        context.user_data["score"] = 0  # Счётчик правильных ответов
        context.user_data["current_question"] = 0  # Текущий вопрос

        await self.send_question(u, context)


    async def send_question(self, u: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

        async with await self.get_db_session() as session:
            # Пример асинхронного запроса к БД
            today = datetime.now().date()
            result = await session.execute(
                text( """SELECT * FROM questions 
            WHERE question_data = :today 
            OR question_data IS NULL
            ORDER BY id"""),
                {"today": today}
            )
            res = result.mappings().all()

            print(len(res))
            print(res)
            if len(res)!=0:
                question_num = context.user_data["current_question"]  # номер вопроса
                # res = result.mappings().all()
                res = [dict(row) for row in res]
                print(question_num)
                # print(res[question_num-1])
                # print(res[question_num]['question_data']==datetime.datetime.now().date())
                # print(datetime.now().date())
                variant = res[question_num]['options'].split(',')
                question = res[question_num]
            # if question['question_data']==datetime.now().date():
                # Создаем кнопки с вариантами
                keyboard = [
                    [InlineKeyboardButton(option, callback_data=f"ans_{i}")]
                    for i, option in enumerate(variant)
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)

                # Отправляем вопрос
                if u.callback_query:
                    await u.callback_query.edit_message_text(
                        f"Вопрос {question_num}: {question['text']}",
                        reply_markup=reply_markup
                    )
                else:
                    await u.message.reply_text(
                        f"Вопрос {question_num}: {question['text']}",
                        reply_markup=reply_markup
                    )
            else:
                await u.message.reply_text('Пока ты выполняешь тесты быстрее чем я мог подумать:)!')

    async def handle_answer(self, u: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        query = u.callback_query
        await query.answer()

        async with await self.get_db_session() as session:
            # Пример асинхронного запроса к БД
            today = datetime.now().date()

            result = await session.execute(
                text("""SELECT * FROM questions 
                    WHERE question_data = :today 
                    OR question_data IS NULL
                    ORDER BY id"""),
                {"today": today}
            )
            res = result.mappings().all()
            # print(res[1])
            res = [dict(row) for row in res]
            # Получаем номер выбранного ответа (из callback_data="ans_1" → 1)
            chosen_option = int(query.data.split("_")[1])
            question_num = context.user_data["current_question"]
            correct_option = res[question_num]["correct"]
            cor_ans = res[question_num]['correct_answers']

            # Проверяем ответ
            if chosen_option == correct_option:
                context.user_data["score"] += 1
                await query.edit_message_text("✅ Правильно!")
                if cor_ans >= 1:
                    cor_ans +=1
                else:
                    cor_ans = 1
                from sqlalchemy import update


                # обновляю данные
                stmt = (
                    update(Questions)
                    .where(Questions.id == res[question_num]['id'])
                    .values(question_data=datetime.now().date() + timedelta(days=cor_ans), correct_answers=cor_ans)
                )
                result = await session.execute(stmt)
                # datetime.now().date() + timedelta(days=cor_ans)
                # print(cor_ans, '____>')
                # print(f"Обновлено строк: {result.rowcount}")
                await session.commit()


            else:
                await query.edit_message_text("❌ Неправильно!")

            # Переходим к следующему вопросу или завершаем тест
            print(len(res),'==============================')
            context.user_data["current_question"] += 1

            if context.user_data["current_question"] < (len(res)):
                # context.user_data["current_question"] += 1

                await self.send_question(u, context)
            else:
                score = context.user_data["score"]
                total = len(res)
                await query.edit_message_text(
                    f"Тест завершен! 🎉\n"
                    f"Правильных ответов: {score}/{total}"
                )


    def main(self):
        application = ApplicationBuilder().token(self.TOKEN).build()

        application.add_handler(CommandHandler("start", self.start))
        application.add_handler(CallbackQueryHandler(self.handle_answer, pattern="^ans_"))

        application.run_polling()

if __name__ == "__main__":
    t=TelegramBot()
    t.main()