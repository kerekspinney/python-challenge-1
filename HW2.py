#Kerek's Pizza Shop Menu & Customer Online Ordering 

#Making the Menu

"""
To make the menu, I need to make dictionaries for the menu  categorieschoices.
 Once I have the menu category choices as a dictionary, I will 
 create a sub dictionaries for the related categories. 
 Here is the psuedocode

 menu = {
        "Category": {
            "Sub Category" : price in int
            "Sub Category" : price in int
                     }
        "Category": {
            "Sub Category" : price in int
            "Sub Category" : price in int
                     }
        }
"""
menu = {

    "Appetizer" : {
        "Garlic Knots" : float(5.00),
        "Garlic Bread" : float(6.00),
        "Cheesy Bread" : float(6.50),
                    },

    "Pizza" : {
        "Cheese Pizza" : float(8.00),
        "Pepperoni Pizza" : float(11.50),
        "Veggie Pizza" : float(12.00),
        "Meat Pizza" : float(13.00),
        "Everything Pizza" : float(15.50),
                },

    "Sandwiches" : {
        "Italian": float(11.00),
        "BLT": float(10.50),
        "Turkey & Swiss": float(9.00),
        "PB & J": float(6.00),
                    },  
                    
    "Dessert" : {
        "Chocolate Fudge Cake" : float(6.50),
        "Tres Leches Cake" : float(7.00),
        "Ice Cream Sandwich" : float(6.50),
                }
        }

#Welcome message for the restaurant
print("Welcome to Kerek's Pizza Shop")

#Create the menu dashes for visible menu
menu_dashes = "-" * 42

# Create a loop that allows customers to choose which section of the 
# menu they want to order from. It needs to loop incase they want to 
# order multiple items 
"""
In order to do this you have to create a while loop and create 
a variable for the menu category number and you'll also need to 
create a dictionary which will store the menu item numbers. Also,
I will need to print the menu category options and once picked the 
menu number must be stored. Then you must add 1 to this number so 
the picked number matches the menu item number since counting 
in dictionaries starts with 0 instead of 1.

While True:
    menu_variable = 1
    stored_number_dictionary = {}

    for key in menu.keys():
        print(f"{menu_variable} : {keys}")

        stored_number_dictionary[menu_variable] = key

        stored_number_dictionary + 1
"""

while True:
    print("Which menu would you like to view? ")

    # Create the menu item number variable
    m = 1

    # Create a dictionary to store the menu for later retrieval 
    menu_items = {}

    # Print the options to choose from the m the first level 
    # dictionary items in menu.
    for key in menu.keys():
        print(f"{m}: {key}")

        # Store the menu category associated with its menu item number
        menu_items[m] = key

        # Add 1 to the menu item number so the menu number doesn't start at 0
        m += 1

    # Create a customer input & variable related to the customers input.
    menu_selection = input("Type the number associated with the menu you want to view.")
    print("If you want to stop ordering press 'x'.")

    # Exit the loop if user typed 'X' once they ordered.
    if menu_selection.lower() == 'x':
        break

    # Make sure the customers answer is a digit, usign the isdigit() funtion.
    elif menu_selection.isdigit():

        # Check if the customer's input is a valid option
        if int(menu_selection) in menu_items.keys():

            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_selection)]

            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Display the heading for the sub-menu
            print(menu_dashes)
            print(f"This is the {menu_category_name} menu.")
            print(menu_dashes)
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

            # Create a menu item counter
            item_counter = 1

            # Print out the menu options from the menu_category_name
            for key, value in menu[menu_category_name].items():

                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:

                    # Iterate through the dictionary items
                    for key2, value2 in value.items():

                        # Print the menu item
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{item_counter}      | "
                              + f"{key} - {key2}{item_spaces} | "
                              + f"${value2}")

                        # Add 1 to the item_counter so that the menu number for each sub category 
                        # is the same as the computer menu number. This is done because computer counting 
                        #starts at 0 instead of 1.
                        item_counter += 1
                else:

                    # Print the menu item
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{item_counter}      | "
                          + f"{key}{item_spaces} | ${value}")

                    # Add 1 to the item_counter so that the menu number for each sub category 
                        # is the same as the computer menu number. This is done because computer counting 
                        #starts at 0 instead of 1.
                    item_counter += 1
            
            print(menu_dashes)
            print("Please a number showing which item you'd like to order.")
            input("Press enter to return to the main menu.")

            """Now I need to create a variable to ask the customer how many of the specific item they would like to buy
            and save this variable answer so that at the end the customer know how many they ordered and
            the total cost of each item and then the sum total of all of the items they purchased.

            Here is the format:

            #Need to create the quantity variable.
            quantity = input(f"How many of the {menu_selectrion} would you like to buy? ")

            total_cost = quantity * 


            """

        else:

            # Tell the customer they didn't select a menu option
            print(f"{menu_selection} was not a menu option. Please try again.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

"""Now that the menu has been created and the customer input selection has been created so that the customer
can go into each sub menu and order. I need to create the portion of the code which stores"""

