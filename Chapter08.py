import Chapter08b
Ch08b = Chapter08b.Subchapter()
from Main import Lessons

Day_3 = Lessons(False, False, False)

class Dialogue():
    def __init__(self, User):
        self.player = User

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
            print(f"\n{self.player.companion.upper()}: Come on, now. Pick one!\n")
            user_num = input()
            self.Decide_Class_One(user_num)

    def Sub_Decide_One(self, user_num):
        if user_num == '1':
            Subchapter.Divination()
            Day_3.Attend2 = True
        elif user_num == '2':
            Subchapter.Astronomy()
            Day_3.Attend3 = True
        else:
            print('\n~You\'re not getting out of this one so easy...~\n')
            user_num = input()
            user_input = input()
            self.Sub_Decide_One(user_input)

    def Sub_Decide_Two(self, x):
        if x == '1':
            Subchapter.Defense()
            Day_3.Attend1 = True
        elif x == '2':
            Subchapter.Astronomy()
            Day_3.Attend3 = True
        else:
            print('\n~You\'re not getting out of this one so easy...~\n')
            user_input = input()
            self.Sub_Decide_Two(user_input)

    def Sub_Decide_Three(self, x):
        if x == '1':
            Subchapter.Defense()
            Day_3.Attend1 = True
        elif x == '2':
            Subchapter.Divination()
            Day_3.Attend2 = True
        else:
            print('\n~You\'re not getting out of this one so easy...~\n')
            user_input = input()
            self.Sub_Decide_Three(user_input)

    def Decide_Class_Two(self, user_num):
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

Branch = Dialogue()

class Chapter():
    def __init__(self, User, Branch, Pts, Ch08b):
        self.player = User
        self.dialogue = Branch
        self.house_pts = Pts
        self.subchapter = Ch08b
        
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
        Branch.Decide_Class_One(user_num)

        #FIRST CLASS ATTENDED

        print('\n~ Now with that out of the way, where would you like to go next? ~', end='')
        user_num = input()
        Branch.Decide_Class_Two(user_num)

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