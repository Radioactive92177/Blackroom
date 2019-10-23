import random

def star():
    for i in range(20):
        print('*',end='')


star()
print("LETS START THE GAME",end='')
star()
print('')

#Player Input
Start = int(input('Enter the Starting point  : '))

End = int(input('Enter the Ending point : '))

Guess = int(input('Guess the number = '))


#Random number generator
Number = random.randint(Start, End)



#Mechanism
while(Number!="Guess"):
    if Guess>Number:
         print('You are a bit higher than the no')
         Guess = int(input('Guess the number again = '))
    elif Guess<Number:
        print('You are a bit lower than the number')
        Guess = int(input('Guess the number again = '))
    else:
         print('You guessed the right no')
         star()
         print('GAME OVER',end='')
         star()
         break
