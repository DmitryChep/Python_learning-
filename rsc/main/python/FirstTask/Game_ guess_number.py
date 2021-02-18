import random

num = random.randint(1, 5)
cnt = 0
while True:
    cnt += 1
    try:
        user_num = int(input('Quess number from 1 to 5. Please enter the number: '))
    except ValueError:
        print('It\'s not number')
        cnt -= 1
        continue
    if user_num == num:
        print(f'Congratulations you guessed the number for {cnt} tries!Thanks for your game)')
        if input('Do you want play again ? y|n:') == 'y':
            num = random.randint(1, 5)
            cnt = 0
        else:
            print('Thanks for your game)')
            break
    elif user_num > num:
        print(f'No! Your number is more.')
        if input('Do you want play again ? y|n:') == 'y':
            num = random.randint(1, 5)
        else:
            print('Thanks for your game)')
            break
    else:
        print(f'No! Your number is less. ')
        if input('Do you want play again ? y|n:') == 'y':
            num = random.randint(1, 5)
        else:
            print('Thanks for your game)')
            break
