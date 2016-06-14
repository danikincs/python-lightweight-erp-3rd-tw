# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
import main
import time
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
table = ''
list1 = ''


def start_module():
    ui.print_menu("Human Resources", ["show", "add", "remove", "update"], "0 exit")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    table = data_manager.get_table_from_file("hr/persons.csv")
    try:
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            remove(table, id_)
        elif option == "4":
            update(table, id_)
        elif option == "0":
            main.main()
        else:
            raise KeyError
    except KeyError:
        ui.print_error_message("There is no such option.")
        start_module()
    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    list1 = ['id', 'name', 'birth_date']
    ui.print_table(table, list1)
    time.sleep(0.5)
    start_module()

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    added_item = ui.get_inputs("Please type in a name:", "")
    added_items = added_item.split(",")
    added_items.insert(0, common.generate_random(table))
    table.append(added_items)
    show_table(table)

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    for sublist in table:
        if id_ in sublist:
            table.remove(sublist[:])
    show_table(table)

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    added_item = ui.get_inputs("Type what what would you like to modify:", "")
    for sublist in table:
        if id_ in sublist:
            table.remove(sublist[:])
            added_items = added_item.split(",")
            added_items.insert(0, id_)
            table.append(added_items)
    show_table(table)

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass
