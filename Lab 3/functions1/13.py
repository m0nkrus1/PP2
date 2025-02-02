from random import randint

def guess():
    name = input('Hello! What is your name? ')
    print("Well, " + name + ', I am thinking of a number between 1 and 20.')

    num = randint(1, 20)
    cnt = 0
    
    while(True):
        print("Take a guess.")
        guessed_num = int(input())
        cnt += 1
        
        if guessed_num < num:
            print("Your guess is too low.")
        elif guessed_num > num:
            print("Your guess is too high.")
        else:
            print("Good job, " + name + "! You guessed my number in " + str(cnt) + " guesses")
            break

guess()
