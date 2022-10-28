def get_range(numb):
    for i in range(1, numb + 1, 1):
        if (5 <= i <= 9) or (17 <= i <= 37) or (78 <= i <= 87):
            continue
        else:
            print(i)


numb = int(input())
get_range(numb)
