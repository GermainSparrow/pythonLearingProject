def trim(str):
    i = 0

    while str[0:i] == '':
        i += 1
    str = str[i:]

    # i = -1

    # while str[i:] == '':
    #     i -= 1
    # str = str[:-i]

    return str

print('12345')