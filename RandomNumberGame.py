import random


def star():
    for i in range(20):
        print('*', end='')


star()
print("LETS START THE GAME", end='')
star()
print('')

# Player Input
Start = int(input('Enter the Starting point  : '))

End = int(input('Enter the Ending point : '))

Guess = int(input('Guess the number = '))

space = End - Start
Points = 0
if 100 >= space > 90:
    Points = 100
    print('Your got 100 Points')
elif 90 >= space > 80:
    Points = 90
    print('Your got 90 Points')
elif 80 >= space > 70:
    Points = 80
    print('Your got 80 Points')
elif 70 >= space > 60:
    Points = 70
    print('Your got 70 Points')
elif 60 >= space > 50:
    Points = 60
    print('Your got 60 Points')
elif 50 >= space > 40:
    Points = 50
    print('Your got 50 Points')
elif 40 >= space > 30:
    Points = 40
    print('Your got 40 Points')
elif 30 >= space > 20:
    Points = 30
    print('Your got 30 Points')
elif 20 >= space > 10:
    Points = 20
    print('Your got 20 Points')
else:
    Points = 10
    print('Your got 10 Points')

# Random number generator
Number = random.randint(Start, End)

# Mechanism
while Number != "Guess":
    if Guess > Number:
        print('You are a bit higher than the no')
        Guess = int(input('Guess the number again = '))
        Points = Points - 10
        if Points == 0:
            print('NOT ENOUGH POINTS')
            break
        else:
            print(Points)
    elif Guess < Number:
        print('You are a bit lower than the number')
        Guess = int(input('Guess the number again = '))
        Points = Points - 10
        if Points == 0:
            print('NOT ENOUGH POINTS')
            break
        else:
            print(Points)
    else:
        print('You guessed the right no')
        star()
        print('GAME OVER', end='')
        star()
        break
