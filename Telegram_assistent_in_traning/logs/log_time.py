from functools import wraps
import time
import logging

def async_timed(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            return await func(*args, **kwargs)
        finally:
            end_time = time.time()
            if func.__name__=='handle_answer':
                logging.warning('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            logging.warning(f"{func.__name__} выполнена за {end_time - start_time:.4f} сек")
    return wrapper
