# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


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
def start_module():
    options = ["Print default records",
               "Add new record",
               "Remove record by id",
               "Update record by id",
               "Find item with the lowest price",
               "Find items sold between dates"]

    ui.print_menu("Sellings of the company", options, "0: Return to main menu")
    inputs = ui.get_inputs("Please enter a number: ", "")
    table = data_manager.get_table_from_file("selling/sellings.csv")
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
            id_ = ui.get_inputs("Enter what you want to update(id):", "")
            update(table, id_)
        elif option == "5":
            get_lowest_price_item_id(table)
        elif option == "6":
            get_items_sold_between \
            (table, month_from, day_from, year_from, month_to, day_to, year_to)
        elif option == "0":
            main.main()
        else:
            raise KeyError("There is no such option.")
    except KeyError as err:
        ui.print_error_message(err)
        start_module()
    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "title", "price", "month", "day", "year"]
    ui.print_table(table)
    start_module()

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    common.add_to_table(table, "selling/sellings.csv")
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    remove_form_table(table, "selling/sellings.csv", id_)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    update_the_table(table, "selling/sellings.csv", id_)
    return table


# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order
def get_lowest_price_item_id(table):
    lowest_priced_items = {}
    for line in table:
        if int(line[2]) in lowest_priced_items:
            lowest_priced_items[int(line[2])].append(line[0])
        else:
            lowest_priced_items[int(line[2])] = [line[0]]
    lowest_priced_item = min(lowest_priced_items.items())
    if len(lowest_priced_item[1]) > 1:
        lowest_priced_item = min(lowest_priced_item[1])
    else:
        lowest_priced_item = lowest_priced_item[1][0]
    return lowest_priced_item
    pass


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):

    # your code

    pass
