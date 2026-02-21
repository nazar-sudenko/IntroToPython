import random

def generate_random_list(size):
    lower_bound = 1
    upper_bound = 100
    random_list = []
    for x in range(size):
        random_number = random.randint(lower_bound, upper_bound)
        random_list.append(random_number)
    return random_list
size = 20
the_list = generate_random_list(size)
print(the_list)

def generate_second_list():
    second_list = []
    for x in range(size):
        random_number = random.randint(1, 100)
        second_list.append(random_number)
    return second_list

second_list = generate_second_list()
print(second_list)

def compare_lists(the_list, second_list):
    same_numbers = []
    for x in the_list:
        if x in second_list:
            same_numbers.append(x)
    return same_numbers

print("Same numbers that are in both lists are: " + str(compare_lists(the_list, second_list)))



