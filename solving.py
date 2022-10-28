def same_digits(num):
    for i in range(len(num)):
        if num[0] != num[i]:
            print('NO')
            return
    print('YES')


num = str(input())
same_digits(num)
