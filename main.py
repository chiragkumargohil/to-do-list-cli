from to_do_list import ToDoList

if __name__ == "__main__":
    myApp = ToDoList()
    myApp.help_menu()

    while True:
        print("\nType 'help' to see the menu OR 'quit' to save your list and close the app,")
        user_input = input("-> What do you want to Do?: ")
        
        if user_input.lower() == "help":
            myApp.help_menu()
        elif user_input == "1":
            myApp.display_items()
        elif user_input == "2":
            myApp.add_item()
        elif user_input == "3":
            myApp.remove_item()
        elif user_input == "4":
            myApp.history()
        elif user_input == "5" or user_input.lower() == 'quit':
            myApp.save_file()
            print("\nThank You! Your To-Do List has been saved.")
            break
        else:
            print("\nEnter valid response.")
            continue
