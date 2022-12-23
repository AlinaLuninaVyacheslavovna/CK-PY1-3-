from random import randint


def get_unique_list_numbers(start=-10, stop=10, count=15) -> list[int]:
    random_digit = []
    while len(random_digit) < count:
        num_ = randint(start, stop)
        if num_ not in random_digit:
            random_digit.append(num_)

    return random_digit


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
