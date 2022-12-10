import string
import random
from random import sample

def get_random_password() -> str:
    n = 8
    uppercase_char = string.ascii_uppercase
    lowercase_char = string.ascii_lowercase
    digits = string.digits

    password_list = uppercase_char + lowercase_char + digits
    password = "".join(random.sample(password_list, n))

    return password

print(get_random_password())
