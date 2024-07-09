#On my own trying to add new things

#Create a dictionary called menu and create sub dicitonaries as menu categories

menu = {
    "Snacks" : {
        "Popcorn" : 4.00,
        "Candy" : 3.50,
        "Pretzel" : 4.50
                },

    "Drinks" : {
        "Coke" : 3.50,
        "Sprite": 3.50,
        "Water": 2.00
                },
            
    "Dessert" : {
        "Cake" : 5.50,
        "Ice cream": 4.00,
        "Chocolate bar" : 3.50
                }
        }

#print the menu to see what it looks like. 
#print(menu)

#print the Snack category of the menu
#print(menu["Snacks"])

#print the value of popcorn
#print(menu["Snacks"]["Popcorn"])



"""Print the menu but assign a number to the menu categories."""


#Create a menu list. This will be used to store the menu item name, price, and quantity. 
order_list = []
#Create menu dashes variable 
menu_dashes = "-" * 20
#create a while loop 
while True:
    #Ask which menu the user would like to view. 
    print("Which menu would you like to view?")
    #Create a number variable for the menu number.
    i = 1
    #create a dictionary to store the menu category for later
    menu_items= {}
    #print menu
    print("------- MENU -------")
    #create a for loop to print the keys of the menu dictionary. 
    #This should show menu category and print a number for each category.
    for key in menu.keys():
        print(f"{i} : {key}")
        #make the key value of the menu_items dict the number associated with
        #the number on the menu. 
        menu_items[i] = key
        #add one so that each item has an ascending number in the menu. 
        i += 1
    print(menu_dashes)
    #create an input variable asking for a number. Make the input lowercase using
    #.lower() so that is the user hits Q or q code breaks. 
    menu_category = input("Please pick the menu you'd like to view. Enter q to quit ").lower()
    print()
    #make sure the menu_category is a digit using the .isdigit() function.
    if menu_category.isdigit():
        #make sure the menu_category is a valid menu_item number. 
        if int(menu_category) in menu_items.keys():
        #create a menu category name variable
            menu_category_name = menu_items[int(menu_category)]
            print(f"You chose the {menu_category_name} section of the menu.")
            #create an item number variable
            x = 1
            #create an item dicitonary
            item_list = {}
            #print menu category
            print(f"--------- {menu_category_name} ---------")
            #create a for loop to iterate through the sub categories items 
            for key, value in menu[menu_category_name].items():
                #print the item number, the key value pair for the menu 
                #dicitonary related to the picked menu value 
                #aka menu_category_name.
                print(f"{x} : {key:14} : ${value:.2f}")  
                #Make the item number variable the key to the item_list dict. 
                item_list[x] = key
                #add one to the item number so they go in ascending order.
                x+= 1
        #create an input variable asking which item the user wants
        # use .lower() so that if they enter Q to quit, the program still quits.
        menu_selection = input("Which item would you like? Enter q to quit. ").lower()
        #create an if statement that if menu_selection is q the code breaks.
        if menu_selection == 'q':
            print("You quitter.")
            break
        #create an if statement to make sure the menu_selection input is a digit
        #use the .isdigit() function.
        if menu_selection.isdigit():
            #create an for loop checking that the menu selection is an menu
            #item possibility in the menu[menu_category_name]
            if int(menu_selection) in item_list.keys():
                #create a item name variable of the menu_selection number 
                #in the item_list
                item_name = item_list[menu_selection]
                print(f"You chose {item_name}.")
                #create a quantity variable as an input
                quantity = input(f"How many {item_name} would you like? Invalid answers will default to 1.")
            
            
                #Need to use key2, value2 for the for loop interation. 
                #create an item price variable turning the value of
                #the menu[menu_category_name] dictionary into an int
                price = menu_selection[menu_category_name][item_name]
                print(price)
                # #create an item total variable which takes the price * quantity
                # item_total = price * quantity
                # print(item_total)

                #TEST this adds the item_name to the order list. TEST
                #order_list.append(item_name)
            
        



    elif menu_category == 'q':
        print("You quit.")
        break

    else:
        print("Not a number. Please try again.")
     




