print """ Welcome to M.A.S.H

This is the abbreviation for Mansion, Apartment, Shack, House. This will make more sense as the game progresses.
Have you ever wondered about your future? What car you will drive, your spouse, children and your living situation?
Well you are in luck! This game has all the answers.

Please answer the question prompted below to find out. 

"""

house = ["Mansion", "Apartment", "Shack", "House"]

spouse = []

children = []

car = []



spouse1 = raw_input("Name one person you have a crush on: ")

spouse2 = raw_input("Name one more person you have a crush on: ")

spouse3 = raw_input("Name one person you hate: ")

spouse4 = raw_input("Name one more person you hate: ")

spouse.extend([spouse1, spouse2, spouse3, spouse4])

children1 = raw_input("Pick a number: ")

children2 = raw_input("Pick your second number: ")

children3 = raw_input("Pick your third number: ")

children4 = raw_input("Pick your final number: ")

children.extend([children1, children2, children3, children4])

car1 = raw_input("Name a car you would love to drive: ")

car2 = raw_input("Name another car you would love to drive: ")

car3 = raw_input("Name a car you hate: ")

car4 = raw_input("Name another car you hate: ")

car.extend([car1, car2, car3, car4])


random_number = int(raw_input("Pick any number between 1 and 10: "))


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