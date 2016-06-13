# implement commonly used functions here

import random
# table = "ASDRF"
# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)


def generate_random(table):
    character_lists = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789', '!@#$%^&*()?']
    length = 8
    while True:
        generated = ''
        used = [False, False, False, False]
        all_used = [True, True, True, True]
        for i in range(length):
            a = random.randint(0, 3)
            used[a] = True
            s = character_lists[a]
            b = random.randint(0, len(s) - 1)
            generated += s[b]
        if used == all_used:
            return generated
            break
        if generated in table:
            return
    # if generated in table:
    #     True

    # your code
generate_random(table)
