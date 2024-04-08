from Common import Player
from Chapter03b import Subchapter
from Common import Lessons

Day_1 = Lessons(False, False, False)

class Chapter():
    class Dialogue():
        def Branch_1(self, user_input):
            if user_input == '1':
                print(f"\n{Player.companion.upper()}: Optimism. I can appreciate that.", end='')
                input()
            elif user_input == '2':
                print(f"\n{Player.companion.upper()}: Everyone’s like that on their first day. It’s nothing to worry about.", end='')
                input()
            elif user_input == '3':
                print(f"\n{Player.companion.upper()}: Can’t say that I blame you.", end='')
                input()
            else:
                print(f"\n{Player.companion.upper()}: Come on. Be honest with me, now.\n")
                user_input = input()
                Chapter.Dialogue.Branch_1(user_input)

        def Decide_Class_One(self, user_input):
            if user_input == '1':
                if Player.house == 'Ravenclaw':
                    print(f"\n{Player.companion.upper()}: Excellent choice! Professor Flitwick is the head of Ravenclaw and you’ll learn so many\n"
                        'useful spells from him.', end='')
                    input()
                else:
                    print(f"\n{Player.companion.upper()}: Interesting choice. You won’t see me in your classes since I’m not a first-year, but I hope it\n"
                    'goes well for you.', end='')
                    input()
                print('...', end='')
                input()
                Subchapter.Charms()
                Day_1.Attend1 = True
                    
            elif user_input == '2':
                if Player.house == 'Gryffindor':
                    print(f"\n{Player.companion.upper()}: Really? Potions with Snape? Everyone in Gryffindor hates him.", end='')
                    input()
                    print('PERCIVAL: Well, I suppose it is your choice. Just don’t say that I didn’t give you a fair warning.', end='')
                    input()
                elif Player.house == 'Slytherin':
                    print('\nMILO: Despite what some may say, potions is one of my favorite subjects.',end='')
                    input()
                    print('MILO: Professor Snape on the other hand is a complete slimeball.',end='')
                    input()
                    print('MILO: What’s worse is that he’s the head of Slytherin house, but I wouldn’t let that get in the way of\n'
                        'learning if I were you.', end='')
                    input()
                else:
                    print(f"\n{Player.companion.upper()}: Interesting choice. You won’t see me in your classes since I’m not a first-year, but I hope it\n"
                    'goes well for you.', end='')
                    input()
                print('...', end='')
                input()
                Subchapter.Potions()
                Day_1.Attend2 = True
                

            elif user_input == '3':
                print(f"\n{Player.companion.upper()}: Interesting choice. You won’t see me in your classes since I’m not a first-year, but I hope it\n"
                'goes well for you.', end='')
                input()
                print('...', end='')
                input()
                Subchapter.Flying()
                Day_1.Attend3 = True
            else:
                print(f"\n{Player.companion.upper()}: Come on, now. You\'ve got to pick one.", end='')
                user_input = input()
                Chapter.Dialogue.Decide_Class_One(user_input)

        def Sub_Decide_One(self, user_input):
            if user_input == '1':
                Subchapter.Potions()
                Day_1.Attend2 = True
            elif user_input == '2':
                Subchapter.Flying()
                Day_1.Attend3 = True
            else:
                print('\n~You\'re not getting out of this one so easy...~\n')
                user_input = input()
                Chapter.Dialogue.Branch_3(user_input)

        def Sub_Decide_Two(self, user_input):
            if user_input == '1':
                Subchapter.Charms()
                Day_1.Attend1 = True
            elif user_input == '2':
                Subchapter.Flying()
                Day_1.Attend3 = True
            else:
                print('\n~You\'re not getting out of this one so easy...~\n')
                user_input = input()
                Chapter.Dialogue.Branch_4(user_input)

        def Sub_Decide_Three(self, user_input):
            if user_input == '1':
                Subchapter.Charms()
                Day_1.Attend1 = True
            elif user_input == '2':
                Subchapter.Potions()
                Day_1.Attend2 = True
            else:
                print('\n~You\'re not getting out of this one so easy...~\n')
                user_input = input()
                Chapter.Dialogue.Branch_5(user_input)

        def Decide_Class_Two(self):
            if Day_1.Attend1 == True:
                print(
                '\n[1] Potions\n'
                '[2] Flying\n'
                )
                user_input = input()
                Chapter.Dialogue.Sub_Decide_One(user_input)
            elif Day_1.Attend2 == True:
                print(
                '\n[1] Charms\n'
                '[2] Flying\n'
                )
                user_input = input()
                Chapter.Dialogue.Sub_Decide_Two(user_input)
            elif Day_1.Attend3 == True:
                print(
                '\n[1] Charms\n'
                '[2] Potions\n'
                )
                user_input = input()
                Chapter.Dialogue.Sub_Decide_Three(user_input)

    def __init__(self):
        self.name = 'Chapter 3'
        
    def Execute_Main(self):
        print('')
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
        print(' ~    CHAPTER 3: READY TO BEGIN    ~ ')
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
        input()
        print('\n~ You wake up early to watch the sunrise from your dormitory window, ready to start your classes. ~', end='')
        input()
        print(f"\n~ {Player.companion} stops to talk to you in the common room. ~", end='')
        input()
        print(f"\n{Player.companion.upper()}: Feeling alright there, {Player.first_name}?", end='')
        input()
        print(
        '\n[1] Feeling ready to learn is more like it.\n'
        '[2] I just hope I’m ready for this.\n'
        '[3] ~Shrug~\n'
        )
        user_input = input()
        Chapter.Dialogue.Branch_1(user_input)
        print(f"{Player.companion.upper()}: If you take a look at the notice board you’ll see the schedule for first-years.", end='')
        input()
        print(f"{Player.companion.upper()}: Remember, this year you can choose the order in which you attend classes.", end='')
        input()
        print(f"{Player.companion.upper()}: It looks like today will be Charms, Potions, and Flying for you.", end='')
        input()
        print(f"{Player.companion.upper()}: So which class will you start the day with?", end='')
        input()
        print(
        '\n[1] Charms\n'
        '[2] Potions\n'
        '[3] Flying\n'
        )
        user_input = input()
        Chapter.Dialogue.Decide_Class_One(user_input)
        print('\n~Now with that out of the way, where would you like to go next?~', end='')
        input()
        Chapter.Dialogue.Decide_Class_Two()
        print('\n~You\'ve finished two of your classes for the day, leaving just one more...~', end='')
        input()
        if Day_1.Attend1 == True and Day_1.Attend2 == True:
            Subchapter.Flying()
            Day_1.Attend3 = True
        elif Day_1.Attend2 == True and Day_1.Attend3 == True:
            Subchapter.Charms()
            Day_1.Attend1 = True
        elif Day_1.Attend1 == True and Day_1.Attend3 == True:
            Subchapter.Potions()
            Day_1.Attend2 = True

#RUN CHAPTER
Chapter.Execute_Main()