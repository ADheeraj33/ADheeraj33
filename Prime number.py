n = eval(input('Enter a number: '))
if n > 1:
    for i in range(2, int(n+1/2)):
        if n % i == 0:
            print(n, 'is not a prime.')
            break
    else:
        print(n, 'is a prime')
else:
    print(n, 'is not a prime')
