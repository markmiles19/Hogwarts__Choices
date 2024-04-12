from Data import Blacklist

class Chapter():
    def __init__(self, User):
        self.player = User

    def Branch_1(self, user_input):
        if user_input == '1':
            if self.player.full_name.upper() in Blacklist:
                print('\nPERCIVAL: *Laughs* You’re really quite the comedian, you are.', end='')
                input()
            else:
                print('\nPERCIVAL: Oh, I remember now! I heard your name called out during the Sorting Ceremony.', end='')
                input()
                print('PERCIVAL: I probably should have mentioned before that I’m actually a second year.', end='')
                input()
        elif user_input == '2':
            print('\nPERCIVAL: Are you sure you’re in the right house? I guess it doesn’t matter anyway...', end='')
            input()
        elif user_input == '3':
            print('\nPERCIVAL: So you\'re the silent type, huh? Interesting.', end='')
            input()
        else:
            print('\nPERCIVAL: Sorry, could you repeat that?\n')
            user_input = input()
            self.Branch_1(user_input)

    def Branch_2(self, user_input):
        if user_input == '1':
            print('\nPERCIVAL: Meet me in the library tomorrow whenever you have the chance. I always go there whenever\n'
                'I have a free period, not just so I can read, but also to think.', end='')
            input()
            print('PERCIVAL: Then I’ll tell you everything about our quest.', end='')
            input()
        elif user_input == '2':
            print('\nPERCIVAL: If you meet me in the library tomorrow, I’ll tell you everything about our quest.', end='')
            input()
        else:
            print('\nPERCIVAL: What was that?\n')
            user_input = input()
            self.Branch_2(user_input)

    def Branch_3(self, user_input):
        if user_input == '1':
            if self.player.full_name.upper() in Blacklist:
                print('\nMILO: Oh you think you’re being funny, do you? That’s fine, I didn’t want to know your real name anyway.', end='')
                input()
            else:
                print('\nMILO: Interesting.', end='')
                input()
        elif user_input == '2':
            print('\nMILO: I would watch the attitude if I were you.', end='')
            input()
        elif user_input == '3':
            print('\nMILO: Okay, I guess that was too much to ask.', end='')
            input()
        else:
            print('\nMILO: What was that?\n')
            user_input = input()
            self.Branch_3(user_input)

    def Branch_4(self, user_input):
        if user_input == '1':
            print('\nMILO: It would be best to talk details tomorrow whenever you have the time. You can meet me down by the boathouse,\n'
                    'since it’s a nice place where I like to get away.', end='')
            input()
        elif user_input == '2':
            print('\nMILO: Alright then. You can meet me down by the boathouse tomorrow and we’ll talk about it then.', end='')
            input()
        else:
            print('\nMILO: What was that?\n')
            user_input = input()
            self.Branch_4(user_input)

    def Execute_Main(self):

        print('')
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
        print(' ~   CHAPTER 2: NEW FRIENDS, NEW BEGINNINGS    ~ ')
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
        input()
        print(f"\n~ You settle into the {self.player.house} common room and you couldn’t feel more at home. ~", end='')
        input()
        print('\n~ A student approaches you as you return from unpacking. ~', end='')
        input()

        #GRYFFINDOR/HUFFLEPUFF/RAVENCLAW PATH
        if self.player.house != 'Slytherin':
            print('\nPERCIVAL: I don’t believe we’ve officially met. I’m Percival, by the way...', end='')
            input()
            print(
            f"\n[1] I’m {self.player.first_name}. {self.player.full_name}.\n"
            '[2] Can’t you see that I’m busy right now.\n'
            '[3] ~ Say nothing ~\n'
            )
            user_input = input()
            self.Branch_1(user_input)
            print('PERCIVAL: I actually have a younger brother who just started this year, Leo. I’m sure you’ll see him around.', end='')
            input()
            print('PERCIVAL: Without giving away too much, I’ll let you in on a little secret...', end='')
            input()
            print('PERCIVAL: The two of us are onto something BIG!', end='')
            input()
            print(
            '\n[1] What do you mean?\n'
            '[2] Is that so?\n'
            )
            user_input = input()
            self.Branch_2(user_input)
            print('PERCIVAL: Anyway, classes start in the morning. I just hope that you’re prepared.', end='')
            input()

        #SLYTHERIN PATH
        elif self.player.house == 'Slytherin':
            print('\nMILO: So you\'re one of the new ones around here. Mind telling me your name?', end='')
            input()
            print(
            f"\n[1] I’m {self.player.first_name}. {self.player.full_name}.\n"
            '[2] Can’t you see that I’m busy right now.\n'
            '[3] ~ Say nothing ~\n'
            )
            user_input = input()
            self.Branch_3(user_input)
            print('\nMILO: My name is Milo, by the way. I’m in my second year at Hogwarts.', end='')
            input()
            print('MILO: I’m sure you’ve noticed by now that the Slytherin house isn’t generally welcoming to first-years, but I’d like to fix that.', end='')
            input()
            print('MILO: As a matter of fact, it would mean a great deal to me if you would take part in my quest inside this castle.', end='')
            input()
            print(
            '\n[1] Quest? What kind of quest?\n'
            '[2] Sure. Why not?\n'
            )
            user_input = input()
            self.Branch_4(user_input)
            print('MILO: I won’t keep you any longer. You’ll need your rest for classes tomorrow.', end='')
            input()

        print('...', end='')
        input()