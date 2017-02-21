print """ \n\t\t\t\t\t\tWelcome to M.A.S.H

This is the abbreviation for Mansion, Apartment, Shack, House. This will make more sense as the game progresses.
Have you ever wondered about your future? What car you will drive, your spouse, children and your living situation?
Well you are in luck! This game has all the answers.

Please answer the questions prompted below to find out.\n 
***********************************************************************************************************************
"""

house = ["Mansion", "Apartment", "Shack", "House"]

spouse = []

children = []

car = []

print "One of the people you mention below will become your spouse.\n "

def spouse_input():

    def spouse_input_1():

        spouse1 = raw_input("Name one person you have a crush on: ")

        if len(spouse1) == 0:
            print "Please type something in"
            return spouse_input_1()

        spouse.extend([spouse1])

    spouse_input_1()

    def spouse_input_2():

        spouse2 = raw_input("Name one more person you have a crush on: ")

        if len(spouse2) == 0:
            print "Please type something in."
            return spouse_input_2()

        spouse.extend([spouse2])

    spouse_input_2()

    def spouse_input_3():

        spouse3 = raw_input("Name one person you hate: ")

        if len(spouse3) == 0:
            print "Please type something in."
            return spouse_input_3()

        spouse.extend([spouse3])

    spouse_input_3()

    def spouse_input_4():

        spouse4 = raw_input("Name one more person you hate: ")

        if len(spouse4) == 0:
            print "Please type something in."
            return spouse_input_4()

        spouse.extend([spouse4])

    spouse_input_4()
    
spouse_input()

print "\n"

print "One of the numbers you pick will determine the quantity of children you will have.\n"

def children_input():

    def children_input_1():

        try:
            children1 = int(raw_input("Pick a number: "))

        except ValueError:
            print "That is not a number, please try again..."
            return children_input_1()

        children1 = str(children1)

        children.extend([children1])

    children_input_1()

    def children_input_2():

        try:
            children2 = int(raw_input("Pick your second number: "))

        except ValueError:
            print "That is not a number, please try again..."
            return children_input_2()

        children2 = str(children2)

        children.extend([children2])

    children_input_2()

    def children_input_3():

        try:
            children3 = int(raw_input("Pick your third number: "))

        except ValueError:
            print "That is not a number, please try again..."
            return children_input_3()

        children3 = str(children3)

        children.extend([children3])


    children_input_3()

    def children_input_4():

        try:
            children4 = int(raw_input("Pick your final number: "))

        except ValueError:
            print "That is not a number, please try again..."
            return children_input_4()

        children4 = str(children4)

        children.extend([children4])

    children_input_4()

children_input()

print "\n"

print "The following will determine what car you will drive. \n" 


def car_input():

    def car_input_1():

        car1 = raw_input("Name a car you would love to drive: ")

        if len(car1) == 0:
            print "Please enter something."
            return car_input_1()

        car.extend([car1])

    car_input_1()

    def car_input_2():

        car2 = raw_input("Name another car you would love to drive: ")

        if len(car2) == 0:
            print "Please enter something. "
            return car_input_2()

        car.extend([car2])

    car_input_2()

    def car_input_3():

        car3 = raw_input("Name a car you hate: ")

        if len(car3) == 0:
            print "Please enter something. "
            return car_input_3()

        car.extend([car3])

    car_input_3()

    def car_input_4():

        car4 = raw_input("Name another car you hate: ")

        if len(car4) ==0:
            print "Please enter something. "
            return car_input_4()
        car.extend ([car4])

    car_input_4()

car_input()

print "\n"

print "Your fate will be determined by the number you enter. \n"
 
def random_number_input():

    try:
        random_number = int(raw_input("Pick any number between 1 and 10: "))

        if random_number > 10:
            print "That number is too high, please pick a number between 1-10!"
            return random_number_input()

        if random_number == 1:
            print "You live in a " + house[3] + ", you are married to " + spouse[3] + ", you have " + children[3] + " children, and you drive a " + car[3] + "."

        if random_number == 2:
            print "You live in a " + house[0] + ", you are married to " + spouse[0] + ", you have " + children[0] + " children, and you drive a " + car[0] + "."

        if random_number == 3:
            print "You live in a " + house[3] + ", you are married to " + spouse[3] + ", you have " + children[1] + " children, and you drive a " + car[1] + "."

        if random_number == 4:
            print "You live in a " + house[1] + ", you are married to " + spouse[2] + ", you have " + children[2] + " children, and you drive a " + car[0] + "."

        if random_number == 5:
            print "You live in a " + house[2] + ", you are married to " + spouse[2] + ", you have " + children[3] + " children, and you drive a " + car[1] + "."

        if random_number == 6:
            print "You live in a " + house[2] + ", you are married to " + spouse[2] + ", you have " + children[1] + " children, and you drive a " + car[1] + "."

        if random_number == 7:
            print "You live in a " + house[3] + ", you are married to " + spouse[3] + ", you have " + children[2] + " children, and you drive a " + car[2] + "."

        if random_number == 8:
            print "You live in a " + house[0] + ", you are married to " + spouse[0] + ", you have " + children[2] + " children, and you drive a " + car[0] + "."

        if random_number == 9:
            print "You live in a " + house[2] + ", you are married to " + spouse[3] + ", you have " + children[2] + " children, and you drive a " + car[2] + "."

        if random_number == 10:
            print "You live in a " + house[0] + ", you are married to " + spouse[3] + ", you have " + children[0] + " children, and you drive a " + car[1] + "."
    

    except ValueError:
        print "That is not a number, please try again..."
        return random_number_input()

    
random_number_input()


def main():

    play_again = raw_input("Would you like to play again? yes/no: ")
    
    if play_again.lower() == "yes":
        spouse_input()
        children_input()
        car_input()
        random_number_input()
        main()
       
    if not play_again:
         return  

main()

