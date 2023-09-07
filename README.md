# Love A.I Restaurant 

This is a Python program that simulates a conversation between a couple and a restaurant's AI assistant named Love A.I. The program first asks the couple's names and then displays a welcome message. It then shows the food, drink, and dessert menus and prompts the couple to make their choices. 

After the couple has made their choices, the program calculates the total expense and shows the remaining budget.
It then asks the user if he/she would like to pay the bill and based on the output of expense > budget, if expense is more than budget he would not be lucky in having another 
date with this person. 

Here are some code snippets and explanations:

`python
# Get user and date's name
uname = input("Enter your name: ")
date_name = input("Enter date's name: ")
```

These lines of code get the user's name and the date's name and store them in the variables `uname` and `date_name`.

```python
# Display welcome screen and conversation between the couples
print(f'Welcome {uname} and {date_name}! My name is Love A.I. Is it your first time at the finest restaurant in town?')

# Pause 2 seconds to simulate conversation
sleep(4)

print(f'Oh really? What a beautiful couple you two are!\nWould you like to see our food and drink menus?')
```

These lines of code display a welcome message and a conversation between the couples. The `sleep()` function pauses the execution of the program for 4 seconds to simulate a conversation.

```python
# Show budget
print(f"Budget: {my_budget}")

for item_no, item_info in food_menu.items():
    print(f"{item_no}: {item_info['name']} - ${item_info['price']:.2f}")

for item_no, item_info in drink_menu.items():
    print(f"{item_no}: {item_info['name']} - ${item_info['price']:.2f}")
```

These lines of code show the budget and the food and drink menus. The `for` loops iterate over the `food_menu` and `drink_menu` dictionaries and print the item number, name, and price of each item.

```python
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
```
First we have a `while` loop stating `while True:` prompt user to make food choice order by dictionary id number. It uses an `if` statement to check if the id corresponds to any food item in food menu dictionary
