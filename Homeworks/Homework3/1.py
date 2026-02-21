import random

def generate_random_list(size):
    lower_bound = 1
    upper_bound = 100
    random_list = []
    for x in range(size):
        random_number = random.randint(lower_bound, upper_bound)
        random_list.append(random_number)
    return random_list

print(generate_random_list(20))