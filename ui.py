# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table


def sum_table_width(col_width):
    table_width = 0
    for i in col_width:
        table_width += i
    return table_width


def column_width(table):
    col_width = [0] * len(table[0])
    for row in table:
        i = 0
        for element in row:
            if len(str(element)) > col_width[i]:
                col_width[i] = len(str(element))
            i += 1
    return col_width


def print_table(table, title_list):
    table.insert(0, title_list)
    col_width = column_width(table)
    tw = sum_table_width(col_width)
    print('/{0:-^{w}}'.format('-', w=tw + len(col_width)-1), end="\\\n")
    for i, row in enumerate(table, start=1):
        for j, element in enumerate(row, start=1):
            if j < len(row):
                print('|{0:^{w}}'.format(element, w=col_width[j-1]), end="")
            elif j == len(row):
                print('|{0:^{w}}'.format(element, w=col_width[j-1]), end="|\n")
        if i < len(table):
            for j, element in enumerate(row, start=1):
                if j < len(row):
                    print('|{0:-^{w}}'.format('-', w=col_width[j-1]), end="")
                elif j == len(row):
                    print('|{0:-^{w}}'.format('-', w=col_width[j-1]), end="|\n")
    print('\{0:-^{w}}'.format('-', w=tw + len(col_width)-1), end="/\n")


    # for element in title_list:
    #
    # for row in table:
    #     for i, element in row:

    # print(title_list)
    # for sublist in table:
    #     print(sublist)
    # for sublist in table:
    #     max_lenght = ""
    #     for i in sublist:
    #         max_lenght += i.strip(", " "")
    #     maxis = (len(max_lenght))
    #     for i in str(maxis):
    #         print(max(i))
    #     # for i in sublist:
    #     #     formatter = "{" + i + ":>"
    pass


# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):
    print(label)
    print(result)

    pass


# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):
    print(title)
    a = 1
    for items in list_options:
        print(a, items)
        a += 1
    print(exit_message)

    # your code

    pass


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    inputs = []
    inputs = input(list_labels)
    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    print(message)

    # your code

    pass
