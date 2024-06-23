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
    to_do_list = load_list("to_do_list.txt")
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        