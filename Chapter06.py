import Chapter06b
Ch06b = Chapter06b.Subchapter()
from Main import Lessons

Day_2 = Lessons(False, False, False)

class Dialogue():
    def __init__(self, User, Branch, Ch06b):
        self.player = User
        self.dialogue = Branch
        self.subchapter = Ch06b

    def Decide_Class_One(self, x):
        print(f"\n{self.player.companion.upper()}: See you later, {self.player.first_name}.", end='')
        input()
        if x == '1':
            self.subchapter.Transfiguration()
            Day_2.Attend1 = True
        elif x == '2':
            self.subchapter.Herbology()
            Day_2.Attend2 = True
        elif x == '3':
            self.subchapter.MagicalCreatures()
            Day_2.Attend3 = True
        else:
            print(f"\n{self.player.companion.upper()}: Come on, now. Pick one!\n")
            x = input()
            self.DecideClassOne(x)

    def Decide_Class_Two(self):
        def SubDecideOne(x):
            if x == '1':
                self.subchapter.Herbology()
                Day_2.Attend2 = True
            elif x == '2':
                self.subchapter.MagicalCreatures()
                Day_2.Attend3 = True
            else:
                print('\n~You\'re not getting out of this one so easy...~\n')
                x = input()
                SubDecideOne(x)
        def SubDecideTwo(x):
            if x == '1':
                self.subchapter.Transfiguration()
                Day_2.Attend1 = True
            elif x == '2':
                self.subchapter.MagicalCreatures()
                Day_2.Attend3 = True
            else:
                print('\n~You\'re not getting out of this one so easy...~\n')
                x = input()
                SubDecideTwo(x)
        def SubDecideThree(x):
            if x == '1':
                self.subchapter.Transfiguration()
                Day_2.Attend1 = True
            elif x == '2':
                self.subchapter.Herbology()
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

class Chapter():
    def __init__(self, User, Decide, Branch, Pts, Ch06b):
        self.player = User
        self.choices = Decide
        self.dialogue = Branch
        self.house_pts = Pts
        self.subchapter = Ch06b
        
    def Execute_Main(self):
        print('')
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
        print(' ~   CHAPTER 6: CHAIRS, CABBAGES, AND CRABS    ~ ')
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
        input()
        if self.player.house != 'Slytherin':
            print('\n~Following the exciting events from last night, you struggle to adjust to start\n'
                'of a new day as you meet Percival in the common room.~', end='')
            input()
            print(f"\n{self.player.companion.upper()}: I was just looking for you.", end='')
            input()
            print(f"{self.player.companion.upper()}: You\'ll be happy to hear that I did a bit of research earlier and I now\n"
                'know exactly where the next step in our journey will take us.', end='')
            input()
            print(f"{self.player.companion.upper()}: Mind you that it will be several miles of walking distance, and should anything\n"
                f"go wrong or one of us gets hurt, it\'ll be points from {self.player.house}.", end='')
            input()
            if self.choices.compromise == True:
                print(f"{self.player.companion.upper()}: As much as I disagree with bringing {self.player.rival.upper()} along, it looks like i have\n"
                    'no choice but to let him know when I get the chance.', end='')
                input()
            else:
                print(f"{self.player.companion.upper()}: And hopefully {self.player.rival.upper()} will learn to keep his fat nose out of our business.", end='')
                input()
        print(f"{self.player.companion.upper()}: Anyway, which class do you think you're going to first?", end='')
        input()
        print(
        '\n[1] Transfiguration\n'
        '[2] Herbology\n'
        '[3] Care for Magical Creatures\n'
        )
        x = input()
        self.dialogue.DecideClassOne(x)
        print('\n~Now with that out of the way, where would you like to go next?~', end='')
        input()
        self.dialogue.DecideClassTwo()
        print('\n~You\'ve finished two of your classes for the day, leaving just one more...~', end='')
        input()
        if Day_2.Attend1 == True and Day_2.Attend2 == True:
            self.subchapter.MagicalCreatures()
            Day_2.Attend3 = True
        elif Day_2.Attend2 == True and Day_2.Attend3 == True:
            self.subchapter.Transfiguration()
            Day_2.Attend1 = True
        elif Day_2.Attend1 == True and Day_2.Attend3 == True:
            self.subchapter.Herbology()
            Day_2.Attend2 = True

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

