# A Complete 'To Do List' with all handled errors.
tasks=[]
def add_task():
    global tasks
    task_input = input("Input Task :- ")
    status = 'Pending'
    b =({'Task Name':task_input,'Task Status': status})
    tasks.append(b)
    print(f"Task '{task_input}' Added Succesfully")
def show_task():
    if len(tasks) != 0:
        x=1
        for i in tasks:
            print(f'{x}.{i}')
            x = x+1
        print('----------------------------------------------------')
    else:
        print("Error - Your To Do List Is Empty , Add Some Tasks.")
        print("--------------------------------------------------")
def update_task():
    if len(tasks) != 0 :
        for i in tasks:
            if i.get("Task Status") == "Pending":
                index= int(input("Input Task Index :- "))
                if tasks[index-1]['Task Status'] == 'Pending':
                    tasks[index-1]['Task Status']='Completed'
                    print(f"Task {index} Updated Succesfully\n")
                    break
                else:
                    print(f"Error , Task {index} Is Already Completed\n")
                    break
            else:
                if i.get("Task Status")==tasks[-1].get("Task Status"):
                    print("All Tasks Are Already Updated , Add New Tasks.\n")
                    break
                else:
                    continue
    else:
        print("Error - Task List Is Empty , There Should Be A Task.")
        print("----------------------------------------------------")
if __name__=='__main__':
    while True:
        i =1
        print('1.Add Task\n2.Show Task\n3.Update Task Status\n4.Exit')
        print("---------------------")
        try :
            user_input = int(input("Enter your choice :- "))
            match user_input :
                case 1:
                    add_task()
                    print('---------------------------------')
                case 2:
                    print('To Do List :-')
                    show_task()
                case 3:
                    update_task()
                    if len(tasks) != 0:
                        show_task()
                    else:
                        pass
                case 4:
                    print('Thank You ')
                    break
                case _ :
                    print('Error , PLease Enter a right Choice')
                    print('-----------------------------------')
        except :
            print(f"Error , Invalid Index")
            print('----------------------')
else:
    print("Not the main file")