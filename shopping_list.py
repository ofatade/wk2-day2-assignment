# Task 1: Write a function that lets the user add items to a list

#shopping_list = []

#def add_item():
 #   add = input("What will you like to add?: ")
  #  shopping_list.append(add)

#add_item()
#print(shopping_list)


# Task 2: Include a feature to remove items from the list

#def remove_item():
 #   remove = input("What will you like to remove?: ")
#    shopping_list.remove(remove)

#remove_item()
#print(shopping_list) 

# Task 3: Add a function that prints out the entire list.

#def view_list():
 #   print("This is your shopping list")
  #  for index in range(len(shopping_list)):
   #     print(index, shopping_list[index])


# The App

shopping_list = []

def app():
    while True:
        option = input('''
Welcome to the Shopping List Maker!
What would you like to do?
Enter the corresponding number for the action you'd like to take:
                    
1 - Add to your shopping list
2 - Remove an item from the shopping list
3 - View the shopping list
4 - Quit
''')
        if option == '1':
            add_item() # add function to add to the list
        elif option == '2':
            remove_item() # function for removing from the list
        elif option == '3':
            view_list() # function to view current list
        elif option == '4':
            print("Thanks for using our app!")
            break

def add_item():
    add = input("What would you like to add? ")
    shopping_list.append(add)

def remove_item():
    take_out = input("what would you like to remove? ")
    shopping_list.remove(take_out)

def view_list():
    print("Here's your current shopping list")
    for index in range(len(shopping_list)):
        print(index, shopping_list[index])

app()

