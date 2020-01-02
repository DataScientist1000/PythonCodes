# @dostuff
# def foo():
#     pass

from functools import wraps
import time


def timeme(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Call our decorated function")
        start = time.time()
        result = func(*args, **kwargs)
        print("Execution time : {}".format(time.time() - start))
        return result

    return wrapper


@timeme
def decorated_func():
    print("Decorated Function !!")


decorated_func()
