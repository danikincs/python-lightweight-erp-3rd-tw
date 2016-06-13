# implement commonly used functions here

import random
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
