def insert():
    print("\n\tInsert Function\n")

def delete():
    print("\n\tDelete Function\n")

def search():
    print("\n\tSearch Function\n")

def display():
    print("\n\tDisplay Function\n")

def exit():
    print("\n\tExit Function\n")

def get_menu(choice):
    menu = {
        1 : insert,
        2 : delete,
        3 : search,
        4 : display,
        5 : exit
    }
    return menu[choice]

def run_menu():
    count = 0
    while True:
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Display")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        get_menu(choice)()
        if choice == 5:
            break
        
run_menu()