# Random number Game
import random
import math

def RandomGenerator(num1,num2):
    randomNumber = random.randint(num1,num2+1)
    return randomNumber

def AutoRandomGenerator():
    randomNumber = random.randint(1,101)
    return randomNumber

def ComputerGuess():
    input_str = input("type in the range of the guessing game with 2 seperate positive integer: ")
    str1 , str2 = input_str.split()
    low , high = int(str1) , int(str2)
    if high < low:
        low , high = high, low
    computer = random.randint(low, high + 1) # computer is not the best name but it's what computer is gussed
    choise = ""
    while True:
        choise = input(f"is {computer} too high (H), too low (L), or correct (C)? ").lower()
        if choise == 'h':
            high = computer - 1
        if choise == 'l':
            low = computer + 1
        if choise != 'c':
                    if low > high:
                        print(f"Your guess is {computer}! Don't lie!\n##########\n#####\n###")
                        return  
                    computer = random.randint(low, high)
        if choise == 'c':
                print(f"Your number is {computer}\n##########\n#####\n###")
                return


    #main()



def main():


    print("Welcome!")
    while True:
        print("Choose the type of game or type 0 to exit:")
        choise = input("1.Play with Range of 1 to 100\n2.Play with Custom Range\n3.Play with computer guessing your choosen number\n")
        if choise == "1":
            randomNumber = AutoRandomGenerator()
            totalTry = round(math.log(100,2))
            break
        elif choise == "2":
            input_str = input("type in 2 positive numbers separated by space: ")
            num1_str,num2_str = input_str.split()
            num1,num2 = int(num1_str),int(num2_str)
            if num2 > num1:
                num1,num2 = num2,num1
            randomNumber = RandomGenerator(num1,num2)
            totalTry = round(math.log(num2-(num1+1),2))
            break
        elif choise == "3":
            ComputerGuess()
        elif choise == "0":
            print("goodbye")
            return 0
        else:
            print("Invalid Input")
    
    print(f"Your total number of guesses you have is: {totalTry}")
    print("Let's Play! :P")
    while totalTry != 0:
        inNumber = int(input("Your Guess: "))
        if inNumber > randomNumber:
            print("You guessed Higher!")
            totalTry -=1
            print(f"Your total number of guesses you have is: {totalTry}")
        if inNumber < randomNumber:
            print("You guessed lower!")
            totalTry -=1
            print(f"Your total number of guesses you have is: {totalTry}")
        if inNumber == randomNumber:
            print("GG. You guessed Right!")
            main()
        '''if totalTry == 0:
            print("You loose!\nBetter Luck Next Time.")
            main()'''
    print("You loose!\nBetter Luck Next Time.")
    main()


if __name__ == "__main__":
    main()