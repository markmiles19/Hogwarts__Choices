class Dialogue():
    def __init__(self, User, Pts, Decide):
        self.player = User
        self.house_pts = Pts
        self.choices = Decide
        self.chapter = Chapter(User, Pts)

    def Branch_1(self, user_input):
        if user_input == '1':
            print(f'\n{self.player.companion.upper()}: Sorry about that. Too much work.', end='')
        elif user_input == '2':
            print(f'\n{self.player.companion.upper()}: Thanks for waiting up for me.', end='')
        else:
            print(f'{self.player.companion.upper()}: Did you say something?\n')
            user_input = input()
            self.Branch_1(user_input)

    def Branch_2(self, user_input):
        if user_input == '1':
            print(f'\n{self.player.companion.upper()}: Well what are you waiting for? Cast Reducto on the glass.', end='')
            input()
        elif user_input == '2':
            print(f'\n{self.player.companion.upper()}: Flitwick taught you both Reducto AND Reparo, right?', end='')
            input()
            print(f'{self.player.companion.upper()}: As long as we repair the glass after we\'re done, no one will ever know.', end='')
            input()
            print(f'{self.player.companion.upper()}: Now go on...', end='')
            input()
        else:
            print(f'{self.player.companion.upper()}: Are you going to cast Reducto or not?\n')
            user_input = input()
            self.Branch_2(user_input)

    def Branch_3(self, user_input):
        if user_input == '1':
            print(f"\n{self.player.companion.upper()}: Not the time, {self.player.first_name}!", end='')
            input()
        elif user_input == '2':
            print('')
        else:
            print('')

    def Reducto(self, user_input):
        if user_input == 'd' or user_input == 'D':
            print('\n~ Reducto! ~', end='')
            input()
        else:
            print(f'\n{self.player.companion.upper()}: Just cast the flippin\' spell already!\n')
            user_input = input()
            self.Reducto(user_input)

    def FiltchIsComing(self):
        print(f"\n{self.player.companion.upper()}: Filtch is coming! Hide!", end='')
        input()
        print('\n~Press H to hide behind a trophy case.~\n')
        user_input = input()
        if user_input == 'h' or user_input == 'H':
            print('\n~The door slowly creeps open and you see the figure of Mr. Filtch holding his cat, Mrs. Norris.~', end='')
            input()
            print('\nFILTCH: Who\'s in here?', end='')
            input()
            print('\n~After what seems like an eternity, he leaves the room.~', end='')
            input()
            print('\n~Now back to what you were doing.~', end='')
            input()
            self.Section_1()
        else:
            print('\n~You accidentally knock over something, alerting Filtch to your presence.~', end='')
            input()
            self.house_pts.Add_House_Points(-15)
            print('\nFILTCH: Looks like it\'s down to the dungeons with you!', end='')
            input()
            print('\n~After another day of classes and a grueling evening serving detention, you start over again...~', end='')
            input()
            self.chapter.Execute_Main()

    def Section_3(self):
        print(
            '\n[<] ~PREV~\n'
            '[1] Zacharias Mumps, 1368\n'
            '[2] Gladys Boothby, 1901\n'
            '[3] Jonathan Able, 1034\n'
            '[4] Katie Rayknolls, 1728\n')
        x = input()
        if x == '<':
            self.Section_2()
        elif x == '3':
            pass
        else:
            self.FiltchIsComing()

    def Section_2(self):
        print(
            '\n[<] ~PREV~\n'
            '[1] Bowman Wright, 1506\n'
            '[2] R. J. H. King, 1968\n'
            '[3] Jocunda Sykes, 1921\n'
            '[4] Modesty Rabnott, 1269\n'
            '[>] ~NEXT~\n')
        x = input()
        if x == '<':
            self.Section_1()
        elif x == '>':
            self.Section_3()
        else:
            self.FiltchIsComing()

    def Section_1(self):
        print(
            '\n[1] M. G. McGonagall, 1971\n'
            '[2] Elfrida Clagg, 1345\n'
            '[3] James Potter, 1973\n'
            '[4] Kennilworthy Whisp, 1954\n'
            '[>] ~NEXT~\n')
        x = input()
        if x == '>':
            self.Section_2()
        else:
            self.FiltchIsComing()

    def Standstill(self, user_input):
        if user_input == '1':
            print(f'\n{self.player.companion.upper()}: No!')
            print(f'{self.player.rival.upper()}: No!\n')
            user_input = input()
            self.Standstill(user_input)
        elif user_input == '2':
            self.choices.compromise = True
            print(f'\n~ You tell {self.player.rival} that he can join the rest of you to the next location. ~', end='')
            input()
            print(f'\n{self.player.rival.upper()}: Alright. I\'ll help you for the time being, but once we find the\n'
                'treasure, it\'s mine!', end='')
            input()
            print(f'\n{self.player.companion.upper()}: I guess that\'s settled then.', end='')
            input()
            print(f'\n{self.player.rival.upper()}: Okay.', end='')
            input()
            print(f'\n{self.player.companion.upper()}: Okay.', end='')
            input()
            print(f'\n~ You dodge patrolling prefects as you return to the {self.player.house} common room and\n'
                'turn in after an exhausting night. ~', end='')
            input()
        elif user_input == '3':
            print('\n~ You cast the stunning spell, Stupefy, and dash out of the room with the trophy. ~')
            input()
            print(f'\n~ After dodging patrolling prefects on your return to the {self.player.house} Common room,\n'
                'you turn in after an exhausting night. ~', end='')
            input()
        elif user_input == '4':
            print(f'\n{self.player.rival.upper}: If that\'s what you want, then so be it.', end='')
            input()
            print(f'{self.player.rival.upper}: Stupefy!', end='')
            input()
            print('\n~ Press D to dodge. ~', end='')
            user_input = input()
            if user_input == 'd' or user_input == 'D':
                pass
            else:
                print(f'\n~ {self.player.rival} stunned you in your right arm. ~', end='')
                input()
            print('\n~ You are hidden behind a column. Will you attack from the left or the right? ~', end='')
            input()
            print(
                '\n[1] Left\n'
                '[2] Right\n'
            )
            user_input = input()
            if user_input == '1':
                print('\n~ You manage to graze his left knee. ~', end='')
                input()
                print(f'\n{self.player.rival.upper}: You\'ll have to do better than that if you want me to yield!', end='')
                input()
            elif user_input == '2':
                print('\n~ You manage to graze his right knee. ~', end='')
                input()
                print(f'\n{self.player.rival.upper}: You\'ll have to do better than that if you want me to yield!', end='')
                input()
            else:
                print('\n~ You sneak a look around the corner... ~', end='')
                input()
                print(f'\n{self.player.rival.upper}: Stupefy!', end='')
                input()
                print('\n~ He blinds your sight temporarily. ~', end='')
                input()
                print(f'\n{self.player.rival.upper}: It\'s never too late to yield!', end='')
                input()
            print('\n~ You leave your cover and open fire on him. ~', end='')
            input()
            print('~ Press S to cast stupefy. ~', end='')
            user_input = input()
            if user_input == 's' or user_input == 'S':
                pass
            else:
                print('~ OUCH ~', end='')
                input()
            print('~Press S to cast stupefy.~', end='')
            user_input = input()
            if user_input == 's' or user_input == 'S':
                pass
            else:
                print('~ OUCH ~', end='')
                input()
            print('~Press P to defend with Protego.~', end='')
            user_input = input()
            if user_input == 'p' or user_input == 'P':
                pass
            else:
                print('~ OUCH ~', end='')
                input()
            print(f'\n~ {self.player.rival} is on the ground now, completely defenseless. What will you do? ~', end='')
            input()
            print(
                '\n[1] Disarm him\n'
                '[2] Let him go\n'
            )
            def RivalFate(x):
                if x == '1':
                    print('\n~ Expelliarmus! ~', end='')
                    input()
                    print(f'\n~ {self.player.rival}\'s wand flies out of his hand and hits the floor. ~', end='')
                    input()
                    print(f'\n{self.player.rival.upper}: Alright! Alright I yield now.', end='')
                    input()
                    print(f'{self.player.rival.upper}: Just take your trophy and go.', end='')
                    input()
                    print(f'\n~ {self.player.rival.upper} trudges out of the room, his pride in shambles. ~', end='')
                    input()
                    print(f'\n~ After dodging patrolling prefects on your return to the {self.player.house} common room,\n'
                    'you turn in after an exhausting night. ~', end='')
                    input()
                elif x == '2':
                    print('\n~ You pocket your want and help him back up on his feet. ~', end='')
                    input()
                    print('\n~ He dashed to the exit, turns back to you briefly, and then disappears. ~', end='')
                    input()
                    print(f'\n~ After dodging patrolling prefects on your return to the {self.player.house} Common room,\n'
                    'you turn in after an exhausting night. ~', end='')
                    input()
                else:
                    print('\nYou have an important decision to make. Now choose!', end='')
                    x = input()
                    RivalFate(x)
            x = input()
            RivalFate(x)
        else:
            print('\n~ This could turn ugly real fast. Now it\'s time to intervene. ~\n')
            user_input = input()
            self.Standstill(user_input)

class Chapter():
    def __init__(self, User, Pts):
        self.player = User
        self.house_pts = Pts
        self.dialogue = Dialogue(User, Pts)
        
    def Execute_Main(self):
        #GRYFFINDOR/RAVENCLAW/HUFFLEPUFF PATH
        print('')
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
        print(' ~   CHAPTER 5: THE LOST SEEKER    ~ ')
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
        input()
        print(f'\n~ Tonight is the night! You wait patiently in the third floor corridor for {self.player.companion} to arrive. ~', end='')
        input()
        if self.player.house != 'Slytherin':
            print('\n~ Finally he approaches you with his younger brother, Leo. ~', end='')
        else:
            print('\n~ Finally he approaches you. ~', end='')
        input()
        print(
            '\n[1] What took you so long?\n'
            '[2] I\'m ready when you are.\n'
        )
        user_input = input()
        self.dialogue.Branch_1(user_input)
        input()
        print(f'{self.player.companion.upper()}: The good news is that the trophy room is open to students at all times.', end='')
        input()
        if self.player.house != 'Slytherin':
            print('\nLEO: The only downside is that the caretaker Mr. Filtch stops by every so often to make sure\n'
                'there aren\'t any students getting up to no good.', end='')
        else:
            print(f'\n{self.player.companion.upper()}: The only downside is that the caretaker Mr. Filtch stops by every so often to make sure\n'
                'there aren\'t any students getting up to no good.', end='')
        input()
        print(f'\n{self.player.companion.upper()}: And as you could imagine that will be a problem for us.', end='')
        input()
        print(f'{self.player.companion.upper()}: Just remember before we go in, Merlin attended Hogwarts around the turn of the 11th century,\n'
            'so we need to find a trophy that was issued to a student around the same time.', end='')
        input()
        print(f'\n~ Without another moment\'s hesitation, {self.player.companion} slowly opens the door... ~', end='')
        input()
        print('\n~ You step foot into a vast assortment of shining silver and gold, making an otherwise small and crowded\n'
            'room feel much bigger in reality. ~', end='')
        input()
        print(f'\n{self.player.companion.upper()}: I\'ll look over here in the Wizard\'s Chess section.', end='')
        input()
        if self.player.house != 'Slytherin':
            print(f'\nLEO: I\'ll check out the Dueling Club section.', end='')
            input()
            print(f"LEO: I guess that leaves you with the Quidditch trophies, {self.player.first_name}.", end='')
            input()
        else:
            print(f'{self.player.companion.upper()}: You can try over in the Quidditch trophies.', end='')
            input()
        print(f'\n{self.player.companion.upper()}: We\'ll meet back up here once we\'re done.', end='')
        input()
        print('\n~ You inch towards a trophy case in the far back, and scan its contents. ~', end='')
        input()
        self.dialogue.Section_1()
        print('\n~ You found it! ~', end='')
        input()
        if self.player.house != 'Slytherin':
            print('\n~ You let Percival and Leo know and they dart over to the trophy. ~', end='')
            input()
        else:
            print('\n~ You let Milo know and he darts over to the trophy. ~', end='')
            input()
        print(f'\n{self.player.companion.upper()}: That\'s great! All we need to do now is break through the glass case.', end='')
        input()
        print(
            '\n[1] That shouldn\'t be too hard.\n'
            '[2] Wouldn\'t that be vandalism?\n'
        )
        x = input()
        self.dialogue.Branch_2(x)
        print('\n~Press D to cast Reducto.~\n')
        x = input()
        self.dialogue.Reducto(x)
        print('\n~ The glass case shatters into a million pieces. Thank Merlin none of them landed on\n'
            'the three of you. ~', end='')
        input()
        print(f'\n{self.player.companion.upper()}: Let\'s see what all the fuss is about with you, Jonathan Able.', end='')
        input()
        print(f'\n~ {self.player.companion} examines the Golden Snitch recreated in fine detail, perched atop the trophy. ~', end='')
        input()
        print(f'\n{self.player.companion.upper()}: There seems to be some sort of markings on the Snitch\'s wings. If I\'m not mistaken...', end='')
        input()
        print(f'{self.player.companion.upper()}: Of course! They\'re coordinates.', end='')
        input()
        print(f'{self.player.companion.upper()}: And they seem to lead off somewhere into the Highlands.', end='')
        input()
        print(f'{self.player.companion.upper()}: We\'re going to need to hold onto this for the moment so that I can study the coordinates\n'
            'and pinpoint the location.', end='')
        input()
        print('\n???: I\'m afraid I can\'t let you do that.', end='')
        input()
        if self.player.house != 'Slytherin':
            print('\n~ Out from behind a trophy case, a Slytherin boy reveals himself. ~', end='')
            input()
            print('\nPERCIVAL: Get lost, Milo! This has nothing to do with you.', end='')
            input()
            print('\nMILO: This has everything to do with me.', end='')
        else:
            print('\n~ Out from behind a trophy case, two Gryffindor boys reveal themselves. ~', end='')
            input()
            print('\nMILO: Get lost, Percival! This has nothing to do with you two.', end='')
            input()
            print('\nPERCIVAL: This has everything to do with us.', end='')
        input()
        print(
            '\n[1] Who\'s this guy?\n'
            '[2] ~ Stay silent ~\n'
        )
        x = input()
        self.dialogue.Branch_3(x)
        print(f'{self.player.companion.upper()}: We found the trophy first. You can leave now.', end='')
        input()
        if self.player.house != 'Slytherin':
            print('\nMILO: I\'m not leaving without that trophy!', end='')
            input()
            print('\nPERCIVAL: What does it matter to you, anyway?', end='')
            input()
            print('\nMILO: The treasure belongs to Slytherin. It always has and it always will.', end='')
            input()
        else:
            print('\nPERCIVAL: We\'re not leaving without that trophy!', end='')
            input()
            print('\nMILO: What does it matter to you, anyway?', end='')
            input()
            print('\nPERCIVAL: We\'re adventurers. Seeking after lost treasure is simply what we do.', end='')
            input()
        print('\n~ Percival and Milo are at a standstill. What are you going to do about it? ~', end='')
        input()
        print(
            '\n[1] I\'m sure if we just talk about it we can come to a mutual understanding.\n'
            '[2] ~ Compromise ~\n'
            '[3] ~ Stun and run ~\n'
            '[4] ~ Wizard\'s duel ~\n'
        )
        x = input()
        self.dialogue.Standstill(x)