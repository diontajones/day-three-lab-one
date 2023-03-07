name = input('Hello, what is your name?: ')

while True:

    random_int = int(input('Enter a number between 1 and 100: '))

    if random_int % 2 == 1 and 0 < random_int < 60:
        print(name + ' you entered ' + str(random_int) + ' and it is odd and less than 60')
    elif random_int % 2 == 0 and 24 >= random_int >= 2:
        print(name + ' your number is even and less than 25')
    elif random_int % 2 == 0 and 60 >= random_int >= 26:
        print(name + ' your number is even and between 26 and 60 inclusive')
    elif random_int % 2 == 0 and 101 > random_int > 60:
        print(name + ' your number is even and greater than 60')
    elif random_int % 2 == 1 and 101 > random_int > 60:
        print(name + ' you entered ' + str(random_int) + ' , and it is odd and greater than 60')
    elif random_int > 100 or random_int < 1:
        print('Invalid Answer')

    response = input('Do you want to continue? (y/n): ')
    if response.lower() == 'n':
        break















