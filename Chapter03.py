from Data import Lessons

Day_1 = Lessons(False, False, False)

class Subchapter():
    def __init__(self, User, Pts):
        self.player = User
        self.house_pts = Pts

    def Branch_1(self, user_input):
        if user_input == '1':
            print('\nFLITWICK: Alright. You can come to the front.', end='')
            input()
        else:
            print('\nFLITWICK: Anyone...?', end='')
            input()
            print('FLITWICK: Let\'s have you, right there in the middle. Is that alright?', end='')
            input()

    def SayUp(self, x):
            if x == 'up' or x == 'UP':
                print('\n~ Say UP ~\n')
                x = input()
                if x == 'up' or x == 'UP':
                    print('\n~ Say UP ~\n')
                    x = input()
                    if x == 'up' or x == 'UP':
                        self.house_pts.Add_House_Points(5)
                    else:
                        print(f"HOOCH: You're going to have to do better than that, {self.player.last_name}.", end='')
                        input()
                        print('\n~Say UP~\n')
                        x = input()
                        self.SayUp(x)
                else:
                    print(f"HOOCH: You're going to have to do better than that, {self.player.last_name}.", end='')
                    input()
                    print('\n~ Say UP ~\n')
                    x = input()
                    self.SayUp(x)
            else:
                print(f"HOOCH: You're going to have to do better than that, {self.player.last_name}.", end='')
                input()
                print('\n~ Say UP ~\n')
                x = input()
                self.SayUp(x)

    def FlyUp(self):
        print('\n~ Press W to fly up. ~\n')
        user_input = input()
        if user_input == 'w' or user_input == 'W':
            pass
        else:
            print('\nHOOCH: Wrong way!\n')
            self.FlyUp()

    def FlyDown(self):
        print('\n~ Press S to fly down. ~\n')
        user_input = input()
        if user_input == 's' or user_input == 'S':
            pass
        else:
            print('\nHOOCH: Wrong way\n')
            self.FlyDown()

    def Charms(self):
        print('\n~ You make your way through the maze of moving staircases, and eventually reach the Charms classroom\n'
        'on the second floor. ~', end='')
        input()
        print('\n~ A small man like a dwarf, Professor Flitwick, stands on a pile of books. ~', end='')
        input()
        print('\nFLITWICK: Good morning, class! Today I thought that we would start the first class of the term with\n'
            'a more exciting spell.', end='')
        input()
        print('FLITWICK: Today, we will be learning the Reducto spell, which put simply, destroys objects.', end='')
        input()
        print('\n~ OOH ~', end='')
        input()
        print('\nFLITWICK: Now I will have you know that after this spell has been put into practice, we will then\n'
            'learn the spell Reparo, which repairs broken objects.', end='')
        input()
        print('FLITWICK: Now may I have a volunteer to demonstrate the Reducto spell?', end='')
        input()
        print(
            '\n[1] ~Raise hand~\n'
            '[2] ~Stay silent~\n'
        )
        user_input = input()
        self.Branch_1(user_input)
        print('FLITWICK: Once you\'re ready, I would like for you to aim at the statue at the far end of the room\n'
            'and repeat my wand movements.', end='')
        input()
        print('FLITWICK: Watch closely!', end='')
        input()
        print('\n~ Replicate Flitwick\'s pattern in order to learn the Reducto spell, but be careful. If you mess\n'
            'up at all, you will not earn house points. ~', end='')
        input()
        print('\nFLITWICK: Let us begin!', end='')
        input()
        print('\n~ tfvbnjytfvbnjy ~\n')
        x = input()
        if x == 'tfvbnjytfvbnjy':
            self.house_pts.Add_House_Points(10)
        else:
            print('FLITWICK: Oh, not good.', end='')

        print('\n~ rdcvbhtrdcvbht ~\n')
        x = input()
        if x == 'rdcvbhtrdcvbht':
            self.house_pts.Add_House_Points(10)
        else:
            print('FLITWICK: Oh, not good.', end='')

        print('\n~ esxcvgresxcvgr ~\n')
        x = input()
        if x == 'esxcvgresxcvgr':
            self.house_pts.Add_House_Points(10)
        else:
            print('FLITWICK: Oh, not good.', end='')

        print('\nFLITWICK: Reducto!', end='')
        input()
        print('\n~ You cast the incantation at the statue and it reduces itself to rubble. ~', end='')
        input()
        print('\nFLITWICK: Excellent casting! Now we will learn how to repair the object.', end='')
        input()
        print('FLITWICK: Let us begin!', end='')
        input()
        print('\n~ tyjnbvftyjnbvf ~\n')
        x = input()
        if x == 'tyjnbvftyjnbvf':
            self.house_pts.Add_House_Points(10)
        else:
            print('FLITWICK: Oh, not good.', end='')

        print('\n~ rthbvcdrthbvcd ~\n')
        x = input()
        if x == 'rthbvcdrthbvcd':
            self.house_pts.Add_House_Points(10)
        else:
            print('FLITWICK: Oh, not good.', end='')

        print('\n~ ergvcxsergvcxs ~\n')
        x = input()
        if x == 'ergvcxsergvcxs':
            self.house_pts.Add_House_Points(10)
        else:
            print('FLITWICK: Oh, not good.', end='')

        print('\nFLITWICK: Reparo!', end='')
        input()
        print('\n~ You pieces of the statue slowly reassemble themselves until they finally become whole. ~', end='')
        input()
        print('\nFLITWICK: Well done! Now you know how to use both Reducto and Reparo.', end='')
        input()
        print('FLITWICK: That is all for today. Class dismissed.', end='')
        input()

    def Potions(self):
        print('\n~ You descend down into the deep, dark dungeons of the castle where you arrive at the potions classroom. ~', end='')
        input()
        print('\nProfessor Snape approaches the front of the class and everyone immediately falls silent.', end='')
        input()
        print('\nSNAPE: There will no foolish wand-waving or silly incantations in this class.', end='')
        input()
        print('SNAPE: Today, your assignment will be to brew the Wiggenweld potion, and seeing that it\'s the most\n'
            'basic of potions, I see no reason for anything other than perfection.', end='')
        input()
        print('SNAPE: Fail to do so, and you will suffer my...', end='')
        input()
        print('SNAPE: Displeasure.', end='')
        input()
        print('SNAPE: Open your books to page 12 and begin.', end='')
        input()
        print('\n~ 12 ~\n'
            '~ Chapter 1 ~\n'
            '~ Wiggenweld Potion ~\n'
            '~ The Wiggenweld potion heals all injuries inflicted upon the one who consumes its contents. In order\n'
            'to begin, you must first acquire bark of the wiggentree, and break apart until no longer possible. ~', end='')
        input()
        print('\n~ Press B to break wiggentree bark. ~\n')
        x = input()
        if x == 'b' or x == 'B':
            print('\n~Press B to break wiggentree bark.~\n')
            x = input()
            if x == 'b' or x == 'B':
                print('\n~Press B to break wiggentree bark.~\n')
                x = input()
                if x == 'b' or x == 'B':
                    self.house_pts.Add_House_Points(5)
                else:
                    print(f"\nSNAPE: {self.player.last_name}! Don't force me to deduct house points.", end='')
                    input()
            else:
                print(f"\nSNAPE: {self.player.last_name}! Don't force me to deduct house points.", end='')
                input()
        else:
            print(f"\nSNAPE: {self.player.last_name}! Don't force me to deduct house points.", end='')
            input()

        print('\n~ Next you must add the broken pieces of wiggentree bark into the cauldron in patient succession. ~', end='')
        input()
        print('\n~ Press A to add the contents to the potion. ~\n')
        x = input()
        if x == 'a' or x == 'A':
            print('\n~ Press A to add the contents to the potion. ~\n')
            x = input()
            if x == 'a' or x == 'A':
                print('\n~ Press A to add the contents to the potion. ~\n')
                x = input()
                if x == 'a' or x == 'A':
                    self.house_pts.Add_House_Points(5)
                else:
                    print(f"SNAPE: {self.player.last_name}! Don't force me to deduct house points.", end='')
                    input()
            else:
                print(f"SNAPE: {self.player.last_name}! Don't force me to deduct house points.", end='')
                input()
        else:
            print(f"SNAPE: {self.player.last_name}! Don't force me to deduct house points.", end='')
            input()

        print('\n~ Finally, stir the wiggentree bark until the potion turns a bright shade of green. ~', end='')
        input()
        print('\n~ Stir: asdfghjkl ~\n')
        x = input()
        if x == 'asdfghjkl':
            print('\n~ Stir: lkjhgfdsa ~\n')
            x = input()
            if x == 'lkjhgfdsa':
                print('\n~ Stir: poiuytrewq ~\n')
                x = input()
                if x == 'poiuytrewq':
                    print('\nStir: zxcvbnm\n')
                    x = input()
                    if x == 'zxcvbnm':
                        self.house_pts.Add_House_Points(5)
                    else:
                        print(f"SNAPE: {self.player.last_name}! Don't force me to deduct house points.", end='')
                else:
                    print(f"SNAPE: {self.player.last_name}! Don't force me to deduct house points.", end='')
            else:
                print(f"SNAPE: {self.player.last_name}! Don't force me to deduct house points.", end='')
        else:
            print(f"SNAPE: {self.player.last_name}! Don't force me to deduct house points.", end='')

        print('\nSNAPE: Time\'s up! Let\'s witness the damage done today.', end='')
        input()
        print('\n~ Professor Snape inches towards your cauldron, towering over you. ~', end='')
        input()
        print('\nSNAPE: What more would I expect from some miserable first year? Count yourself grateful that with\n'
            'this being the first day of term, I\'ve chosen not to deduct house points.', end='')
        input()
        print('SNAPE: That is all for today. Class dismissed.', end='')
        input()

    def Flying(self):
        print('\n~ After navigating the vast, open grounds of the castle, you find yourself lined up alongside\n'
        'other first-years, a broomstick on the ground separating each one of you. ~', end='')
        input()
        print('\n~ Madame Hooch approaches the class. ~', end='')
        input()
        print('\nHOOCH: Welcome to your first flying lesson. We\'ll start with the basics. Everyone hold your hand\n'
            'over the broom on your right and say "up!"', end='')
        input()
        print('\n~ Say UP ~\n')
        user_input = input()
        self.SayUp(user_input)
        print('\nHOOCH: Right. Once you\'ve managed to lift your broomstick, you will be ready to mount it.', end='')
        input()
        print('HOOCH: Start by flying up slowly and then touching back down again.', end='')
        input()
        self.FlyUp()
        self.FlyDown()
        self.house_pts.Add_House_Points(10)
        print('\nHOOCH: Well done. I hope you\'ve grown more acquainted with the basics of broom control during our brief\n'
            'class period, although unfortunately we\'ve still got a long ways to go before any of you are ready to fly.', end='')
        input()
        print('HOOCH: Class dismissed!', end='')
        input()

class Dialogue():
    def __init__(self, User, Pts):
        self.player = User
        self.house_pts = Pts
        self.subchapter = Subchapter(User, Pts)

    def Branch_1(self, user_input):
        if user_input == '1':
            print(f"\n{self.player.companion.upper()}: Optimism. I can appreciate that.", end='')
            input()
        elif user_input == '2':
            print(f"\n{self.player.companion.upper()}: Everyone’s like that on their first day. It’s nothing to worry about.", end='')
            input()
        elif user_input == '3':
            print(f"\n{self.player.companion.upper()}: Can’t say that I blame you.", end='')
            input()
        else:
            print(f"\n{self.player.companion.upper()}: Come on. Be honest with me, now.\n")
            user_input = input()
            self.Branch_1(user_input)

    def Decide_Class_One(self, user_input):
        if user_input == '1':
            if self.player.house == 'Ravenclaw':
                print(f"\n{self.player.companion.upper()}: Excellent choice! Professor Flitwick is the head of Ravenclaw and you’ll learn so many\n"
                    'useful spells from him.', end='')
                input()
            else:
                print(f"\n{self.player.companion.upper()}: Interesting choice. You won’t see me in your classes since I’m not a first-year, but I hope it\n"
                'goes well for you.', end='')
                input()
            print('...', end='')
            input()
            self.subchapter.Charms()
            Day_1.Attend1 = True
                
        elif user_input == '2':
            if self.player.house == 'Gryffindor':
                print(f"\n{self.player.companion.upper()}: Really? Potions with Snape? Everyone in Gryffindor hates him.", end='')
                input()
                print('PERCIVAL: Well, I suppose it is your choice. Just don’t say that I didn’t give you a fair warning.', end='')
                input()
            elif self.player.house == 'Slytherin':
                print('\nMILO: Despite what some may say, potions is one of my favorite subjects.',end='')
                input()
                print('MILO: Professor Snape on the other hand is a complete slimeball.',end='')
                input()
                print('MILO: What’s worse is that he’s the head of Slytherin house, but I wouldn’t let that get in the way of\n'
                    'learning if I were you.', end='')
                input()
            else:
                print(f"\n{self.player.companion.upper()}: Interesting choice. You won’t see me in your classes since I’m not a first-year, but I hope it\n"
                'goes well for you.', end='')
                input()
            print('...', end='')
            input()
            self.subchapter.Potions()
            Day_1.Attend2 = True
            

        elif user_input == '3':
            print(f"\n{self.player.companion.upper()}: Interesting choice. You won’t see me in your classes since I’m not a first-year, but I hope it\n"
            'goes well for you.', end='')
            input()
            print('...', end='')
            input()
            self.subchapter.Flying()
            Day_1.Attend3 = True
        else:
            print(f"\n{self.player.companion.upper()}: Come on, now. You\'ve got to pick one.", end='')
            user_input = input()
            self.Decide_Class_One(user_input)

    def Sub_Decide_One(self, user_input):
        if user_input == '1':
            self.subchapter.Potions()
            Day_1.Attend2 = True
        elif user_input == '2':
            self.subchapter.Flying()
            Day_1.Attend3 = True
        else:
            print('\n~You\'re not getting out of this one so easy...~\n')
            user_input = input()
            self.Sub_Decide_One(user_input)

    def Sub_Decide_Two(self, user_input):
        if user_input == '1':
            self.subchapter.Charms()
            Day_1.Attend1 = True
        elif user_input == '2':
            self.subchapter.Flying()
            Day_1.Attend3 = True
        else:
            print('\n~You\'re not getting out of this one so easy...~\n')
            user_input = input()
            self.Sub_Decide_Two(user_input)

    def Sub_Decide_Three(self, user_input):
        if user_input == '1':
            self.subchapter.Charms()
            Day_1.Attend1 = True
        elif user_input == '2':
            self.subchapter.Potions()
            Day_1.Attend2 = True
        else:
            print('\n~You\'re not getting out of this one so easy...~\n')
            user_input = input()
            self.Sub_Decide_Three(user_input)

    def Decide_Class_Two(self):
        if Day_1.Attend1 == True:
            print(
            '\n[1] Potions\n'
            '[2] Flying\n'
            )
            user_input = input()
            self.Sub_Decide_One(user_input)
        elif Day_1.Attend2 == True:
            print(
            '\n[1] Charms\n'
            '[2] Flying\n'
            )
            user_input = input()
            self.Sub_Decide_Two(user_input)
        elif Day_1.Attend3 == True:
            print(
            '\n[1] Charms\n'
            '[2] Potions\n'
            )
            user_input = input()
            self.Sub_Decide_Three(user_input)

class Chapter():
    def __init__(self, User, Pts):
        self.player = User
        self.house_pts = Pts
        self.dialogue = Dialogue(User, Pts)
        self.subchapter = Subchapter(User, Pts)
        
    def Execute_Main(self):
        print('')
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
        print(' ~    CHAPTER 3: READY TO BEGIN    ~ ')
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
        input()
        print('\n~ You wake up early to watch the sunrise from your dormitory window, ready to start your classes. ~', end='')
        input()
        print(f"\n~ {self.player.companion} stops to talk to you in the common room. ~", end='')
        input()
        print(f"\n{self.player.companion.upper()}: Feeling alright there, {self.player.first_name}?", end='')
        input()
        print(
        '\n[1] Feeling ready to learn is more like it.\n'
        '[2] I just hope I’m ready for this.\n'
        '[3] ~ Shrug ~\n'
        )
        user_input = input()
        self.dialogue.Branch_1(user_input)
        print(f"{self.player.companion.upper()}: If you take a look at the notice board you’ll see the schedule for first-years.", end='')
        input()
        print(f"{self.player.companion.upper()}: Remember, this year you can choose the order in which you attend classes.", end='')
        input()
        print(f"{self.player.companion.upper()}: It looks like today will be Charms, Potions, and Flying for you.", end='')
        input()
        print(f"{self.player.companion.upper()}: So which class will you start the day with?", end='')
        input()
        print(
        '\n[1] Charms\n'
        '[2] Potions\n'
        '[3] Flying\n'
        )
        user_input = input()
        self.dialogue.Decide_Class_One(user_input)
        print('\n~Now with that out of the way, where would you like to go next?~', end='')
        input()
        self.dialogue.Decide_Class_Two()
        print('\n~You\'ve finished two of your classes for the day, leaving just one more...~', end='')
        input()
        if Day_1.Attend1 == True and Day_1.Attend2 == True:
            self.subchapter.Flying()
            Day_1.Attend3 = True
        elif Day_1.Attend2 == True and Day_1.Attend3 == True:
            self.subchapter.Charms()
            Day_1.Attend1 = True
        elif Day_1.Attend1 == True and Day_1.Attend3 == True:
            self.subchapter.Potions()
            Day_1.Attend2 = True