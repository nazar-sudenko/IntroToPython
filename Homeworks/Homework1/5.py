#Write a program to calculate the total cost of a super market self-checkout:
#Example output:

#Item price: 12.1
#Have more items? (y/n): y
#Item price: 4.0
#Have more items? (y/n): y
#Item price: 3.1
#Have more items? (y/n): n
#TOTAL: 19.2

item_price = float(input("Item price: "))

question = input("Have more items? ")

while question == "y":
        new_item = float(input("Item price: "))
        item_price = item_price + new_item
        question = input("Have more items? ")

print("Total: " + str(item_price))