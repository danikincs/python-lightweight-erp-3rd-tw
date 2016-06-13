# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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
table = data_manager.get_table_from_file("tool_manager/tools.csv")


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    options = ["Print default records",
               "Add new record",
               "Remove record by id",
               "Update record by id",
               "Avalible tools",
               "Customers subscribed to the newsletter"]

    ui.print_menu("Customer relationship management (CRM)", options, "0: Return to main menu")
    inputs = ui.get_inputs("Please enter a number: ", "")
    option = inputs[0]
    try:
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            id_ = ui.get_inputs("Enter what you want to delete:", "")
            remove(table, id_)
        elif option == "4":
            update()
        elif option == "5":
            get_available_tools()
        elif option == "6":
            get_average_durability_by_manufacturers()
        elif option == "0":
            main.main()
        else:
            raise KeyError("There is no such option.")
    except KeyError as err:
        ui.print_error_message(err)
    pass

# print the default table of records from the file
#
# @table: list of lists


def show_table(table):
    title_list = ['id', 'name', 'manufacturer', 'purchase_date', 'durability']
    ui.print_table(table, title_list)
    start_module()

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    added_item = ui.get_inputs("Enter what you want to add:", "")
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

    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table):

    # your code

    pass


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):

    # your code

    pass
