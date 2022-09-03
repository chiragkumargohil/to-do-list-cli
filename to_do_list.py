import csv
import datetime


current_time = str(datetime.datetime.today()).split()
save_time = str('-'.join(list(reversed(current_time[0].split('-')))) + ' @ ' +':'.join(current_time[1].split(':')[:2]))
fieldnames = ['Timestamp', 'Task']
fieldnames2 = ['Timestamp', 'Task', 'DeletedOn']
data_file = 'data.csv'
history_file = 'history.csv'

class ToDoList:

    def __init__(self):
        
        with open(data_file) as f1:
            items = csv.DictReader(f1)
            self.items = list(items)
        
        with open(history_file) as f2:
            deleted_items = csv.DictReader(f2)
            self.deleted_items = list(deleted_items)
            
        print('''\n=== Welcome to To-Do List App ===''')

    def display_items(self):
        print("\n--- Your To-Do List ---\n")
        sr = 1
        for item in self.items:
            print(f"{sr}. {item['Timestamp']} | {item['Task']}")
            sr += 1
    
    def add_item(self):
        item = input("\nAdd Task: ")
        adding = {'Timestamp': save_time, 'Task': item}
        self.items += [adding]
        print("The item has been added.")

    def remove_item(self):
        ToDoList.display_items(self)
        print("\nWhat do you want to remove from the items above?")
        
        try:
            deletion = int(input("Remove Item by just typing number assigned: "))
            if deletion <= 0 or deletion > len(self.items):
                raise ValueError

            deleted_item = self.items.pop(deletion-1)
            print('The item has been deleted.')
            
            action = {'DeletedOn': save_time}
            deleted_item.update(action)
            self.deleted_items += [deleted_item]
        except:
            print("Please enter a valid number assigned to item in the above list.")

    def history(self):
        print("\n--- Your Deleted To-Do List ---\n")
        sr = 1
        for del_item in self.deleted_items:
            print(f"{sr}. Deleted On: {del_item['DeletedOn']} -> {del_item['Timestamp']} | {del_item['Task']}")
            sr += 1
    
    def save_file(self):
        with open(data_file, 'w', encoding='UTF8', newline='') as f1:
            writer = csv.DictWriter(f1, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.items)
        
        with open(history_file, 'w', encoding='UTF8', newline='') as f2:
            writer = csv.DictWriter(f2, fieldnames=fieldnames2)
            writer.writeheader()
            writer.writerows(self.deleted_items)
        
        print("\nThank You! Your To-Do List has been saved.")


    @staticmethod
    def help_menu():
        menu_message ='''
Press '1' to See Items
Press '2' to Add Item
Press '3' to Remove Item
Press '4' to See Deleted Items
Press '5' or 'quit' to Quit the App (You must quit by pressing '5' to save your data.)
'''
        print(menu_message)
