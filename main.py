from importlib.resources import contents


user_input = ""
to_do_list = []

print('''"Welcome to To-Do List App"''')
def menu_list():
    print("\nPress '1' to Add Item.\nPress '2' to Remove Item.\nPress '3' to View the List.\nPress '4' to Quit the App\n")

with open("to-do-list.txt") as f:
    lines = f.readlines()
    for line in lines:
        line.strip("")
        to_do_list.append(line.strip("\n"))

while user_input != "4":
    menu_list()
    user_input = input("What do you want to Do? ")
    
    if user_input == "1":
        item = input("\nAdd: ")
        to_do_list.append(item)
        print(f"Item is added.")
    elif user_input == "2":
        c = len(to_do_list)
        print("\nWhat do you want remove?")
        for item in range(1, (c+1)):
            print(f"{item}. {to_do_list[item-1]}")
        item = input("Remove: ")
        if item in to_do_list:
            to_do_list.remove(item)
            print(f"Item is removed successfully.")
        else:
            print("\nItem is not in your To-Do List.")
    elif user_input == "3":
        c = len(to_do_list)
        print("\nYour To-Do Lists:")
        for item in range(1, (c+1)):
            print(f"{item}. {to_do_list[item-1]}")
    elif user_input == "4":
        print("\nThank You! Your To-Do Lists have been saved.")
    else: 
        print("\nEnter valid response.")
    
with open("to-do-list.txt", "w") as f:
    for item in to_do_list:
        print(item, file=f)