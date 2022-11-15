#!/bin/env python3
#Created by Frankie 
#Created on November 15 , 2022
#This is basically e process of guessing numbers but with loop
#The loop breaks when you finally guess the correct number 

import random 


secret_num= secret_num = random.randint(0, 9)


def main():

    #This tries to cast it to an integer 
    try:
        user_num = int(input("Enter a positive integer between (0, 9)"))
        print()
        #Exception is used to make sure the code doesn't crash by entering a non integer
    except ValueError :
        input("Please enter a positive integer. Try again")

        #Restarts the program if a negative number is entered 
    if (user_num < 0 and user_num < 9):
        print("Please enter numbers between 0-9")
        
    else:
        # If while user's guess it continues running 
         # Using a while loop and will break out of the loop 
         while secret_num == user_num:
             print("You guessed correct")
             break

         if user_num != secret_num:
          print("Your guess is incorrect. Please retry ")
          main()
 
 
if __name__ == "__main__":
    main()
