import os

def menu_interface():
    print("Welcome to your to-do list.")
    print("-> View list")
    print("-> Add list element")
    print("-> Remove list element")
    print("-> Leave")

def view_list():


def add_element():




def remove_element():




def save_list():




def load_list():




def main():
    
    todo_list = load_list("todo_list.txt")

    while True:
        show_menu()
        option = input("Enter your choice: ")
        
        if option == '1':
            view_list(todo_list)
        
        elif option == '2':
            add_element(todo_list)
        
        elif option == '3':
            remove_element(todo_list)
        
        elif option == '4':
            break
        
        else:
            print("Error in choice. Try again.")
        
if __name__ == "__main__":
    main()