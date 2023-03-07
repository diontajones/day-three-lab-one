while True:
    num = int(input('Please enter a whole number: '))
    print('Number\tSquare\tCube')

    for a in range(1, num + 1):
        square = a ** 2
        cube = a ** 3
        print(f'{a:6}\t{square:6}\t{cube:4}')

    response = input('Do you want to continue? (y/n): ')
    if response.lower() == 'n':
        break


