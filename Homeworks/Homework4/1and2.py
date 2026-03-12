file = open('Homeworks/Homework4/expenses.txt', 'a')
while True:
    ans = input("Add expense? y/n ")
    if ans == 'n':
        break
    expense = input("Enter expense: ")
    cost = input("Enter cost: ")
    file.write(expense + ", " + cost + "\n")

file.close()