import time
from Data import Player
from Data import Choices
from Data import Lessons
from Data import HousePts

class Player():
    def __init__(self):
        self.first_name = 'Firstname'
        self.last_name = 'Lastname'
        self.full_name = 'Firstname Lastname'
        self.fear = 'the default fear'
        self.house = 'Default'
        self.companion = 'your companion'
        self.rival = 'your rival'
        self.win_house_cup = False

User = Player()

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

Decide = Choices()

class HousePts():
    def __init__(self, User):
        self.player = User
        self.gryffindor = 0
        self.hufflepuff = 0
        self.ravenclaw = 0
        self.slytherin = 0

    def Add_House_Points(self, num_value):
        if self.player.house == 'Gryffindor':
            self.gryffindor += int(num_value)
            if int(num_value) >= 0:
                print('\n+' + str(num_value) + '*', end='')
                time.sleep(0.5)
                print('')
            else:
                print('\n' + str(num_value) + '*', end='')
                time.sleep(0.5)
                print('')
        elif self.player.house == 'Hufflepuff':
            self.hufflepuff += int(num_value)
            if int(num_value) >= 0:
                print('\n+' + str(num_value) + '*', end='')
                time.sleep(0.5)
                print('')
            else:
                print('\n' + str(num_value) + '*', end='')
                time.sleep(0.5)
                print('')
        elif self.player.house == 'Ravenclaw':
            self.ravenclaw += int(num_value)
            if int(num_value) >= 0:
                print('\n+' + str(num_value) + '*', end='')
                time.sleep(0.5)
                print('')
            else:
                print('\n' + str(num_value) + '*', end='')
                time.sleep(0.5)
                print('')
        elif self.player.house == 'Slytherin':
            self.slytherin += int(num_value)
            if int(num_value) >= 0:
                print('\n+' + str(num_value) + '*', end='')
                time.sleep(0.5)
                print('')
            else:
                print('\n' + str(num_value) + '*', end='')
                time.sleep(0.5)
                print('')
        else:
            if int(num_value) >= 0:
                print('\n+' + str(num_value) + '*', end='')
                time.sleep(0.5)
                print('')
            else:
                print('\n' + str(num_value) + '*', end='')
                time.sleep(0.5)
                print('')

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

Pts = HousePts(User)

#ALWAYS MAKE SURE THAT TESTING AND RUN STATEMENTS IN EVERY CHAPTER HAVE BEEN COMMENTED.



import Chapter01
import Chapter02
import Chapter03
import Chapter04
import Chapter05
import Chapter06
import Chapter07
import Chapter08
import Chapter09
import Chapter10

Ch01 = Chapter01.Chapter(User)
Ch02 = Chapter02.Chapter(User)
Ch03 = Chapter03.Chapter(User, Pts)
Ch04 = Chapter04.Chapter(User, Pts)
Ch05 = Chapter05.Chapter(User, Pts, Decide)
Ch06 = Chapter06.Chapter(User, Pts, Decide)
Ch07 = Chapter07.Chapter(User, Pts, Decide)
Ch08 = Chapter08.Chapter(User, Pts)
Ch09 = Chapter09.Chapter(User, Decide)
Ch10 = Chapter10.Chapter(User, Pts, Decide)

Ch01.Execute_Main()
Ch02.Execute_Main()
Ch03.Execute_Main()
Ch04.Execute_Main()
Ch05.Execute_Main()
Ch06.Execute_Main()
Ch07.Execute_Main()
Ch08.Execute_Main()
Ch09.Execute_Main()
Ch10.Execute_Main()