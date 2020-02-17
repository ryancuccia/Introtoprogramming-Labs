def main():
    print("Welcome to THE Python Guessing Game.")
    animal = "wolf"
    user_animal = input("Please try to guess the correct animal: ")
    butt = input("Do you want to try again? ")
    while True:
        if user_animal != animal:
            user_animal = input("Try again. Please try to guess the correct animal: ")
        else:
            print("Congradualtions! You win!!")
            break

main()
