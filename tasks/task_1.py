from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_list = [repr(a) for a in args]
        kwargs_list = [f"{k}={v!r}" for k, v in kwargs.items()]
        args_str = ", ".join(args_list + kwargs_list)

        print(f"Вызов: {func.__name__}({args_str})")
        try:
            result = func(*args, **kwargs)
            print(f"Результат: {result}")
            return result
        except Exception as e:
            print(f"Ошибка: {e.__class__.__name__}: {e}")
            raise  # обязательно пробрасываем дальше
    return wrapper
