# def func_decorator():
#     def wrapper():
#         print("YDC")
#     return wrapper
#
# p = func_decorator()
#
# print(p())

# def func_2(f):
#     print("func_2")
#     return f
#
#
# @func_2
# def func_1():
#     print("func_1")
#
# func_1()

registry = {}


def register(name):
    def decorator(cls):
        registry[name] = cls
        return cls
    return decorator


@register("email")
class EmailNotifier:
    def send(self, msg): print(f"Email: {msg}")


@register("sms")
class SMSNotifier:
    def send(self, msg): print(f"SMS: {msg}")


print(registry)  # {'email': <class...>, 'sms': <class...>}
