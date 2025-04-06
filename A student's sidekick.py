while True:
    print("Welcome to A Student's Sidekick")
    print("Do you want to calculate your budget (1), planner (2), or grade calculator(3)? If you want to exit, type exit.")
    choice = input("Choose 1,2,3,or exit: ")
    if choice == 'exit':
        print("Bye! Hope to see you again soon!")
        break
    if choice==('1'):
      print("-----------Budgeting App-----------")
      new_budget = float(input("What is your budget for today in dollars?"))
      while new_budget >0:    
          place_one = input("what is your location (If you want to exit say no)?")
          if place_one=='no':
              break
          price_one = float(input("How much did you spend there?"))
          new_budget = new_budget - price_one
          print('You have $', new_budget, 'left')
          if new_budget<0:
              print("You exceeded the budget's limit.")
          elif new_budget==0:
              print('You have satisfied your budget')
      print("------------------------------------")
    elif choice == ('2'):
        print("-------------Planner-------------")
        tasks = []
        print("\nLet's add your tasks. Tests will be prioritized.")
        while True:
            description = input(" Enter the subject (or 'done' to finish): ")
            if description.lower() == 'done':
                break
            while True:
                due_date_str = input("How many days from now is it due? ")
                try:
                    due_date = int(due_date_str)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number of days.")

            task_type = input("Is this a (T)est or (H)omework? ").upper()
            priority_offset = -0.5 if task_type == 'T' else 0
            priority_due_date = due_date + priority_offset

            tasks.append({
                "description": description,
                "due_date": due_date,
                "priority_due_date": priority_due_date,
                "type": task_type
            })

        sorted_tasks = sorted(tasks, key=lambda x: x["priority_due_date"])

        print("\n--- Your Planner ---")
        if sorted_tasks:
            for task in sorted_tasks:
                task_label = "Test" if task["type"] == 'T' else "Homework"
                print(f"- [{task_label}] {task['description']} (Due in {task['due_date']} days)")
        else:
            print("No tasks entered.")
        print("------------------------------------")

    elif choice==('3'):
        print("--------Grade Calculator---------")
        points_possible = int(input("What was the total points? "))  
        points_scored = int(input("How many points did you get? ")) 
        grade = (points_scored / points_possible) * 100
        if grade >= 90:
            print("Grade: A")
        elif grade >= 80:
            print("Grade: B")
        elif grade >= 70:
            print("Grade: C")
        elif grade >= 60:
            print("Grade: D")
        else:
            print("Grade: F")
        print("You got ", grade,"%")
        print("------------------------------------")