from random import sample
from string import ascii_lowercase, ascii_uppercase, digits


def get_random_password() -> str:
    n = 8
    password = "".join(sample(ascii_uppercase + ascii_lowercase + digits, n))
    return password


print(get_random_password())
