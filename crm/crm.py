# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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
    table = data_manager.get_table_from_file("crm/customers_test.csv")
    options = ["- Print default records",
               "- Add new record",
               "- Remove record by id",
               "- Update record by id",
               "- ID of customer with the longest name",
               "- Customers subscribed to the newsletter"]

    ui.print_menu("\nCustomer relationship management (CRM)\n", options, "0 - Return to main menu\n")
    inputs = ui.get_inputs("Please enter a number: ", "")
    option = inputs[0]
    while True:
        try:
            if option == "1":
                show_table(table)
            elif option == "2":
                add(table)
            elif option == "3":
                remove(table, id_=ui.get_inputs("Enter the id of the record you'd like to remove: ", ""))
            elif option == "4":
                update(table, id_=ui.get_inputs("Enter the id of the record you'd like to update: ", ""))
            elif option == "5":
                get_longest_name_id(table)
            elif option == "6":
                get_subscribed_emails(table)
            elif option == "0":
                break
            else:
                raise KeyError
            break
        except KeyError:
            ui.print_error_message("\nThere is no such option.")
            start_module()
    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "name", "email", "subscribed"]
    ui.print_table(table, title_list)

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    common.add_to_table(table, "crm/customers_test.csv")

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):

    common.remove_form_table(table, "crm/customers_test.csv", id_)

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    common.update_the_table(table, "crm/customers_test.csv", id_)

    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):
    max_name_length = 0
    longest_names = []
    for i in table:
        if len(i[1]) > max_name_length:
            max_name_length = len(i[1])
    for i in table:
        if max_name_length == len(i[1]):
            longest_names.append(i[1])
    first_longest_name = min(longest_names)
    for i in table:
        if first_longest_name in i:
            ui.print_result(i[0], "ID of the longest (alphabetical first, if there's more than one) name:")
            return i[0]
    pass


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    subscribers = []
    for i in table:
        if i[3] == "0":
            subscribers.append("{0};{1}".format(i[2], i[1]))
    ui.print_result(subscribers, "Names and emails of newsletter subscribers")
    return subscribers
    pass
