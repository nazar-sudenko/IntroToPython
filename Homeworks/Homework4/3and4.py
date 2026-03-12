file = open('Homeworks/Homework4/expenses.txt')

lines = file.readlines()

expenses = {}

for line in lines:
    line = line.strip().split(',')
    category = line[0].lower()
    amount = float(line[1])

    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

item = expenses.items()
def sort_key(item):
    return item[1]

sorted_expenses = sorted(item, key=sort_key, reverse=True)

print("Unsorted:")
for category in expenses:
    print(f"{category}: {expenses[category]}")

print("\nSorted:")
for (category, amount) in sorted_expenses:
    print(f"{category}: {amount}")

