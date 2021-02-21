initial = 67
print('Mini "Guess the number" game, Enter "0" to exit program')
number = int(input('Enter number to guess: '))
while number != initial:
    if number > initial and number != 0:
        print('The number is greater than initial, try again ...')
        number = int(input('Enter number to guess: '))
    elif number < initial and number != 0:
        print('The number is less than initial, try again ... ')
        number = int(input('Enter number to guess: '))
    elif number == 0:
        exit()
else:
    print('Congratulations, You Won!')
    exit()
