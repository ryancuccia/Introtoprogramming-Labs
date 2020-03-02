def main():
    def nameget():
        first = input("Enter your first name: ")
        last = input("Enter your last name: ")
        first = first.lower()
        last = last.lower()
        return(first, last)
    def namebuild(first, last):
        return(first + "." + last)
    def strengthcheck2(password):
        while password.islower() or password.isupper():
            print("Password must contain atleast one uppercase and one lowercase character.")
            password = input("Pick a new password: ")
    def strengthcheck(password):
        while len(password)<8:
            print("Password too short.")
            password = input("Pick a new password: ")
        strengthcheck2(password)
        print("Valid password.")
        return password
    def operator():
        first, last = nameget()
        username = namebuild(first, last)
        password = input("Create a new password: ")
        strengthcheck(password)
        print("Your email adress is "+ username + "@marist.edu")
    operator()
main()
