from random import randint


def get_unique_list_numbers(start=-10, stop=10, count=15) -> list[int]:

    random_digit = [randint(start, stop)]

    for digit in range(count):

        if digit not in random_digit:
            random_digit.append(digit)
        else:
            randint(start, stop)
    return random_digit


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
