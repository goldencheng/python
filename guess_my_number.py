"""
File: guess_my_number.py
Name:
-----------------------------
This program plays a Console game
"Guess My Number" which asks user
to input a number until he/she gets it
"""

# This number controls when to stop the game
SECRET1 = 82
EEEE = 99
print('guess a numbur 0-99')
def main():
    ans = int(input('guess'))
    while SECRET1 != ans:
        if ans > EEEE:
            print('out of 99')
        if ans > SECRET1:
            print('too big!')
        if ans < SECRET1:
            print('too small!')
        ans = int(input('guess'))
    print('you got it!:',end='')
    print( SECRET1)










































































































































































































### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
