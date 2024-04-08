from Common import Player
from Common import Choices
from Chapter06b import Subchapter
from Common import HousePointTotals
from Common import Lessons
from Common import EndOfDay

Day_2 = Lessons(False, False, False)

class Chapter():
    def __init__(self):
        self.name = 'Chapter 6'
        
    def Execute_Main(self):
        pass

def Chapter06():
    #BRANCH FUNCTIONS
    def Decide_Class_One(x):
        print(f"\n{Player.companion.upper()}: See you later, {Player.first_name}.", end='')
        input()
        if x == '1':
            Transfiguration()
            Day_2.Attend1 = True
        elif x == '2':
            Herbology()
            Day_2.Attend2 = True
        elif x == '3':
            MagicalCreatures()
            Day_2.Attend3 = True
        else:
            print(f"\n{Player.companion.upper()}: Come on, now. Pick one!\n")
            x = input()
            DecideClassOne(x)

    def Decide_Class_Two():
        def SubDecideOne(x):
            if x == '1':
                Herbology()
                Day_2.Attend2 = True
            elif x == '2':
                MagicalCreatures()
                Day_2.Attend3 = True
            else:
                print('\n~You\'re not getting out of this one so easy...~\n')
                x = input()
                SubDecideOne(x)
        def SubDecideTwo(x):
            if x == '1':
                Transfiguration()
                Day_2.Attend1 = True
            elif x == '2':
                MagicalCreatures()
                Day_2.Attend3 = True
            else:
                print('\n~You\'re not getting out of this one so easy...~\n')
                x = input()
                SubDecideTwo(x)
        def SubDecideThree(x):
            if x == '1':
                Transfiguration()
                Day_2.Attend1 = True
            elif x == '2':
                Herbology()
                Day_2.Attend2 = True
            else:
                print('\n~You\'re not getting out of this one so easy...~\n')
                x = input()
                SubDecideThree(x)
        if Day_2.Attend1 == True:
            print(
            '\n[1] Herbology\n'
            '[2] Care for Magical Creatures\n'
            )
            x = input()
            SubDecideOne(x)
        elif Day_2.Attend2 == True:
            print(
            '\n[1] Transfiguration\n'
            '[2] Care for Magical Creatures\n'
            )
            x = input()
            SubDecideTwo(x)
        elif Day_2.Attend3 == True:
            print(
            '\n[1] Transfiguration\n'
            '[2] Herbology\n'
            )
            x = input()
            SubDecideThree(x)
    #END BRANCH FUNCTIONS



    #BEGIN COMMON ROOM
    print('')
    print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
    print(Back.WHITE + Fore.BLACK + ' ~   CHAPTER 6: CHAIRS, CABBAGES, AND CRABS    ~ ')
    print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
    input()



    #BEGIN GRYFFINDOR PATH
    if Player.house != 'Slytherin':
        print('\n~Following the exciting events from last night, you struggle to adjust to start\n'
              'of a new day as you meet Percival in the common room.~', end='')
        input()
        print(f"\n{Player.companion.upper()}: I was just looking for you.", end='')
        input()
        print(f"{Player.companion.upper()}: You\'ll be happy to hear that I did a bit of research earlier and I now\n"
              'know exactly where the next step in our journey will take us.', end='')
        input()
        print(f"{Player.companion.upper()}: Mind you that it will be several miles of walking distance, and should anything\n"
              f"go wrong or one of us gets hurt, it\'ll be points from {Player.house}.", end='')
        input()
        if Choices['Compromise'] == True:
            print(f"{Player.companion.upper()}: As much as I disagree with bringing {Player.rival.upper()} along, it looks like i have\n"
                  'no choice but to let him know when I get the chance.', end='')
            input()
        else:
            print(f"{Player.companion.upper()}: And hopefully {Player.rival.upper()} will learn to keep his fat nose out of our business.", end='')
            input()
        #END GRYFFINDOR PATH



    #CONTINUE COMMON ROOM
    print(f"{Player.companion.upper()}: Anyway, which class do you think you're going to first?", end='')
    input()
    print(
    '\n[1] Transfiguration\n'
    '[2] Herbology\n'
    '[3] Care for Magical Creatures\n'
    )
    x = input()
    DecideClassOne(x)
    print('\n~Now with that out of the way, where would you like to go next?~', end='')
    input()
    DecideClassTwo()
    print('\n~You\'ve finished two of your classes for the day, leaving just one more...~', end='')
    input()
    if Day_2.Attend1 == True and Day_2.Attend2 == True:
        MagicalCreatures()
        Day_2.Attend3 = True
    elif Day_2.Attend2 == True and Day_2.Attend3 == True:
        Transfiguration()
        Day_2.Attend1 = True
    elif Day_2.Attend1 == True and Day_2.Attend3 == True:
        Herbology()
        Day_2.Attend2 = True



    if Player.house == 'Gryffindor':
        EndOfSecondDay = EndOfDay(0, 60, 65, 80)
    elif Player.house == 'Hufflepuff':
        EndOfSecondDay = EndOfDay(65, 0, 60, 80)
    elif Player.house == 'Ravenclaw':
        EndOfSecondDay = EndOfDay(65, 60, 0, 80)
    elif Player.house == 'Slytherin':
        EndOfSecondDay = EndOfDay(80, 60, 65, 0)

    EndOfSecondDay.Display_Points()



#RUN CHAPTER
