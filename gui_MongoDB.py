import tkinter as tk
from tkinter.constants import END, LEFT, RIGHT
import pymongo


def main():
    # Conection to local DB
    client = pymongo.MongoClient("localhost", 27017)
    db = client.myblog
    # Connection confirmation
    print("Connected to " + db.name)
    # Call to build GUI
    window = tk.Tk()
    buildMenu(db, window)


def buildMenu(db, window):
    for element in window.grid_slaves():
        element.grid_forget()
    window.title("Menu")
    # Building and styling
    title = tk.Label(text="Menu", height=5, width=30, font=10)

    # Buttons
    insertOnebtn = tk.Button(text="InsertOne", width=15,
                             height=2, command=lambda: buildInsertOne(db, window))
    deleteOnebtn = tk.Button(text="DeleteOne", width=15,
                             height=2, command=lambda: buildDeleteOne(db, window))
    deleteManbtn = tk.Button(text="DeleteMany", width=15,
                             height=2, command=lambda: buildDeleteMan(db, window))
    findbtn = tk.Button(text="Find", width=15,
                        height=2, command=lambda: buildFind(db, window))

    # Displaying
    title.grid(column=1, row=0)
    insertOnebtn.grid(column=1, row=2)
    deleteOnebtn.grid(column=1, row=3)
    deleteManbtn.grid(column=1, row=4)
    findbtn.grid(column=1, row=5)

    window.mainloop()


def buildInsertOne(db, window):
    # Cleaning
    for element in window.grid_slaves():
        element.grid_forget()
    window.title("InsertOne")

    # Building and styling
    title = tk.Label(text="InsertOne", height=5, width=30, font=10)
    user_name_entry = tk.Entry(width=20)
    user_age_entry = tk.Entry(width=20)

    # Button calls for lambda function on click
    back = tk.Button(text="Menu", width=10, height=2,
                     command=lambda: buildMenu(db, window))
    submit = tk.Button(text="Submit", width=20, height=2, command=lambda: insertOne(
        user_name_entry, user_age_entry, db))

    # Displaying
    title.grid(column=1, row=0)
    tk.Label(text="Name").grid(column=0, row=2)
    user_name_entry.grid(column=1, row=2)
    tk.Label(text="Age").grid(column=0, row=3)
    user_age_entry.grid(column=1, row=3)
    submit.grid(column=1, row=4)
    back.grid(column=1, row=5)
    window.mainloop()


def buildDeleteOne(db, window):
    # Cleaning
    for element in window.grid_slaves():
        element.grid_forget()
    window.title("DeleteOne")

    # Building and styling
    title = tk.Label(text="DeleteOne", height=5, width=30, font=10)
    user_name_entry = tk.Entry(width=20)
    user_age_entry = tk.Entry(width=20)

    # Button calls for lambda function on click
    back = tk.Button(text="Menu", width=10, height=2,
                     command=lambda: buildMenu(db, window))
    submit = tk.Button(text="Submit", width=20, height=2, command=lambda: deleteOne(
        user_name_entry, user_age_entry, db))

    # Displaying
    title.grid(column=1, row=0)
    tk.Label(text="Name").grid(column=0, row=2)
    user_name_entry.grid(column=1, row=2)
    tk.Label(text="Age").grid(column=0, row=3)
    user_age_entry.grid(column=1, row=3)
    submit.grid(column=1, row=4)
    back.grid(column=1, row=5)
    window.mainloop()


def buildDeleteMan(db, window):
    # Cleaning
    for element in window.grid_slaves():
        element.grid_forget()
    window.title("DeleteMany")

    # Building and styling
    title = tk.Label(text="DeleteMany", height=5, width=30, font=10)
    user_name_entry = tk.Entry(width=20)
    user_age_entry = tk.Entry(width=20)

    # Button calls for lambda function on click
    back = tk.Button(text="Menu", width=10, height=2,
                     command=lambda: buildMenu(db, window))
    submit = tk.Button(text="Submit", width=20, height=2, command=lambda: deleteMany(
        user_name_entry, user_age_entry, db))

    # Displaying
    title.grid(column=1, row=0)
    tk.Label(text="Name").grid(column=0, row=2)
    user_name_entry.grid(column=1, row=2)
    tk.Label(text="Age").grid(column=0, row=3)
    user_age_entry.grid(column=1, row=3)
    submit.grid(column=1, row=4)
    back.grid(column=1, row=5)
    window.mainloop()


def buildFind(db, window):
    # Cleaning
    for element in window.grid_slaves():
        element.grid_forget()
    window.title("Find")

    # Building and styling
    title = tk.Label(text="Find", height=5, width=30, font=10)
    user_name_entry = tk.Entry(width=20)
    user_age_entry = tk.Entry(width=20)

    # Button calls for lambda function on click
    back = tk.Button(text="Menu", width=10, height=2,
                     command=lambda: buildMenu(db, window))
    submit = tk.Button(text="Submit", width=20, height=2, command=lambda: find(
        user_name_entry, user_age_entry, db))

    # Displaying
    title.grid(column=1, row=0)
    tk.Label(text="Name").grid(column=0, row=2)
    user_name_entry.grid(column=1, row=2)
    tk.Label(text="Age").grid(column=0, row=3)
    user_age_entry.grid(column=1, row=3)
    submit.grid(column=1, row=4)
    back.grid(column=1, row=5)
    window.mainloop()


def insertOne(username, userage, db):
    # Inserts into DB the values and clears them
    db.users.insert_one(
        {"name": username.get(), "age": int(userage.get())}).inserted_id
    print(username.get(), int(userage.get()),
          "was succesfully inserted into", db.name)
    username.delete(0, END)
    userage.delete(0, END)


def deleteOne(username, userage, db):
    # Inserts into DB the values and clears them
    db.users.delete_one(
        {"name": username.get(), "age": int(userage.get())})
    print(username.get(), int(userage.get()),
          "was succesfully deleted from", db.name)
    username.delete(0, END)
    userage.delete(0, END)


def deleteMany(username_entry, userage_entry, db):
    if userage_entry.get() == "" and username_entry.get() == "":
        failLabel = tk.Label(
            text='No se puede hacer delete sin filtrar').grid(column=1, row=1)
        print("Error, no se puede hacer delete sin filtrar")
    elif userage_entry.get() == "":
        db.users.delete_many({'name': username_entry.get()})
        print('Deleted all docs with name: ' + username_entry.get())
    elif username_entry.get() == "":
        db.users.delete_many({'age': int(userage_entry.get())})
        print('Deleted all docs with age: ' + userage_entry.get())
    else:
        db.users.delete_many(
            {'name': username_entry.get(), 'age': int(userage_entry.get())})
        print('Deleted all docs with name: ' +
              username_entry.get() + ' and age: '+userage_entry.get())
    username_entry.delete(0, END)
    userage_entry.delete(0, END)


def find(username_entry, userage_entry, db):
    findRes = tk.Tk()
    findRes.title("Result")
    if userage_entry.get() == "" and username_entry.get() == "":
        for doc in db.users.find({}, {'_id': 0}):
            tempLabel = tk.Label(findRes, text=doc).pack()
            print(doc)
    elif userage_entry.get() == "":
        for doc in db.users.find({'name': username_entry.get()}, {'_id': 0}):
            tempLabel = tk.Label(findRes, text=doc).pack()
            print(doc)
    elif username_entry.get() == "":
        for doc in db.users.find({'age': int(userage_entry.get())}, {'_id': 0}):
            tempLabel = tk.Label(findRes, text=doc).pack()
            print(doc)
    else:
        for doc in db.users.find({'name': username_entry.get(), 'age': int(userage_entry.get())}, {'_id': 0}):
            tempLabel = tk.Label(findRes, text=doc).pack()
            print(doc)
    username_entry.delete(0, END)
    userage_entry.delete(0, END)


if __name__ == "__main__":
    main()
