def fizzBuzz(n):
    for num in range(1,n+1):
        if num % 3 == 0 and num % 5 == 0:
            print('Bitmaker')
        elif num % 3 == 0:
            print('Bit')
        elif num % 5 == 0:
            print('Maker')
        else:
            print(num)

fizzBuzz(100)
