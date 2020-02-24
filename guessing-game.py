def main():
    print("Welcome to THE Python Guessing Game.")
    animal = "wolf"
    zero = 0
    while zero == 0:
        guess = input("Please try to guess the right answer: ")
        if guess.lower()== animal:
            zero += 1
            print("You're right!")
            wolfgang = 0
            while wolfgang == 0:
                response = input("Do you think this animal is cool? :")
                if response[0].lower() == "n":
                    print("Watch yourself wolves can eat you.")
                    wolfgang += 1
                elif response[0].lower() == "y":
                    print("Nice.")
                    wolfgang += 1
        elif guess[0].lower() == "q":
            zero += 1
        else:
            print("Wrong animal, try again.")
    print("THE Python Guessing Game is over, good bye.")
main()
