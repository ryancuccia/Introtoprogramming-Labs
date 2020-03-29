colors = ["RED", "BLUE", "GREEN", "YELLOW", "ORANGE", "PURPLE"]
color = 'PLACE HOLDING STRING'

def showTitle():
    print("Color Preference Evaluator")

def promptForColor():
    global color
    color = input("Please enter a color: ")
    color = color.strip()
    color = color.upper()
    return color

def confirmColor(block):
    confirm = input("You entered " + block + ". Is this correct? (Y/N)")
    confirm = confirm.upper()
    if confirm == "Y":
        return True
    else:
        return False

def containsElement():
    squidward = 0
    global color
    while squidward < 6:
        if colors[squidward] == color:
            return True
        squidward = squidward + 1
        

def praiseUser():
    print("You have succesfully guessed a listed color.")

def ridiculeUser():
    print("That was a terrible guess.")

def colorLoop():
    gary = 0
    while gary == 0:
        the_color = promptForColor()
        if confirmColor(the_color) == True:
            gary = gary + 1

def praisalLoop():
    if containsElement() == True:
        praiseUser()
    else:
        ridiculeUser()

def main():
    showTitle()
    colorLoop()
    praisalLoop()
    
        

main()
