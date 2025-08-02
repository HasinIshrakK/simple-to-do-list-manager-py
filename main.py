import pandas as pd
import os

# add task
add = input("Do you want to a new task? (Write 'y' or 'n') ")

if add.lower() == "y":
    q1 = input("Do you want to write or import task? (Write 'w' or 'i') ")
    if q1.lower() == "w":
        f_name = input("Please input task name: ")
        if os.path.exists(f_name):
            raise FileExistsError(f"Cannot create '{f_name}': Because this name is already used")
        else:
            with open(f_name, "x") as f:
                f.write(input("Write here: "))
    elif q1.lower() == "i":
        q2 = input("Is it JSON file or text file (Write 'j' or 't')")
        if q2.lower() == "j":
            j_name = input("Write the location of the JSON file in your computer: ")
            js = pd.read_json(j_name)
            f = js.to_string()
        elif q2.lower() == "t":
            t_name = input("Write the location of the text file in your computer: ")
            t = open(t_name, "r")
            f = t.read()
    else:
        print("The input is not valid.")
    print("New task added.")
elif add.lower() == "n":
    exit()
else:
    print("The input is not valid.")

# view task
view = input("Do you want to view a task? (Write 'y' or 'n') ")

if view.lower() == "y":
    name = input("Write the name of the file: ")
    if os.path.exists(name):
        with open(name) as v:
            print(v.read())
    else:
        print("The file does not exist.")
elif view.lower() == "n":
    exit()
else:
    print("The input is not valid.")

# delete task
delete = input("Do you want to delete a task? (Write 'y' or 'n') ")

if delete.lower() == "y":
    d = input("Write the name of the file: ")
    if os.path.exists(d):
        os.remove(d)
        print("The file has been successfully deleted.")
    else:
        print("The file does not exist.")
elif delete.lower() == "n":
    exit()
else:
    print("The input is not valid")