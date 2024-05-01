from Data import Lessons

Day_3 = Lessons(False, False, False)

class Subchapter():
    def __init__(self, User, Pts):
        self.player = User
        self.house_pts = Pts

    #BEGIN DEFENSE CLASS
    def Defense(self):
        print('\n~You reach the Defense Against the Dark Arts Classroom. You don\'t even bother remembering\n'
            'the teacher\'s name since you know he\'ll be gone at the end of the year.~', end='')
        input()
        print('\nTEACHER: Good morning, class!', end='')
        input()
        print('TEACHER: We\'ll be learning about a most fascinating creature called a boggart.', end='')
        input()
        print('TEACHER: Now a boggart takes the shape of what one fears the most, and they often hide\n'
            'inside of everyday objects such as wardrobes or cabinets.', end='')
        input()
        print('TEACHER: They can be banished through a simple spell...', end='')
        input()
        print('TEACHER: Riddikulus.', end='')
        input()
        print('TEACHER: Now pay close attention to my movements and repeat the spell.', end='')
        input()
        print('\n~ TYPE: qazmlp ~\n')
        x = input()
        if x == 'qazmlp':
            self.house_pts.Add_House_Points(10)
            print('\nTEACHER: Very good!', end='')
            input()
        else:
            print('\nTEACHER: Ooh! Not good.', end='')
            input()
        print('\n~ TYPE: weiosdjkxcbn ~\n')
        x = input()
        if x == 'weiosdjkxcbn':
            self.house_pts.Add_House_Points(10)
            print('\nTEACHER: Very good!', end='')
            input()
        else:
            print('\nTEACHER: Ooh! Not good.', end='')
            input()
        print('\n~ TYPE: rfvbhuh ~\n')
        x = input()
        if x == 'rfvbhuh':
            self.house_pts.Add_House_Points(10)
            print('\nTEACHER: Very good!', end='')
            input()
        else:
            print('\nTEACHER: Ooh! Not good.', end='')
            input()
        print('\n~ Riddikulus! ~', end='')
        input()
        print('\n~ Your spell disappears into thin air. ~', end='')
        input()
        print('\nTEACHER: Unfortunately we won\'t be able to put the spell to practical\n'
            'use during this class period since all boggarts have been curiously displaced.', end='')
        input()
        print('TEACHER: Alright, I won\'t hold you any longer. Off you go!', end='')
        input()
        #END DEFENSE AGAINST THE DARK ARTS CLASS

    #BEGIN DIVINATION CLASS
    def Divination(self):
        print('\n~You ascend into the highest levels of the castle until you find the Divination classroom.~', end='')
        input()
        print('\n~Professor Trelawney is the strangest person you have ever met.~', end='')
        input()
        print('\nTRELAWNEY: Today we will learn to cast ourselves into the future through the noble art of\n'
            'Divination.', end='')
        input()
        print('TRELAWNEY: Today\'s lesson will be on Tessomancy, which is the reading of tea leaves.', end='')
        input()
        print('TRELAWNEY: Now I will pass around these cups, and I want for you to tell me what you see.', end='')
        input()

        #QUESTION #1
        print('')
        print('@@@@@@@@@@@@@@@@BB@@@@@@@@@@@@\n'
            '@@@@@@@@&&##BBBPPB#&@@@@@@@@@@\n'
            '@@@@@&BP5Y55YJYJ?JY5PGB#@@@@@@\n'
            '@@@@B5YYYJJJJ??7?Y5PPP555B@@@@\n'
            '@@@5JYJJ7!!!!!!7Y555PPP55JP@@@\n'
            '@@B?JY?7!~~!7JYY555555PPP5J#@@\n'
            '@@P?JJJ?7!!!7YYYY555555PP5YG@@\n'
            '@@B7JJJ??????YYY5555555PPPYP@@\n'
            '@@@Y?JJJ?JJYJYYYY5555555P5YB@@\n'
            '@@@&J?JJJJJJJYYYYY555555555@@@\n'
            '@@@@@P?????JJJYYYYY5555555&@@@\n'
            '@@@@@@#5J??7?JJYYYY55555P&@@@@\n'
            '@@@@@@@@&G5JJJJYYY5555PB@@@@@@\n'
            '@@@@@@@@@@@&#GPPGGBB#&@@@@@@@@\n')
        print('[1] Acorn\n'
            '[2] Skull\n'
            '[3] Apple\n'
            '[4] Sun\n')
        x = input()
        if x == '3':
            self.house_pts.Add_House_Points(10)
        else:
            print('\nTRELAWNEY: Oh are you sure you\'re using your inner eye?', end='')
            input()

        #QUESTION #2
        print('')
        print('@@@@@@@@@@@@@@&#@@@@@@@@@@@@@@\n'
            '@@@@@@@@@@@@@&###&@@@@@@@@@@@@\n'
            '@@@@@@@@@@@&######&@@@@@@@@@@@\n'
            '@@@@@@@@@&##########&@@@@@@@@@\n'
            '@@@@@@@&##############&@@@@@@@\n'
            '@@@@@&################B#&@@@@@\n'
            '@@@@#B#################BB#&@@@\n'
            '@@@#B###################BBB@@@\n'
            '@@&B###################BBBB#@@\n'
            '@@&B###########B#####BBBBBB&@@\n'
            '@@@#BB######B####BBBBBBBBB#@@@\n'
            '@@@@&#######&&B#@&#######&@@@@\n'
            '@@@@@@@@@@@@@##B#@@@@@@@@@@@@@\n'
            '@@@@@@@@@@@&BB##B#@@@@@@@@@@@@\n')
        print('[1] Club\n'
            '[2] Spade\n'
            '[3] Mountain\n'
            '[4] Kite\n')
        x = input()
        if x == '2':
            self.house_pts.Add_House_Points(10)
        else:
            print('\nTRELAWNEY: Oh are you sure you\'re using your inner eye?', end='')
            input()

        #QUESTION #3
        print('')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
            '@@@@@@@@@@##@@@@@@@#&@@@@@@@@@\n'
            '@@@@@@@@@@&PB@&5@@#5@@@@@@@@@@\n'
            '@@@@@@@&G&@&J&#Y@#Y&@&B@@@@@@@\n'
            '@@@&B##&&GP57!!~!7Y#GG&@@&&@@@\n'
            '@@@@@&#GG5~^^~~~^^^~J#GGG#&@@@\n'
            '@@@@#B##G^~~~~~~~~~~^P###&@@@@\n'
            '@@@@@&##G~^~~~~~~~~~^G###&@@@@\n'
            '@@@#BGGG#5~^^^~^^^^~PBPB#&@@@@\n'
            '@@@&&@@&PG&5?7!!!?PPG&@&###@@@\n'
            '@@@@@@@#&@#Y&@Y&&J@@#G&@@@@@@@\n'
            '@@@@@@@@@@5&@@5&@BP@@@@@@@@@@@\n'
            '@@@@@@@@@#&@@@@@@@##@@@@@@@@@@\n'
            '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
        print('[1] Spider\n'
            '[2] Ferns\n'
            '[3] Hand\n'
            '[4] Sun\n')
        x = input()
        if x == '4':
            self.house_pts.Add_House_Points(10)
        else:
            print('\nTRELAWNEY: Oh are you sure you\'re using your inner eye?', end='')
            input()

        #QUESTION #4
        print('')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
            '@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@\n'
            '@@@@@@@@@@@&@@&@@&@@@@@@@@@@@@\n'
            '@@@@@@@@@@@&&&@@@@@&@@@@@@@@@@\n'
            '@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@\n'
            '@@@@@@@@&@&#@@@@@@@@@@@@@@@@@@\n'
            '@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@\n'
            '@@@@@@@@@@@&&&&@@@&@@@@&&&@@@@\n'
            '@@@&@@&&#BBB#B###&&&@@@&&&@@@@\n'
            '@@@@@#BBB#@@@@@@&&@&@&@&@@@@@@\n'
            '@@@@@@@@@@@@@@@@@@@@@&@&@@@@@@\n'
            '@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@\n'
            '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
            '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
        print('[1] House\n'
            '[2] Grim\n'
            '[3] Fox\n'
            '[4] Hammer\n')
        x = input()
        if x == '2':
            self.house_pts.Add_House_Points(10)
        else:
            print('\nTRELAWNEY: Oh are you sure you\'re using your inner eye?', end='')
            input()
        print('\nTRELAWNEY: I\'m afraid that\'s all of the time we have for today.', end='')
        input()
        print('TRELAWNEY: You may go now.', end='')
        input()
        #END DIVINATION CLASS

    #BEGIN ASTRONOMY CLASS
    def Astronomy(self):
        print('\n~You gather with other students in the astronomy tower where you can see the\n'
            'entire grounds of Hogwarts all around you. Professor Sinistra stands before you.~', end='')
        input()
        print('\nSINISTRA: Settle down now, please!', end='')
        input()
        print('SINISTRA: I\'m sure many of you are eager to break out those telescopes you bought\n'
            'from Diagon Alley, but I thought I would warm all of you up a different way...', end='')
        input()
        print('SINISTRA: With a pop quiz!', end='')
        input()
        print('\n~Every one of you groan.~', end='')
        input()
        print('\nSINISTRA: Now I\'ll be a lot more forgiving with your grades since this is the first\n'
            'day, so let us begin.', end='')
        input()

        #QUESTION #1
        print('SINISTRA: Question one - The constellation Ursa Major is often seen as either a bear, wagon,\n'
            'or ladle, but it is more commonly known by what other name?', end='')
        input()
        print(
            '\n[1] Big Dipper\n'
            '[2] Little Dipper\n'
            '[3] Plough\n'
            '[4] Polaris\n'
        )
        x = input()
        if x == '1':
            print('\nSINISTRA: Incorrect.', end='')
            input()
            print('SINISTRA: In the United Kingdom, Ursa Major is known as the Plough, whereas the name Big\n'
                'Dipper is used in the United States and Canada.', end='')
            input()
        elif x == '2':
            print('\nSINISTRA: Incorrect.', end='')
            input()
            print('SINISTRA: In the United Kingdom, Ursa Major is known as the Plough, whereas the name Little\n'
                'Dipper is used in the United States and Canada to refer to Ursa Minor.', end='')
            input()
        elif x == '3':
            self.house_pts.Add_House_Points(5)
            print('\nSINISTRA: Correct.', end='')
            input()
            print('SINISTRA: In the United Kingdom, Ursa Major is known as the Plough.', end='')
            input()
        elif x == '4':
            print('\nSINISTRA: Incorrect.', end='')
            input()
            print('SINISTRA: In the United Kingdom, Ursa Major is known as the Plough, whereas Polaris is the\n'
                'star located at the tip of Ursa Minor.', end='')
            input()
        else:
            print('\nSINISTRA: Time\'s up!', end='')
            input()
            print('SINISTRA: In the United Kingdom, Ursa Major is known as the Plough.', end='')
            input()

        #QUESTION #2
        print('SINISTRA: Question two - Which zodiac constellation is located between Cancer and Taurus?', end='')
        input()
        print(
            '\n[1] Taurus\n'
            '[2] Gemini\n'
            '[3] Leo\n'
            '[4] Virgo\n'
        )
        x = input()
        if x == '1':
            print('\nSINISTRA: Incorrect!', end='')
            input()
            print('SINISTRA: Taurus can be found between Aries and Gemini, however Leo is found between Cancer and Taurus.', end='')
            input()
        elif x == '2':
            print('\nSINISTRA: Incorrect!', end='')
            input()
            print('SINISTRA: Gemini can be found between Taurus and Cancer, however Leo is found between Cancer and Taurus.', end='')
            input()
        elif x == '3':
            self.house_pts.Add_House_Points(5)
            print('\nSINISTRA: Correct!', end='')
            input()
            print('SINISTRA: Leo is found in the fifth position of the Zodiac constellations and appears in the\n'
                'sky from July 23 to August 22.', end='')
            input()
        elif x == '4':
            print('\nSINISTRA: Incorrect!', end='')
            input()
            print('SINISTRA: Virgo can be found between Leo and Libra, however Leo is found between Cancer and Taurus.', end='')
            input()
        else:
            print('\nSINISTRA: Time\'s up!', end='')
            input()
            print('SINISTRA: Leo is found in the fifth position of the Zodiac constellations and appears in the\n'
                'sky from July 23 to August 22.', end='')
            input()

        #QUESTION #3
        print('\nSINISTRA: Question 3 - At what time of the year can Orion be seen?', end='')
        input()
        print(
            '\n[1] Summer\n'
            '[2] Winter\n'
            '[3] Spring\n'
            '[4] Fall\n'
        )
        x = input()
        if x == '1':
            print('\nSINISTRA: Incorrect!', end='')
            input()
            print('SINISTRA: The constellation Orion is visible during Winter, not Summer.', end='')
            input()
        elif x == '2':
            self.house_pts.Add_House_Points(5)
            print('\nSINISTRA: Correct!', end='')
            input()
            print('SINISTRA: The constellation Orion is visible during Winter.', end='')
            input()
        elif x == '3':
            print('\nSINISTRA: Incorrect!', end='')
            input()
            print('SINISTRA: The constellation Orion is visible during Winter, not Spring.', end='')
            input()
        elif x == '4':
            print('\nSINISTRA: Incorrect!', end='')
            input()
            print('SINISTRA: The constellation Orion is visible during Winter, not Fall.', end='')
            input()
        else:
            print('\nSINISTRA: Time\'s up!', end='')
            input()
            print('SINISTRA: The constellation Orion is visible during Winter.', end='')
            input()
        print('SINISTRA: Unfortunately that\'s all the time we have for today.', end='')
        input()
        print('SINISTRA: Class dismissed!', end='')
        input()
        #END ASTRONOMY CLASS

class Chapter():
    def __init__(self, User, Pts):
        self.player = User
        self.house_pts = Pts
        self.subchapter = Subchapter(User, Pts)
        
    def Decide_Class_One(self, user_num):
        if user_num == '1':
            self.subchapter.Defense()
            Day_3.Attend1 = True
        elif user_num == '2':
            self.subchapter.Divination()
            Day_3.Attend2 = True
        elif user_num == '3':
            self.subchapter.Astronomy()
            Day_3.Attend3 = True
        else:
            print(f"\n{self.player.companion.upper()}: Come on, now. Pick one!\n")
            user_num = input()
            self.Decide_Class_One(user_num)

    def Sub_Decide_One(self, user_num):
        if user_num == '1':
            self.subchapter.Divination()
            Day_3.Attend2 = True
        elif user_num == '2':
            self.subchapter.Astronomy()
            Day_3.Attend3 = True
        else:
            print('\n~You\'re not getting out of this one so easy...~\n')
            user_num = input()
            user_input = input()
            self.Sub_Decide_One(user_input)

    def Sub_Decide_Two(self, x):
        if x == '1':
            self.subchapter.Defense()
            Day_3.Attend1 = True
        elif x == '2':
            self.subchapter.Astronomy()
            Day_3.Attend3 = True
        else:
            print('\n~You\'re not getting out of this one so easy...~\n')
            user_input = input()
            self.Sub_Decide_Two(user_input)

    def Sub_Decide_Three(self, x):
        if x == '1':
            self.subchapter.Defense()
            Day_3.Attend1 = True
        elif x == '2':
            self.subchapter.Divination()
            Day_3.Attend2 = True
        else:
            print('\n~You\'re not getting out of this one so easy...~\n')
            user_input = input()
            self.Sub_Decide_Three(user_input)

    def Decide_Class_Two(self, user_input):
        if Day_3.Attend1 == True:
            print(
            '\n[1] Divination\n'
            '[2] Astronomy\n'
            )
            user_input = input()
            self.Sub_Decide_One(user_input)
        elif Day_3.Attend2 == True:
            print(
            '\n[1] Defense Against the Dark Arts\n'
            '[2] Astronomy\n'
            )
            user_input = input()
            self.Sub_Decide_Two(user_input)
        elif Day_3.Attend3 == True:
            print(
            '\n[1] Defense Against the Dark Arts\n'
            '[2] Divination\n'
            )
            user_input = input()
            self.Sub_Decide_Three(user_input)
    
    def Execute_Main(self):
        #BEGIN COMMON ROOM
        print('')
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
        print(' ~     CHAPTER 8: The Beyond     ~ ')
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
        input()

        print('\n~ You\'ve nearly recovered from your great battle yesterday, and now you must return\n'
                'your mind to your studies. ~', end='')
        input()
        print(f"\n{self.player.companion.upper()}: I don\'t know how I\'m supposed to pay attention in class today\n"
                'knowing that the treasure it so close now.', end='')
        input()
        print(f"{self.player.companion.upper()}: Anyway, I think you know the drill by now.", end='')
        input()
        print(
        '\n[1] Defense Against the Dark Arts\n'
        '[2] Divination\n'
        '[3] Astronomy\n'
        )
        user_num = input()
        self.Decide_Class_One(user_num)

        #FIRST CLASS ATTENDED

        print('\n~ Now with that out of the way, where would you like to go next? ~', end='')
        user_num = input()
        self.Decide_Class_Two(user_num)

        #SECOND CLASS ATTENDED

        print('\n~ You\'ve finished two of your classes for the day, leaving just one more... ~', end='')
        input()

        if Day_3.Attend1 == True and Day_3.Attend2 == True:
            self.subchapter.Astronomy()
            Day_3.Attend3 = True
        elif Day_3.Attend2 == True and Day_3.Attend3 == True:
            self.subchapter.Defense()
            Day_3.Attend1 = True
        elif Day_3.Attend1 == True and Day_3.Attend3 == True:
            self.subchapter.Divination()
            Day_3.Attend2 = True

        #THIRD CLASS ATTENDED

        if self.player.house == 'Gryffindor':
            self.house_pts.Add_Gryffindor(0)
            self.house_pts.Add_Hufflepuff(60)
            self.house_pts.Add_Ravenclaw(65)
            self.house_pts.Add_Slytherin(80)
        elif self.player.house == 'Hufflepuff':
            self.house_pts.Add_Gryffindor(65)
            self.house_pts.Add_Hufflepuff(0)
            self.house_pts.Add_Ravenclaw(60)
            self.house_pts.Add_Slytherin(80)
        elif self.player.house == 'Ravenclaw':
            self.house_pts.Add_Gryffindor(65)
            self.house_pts.Add_Hufflepuff(60)
            self.house_pts.Add_Ravenclaw(0)
            self.house_pts.Add_Slytherin(80)
        elif self.player.house == 'Slytherin':
            self.house_pts.Add_Gryffindor(80)
            self.house_pts.Add_Hufflepuff(60)
            self.house_pts.Add_Ravenclaw(65)
            self.house_pts.Add_Slytherin(0)

        self.house_pts.Display_Points()