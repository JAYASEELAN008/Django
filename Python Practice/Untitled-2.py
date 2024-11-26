add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b

while True:
    print("""\nEnter
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit""")
    try:
        choice = int(input('\nEnter choice: '))
    except:
        print('Enter integer values only!')
        continue
    if 1<=choice<=5:
        if choice==5:
            print('Exiting...\n')
            break
        numbers = [int(i) for i in input('Enter numbers: ').split()]
        if choice==1:
            print('\nResult is: ', add(numbers[0], numbers[1]), '\n')
            continue
        if choice==2:
            print('\nResult is: ', subtract(numbers[0], numbers[1]), '\n')
            continue
        if choice==3:
            print('\nResult is: ', multiply(numbers[0], numbers[1]), '\n')
            continue
        if choice==4:
            print('\nResult is: ', divide(numbers[0], numbers[1]), '\n')
            continue
    else:
        print('Enter choice between 1 and 5')