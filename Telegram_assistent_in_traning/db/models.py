import asyncio

from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, DeclarativeBase, Mapped, mapped_column

# Base = declarative_base()
# engine = create_engine('postgresql://postgres:123Qwezxcasd@localhost:5432/stock')
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncAttrs
from sqlalchemy.orm import sessionmaker

# Для PostgreSQL (asyncpg)
engine = create_async_engine(
    "postgresql+asyncpg://postgres:123Qwezxcasd@localhost/my_assistant_in_training",
    echo=True  # Логирование запросов
)

class Base(AsyncAttrs, DeclarativeBase):
    pass

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Date, Float, ForeignKey
from datetime import date
class Base(DeclarativeBase):
    pass

class Questions(Base):
        __tablename__ = 'questions'

        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        current_question: Mapped[int] = mapped_column()
        text: Mapped[str] = mapped_column(String)
        options: Mapped[str] = mapped_column(String)
        correct: Mapped[int] = mapped_column(default=0)
        question_data: Mapped[date] = mapped_column(Date, nullable=True, default=None)

        variants: Mapped[list["Variants"]] = relationship(
            "Variants",
            back_populates="question",
            cascade="all, delete-orphan"
        )
        correct_answers: Mapped[int] = mapped_column(Integer)


class Variants(Base):
        __tablename__ = 'variants'

        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        text: Mapped[str] = mapped_column(String)
        question_id: Mapped[int] = mapped_column(ForeignKey('questions.id'))  # Ключевое добавление
        question: Mapped["Questions"] = relationship(
            "Questions",
            back_populates="variants"
        )
# Database setup
# Base.metadata.create_all(engine)
async def create_tables():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(create_tables())