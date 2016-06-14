# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


# importing everything you need
import main
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
               "Get average durability"]

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
            id_ = ui.get_inputs("Enter what you want to update(id):", "")
            update(table, id_)
        elif option == "5":
            get_available_tools(table)
        elif option == "6":
            get_average_durability_by_manufacturers(table)
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
    common.add_to_table(table, "tool_manager/tools.csv")

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    common.remove_form_table(table, "tool_manager/tools.csv", id_)

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    common.update_the_table(table, "tool_manager/tools.csv", id_)

    return table


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table):
    date = []
    remain_year = []
    for sublist in table:
        date.append(int(sublist[3]))
    for sublist in table:
        remain_year.append(int(sublist[4]))
    sum_year = [x + y for x, y in zip(date, remain_year)]
    number = []
    a = 0
    avalible = []
    line = 1
    result = []
    # print(sum_year)
    for i in sum_year:
        if i >= 2016:
            a += 1
            number.append(a)
    print(number)
    for sublist in table:
        if line in number:
            result.append(sublist)
            line += 1

    ui.print_result(result, "Avalible resources")
    return(result)


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):
    # manufacturers = []
    # for sublist in table:
    #     if sublist[2] not in manufacturers:
    #         manufacturers.append(sublist[2])
    # print(manufacturers)
    # manufacturer_1 = []
    # manufacturer_2 = []
    # manufacturer_3 = []
    # result = {}
    # for sublist in table:
    #
    #     # for i in manufacturers:
    #     #     if i in sublist:
    #     #         if manufacturers not in manufacturer_2:
    #     #             manufacturer_2.append(sublist[4])
    #     # for i in manufacturers:
    #     #     if i in sublist:
    #     #         if manufacturers not in manufacturer_2:
    #     #             manufacturer_2.append(sublist[4])
    # print(manufacturer_1)
    # sony_avarage = {"Sony": 0}
    # s_b = 0
    # s_a = 0
    # for elem in sony:
    #     s_a += int(elem)
    #     s_b += 1
    # s_a = s_a / s_b
    # sony_avarage["Sony"] = float(s_a)
    # microsoft_avarage = {"Microsoft": 0}
    # m_b = 0
    # m_a = 0
    # for elem in microsoft:
    #     m_a += int(elem)
    #     m_b += 1
    # m_a = m_a / m_b
    # microsoft_avarage["Microsoft"] = float(m_a)
    # nintendo_avarage = {"Nintendo": 0}
    # n_b = 0
    # n_a = 0
    # for elem in nintendo:
    #     n_a += int(elem)
    #     n_b += 1
    # n_a = n_a / n_b
    # nintendo_avarage["Nintendo"] = n_a
    # result.update(sony_avarage)
    # result.update(nintendo_avarage)
    # result.update(microsoft_avarage)
    #
    # print(result)
    # return result
    # # your code

    pass
