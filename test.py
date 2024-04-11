from time import time

def my_decorator(function):
    def counter():
        start = time()
        function()
        finish = time()
        print(finish - start)
    return counter


@my_decorator
def display():
    num1 = 1
    num2 = 50000
    while num1 <= num2:
        print(num1)
        num1 += 1

#display = my_decorator(display)
display()
