Blacklist = ['HARRY POTTER', 'RON WEASLEY', 'HERMIONE GRANGER', 'NEVILLE LONGBOTTOM', 'ALBUS DUMBLEDORE',
             'SEVERUS SNAPE', 'SIRIUS BLACK', 'DRACO MALFOY', 'TOM RIDDLE', 'GILDEROY LOCKHART',
             'DOLORES UMBRIDGE', 'BATHILDA BAGSHOT', 'BELLATRIX LESTRANGE', 'SUSAN BONES', 'LAVENDER BROWN',
             'CHO CHANG', 'COLIN CREEVY', 'VERNON DURSLEY', 'LUNA LOVEGOOD', 'RUBEUS HAGRID']

class Player():
    def __init__(self):
        self.first_name = 'Firstname'
        self.last_name = 'Lastname'
        self.full_name = 'Firstname Lastname'
        self.fear = 'the default fear'
        self.house = 'Default'
        self.house_color = 'default'
        self.companion = 'your companion'
        self.rival = 'your rival'
        self.rival = 'your rival'
        self.win_house_cup = False

class Choices():
    def __init__(self):
        self.compromise = False
        self.help_companion = False
        self.help_rival = False
        self.take_fake_potion = False
        self.take_real_potion = False
        self.sacrifice_self = False
        self.take_full_credit = False
        self.give_full_credit = False
        self.split_credit = False

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
            print('\n+' + str(num_value) + '*', end='')
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

    def Add_Gryffindor(self, G):
        self.G = G
        self.gryffindor += int(self.G)

    def Add_Hufflepuff(self, H):
        self.H = H
        self.hufflepuff += int(self.H)

    def Add_Ravenclaw(self, R):
        self.R = R
        self.ravenclaw += int(self.R)

    def Add_Slytherin(self, S):
        self.S = S
        self.slytherin += int(self.S)

    def Display_Points(self):
        print('\n~ The house point totals are being calculated. ~', end='')
        input()
        print(f"\n~ Gryffindor: {self.gryffindor} ~", end='')
        input()
        print(f"~ Hufflepuff: {self.hufflepuff} ~", end='')
        input()
        print(f"~ Ravenclaw: {self.ravenclaw} ~", end='')
        input()
        print(f"~ Slytherin: {self.slytherin} ~", end='')
        input()
        #FIND ALTERNATE METHOD
        temp_dict = {'Gryffindor': self.gryffindor,
                     'Hufflepuff': self.hufflepuff,
                     'Ravenclaw': self.ravenclaw,
                     'Slytherin': self.slytherin}
        keymax = max(zip(temp_dict.values(), temp_dict.keys()))[1]
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
