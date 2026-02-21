import random

def generate_random_list(size):
    lower_bound = 1
    upper_bound = 100
    random_list = []
    for x in range(size):
        random_number = random.randint(lower_bound, upper_bound)
        random_list.append(random_number)
    return random_list

the_list = generate_random_list(20)
print(the_list)

even_list = []

for x in the_list:
    if x % 2 == 0:
        even_list.append(x)

print("Even numbers are: " + str(even_list))

total_number = sum(even_list)

print("Sum of even number list: " + str(total_number))
