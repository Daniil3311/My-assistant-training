# Вопросы и ответы (вопрос: {"текст": str, "варианты": list[str], "правильный": int})
import datetime


knowledge_counter_base = 0
QUESTIONS_base = {
    1: {
        "text": "Как объявить список в Python?",
        "options": ["list = {}", "list = []", "list = ()", "list = set()"],
        "correct": 1  # Индекс правильного ответа (начиная с 0)
    },
    2: {
        "text": "Что выведет `print(2 + 2 * 2)`?",
        "options": ["6", "8", "4", "Ошибку"],
        "correct": 0
    },
    3: {
        "text": "Какой тип данных изменяемый в Python?",
        "options": ["tuple", "str", "list", "int"],
        "correct": 2
    },

}
QUESTIONS_Django = {
    1: {
        "text": "Какие основные сущности есть в Django REST Framework?",
        "options": [
            "Viewsets, Serializers, Routers, Permissions",
            "Models, Templates, Views",
            "Forms, Admin, Signals",
            "Middleware, Context, Handlers"
        ],
        "correct": 0
    },
    2: {
        "text": "Какие существуют основные этапы валидации в DRF?",
        "options": [
            "Проверка данных, Валидация поля, Валидация объекта",
            "Парсинг запроса, Генерация ответа",
            "Аутентификация, Авторизация",
            "Миграции, Кэширование"
        ],
        "correct": 0
    },
    3: {
        "text": "Для чего в DRF нужен Router, если в Django есть dispatch?",
        "options": [
            "Для автоматической маршрутизации URL к ViewSets",
            "Для замены системы шаблонов Django",
            "Для валидации JSON-данных",
            "Для работы с WebSockets"
        ],
        "correct": 0
    },
    4: {
        "text": "Какой формат ответа будет у API, написанного на DRF?",
        "options": [
            "JSON (по умолчанию), но можно настроить другие",
            "Только XML",
            "Только бинарный формат",
            "HTML-страницы"
        ],
        "correct": 0
    },
    5: {
        "text": "Что умеют делать сериализаторы?",
        "options": [
            "Преобразовывать сложные типы данных в Python-объекты и обратно, валидировать данные",
            "Только генерировать HTML-формы",
            "Только кэшировать запросы",
            "Только работать с БД без ORM"
        ],
        "correct": 0
    },
    6: {
        "text": "Цикл жизни запроса в Django",
        "options": [
            "Middleware → URL-роутинг → View → Response → Middleware",
            "View → Model → Template → Response",
            "URL → Form → Validator → Response",
            "Serializer → Router → View → Response"
        ],
        "correct": 0
    },
    7: {
        "text": "Что такое middleware?",
        "options": [
            "Прослойка, обрабатывающая запрос и ответ на глобальном уровне",
            "Инструмент для работы с БД",
            "Аналог Django-форм",
            "Система шаблонов"
        ],
        "correct": 0
    },
    8: {
        "text": "Какая польза от middleware в Django?",
        "options": [
            "Обработка запросов/ответов (аутентификация, CORS, логирование)",
            "Генерация HTML-страниц",
            "Замена ORM Django",
            "Управление миграциями"
        ],
        "correct": 0
    },
    9: {
        "text": "Как изменять middleware?",
        "options": [
            "Через список MIDDLEWARE в settings.py",
            "Через файл urls.py",
            "Через административную панель Django",
            "Middleware нельзя изменить"
        ],
        "correct": 0
    },
    10: {
        "text": "В каком порядке вызываются middleware?",
        "options": [
            "Сверху вниз при запросе, снизу вверх при ответе",
            "Случайным образом",
            "Только указанные в views.py",
            "Все одновременно"
        ],
        "correct": 0
    },
    11: {
        "text": "В какой момент выполняется middleware?",
        "options": [
            "До и после обработки view",
            "Только до обработки view",
            "Только после рендеринга шаблона",
            "Только при ошибках"
        ],
        "correct": 0
    },
    12: {
        "text": "Что такое Uvicorn/Gunicorn?",
        "options": [
            "ASGI/WSGI-серверы для запуска Django",
            "Библиотеки для валидации данных",
            "Модули Django для API",
            "Инструменты для тестирования"
        ],
        "correct": 0
    },
    13: {
        "text": "Какие аналоги есть у Uvicorn/Gunicorn?",
        "options": [
            "Hypercorn, Daphne, Waitress",
            "Celery, Redis, RabbitMQ",
            "Pytest, Unittest",
            "Nginx, Apache"
        ],
        "correct": 0
    },
    14: {
        "text": "Что такое NGINX?",
        "options": [
            "Веб-сервер и обратный прокси",
            "Язык программирования",
            "Система управления БД",
            "Фреймворк для Django"
        ],
        "correct": 0
    }
}
QUESTIONS_new = {
    1: {
        "text": "Чем отличается list от tuple?",
        "options": [
            "list изменяемый, а tuple нет",
            "tuple быстрее для чтения",
            "list занимает меньше памяти",
            "tuple поддерживает сложение, а list нет"
        ],
        "correct": 0
    },
    2: {
        "text": "Что такое GIL?",
        "options": [
            "Глобальная блокировка интерпретатора Python",
            "Генератор итераторов для списков",
            "Инструмент для сборки мусора",
            "Менеджер контекста"
        ],
        "correct": 0
    },
    3: {
        "text": "Какой декоратор превращает метод в статический?",
        "options": [
            "@staticmethod",
            "@classmethod",
            "@property",
            "@abstractmethod"
        ],
        "correct": 0
    },
    4: {
        "text": "Что делает yield?",
        "options": [
            "Возвращает значение и приостанавливает функцию",
            "Вызывает исключение",
            "Завершает выполнение функции",
            "Создает новый процесс"
        ],
        "correct": 0
    },
    5: {
        "text": "Какой JOIN вернет только совпадающие строки из обеих таблиц?",
        "options": [
            "INNER JOIN",
            "LEFT JOIN",
            "RIGHT JOIN",
            "FULL OUTER JOIN"
        ],
        "correct": 0
    },
    6: {
        "text": "Что такое ACID в базах данных?",
        "options": [
            "Atomicity, Consistency, Isolation, Durability",
            "Async, Concurrent, Isolated, Durable",
            "Abstract, Concrete, Interface, Delegate",
            "Array, Class, Instance, Data"
        ],
        "correct": 0
    },
    7: {
        "text": "Как создать асинхронную функцию в Python?",
        "options": [
            "async def func(): ...",
            "def async func(): ...",
            "def func() async: ...",
            "async function func(): ..."
        ],
        "correct": 0
    },
    8: {
        "text": "Какой метод вызывается при создании объекта?",
        "options": [
            "__init__",
            "__new__",
            "__call__",
            "__str__"
        ],
        "correct": 0
    },
    9: {
        "text": "Что делает @property?",
        "options": [
            "Превращает метод в свойство",
            "Делает метод приватным",
            "Позволяет метод переопределять",
            "Автоматически кэширует результат"
        ],
        "correct": 0
    },
    10: {
        "text": "Какой алгоритм сортировки использует sorted() в Python?",
        "options": [
            "Timsort",
            "Quicksort",
            "Mergesort",
            "Bubblesort"
        ],
        "correct": 0
    },
    11: {
        "text": "Как получить текущий event loop в asyncio?",
        "options": [
            "asyncio.get_event_loop()",
            "asyncio.current_loop()",
            "asyncio.loop()",
            "asyncio.get_loop()"
        ],
        "correct": 0
    },
    12: {
        "text": "Какой статус код у 'Not Found' в HTTP?",
        "options": [
            "404",
            "400",
            "403",
            "500"
        ],
        "correct": 0
    },
    13: {
        "text": "Что делает __slots__?",
        "options": [
            "Ограничивает атрибуты класса для экономии памяти",
            "Запрещает наследование",
            "Делает все атрибуты приватными",
            "Автоматически генерирует геттеры и сеттеры"
        ],
        "correct": 0
    },
    14: {
        "text": "Какой метод Django ORM выполняет SQL-запрос сразу?",
        "options": [
            "iterator()",
            "all()",
            "execute()",
            "eval()"
        ],
        "correct": 0
    },
    15: {
        "text": "Что такое LRU Cache?",
        "options": [
            "Кэш, вытесняющий редко используемые элементы",
            "Кэш только для чтения",
            "Кэш с фиксированным временем жизни",
            "Кэш, работающий в отдельном потоке"
        ],
        "correct": 0
    }
}
""" 1: {
        "text": "Какие основные сущности есть в Django REST Framework?",
        "options": [
            "Viewsets, Serializers, Routers, Permissions",
            "Models, Templates, Views",
            "Forms, Admin, Signals",
            "Middleware, Context, Handlers"
        ],
        "correct": 0"""


print(QUESTIONS_Django[1]['options'])