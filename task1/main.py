message="""1.add task 
2.mark task as complete 
3.view tasks
4.Quit"""
def add_task():
    task=input("enter the task")
    task_time=input("enter the date of the task")
    note=input("enter note about task")
    task_info={
        "task" : task,
        "completed" : False,
        "dead line" : task_time,
        "note": note
    }
    tasks.append(task_info)
    print("task added successfully")


def mark_task_completed():
    pass

def view():
    ...


tasks=[]

while True:
 print(message)
 choice=input("enter your choice:")

 if(choice=="1"):
     add_task()
 elif(choice=="2"):
     mark_task_completed()
 elif(choice=="3"):
     view()
 elif(choice=="4"):
     break
 else:
     print("invalid choice , enter between 1 and 4")