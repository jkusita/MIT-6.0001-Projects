# A program that tries to guess the user's number. 

test_list = [0, 100]
test_divide = 0
answer = ""
curret_program_guess = ""

print("\nPlease think of a number between 0 (inclusive) and 100 (not inclusive)!")

# Guesses the number by using bisection search 
while True: 
    test_divide = int((test_list[0] + test_list[1])/2)
    answer = test_divide
    print("\nIs your secret number " + str(answer) + "?")
    current_program_guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")
    if current_program_guess == "h":
        test_list[1] = answer 
    elif current_program_guess == "l":
        test_list[0] = answer    
    elif current_program_guess == "c":
        print("Game over. Your secret number was: " + str(test_divide) + "\n")
        break
    else:
        print("Sorry, I did not understand your input.")