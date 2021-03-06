# implement commonly used functions here
import ui
import random
import common
import data_manager
# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)


def format_inst(file_name):  # module dependant format instructions, only to be used inside common.py
    table_attribute = ""
    file_list = [
        "accounting/items.csv",
        "crm/customers.csv",
        "hr/persons.csv",
        "selling/sellings.csv",
        "store/games.csv",
        "tool_manager/tools.csv"
        ]
    attribute_list = [
        "<month>;<day>;<year>;<type>;<amount>",
        "<name>;<email>;<subscribed(1/0)>",
        "<name>;<birth year>",
        "<title>;<price>;<month>;<day>;<year>",
        "<title>;<manufacturer>;<price>;<stock>",
        "<name>;<manufacturer>;<purchase year>;<durability>"
        ]
    for i, j in enumerate(file_list):
        if j == file_name:
            table_attribute = attribute_list[i]
    return table_attribute


def add_to_table(table, file_name):
    added_item = ui.get_inputs("Enter what you want to add (format: {0}):".format(format_inst(file_name)), "")
    added_items = added_item.split(",")
    added_items.insert(0, common.generate_random(table))
    table.append(added_items)
    data_manager.write_table_to_file(file_name, table)


def remove_form_table(table, file_name, id_):
    for sublist in table:
        if id_ in sublist:
            table.remove(sublist[:])
    data_manager.write_table_to_file(file_name, table)


def update_the_table(table, file_name, id_):
    added_item = ui.get_inputs("Enter what you want to update (format: {0}):".format(format_inst(file_name)), "")
    for sublist in table:
        if id_ in sublist:
            table.remove(sublist[:])
            added_items = added_item.split(",")
            added_items.insert(0, id_)
            table.append(added_items)
    data_manager.write_table_to_file(file_name, table)


def generate_random(table):
    character_lists = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789', '!@#$%^&*()?']
    length = 8
    while True:
        generated = ''
        used = [False, False, False, False]
        all_used = [True, True, True, True]
        for i in range(2):
            a = 0
            s = character_lists[a]
            b = random.randint(0, len(s) - 1)
            generated += s[b]
            used[a] = True
        for i in range(2):
            a = 1
            s = character_lists[a]
            b = random.randint(0, len(s) - 1)
            generated += s[b]
            used[a] = True
        for i in range(2):
            a = 2
            s = character_lists[a]
            b = random.randint(0, len(s) - 1)
            generated += s[b]
            used[a] = True
        for i in range(2):
            a = 3
            s = character_lists[a]
            b = random.randint(0, len(s) - 1)
            generated += s[b]
            used[a] = True

        if generated in table:
            generate_random(table)

        if used == all_used:
            return generated
            break

        if generated in table:
            return
    # if generated in table:
    #     True

    # your code
