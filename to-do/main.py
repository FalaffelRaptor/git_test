def show_menu():
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Quit")

def view_tasks(tasks):
    if not tasks:
        print("NO Tasks Yet Dummy")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}, {task}")

def add_task(tasks):
    new_task = input("Enter new task: ")  # Fixed: use a different variable name
    tasks.append(new_task)                # Fixed: append the new task, not the list
    print(f"Task '{new_task}' added!") 

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter task number to remove: ")) - 1
            removed = tasks.pop(index)
            print(f"Task '{removed}' removed!")
        except (ValueError, IndexError):
            print("Invalid Choice!")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()