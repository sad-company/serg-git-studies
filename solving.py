def same_digits(num):
    if max(num) == min(num):
        print("YES")
    else:
        print('NO')


num = str(input())
same_digits(num)
