# Python To-Do List

def add_task():
    task = input("\nEnter a task To Do: ")

    tasks.append(task)

    print(f"{task} was successfully added to your list\n")

def view_task():
    if not tasks:
        print("Your to-do list is empty. \n")
    else:
        print(f"Here are your tasks: {tasks} \n")

def remove_task():
    if not tasks:
        print("Your to-do list is empty. Nothing to remove. \n")
        return

    task = input("Enter a task To remove: ")

    if task in tasks:
        tasks.remove(task)
        print(f"'{task}' was successfully removed from your list \n")
    else:
        print("This task is not in your list. Please enter the exact task.\n")


tasks = []
is_running = True

print("Welcome to your To-Do List")

print()

while is_running:
    print("Select an option:\n 1. Add Task \n 2. View Tasks \n 3. Remove Task \n 4. Exit")

    choice = input("Enter your choice (1-4): ")

    if not choice.isdigit():
        print("Please enter a valid choice")
        continue

    choice = int(choice)

    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        remove_task()
    elif choice == 4:
        print("Goodbye!")
        is_running = False
    else:
        print("Invalid Option")

