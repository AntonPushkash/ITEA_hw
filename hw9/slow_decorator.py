"""
    Напишите декоратор, который будет замедлять выполнение функции на 5 секунд.

    Если функция выполняется более 10 секунд (с учетом замедления), то
    дополнительно выводить сообщение f'{func.__name__} - very slow function'
"""
import time


def timed(func):

    def wrapper(*args, **kwargs):
        print('Выполняется функция', func.__name__)
        start = time.time()
        time.sleep(5)
        result = func(*args, **kwargs)
        end = time.time() - start
        if end > 10:
            print(f'{func.__name__} - very slow function')
        else:
            print(end, 'seconds')
        return result

    return wrapper


@timed
def summ(a, b):
    return a + b


result = summ(10, 5)
print('10 + 5 =', result)