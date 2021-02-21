import time
initial = 46


def numbers():
    number = int(input('Enter number to guess: '))
    if number < initial:
        print('Number is less than ...')
    elif number > initial:
        print('Number is more than ...')
    else:
        print('Congratulations, you win!')
        exit()


numbers()
time.sleep(0.5)
reset = input('Enter yes to try again, or no to exit: ')
while reset == 'yes':
    numbers()
time.sleep(0.7)
exit()
