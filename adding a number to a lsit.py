#import time #will import time for delay

#asks the user's input so that the number can be added to the list

#will set the list of numbers empty so that users can enter the list
list_of_numbers = []
game_run = True

while game_run:

    #will set the user input value to numbers_input
    numbers_input= int(input("Enter in a number: "))

    #will set the conditions so only positive number can be entered
    if numbers_input <= 0 or numbers_input > 100:
        print("Numbers must be greater than 0 and less than 100!")
        numbers_input = int(input("Enter in a number:"))



    #will append the list after user input a number
    list_of_numbers.append(numbers_input)
    #will print out the list of numbers the user input
    print(list_of_numbers)
    #time.sleep(5) #will delay by 5 seconds

    #will now set the lowest number of the list to lowest_number
    lowest_number = min(list_of_numbers)
    #will now set the highest number of the list to highest_number
    highest_number = max(list_of_numbers)

#will print out the lowest_number, highest_number, and random number based on the list
    #will make sure that the output will only show if the list of numbers is more than 1
    if len(list_of_numbers) > 1:
        print("Lowest number is: ", lowest_number)
        #time.sleep(5)  # will delay by 5 seconds

        print("Highest number is: ", highest_number)
        #time.sleep(5)  # will delay by 5 seconds

        #will try to find the sum of the list
        total = sum(list_of_numbers)
        print("The sum of the list is: ", total)
#user must enter at least 10 numbers so that they can exist the game
    if len(list_of_numbers) >= 20:
        # Ask if the player wants to play again by pressing Y
            play_again = input("Play again? (y/n): ").lower()
        #ill stop the game if user didn't press y
            if play_again != "y":
                game_run = False

#will now exist the program
print("Bye")


