def get_divider(numb):
    divider = 2
    while numb % divider != 0:
        divider += 1
    print(divider)


numb = int(input())
get_divider(numb)
