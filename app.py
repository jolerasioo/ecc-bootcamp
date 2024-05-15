from flask import Flask, render_template, request, redirect, url_for, g
import os

from database import db, Todo


app = Flask(__name__)

todo_list = []

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "todos.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# database initialization
db.init_app(app)
with app.app_context():
    db.create_all()

# file to store the to-do list
@app.before_request
def load_data_to_g():
    todos = Todo.query.all()
    g.todos = todos
    g.todo = None

# index or home page
@app.route("/")
def index():
    return render_template("index.html")

# add a to-do item
@app.route("/add", methods=["POST"])
def add_todo():
    # get the data from the form
    todo = Todo(
        name=request.form["todo"],
    )

    # add the new ToDo to the list
    db.session.add(todo)
    db.session.commit()
    
    # add the new ToDo to the list
    return redirect(url_for("index"))

# remove a to-do item
@app.route("/remove/<int:id>", methods=["GET", "POST"])
def remove_todo(id):
    db.session.delete(Todo.query.filter_by(id=id).first())
    db.session.commit()
    return redirect(url_for("index"))




if __name__ == "__main__":
    app.run(debug=True)

# #continue to loop and display menu until user selects to exit the program
# while True:
#     print() # Add a couple of blank lines
#     print()
#     print("To-do list: ") # Print the title of the list
#     item_number = 1
#     for todo in todo_list: # Loop through existing to-do items
#         print(f'{item_number}: {todo}')
#         item_number += 1
# 
# # Print the menu
#     print() # Add a of blank lines
#     print("Actions:")
#     print("A - Add to-do item")
#     print("R - Remove to-do item")
#     print("X - Exit")
#     choice = input("Enter your choice (A, R, or X): ")
#     choice = choice.upper() #converts the choice to uppercase
# 
#     #user selected 'a' or 'A' - To Add an item to the list
#     if choice == "A":
#         todo = input("Enter the to-do item: ")
#         todo_list.append(todo)
#         continue  #tells the program to go back to the start of the loop
# 
#     #user selected 'r' or 'R' - To Remove an item from the list
#     if choice == "R":
#         item_number = int(input("Enter the number of the item to remove: "))
#         if item_number > 0 and item_number <= len(todo_list):
#             todo_list.pop(item_number - 1)
#         else:
#             print("Invalid item number")
#         continue
# 
#     #user 1 selected 'x' or 'X' to exit programs
#     if choice == "X":
#         #on exit save your current list to a file
#         print("Saving to-do list to file")
#         with open("todo_list.txt", "w") as file:
#             for todo in todo_list:
#                 file.write(todo + "\n")
# 
#         break #tells the program to exit the loop
# 
#     #user selected something else
#     print("Invalid choice")
# 
# 
#     