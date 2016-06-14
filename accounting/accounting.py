# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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
def handle_menu():
    options = ["Show table",
               "Add to table",
               "Remove from table",
               "Update table",
               "The highest profit according to year",
               "Average profit per item in a given year"]

    ui.print_menu("Accounting", options, "0: Back to main menu")


def start_module():
    handle_menu()
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    table = data_manager.get_table_from_file("accounting/items.csv")
    back_to_main = False
    while not back_to_main:
        try:
            if option == "1":
                show_table(table)
            elif option == "2":
                add(table)
            elif option == "3":
                id_ = ui.get_inputs("What item would you like to delete:", "")
                remove(table, id_)
            elif option == "4":
                id_ = ui.get_inputs("Which item would you like to update:", "")
                update(table, id_)
            elif option == "5":
                which_year_max(table)
            elif option == "6":
                avg_amount(table)
            elif option == "0":
                back_to_main = True
            else:
                raise KeyError
            break
        except KeyError:
            ui.print_error_message("Press the key to get the need option!")
            start_module()


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "month", "day", "year", "type", "type", "amount"]
    ui.print_table(table)
    start_module()
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    common.add_to_table(table, "items.csv")
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    common.remove_form_table(table, "items.csv", id_)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    common.update_the_table(table, "items.csv", id_)
    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
