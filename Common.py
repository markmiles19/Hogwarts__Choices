import time

#LISTS
Blacklist = ['HARRY POTTER', 'RON WEASLEY', 'HERMIONE GRANGER', 'NEVILLE LONGBOTTOM', 'ALBUS DUMBLEDORE',
             'SEVERUS SNAPE', 'SIRIUS BLACK', 'DRACO MALFOY', 'TOM RIDDLE', 'GILDEROY LOCKHART',
             'DOLORES UMBRIDGE', 'BATHILDA BAGSHOT', 'BELLATRIX LESTRANGE', 'SUSAN BONES', 'LAVENDER BROWN',
             'CHO CHANG', 'COLIN CREEVY', 'VERNON DURSLEY', 'LUNA LOVEGOOD', 'RUBEUS HAGRID']


#DICTIONARIES
Choices = {'Compromise': False,
           'HelpCompanion': False,
           'HelpRival': False,
           'TakeFakePotion': False,
           'TakeRealPotion': False,
           'SacrificeSelf': False,
           'TakeFullCredit': False,
           'GiveFullCredit': False,
           'SplitCredit': False}

#CLASSES
class Player():
    def __init__(self):
        self.first_name = 'Default'
        self.last_name = 'Default'
        self.full_name = 'Default'
        self.fear = 'Default'
        self.house = 'Default'
        self.house_color = 'Default'
        self.companion = 'Default'
        self.rival = 'Default'
        self.win_house_cup = False

class Lessons():
    def __init__(self, Attend1, Attend2, Attend3):
        self.Attend1 = Attend1
        self.Attend2 = Attend2
        self.Attend3 = Attend3

    def Lesson1(self):
        self.Attend1 = False

    def Lesson2(self):
        self.Attend2 = False

    def Lesson3(self):
        self.Attend3 = False

class HousePts():
    def __init__(self):
        self.gryffindor = 0
        self.hufflepuff = 0
        self.ravenclaw = 0
        self.slytherin = 0

    def Add_House_Points(self, num_value):
        if Player.house == 'Gryffindor':
            self.gryffindor += int(num_value)
            print('\n+' + str(num_value) + '*', end='')
            time.sleep(0.5)
            print()
        elif Player.house == 'Hufflepuff':
            self.hufflepuff += int(num_value)
            print('\+' + str(num_value) + '*', end='')
            time.sleep(0.5)
            print()
        elif Player.house == 'Ravenclaw':
            self.ravenclaw += int(num_value)
            print('\n+' + str(num_value) + '*', end='')
            time.sleep(0.5)
            print()
        elif Player.house == 'Slytherin':
            self.slytherin += int(num_value)
            print('\n+' + str(num_value) + '*', end='')
            time.sleep(0.5)
            print()
        else:
            print('\n~ Wait, are you unsorted? What are you doing here? ~', end='')
            time.sleep(0.5)
            print()

class EndOfDay():
    def __init__(self, G, H, R, S):
        self.G = G
        self.H = H
        self.R = R
        self.S = S

    def Add_Gryffindor(self):
        HousePts.gryffindor += self.G

    def Add_HufflePuff(self):
        HousePts.hufflepuff += self.H

    def Add_Ravenclaw(self):
        HousePts.ravenclaw += self.R

    def Add_Slytherin(self):
        HousePts.slytherin += self.S

    def Display_Points(self):
        EndOfDay.Add_Gryffindor()
        EndOfDay.Add_HufflePuff()
        EndOfDay.Add_Ravenclaw()
        EndOfDay.Add_Slytherin()
        print('\n~ The house point totals are being calculated. ~', end='')
        input()
        print(f"\n~ Gryffindor: {HousePts.gryffindor} ~", end='')
        input()
        print(f"~ Hufflepuff: {HousePts.hufflepuff} ~", end='')
        input()
        print(f"~ Ravenclaw: {HousePts.ravenclaw} ~", end='')
        input()
        print(f"~ Slytherin: {HousePts.slytherin} ~", end='')
        input()
        #FIND ALTERNATE METHOD
        keymax = max(zip(HousePts.values(), HousePts.keys()))[1]
        if keymax == 'Gryffindor':
            print('\n~ Gryffindor is in the lead! ~', end='')
            input()
        elif keymax == 'Hufflepuff':
            print('\n~ Hufflepuff is in the lead! ~', end='')
            input()
        elif keymax == 'Ravenclaw':
            print('\n~ Ravenclaw is in the lead! ~', end='')
            input()
        elif keymax == 'Slytherin':
            print('\n~ Slytherin is in the lead! ~', end='')
            input()
            
Test = EndOfDay(10, 20, 30, 40)
Test.Display_Points()

#FOR REFERENCE ONLY
def StoreName(name):
    tokens = name.split()
    if len(tokens) == 2:
        if tokens[0].isalpha and tokens[1].isalpha():
            PlayerDict['FirstName'] = tokens[0]
            PlayerDict['FirstName'] = PlayerDict['FirstName'][0].upper() + PlayerDict['FirstName'][1:].lower()
            PlayerDict['LastName'] = tokens[1]
            PlayerDict['LastName'] = PlayerDict['LastName'][0].upper() + PlayerDict['LastName'][1:].lower()
            PlayerDict['FullName'] = PlayerDict['FirstName'] + ' ' + PlayerDict['LastName']
        else:
            print('\n~ Preferably first and last name AND NO SYMBOLS. ~\n')
            PlayerName = input()
            StoreName(PlayerName)
    elif len(tokens) < 2:
        print('\n~ Preferably first AND last name. ~\n')
        PlayerName = input()
        StoreName(PlayerName)
    elif len(tokens) > 2:
        print('\n~ Preferably first and last name ONLY. ~\n')
        PlayerName = input()
        StoreName(PlayerName)

def FinalizeSort():
    keymax = max(zip(SortingDict.values(), SortingDict.keys()))[1]
    if keymax == 'Red':
        PlayerDict['House'] = 'Gryffindor'
        PlayerDict['Companion'] = 'Percival'
        PlayerDict['HouseColor'] = 'RED'
    elif keymax == 'Yellow':
        PlayerDict['House'] = 'Hufflepuff'
        PlayerDict['Companion'] = 'Percival'
        PlayerDict['HouseColor'] = 'YELLOW'
    elif keymax == 'Blue':
        PlayerDict['House'] = 'Ravenclaw'
        PlayerDict['Companion'] = 'Percival'
        PlayerDict['HouseColor'] = 'BLUE'
    elif keymax == 'Green':
        PlayerDict['House'] = 'Slytherin'
        PlayerDict['Companion'] = 'Milo'
        PlayerDict['HouseColor'] = 'GREEN'

Potions = {'User': 'None',
           'Percival': 'None',
           'Leo': 'None',
           'Milo': 'None'}

Dueling = {'User': False,
           'Percival': False,
           'Leo': False,
           'Milo': False}