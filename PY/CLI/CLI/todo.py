import os
import sys

clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def print_items(lst):
    for i, item in enumerate(lst):
        print(f"{str(i+1).rjust(3, '0')}.  {item}")
    print()

def add_list(list_name):
    with open(f'{list_name}.txt', 'w') as f:
        f.write('')

def remove_list(list_name):
    os.remove(list_name)

def default_list(files):
    if not files:
        print("You don't have any TODO lists. Would you like to create one? (y/n)")
        option = input("> ").lower()[0]
        if option == 'y':
            print("Name of TODO list to add: ")
            lst = input("> ")
            add_list(lst)
            print()
            return True
        else:
            sys.exit()
    return False

def todo_read(todo):
    while True:
        with open(todo) as f:
            items = f.read().split('\n')[:-1]
        
        clear_screen()
        print(f"TODO: {todo[:-4]}")
        print()

        if len(items) == 0:
            print("You don't have any tasks yet.")

        print_items(items)

        print("1. Add item")
        print("2. Delete item")
        print("3. Exit")

        option = input("> ")
        print()
        if option == '1':
            print("Item to add to TODO list: ")
            item = input("> ")
            with open(todo, 'a') as f:
                f.write(item + '\n')
            print()

        elif option == '2':
            print("Item number to delete from TODO list: ")

            try:
                item = int(input("> "))
                item_name = items[item - 1]
            except:
                continue

            print(f"This action is permanent and can not be reverted. Are you sure you want to delete {item_name}? (y/n)")
            option = input("> ").lower()[0]
            if option == 'y':
                items.pop(item - 1)

                text = '\n'.join(items) + '\n'
            
                with open(todo, 'w') as f:
                    f.write(text)

            print()

        elif option == '3':
            return None

def mainloop():
    cwd = os.getcwd()
    directory = os.path.join(cwd, "TODO Lists")

    if not os.path.isdir(directory):
        os.mkdir(directory)

    os.chdir(directory)

    files = [file for file in os.listdir() if file.endswith('.txt')]

    while True:
        files = [file for file in os.listdir() if file.endswith('.txt')]
        
        if default_list(files):
            continue
        
        clear_screen()
        print("TODO Lists:")
        
        print_items(files)

        print("Options:")
        print("1. Add TODO list")
        print("2. Delete TODO list")
        print("3. Access TODO list")
        print("4. Exit")

        option = input("> ")
        print()

        if option == '1':
            print("Name of TODO list to add: ")
            lst = input("> ")
            print()
            if f'{lst}.txt' not in files:
                add_list(lst)
                print(f'{lst}.txt was added.')
                print()
            else:
                print("A list by that name already exists.")
                print()
        
        elif option == '2':
            print("Entry number of TODO list to delete: ")
            try:
                index = int(input("> "))
                item = files[index - 1]
            except:
                continue

            print(f"This action is permanent and can not be reverted. Are you sure you want to delete {item}? (y/n)")
            option = input("> ").lower()[0]
            if option == 'y':
                remove_list(item)
            print()

        elif option == '3':
            print("Entry number of TODO list to access")
            try:
                index = int(input("> "))
                todo = files[index - 1]
                todo_read(todo)

            except:
                pass
            

        elif option == '4':
            sys.exit()

if __name__ == "__main__":
    mainloop()