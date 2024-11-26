# #calculator

# add=lambda a,b:a+b
# sub=lambda a,b:a-b
# mul=lambda a,b:a*b
# div=lambda a,b:a/b


# while True:
#     print("""\nEnter
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit""")
#     value=" "
#     for a in value:
#         value = int(input('\nEnter choice: '))
#         continue
#     if 1<=value<=5:
#         if value==5:
#             print('Exiting...\n')
#             break
#         numbers = [int(i) for i in input('Enter numbers: ')]
#         numbers = [int(i) for i in input('Enter numbers: ')]
#         if value==1:
#             print('\nResult is: ', add(numbers[0], numbers[1]), '\n')
#             continue
#         if value==2:
#             print('\nResult is: ', sub(numbers[0], numbers[1]), '\n')
#             continue
#         if value==3:
#             print('\nResult is: ', mul(numbers[0], numbers[1]), '\n')
#             continue
#         if value==4:
#             print('\nResult is: ', div(numbers[0], numbers[1]), '\n')
#             continue
#     else:
#         print('Enter choice between 1 and 5')


# class Python(n):
#     return n+n



    print("Addition: 5 + 3 =", calc.add(5, 3))
    print("Subtraction: 10 - 4 =", calc.subtract(10, 4))
    print("Multiplication: 6 * 7 =", calc.multiply(6, 7))
    
    try:
        print("Division: 8 / 2 =", calc.divide(8, 2))
        print("Division: 8 / 0 =", calc.divide(8, 0))
    except ValueError as e:
        print(e)    























