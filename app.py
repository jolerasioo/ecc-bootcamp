from flask import Flask, render_template, request, redirect, url_for
import os


app = Flask(__name__)

todo_list = []

basedir = os.path.abspath(os.path.dirname(__file__))
todo_file = os.path.join(basedir, "todo_list.txt")


try:
    with open("todo_list.txt", "r") as file:
        for line in file:
            todo_list.append(line.strip())
except FileNotFoundError:
    print("No saved items found")

@app.route("/")
def index():
    return render_template("index.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add_todo():
    todo = request.form["todo"]
    todo_list.append(todo)
    save_todo_list()
    return redirect(url_for("index"))

@app.route("/remove", methods=["POST"])
def remove_todo():
    item_number = int(request.form["item_number"])
    if 0 < item_number <= len(todo_list):
        todo_list.pop(item_number - 1)
        save_todo_list()
    return redirect(url_for("index"))


def save_todo_list():
    with open(todo_file, "w") as file:
        for todo in todo_list:
            file.write(todo + "\n")



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