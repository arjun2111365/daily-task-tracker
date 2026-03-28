from datetime import datetime
import json

def save(data,check):
    if check==2:
        with open("task.json","w") as f:
            json.dump(data,f)
    else:
        with open("reminder.json","w") as f:
            json.dump(data,f)

def read_reminder():
    with open("reminder.json","r") as f:
        data=json.load(f)
        return data

def read_task():
    with open("task.json","r") as f:
        data=json.load(f)
        return data

def write_data(check):
    
    if check==1:
        data=read_reminder()
        i=0
        dic={}
        
        print("enter '/save' to save data")
        
        while True:
            text=input(f"enter reminder {i}=")
            
            if text=="/save":
                save(data,1)
                break
            
            dic[text]=False
            data.append(dic)
            i+=1

    elif check==2:
        data=read_task()
        print("enter '/save' to save data")

        today_date=datetime.now().strftime("%Y-%m-%d")

        # create new day if it doesn't exist
        if not data or today_date not in data[-1]:
            data.append({today_date:[]})

        while True:
            text=input("enter=")

            if text=="/save":
                save(data,2)
                break

            data[-1][today_date].append(text)


while True:

    print(
        "enter 1 to enter reminder in current date\n",
        "enter 2 to enter task in current date\n",
        "enter 3 to exit program\n",
        sep=""
    )

    x=int(input("enter option="))

    if x==1:
        write_data(1)

    elif x==2:
        write_data(2)

    elif x==3:
        print("program complete")
        break
