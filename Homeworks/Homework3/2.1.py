all_list = []

question = input("Would you like to add another number? (y/n): ")

while question != "n":
    all_list.append(int(input("what is the number? ")))
    question = input("Would you like to add another number? (y/n): ")

print("The unprocessed list looks like this: " + str(all_list))

even_list = []

for x in all_list:
    if x % 2 == 0:
        even_list.append(x)

print("The even numbers in the list are: " + str(even_list))

sum_of_even_list = sum(even_list)

print("Sum of the even list is: " + str(sum_of_even_list))