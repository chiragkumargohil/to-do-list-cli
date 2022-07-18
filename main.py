class ToDoList:

    def __init__(self, li):
        self.items = li

    def displayItems(self):
        print("\n|| Your To-Do List ||\n")
        for i, item in enumerate(self.items):
            print(f"{i+1}. {item}")
    
    def addItem(self):
        item = input("\nAdd : ")
        self.items.append(item)
        print(f"Item has been added.")

    def removeItem(self):
        ToDoList.displayItems(self)
        print("\nWhat do you want remove from above items?")
        try:
            i = int(input("Remove (Just type assigned number) : "))
            self.items.remove(self.items[i - 1])
            print(f"Item has been removed successfully.")
        except:
            print("Please enter a number assigned to item in above list.")

    @staticmethod
    def menu_list():
        menu_message ='''
Press '1' to Show Items
Press '2' to Add Item
Press '3' to Remove Item
Press '4' to Quit the App
'''
        print(menu_message)

if __name__ == "__main__":
    user_input = ""
    to_do_list = []

    print('''"Welcome to To-Do List App"''')

    with open("to-do-list.txt") as f:
        lines = f.readlines()
        for line in lines:
            line.strip("")
            to_do_list.append(line.strip("\n"))

    listing = ToDoList(to_do_list)

    while user_input != "4":

        ToDoList.menu_list()
        user_input = input("What do you want to Do? ")
        
        if user_input == "1":
            listing.displayItems()
        elif user_input == "2":
            listing.addItem()
        elif user_input == "3":
            listing.removeItem()
        elif user_input == "4":
            print("\nThank You! Your To-Do Lists have been saved.")
        else:
            print("\nEnter valid response.")
        
        with open("to-do-list.txt", "w") as f:
            for item in to_do_list:
                print(item, file=f)
