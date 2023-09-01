import time
#Open a list
tasks = []

#Main menu

def main_menu():
  print("To do list main menu:")
  print("Press a to add a task.")  
  print("Press b to view tasks.")  
  print("Press c to check off tasks.")
  print("Press d to delete tasks.")
  print("Press q to quit.")

def add_tasks():
  task = input("Please enter the task: ")
  tasks.append({"task": task, "completed": False})
  print("Task added.")
  task_choice = input("Press a to add another task.  Press b to return to main menu. ")
  if task_choice == "a":
    add_tasks()
  elif task_choice == "b":
    return
  else:
    print("Invalid choice. Please enter a valid option.")

def view_tasks():
  if not tasks:
    print("No tasks in the list.")
  else:
    print("Tasks:")
    for index, task_info in enumerate(tasks, start=1):
      task_status = "Complete" if task_info["completed"] else "Incomplete"
      print(f"{index}. {task_info['task']} - {task_status}")

def checkoff_tasks():
  view_tasks()
  if not tasks:
    return

  try:
    index = int(input("Enter the task number to check off: ")) - 1
    if 0 <= index < len(tasks):
      tasks[index]["completed"] = True
      print("Task checked off successfully!  Congrats!")
      time.sleep(3)
      task_choice = input("Press a to check off another task.  Press b to return to main menu. ")
      if task_choice == "a":
        checkoff_tasks()
      elif task_choice == "b":
        return
      else:
        print("Invalid choice. Please enter a valid option.")  
    else:
      print("Invalid task number.")
  except ValueError:
    print("Invalid input. Please enter a number.")

def delete_tasks():
  view_tasks()
  if not tasks:
    return

  try:
    index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= index < len(tasks):
      removed_task = tasks.pop(index)
      print(f"Removed task: {removed_task}")
    else:
      print("Invalid task number.")
  except ValueError:
    print("Invalid input. Please enter a number.")

while True:
  main_menu()
  choice = input("Enter your choice: ")

  if choice == "a":
    add_tasks()
  elif choice == "b":
    view_tasks()
  elif choice == "c":
    checkoff_tasks()
  elif choice == "d":
    delete_tasks()
  elif choice == "q":
    print("Goodbye!")
    time.sleep(3)
    break
  else:
    print("Invalid choice. Please enter a valid option.")
