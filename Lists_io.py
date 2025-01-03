#To Do List# Exercise 2

#Define base functions
def get_task():
    task = input('\nWhat would you like to add? ')
    return task

def sel_task(my_list):
    print(my_list)
    remove_task = input('\nPlease select the task to delete. ')
    return remove_task
    
def add_task(my_list, task):
    my_list.append(task)

def view(my_list):
    print(my_list if my_list else "No tasks yet.")

def del_task(my_list, remove_task):
    try:
        my_list.remove(remove_task)
        print(f"Task '{remove_task}' removed.")

    except ValueError:
        print("Task not found.")


##Get desired operation
def get_operation():

    while True:
        try:
            print('\nAvailable operations:')
            print('\n 1. Add task:')
            print('\n 2. View list:')
            print('\n 3. Remove task:')
            print('\n 4. Exit:\n')

            choice = input('Select operation number (1-4): ')
        
            if choice not in ['1', '2', '3', '4']:
                raise ValueError("Invalid choice. Please select a number between 1 and 4.")
             
            return choice

        except ValueError as e:
            print(e)

def create_list():

    print('Welcome to Lists.io!')
    print('\nTo Do List 1')

    my_list = []
    while True:
        choice = get_operation()

        if choice == '1':
            add_task(my_list, get_task())

        if choice == '2':
            view(my_list)

        if choice == '3':
            del_task(my_list, sel_task(my_list))

        if choice == '4':
            print('\nThanks for using this program!')
            break

        #print(f"\n {my_list}") -- Displays to-do-list permanently


if __name__ == "__main__":
    create_list()
    