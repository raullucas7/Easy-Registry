import os


def menu_interface():
    print("Welcome to your to-do list.")
    print("1. View list")
    print("2. Add list element")
    print("3. Remove list element")
    print("4. Leave")


def view_list(todo_list):
    if not todo_list:
        print("-> List is empty")
    
    else:
        print("-> Your list:")
        for idx, item in enumerate(todo_list, start=1):
            print(f"{idx}. {item}")


def add_element(todo_list):
    item = input("Enter a to-do item: ")
    todo_list.append(item)
    
    print(f"'{item}' has been added to your to-do list.")

def remove_element(todo_list):
    view_list(todo_list)
    if todo_list:
        try:
            item_number = int(input("Enter the number of the item to remove: "))
            
            if 1 <= item_number <= len(todo_list):
                removed_item = todo_list.pop(item_number - 1)
                print(f"'{removed_item}' has been removed from your to-do list.")
            
            else:
                print("Invalid item number.")
        
        except ValueError:
            print("Please enter a valid number.")


def save_list(filename, todo_list):
    with open(filename, 'w') as file:
        
        for item in todo_list:
            file.write(item + '\n')
    
    print("List saved.")

def load_list(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            todo_list = [line.strip() for line in file.readlines()]
        
        print("List loaded.")
        return todo_list
    
    else:
        return []

def main():
    todo_list = load_list("todo_list.txt")
    while True:
        menu_interface()
        option = input("Enter your choice: ")
        
        if option == '1':
            view_list(todo_list)
        
        elif option == '2':
            add_element(todo_list)
        
        elif option == '3':
            remove_element(todo_list)
        
        elif option == '4':
            save_list("todo_list.txt", todo_list)
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
