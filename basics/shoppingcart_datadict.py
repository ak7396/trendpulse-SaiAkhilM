'''
problem statemnt:
You have a shopping list with items and their prices:

shopping_list = [
    {"item": "Milk", "price": 50},
    {"item": "Bread", "price": 30},
    {"item": "Eggs", "price": 60},
    {"item": "Rice", "price": 120}
]
Complete the following tasks:

Task 1: Add and Remove Items (30 points)
Add a new item {"item": "Butter", "price": 80} to the shopping list
Remove the first item from the list using .pop(0)
Print how many items are in the list now
Task 2: Calculate Total Cost (35 points)
Calculate the total cost of all items in the shopping list
Find the most expensive item and print its name and price
Print the total cost
Task 3: Create Summary Dictionary (35 points)
Create a dictionary called summary with:
"total_items": Number of items in the list
"total_cost": Total price of all items
"average_price": Average price per item (round to 2 decimals)
Print the summary dictionary

'''
from pprint import pprint #used to get the orint in muc more readable format
shopping_list = [
    {"item": "Milk", "price": 50},
    {"item": "Bread", "price": 30},
    {"item": "Eggs", "price": 60},
    {"item": "Rice", "price": 120}
]
shopping_list.append({"item": "Butter", "price": 80})
#pprint(shopping_list)
'''
Expected Output:
[{'item': 'Milk', 'price': 50},
 {'item': 'Bread', 'price': 30},
 {'item': 'Eggs', 'price': 60},
 {'item': 'Rice', 'price': 120},
 {'item': 'Butter', 'price': 80}]
 '''

shopping_list.pop(0)
print(f"number of itemts in the list : {len(shopping_list)}")
l=[]
'''
other way i can do without creating an emplty list is i can directly add 
the orice to avariable and sum it  like (took AI help for alternate solution instead of adding a an empty list)

Total=0
for d in shopping_list:
    Total+=d["price"]
print(f"total cost of all items in the shopping list = {Total}")
'''
for d in shopping_list:
    k=(d["price"])## we are using the key which is price to get all the prices of items in list as assigning then to k
    #print(k)
    l.append(k)#l is enpty list and appending all values to list
    cost=sum(l)
most_expensive = max(shopping_list, key=lambda x: x["price"])
print(f"most expensive item is {most_expensive['item']} and price is {most_expensive['price']}")

print(f" total cost of all items in the shopping list = {cost}")

summary={}

total_items=len(shopping_list)
total_cost=cost
average_price=total_cost/total_items
summary["total_items"]=len(shopping_list)
summary["total_cost"]=cost
summary["average_price"]=round(total_cost/total_items,2)
print(f"summary={summary}")
