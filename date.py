# import all modules needed for this app
from time import sleep

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
        {"item_no": "11", "name": "cheesecake", "price": 4.99},
        {"item_no": "12", "name": "chocolate cake", "price": 5.99},
        {"item_no": "13", "name": "apple pie", "price": 3.99},
        {"item_no": "14", "name": "strawberry ice cream", "price": 2.99},
        {"item_no": "15", "name": "tiramisu", "price": 8.99}
    ]
}

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

# Starts while loop
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

# Show balance of money
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
    

# Decide if there would be another date
if total_expense > my_budget:
    print(f"{uname}, you have run out of cash! You don't deserve a second date!")
    print('High maintenance girls need men with a high maintenance lifestyle!\nBetter luck next time!')
else:
    print(f"{uname}, congrats! You won yourself another date with {date_name}")

