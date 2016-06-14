# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


# importing everything you need
import os
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
#


def handle_menu():
    options = ["Show table",
               "Add to table",
               "Remove from table",
               "Update table",
               "Available kinds of games by manufacturers",
               "Average amount of games by manufacturers"]

    ui.print_menu("Store manager", options, "0: Back to main menu")


def start_module():
    handle_menu()
    inputs = ui.get_inputs(["Please enter a number: "], "")
    table = data_manager.get_table_from_file("store/games.csv")
    option = inputs[0]
    back_to_main = 0
    while not back_to_main:
        try:
            if option == "1":
                show_table(table)
            elif option == "2":
                add(table)
            elif option == "3":
                id_ = ui.get_inputs("Enter what you want to delete:", "")
                remove(table, id_)
            elif option == "4":
                id_ = ui.get_inputs("Enter what you want to update(id):", "")
                update(table, id_)
            elif option == "5":
                get_counts_by_manufacturers(table)
            elif option == "6":
                get_average_by_manufacturer(table)
            elif option == "0":
                back_to_main = 1
            else:
                raise KeyError
            break
        except KeyError:
            ui.print_error_message("There's no such option.")
            start_module()


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ['id', 'title', 'manufacturer', 'price', 'in_stock']
    ui.print_table(table, title_list)
    # your code
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    common.add_to_table(table, "store/store.csv")

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    common.remove_form_table(table, "store/store.csv", id_)

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    common.update_the_table(table, "store/store.csv", id_)

    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):

    # your code

    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):

    # your code

    pass
