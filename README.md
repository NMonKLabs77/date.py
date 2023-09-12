 # Love A.I. - Restaurant Date App

This is a restaurant date app that allows users to order food, drinks, and desserts from a menu. The app also calculates the total expense of the meal and provides a running balance of the user's budget. If the user's total expenses exceeds his/her budget it would result in him not having another date with his/her partner but if his total expenses does not exceed his budget, Love A.I grants him the free pass to have a second date with, well, his date ofcourse! 

### Code Explanation

The code for this app is written in Python. The main file is `date.py`. This file imports all of the necessary modules, defines the menus, and gets the user's name and date's name. It also displays the welcome screen and conversation between the couples.

The `menus` dictionary contains the food, drink, and dessert menus. Each menu item is a dictionary with the following keys:

* `item_no`: The item number.
* `name`: The name of the item.
* `price`: The price of the item.

### Here are snippets of my python code with a summary of the inner workings:

'''python

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
'''
<em>This is the menu for the Love A.I App. It's basically nesting of dictionaries holding menu item information inside of food, drink, dessert menu lists which are inturn inside of a 'menus' dictionary.<em> The nesting of lists inside made it possible for me to use the 'enumerate' method to add a counter or more specifically helps number my menu items so that the user would easily be able to access the menus and menu items by an item number when making orders.


