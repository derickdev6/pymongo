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
    buildInterface(db)


def buildInterface(db):
    window = tk.Tk()
    # Building and styling
    title = tk.Label(text="MongoDB GUI InsertOne",
                     height=5, width=30, font=10)
    user_name_entry = tk.Entry(width=20)
    user_age_entry = tk.Entry(width=20)

    # Button calls for lambda function on click
    submit = tk.Button(text="Submit", width=20, height=2, command=lambda: insertOne(
        user_name_entry, user_age_entry, db))

    # Displaying
    title.pack()
    tk.Label(text="Name").pack()
    user_name_entry.pack()
    tk.Label(text="Age").pack()
    user_age_entry.pack()
    submit.pack()
    window.mainloop()


def insertOne(username, userage, db):
    # Inserts into DB the values and clears them
    db.users.insert_one(
        {"name": username.get(), "age": int(userage.get())}).inserted_id
    print(username.get(), int(userage.get()),
          "was succesfully inserted into", db.name)
    username.delete(0, END)
    userage.delete(0, END)


if __name__ == "__main__":
    main()
