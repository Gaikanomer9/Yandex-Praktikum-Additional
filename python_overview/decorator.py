def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(args)
        print("Something is happening before the function is called. 1st")
        func(*args, **kwargs)
        print("Something is happening after the function is called. 1st")
    return wrapper

# def say_whee():
#     print("Whee!")

# say_whee = my_decorator(say_whee)
# say_whee()

@my_decorator
def say_whee(name):
    print(f"Greetings {name}!")

@my_decorator
def greet_with_surname(name, surname):
    print(f"Greetings {name} {surname}!")


say_whee('Max')
greet_with_surname('Max', 'Richter')


# print(say_whee.__name__)
# @functools.wraps(func) - why is it needed?