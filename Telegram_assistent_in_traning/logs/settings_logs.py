import logging

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.basicConfig(
    filename='logs/app.log',          # Файл для записи логов
    filemode='a',                # Режим записи ('a' - append, 'w' - overwrite)
    level=logging.WARNING,         # Уровень логирования
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    encoding='utf-8'
)