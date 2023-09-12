 # Love A.I. - Restaurant Date App

This is a restaurant date app that allows users to order food, drinks, and desserts from a menu. The app also calculates the total expense of the meal and provides a running balance of the user's budget. If the user's total expenses exceeds his/her budget it would result in him not having another date with his/her partner but if his total expenses does not exceed his budget, Love A.I grants him the free pass to have a second date with, well, his date ofcourse!

[Link to date.py][/date.py]

### Code Explanation

The code for this app is written in Python. The main file is `date.py`. This file imports all of the necessary modules, defines the menus, and gets the user's name and date's name. It also displays the welcome screen and conversation between user and Love A.I. The code also accesses the menu and makes financial calculations using the prices set in the menu items dictionaries.

### Here are snippets of my python code with a summary of the inner workings:
```python
from time import sleep
````
<em>This line imports the sleep function from the time module, which is used later to add delays in the program so as to simulate conversation.</em>


```python
# Define loveai's menus
menus = {
    "food": [
        {"item_no": "1", "name": "bouillon", "price": 22},
        {"item_no": "2", "name": "marinate chicken", "price": 25},
        {"item_no": "3", "name": "double burger", "price": 15},
        {"item_no": "4", "name": "salad", "price": 5},
        {"item_no": "5", "name": "sauteed fish", "price": 5.99}
    ],
    "drink": [
        {"item_no": "6", "name": "red wine", "price": 10},
        {"item_no": "7", "name": "white wine", "price": 15},
        {"item_no": "8", "name": "prosecco", "price": 30},
        {"item_no": "9", "name": "virgin mojito", "price": 35},
        {"item_no": "10", "name": "shirley temple", "price": 25}
    ],
    "dessert": [
        {"item_no": "11", "name": "cheesecake", "price":
```

<em>menus is a Python dictionary that stores different menus for a restaurant. It has three categories: "food," "drink," and "dessert." Each category contains a list of items with their item numbers, names, and prices.</em>

The `menus` dictionary contains the food, drink, and dessert menus. Each menu item is a dictionary with the following keys:

* `item_no`: The item number.
* `name`: The name of the item.
* `price`: The price of the item.

```python
# Get user and date's name
uname = input("Enter your name: ")
date_name = input("Enter date's name: ")
my_budget = float(input("Enter budget: "))

# Display welcome screen and conversation between the couples
print(f'Welcome {uname} and {date_name}! My name is Love A.I. Is it your first time at the finest restaurant in town?')

# Pause 4 seconds to simulate conversation
sleep(4)

print(f'Oh really? What a beautiful couple you two are!\nWould you like to see our food and drink menus?')

# Show budget
print(f"Budget: ${my_budget:.2f}")
```
<em>This block of code is self explanotory. The user is prompted to enter their name, their date's name and their budget for the restaurant date.
Love A.I then welcomes and simulate conversation with the couples, asking if they would like to see the menu even presenting the user's chosen budget formatted to 2 decimal places.</em>

```python
# Display menus
# Iterate through each menu in the 'menus' dictionary
for menu_name, menu_items in menus.items():
    print(f'{menu_name.capitalize()} Menu:') # Print the menu name with the first letter capitalized, followed by ' Menu:'
    for item_no, item_info in enumerate(menu_items, 1): #Iterate through the menu items using enumerate(enumerate basically numbers your items)
        print(f"{item_no}: {item_info['name']} - ${item_info['price']:.2f}") # print output in format e.g 1: bouillon - $22.00 ":.2f" means formatted to 2 decimal places

# Give 2 seconds to look through the menu
sleep(2)

# Initialize orders
orders = []
# Initialize expenses
total_expense = 0
```
<em> The code iterates through the menus dictionary, capitalizes the menu names, and displays each menu's items along with their item numbers and prices.Lists orders and total_expense are initialized to keep track of the user's orders and the total expense.</em>
```python
while True:
    # Prompt user for orders stores it in a variable
    menu_name = input(f'{uname}, What menu would you like to order from (food/drink/dessert)? Enter 0 to finish: ')
    # Nested if statement checks if menu_name in menus
    if menu_name in menus:
        print(f'Please select items from the {menu_name.capitalize()} menu:') #formatted string, displays a text with menu_name first letter capitalized
        while True:
            item_no = input(f'Choose Item Number: 1 - {len(menus[menu_name])}, 0 to exit: ')  # Prompt the user to choose an item number within the menu
            if item_no == '0': # if item number equals zero break loop
                break
            elif item_no.isdigit() and 1 <= int(item_no) <= len(menus[menu_name]): # Checks if 'item_no' is a valid number(isdigit()) within the range of our available menu items
                item_choice = menus[menu_name][int(item_no) - 1] # Get the selected menu item based on the entered 'item_no'
                orders.append(item_choice) # adds item to orders lists 
                total_expense += item_choice['price'] # increments total expense with the price of selected item
            else:
                print("Invalid choice! Please select a valid item number or 0 to exit.")
    elif menu_name == '0':
        break
    else:
        print("Invalid menu choice! Please enter 'food', 'drink', 'dessert', or 0 to finish.")
```

<em>This is where the entire magic happens! The program enters a while True loop to allow the user to place orders. It prompts the user for a menu choice, validates it, and adds the selected item to the orders list while updating the total_expense. Users can exit the loop by entering '0.</em>

```python
balance = my_budget - total_expense

print(f"Your remaining budget is now: ${balance:.2f}")

# Decide to pay the bill
print(f"Here's your bill: ${total_expense:.2f}")
pay = input(f'{uname} Are you paying now? (yes/no) ')

# if yes  total expense is subtract from budget and  remaining budget is displayed, if no user lost a chance of another date
if pay.lower() == 'yes':
    my_budget -= total_expense
    print(f"Payment successful! Your remaining budget is now: ${my_budget:.2f}")
else:
    print(f"{uname}, as a man you must pay the bills of all dates you take a woman on! You have therefore lost a chance at another date")
```
<em>The remaining budget is calculated by subtracting the total_expense from the initial budget and is displayed. Love A.I then asks if the user will pay the bill.There are two
ways that the user will lose a chance of having a second date: (1) If he answer's "no" to paying the bills of the date and (2) if his expenses exceeds his budget as seen below:

```python
if total_expense > my_budget:
    print(f"{uname}, you have run out of cash! You don't deserve a second date!")
    print('High maintenance girls need men with a high maintenance lifestyle!\nBetter luck next time!')
else:
    print(f"{uname}, congrats! You won yourself another date with {date_name}")
```
<em>If the budget is sufficient, a message congratulating the user on winning another date is displayed.</em>







