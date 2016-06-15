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
    ui.print_menu("Human Resources", ["show", "add", "remove", "update", "oldest", "average"], "0 exit")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    table = data_manager.get_table_from_file("hr/persons.csv")
    try:
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            id_ = ui.get_inputs("Enter the item/'s id you want to remove:","")
            remove(table, id_)
        elif option == "4":
            id_ = ui.get_inputs("Enter the item/'s id you want to update:","")
            update(table, id_)
        elif option == "5":
            get_oldest_person(table)
        elif option == "6":
            get_persons_closest_to_average(table)
        elif option == "0":
            main.main()
        else:
            raise KeyError
    except KeyError:
        ui.print_error_message("There is no such option, choose from given numbers.")
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
    common.add_to_table(table, "hr/persons.csv")

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    common.remove_form_table(table, "hr/persons.csv", id_)

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    common.update_the_table(table, "hr/persons.csv", id_)

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    oldest_person = 0
    birth_date = []
    person = []
    for sublist in table:
        birth_date.append(int(sublist[2]))
    oldest = min(birth_date)
    for line in table:
        if int(line[2]) == oldest:
            person.append(line[1])
    return person


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    name = []
    year = []
    total = 0
    nr_people = 0
    for row in table:
        nr_people += 1
        total = total + int(row[2])
        name.append(row[1])
        year.append(int(row[2]))
    average = total/nr_people
    final = []
    difference = []
    for element in year:
        if element < average:
            difference.append(average - element)
        elif element > average:
            difference.append(element - average)
        else:
            difference.append(0)
    mini = None
    for element in difference:
        if mini is None:
            mini = element
        if mini > element:
            mini = element
    i = 0
    for elem in difference:
        if mini == elem:
            final.append(name[i])
        i += 1
   # ui.print_result(final, "The people closest to the average age is/are: ")
    return final
