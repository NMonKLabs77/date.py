from time import sleep



# Stores orders in this list stored in orders variable
orders = []
# Total expense value variable will change on purchase
total_expense = 0

# Love A.I Menu
food_menu = {
    "1": {"name": "bouillon", "price": 22},
    "2": {"name": "marinate chicken", "price": 25},
    "3": {"name": "double burger", "price": 15},
    "4": {"name": "salad", "price": 5},
    "5": {"name": "sauteed fish", "price": 5.99}
}
drink_menu = {
    "1.1": {"name": "red wine", "price": 10},
    "2.2": {"name": "white wine", "price": 15},
    "3.3": {"name": "prosecco", "price": 30},
    "4.4": {"name": "virgin mojito", "price": 35},
    "5.5": {"name": "shirley temple", "price": 25}
}
dessert_menu = {
    "01": {"name": "cheesecake", "price": 4.99},
    "02": {"name": "chocolate cake", "price": 5.99},
    "03": {"name": "apple pie", "price": 3.99},
    "04": {"name": "strawberry icecream", "price": 2.99},
    "05": {"name": "tiramisu", "price": 8.99}
}


# Get user and date's name
uname = input("Enter your name: ")
date_name = input("Enter date's name: ")
my_budget = int(input(("Enter budget: ")))

# Display welcome screen and conversation between the couples
print(f'Welcome {uname} and {date_name}! My name is Love A.I. Is it your first time at the finest restaurant in town?')

# Pause 2 seconds to simulate conversation
sleep(4)

print(f'Oh really? What a beautiful couple you two are!\nWould you like to see our food and drink menus?')

# Show budget
print(f"Budget: {my_budget}")

for item_no, item_info in food_menu.items():
    print(f"{item_no}: {item_info['name']} - ${item_info['price']:.2f}")

for item_no, item_info in drink_menu.items():
    print(f"{item_no}: {item_info['name']} - ${item_info['price']:.2f}")

# Give 2 seconds to look through the food and drink menu
sleep(2)

# Prompt user for food choice
while True: 
  u_order = input(f'{uname}, What food item would you and {date_name} like to order? Choose Item Number: 1 - 5,  0 to exit')
  if u_order in food_menu:
   food_choice = food_menu[u_order]
   orders.append(food_choice)
   total_expense += food_choice['price']
  elif u_order == '0':
      break
  else: "Invalid choice!\nPlease select 1-5 or 0 to exit"

# Prompt user for drink choice
while True: 
  drink_order = input(f"{uname}, What would you'all like to drink? Choose Item Number: 1.1 - 5.5, 0 to exit")
  if drink_order in drink_menu:
   drink_choice = drink_menu[drink_order]
   orders.append(drink_choice)
   total_expense += drink_choice['price']
  elif u_order == '0':
      break
  else: 
     "Invalid choice!\nPlease select 1.1 - 5.5 or 0 to exit" 

sleep(2)

print("You'all seem to enjoy your meal. Are you ready for the best dessert in town?")

# Show dessert menu
print('Here is the dessert menu')

for item_no, item_info in dessert_menu.items():
    print(f"{item_no}: {item_info['name']} - ${item_info['price']:.2f}")

sleep(2)

# Prompt user for dessert choice
while True: 
  dsert_order = input(f'What would yall like for dessert? Choose Item Number: 01 - 05, 0 to exit')
  if dsert_order in dessert_menu:
   dsert_choice = dessert_menu[dsert_order]
   orders.append(dsert_choice)
   total_expense += dsert_choice['price']
  elif u_order == '0':
      break
  else: 
     "Invalid choice!\nPlease select 01 - 05 or 0 to exit" 



# Show balance of money
balance = my_budget - total_expense

print(f"Your remaining budget is now: {balance}")

# Decide to pay bill
print(f"Here's your bill: {total_expense}")
pay = input(f'{uname} Are you paying now?')

if pay == 'yes':
   my_budget -= total_expense
else:
   print("I am calling security!")
# Decide if there would be another date
if total_expense > my_budget:
   print(f"{uname} You have run out of cash! You dont deserve a second date!")
   print('High maintenance girls need men with a high maintenance lifestyle!\nBetter luck next time!')
else:
   print(f"{uname}, congrats! You won yourself another date with {date_name}")
