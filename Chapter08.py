from Common import Player
from Chapter08b import Subchapter
from Common import HousePointTotals
from Common import Lessons
from Common import EndOfDay
Day_3 = Lessons(False, False, False)

class Chapter():
    class Dialogue():
        def __init__(self):
            pass

        def Decide_Class_One(self, user_num):
            if user_num == '1':
                Subchapter.Defense()
                Day_3.Attend1 = True
            elif user_num == '2':
                Subchapter.Divination()
                Day_3.Attend2 = True
            elif user_num == '3':
                Subchapter.Astronomy()
                Day_3.Attend3 = True
            else:
                print(f"\n{Player.companion.upper()}: Come on, now. Pick one!\n")
                user_num = input()
                Chapter.Dialogue.Decide_Class_One(self, user_num)

        def Decide_Class_Two(self, user_num):
            def SubDecideOne(user_num):
                if user_num == '1':
                    Subchapter.Divination()
                    Day_3.Attend2 = True
                elif user_num == '2':
                    Subchapter.Astronomy()
                    Day_3.Attend3 = True
                else:
                    print('\n~You\'re not getting out of this one so easy...~\n')
                    user_num = input()
                    SubDecideOne(user_num)
            def SubDecideTwo(x):
                if x == '1':
                    Subchapter.Defense()
                    Day_3.Attend1 = True
                elif x == '2':
                    Subchapter.Astronomy()
                    Day_3.Attend3 = True
                else:
                    print('\n~You\'re not getting out of this one so easy...~\n')
                    x = input()
                    SubDecideTwo(x)
            def SubDecideThree(x):
                if x == '1':
                    Subchapter.Defense()
                    Day_3.Attend1 = True
                elif x == '2':
                    Subchapter.Divination()
                    Day_3.Attend2 = True
                else:
                    print('\n~You\'re not getting out of this one so easy...~\n')
                    x = input()
                    SubDecideThree(x)
            if Day_3.Attend1 == True:
                print(
                '\n[1] Divination\n'
                '[2] Astronomy\n'
                )
                x = input()
                SubDecideOne(x)
            elif Day_3.Attend2 == True:
                print(
                '\n[1] Defense Against the Dark Arts\n'
                '[2] Astronomy\n'
                )
                x = input()
                SubDecideTwo(x)
            elif Day_3.Attend3 == True:
                print(
                '\n[1] Defense Against the Dark Arts\n'
                '[2] Divination\n'
                )
                x = input()
                SubDecideThree(x)

    def __init__(self):
        self.name = 'Chapter 8'
        
    def Execute_Main(self):
        #BEGIN COMMON ROOM
        print('')
        print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
        print(Back.WHITE + Fore.BLACK + ' ~     CHAPTER 8: The Beyond     ~ ')
        print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
        input()

        print('\n~ You\'ve nearly recovered from your great battle yesterday, and now you must return\n'
                'your mind to your studies. ~', end='')
        input()
        print(f"\n{Player.companion.upper()}: I don\'t know how I\'m supposed to pay attention in class today\n"
                'knowing that the treasure it so close now.', end='')
        input()
        print(f"{Player.companion.upper()}: Anyway, I think you know the drill by now.", end='')
        input()
        print(
        '\n[1] Defense Against the Dark Arts\n'
        '[2] Divination\n'
        '[3] Astronomy\n'
        )
        user_num = input()
        Chapter.Decide_Class_One(user_num)

        #FIRST CLASS ATTENDED

        print('\n~Now with that out of the way, where would you like to go next?~', end='')
        user_num = input()
        Chapter.Decide_Class_Two(user_num)

        #SECOND CLASS ATTENDED

        print('\n~You\'ve finished two of your classes for the day, leaving just one more...~', end='')
        input()

        if Day_3.Attend1 == True and Day_3.Attend2 == True:
            Subchapter.Astronomy()
            Day_3.Attend3 = True
        elif Day_3.Attend2 == True and Day_3.Attend3 == True:
            Subchapter.Defense()
            Day_3.Attend1 = True
        elif Day_3.Attend1 == True and Day_3.Attend3 == True:
            Subchapter.Divination()
            Day_3.Attend2 = True

        #THIRD CLASS ATTENDED
        
        if Player.house == 'Gryffindor':
            EndOfThirdDay = EndOfDay(0, 60, 65, 80)
        elif Player.house == 'Hufflepuff':
            EndOfThirdDay = EndOfDay(65, 0, 60, 80)
        elif Player.house == 'Ravenclaw':
            EndOfThirdDay = EndOfDay(65, 60, 0, 80)
        elif Player.house == 'Slytherin':
            EndOfThirdDay = EndOfDay(80, 60, 65, 0)

        EndOfThirdDay.Display_Points()