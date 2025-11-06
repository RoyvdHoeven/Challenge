import random
from time import sleep

def d20():
    return int(random.randint(1,20))

def d8():
    return int(random.randint(1,8))

def print_text(string: str, delay: float):
    for char in string:
        print(char, end='', flush=True)
        sleep(delay)
        

