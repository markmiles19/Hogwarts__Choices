import time

class Dialogue():
    def __init__(self, User, Decide, Potion, Duel):
        self.player = User
        self.choices = Decide
        self.potions = Potion
        self.dueling = Duel

    def Branch_1(self, x):
        if x == '3':
            pass
        elif x == '1':
            print(f"\n{self.player.rival}: Hey! I\'m standing right here!", end='')
            input()
            print(f"\n{self.player.companion}: Not nearly good enough. Try Again.\n")
            x = input()
            self.Branch_1(x)
        else:
            print(f"\n{self.player.companion}: Not nearly good enough. Try Again.\n")
            x = input()
            self.Branch_1(x)

    def Branch_2(self, x):
        if x == '1':
            print(f"\n{self.player.companion.upper()}: Then I think you know what to do. Good luck!", end='')
            input()
        elif x == '2':
            print(f"\n{self.player.companion.upper()}: That\'s what you were learning about in Defense Against\n"
                'the Dark Arts.', end='')
            input()
            print(f"{self.player.companion.upper()}: A boggart.", end='')
            input()
            print(f"{self.player.companion.upper()}: I think you can take it from here. Good luck!", end='')
            input()
        else:
            print('\nLEO: Well?\n')
            x = input()
            self.Branch_2(x)

    def OrangeVial(self, x):
        if x == '1':
            self.potions.orange = 'Percival'
        elif x == '2':
            self.potions.orange = 'Leo'
        elif x == '3':
            self.potions.orange = 'Milo'
        elif x == '4':
            self.potions.orange = 'User'
        else:
            print('\nPERCIVAL: Come on, this is no time to play around.\n')
            x = input()
            self.OrangeVial(x)

    def PinkVial_1(self, x):
        if x == '1':
            self.potions.pink = 'Leo'
        elif x == '2':
            self.potions.pink = 'Milo'
        elif x == '3':
            self.potions.pink = 'User'
            Choices['TakeFakePotion'] = True
        else:
            print('\nPERCIVAL: Come on, this is no time to play around.\n')
            x = input()
            self.PinkVial_1(x)

    def PinkVial_2(self, x):
        if x == '1':
            Potions['Percival'] = 'Pink'
        elif x == '2':
            Potions['Milo'] = 'Pink'
        elif x == '3':
            Potions['User'] = 'Pink'
            Choices['TakeFakePotion'] = True
        else:
            print('\nPERCIVAL: Come on, this is no time to play around.\n')
            x = input()
            self.PinkVial_2(x)

    def PinkVial_3(self, x):
        if x == '1':
            Potions['Percival'] = 'Pink'
        elif x == '2':
            Potions['Leo'] = 'Pink'
        elif x == '3':
            Potions['User'] = 'Pink'
            Choices['TakeFakePotion'] = True
        else:
            print('\nPERCIVAL: Come on, this is no time to play around.\n')
            x = input()
            self.PinkVial_3(x)

    def PinkVial_4(self, x):
        if x == '1':
            Potions['Percival'] = 'Pink'
        elif x == '2':
            Potions['Leo'] = 'Pink'
        elif x == '3':
            Potions['Milo'] = 'Pink'
        else:
            print('\nPERCIVAL: Come on, this is no time to play around.\n')
            x = input()
            self.PinkVial_4(x)

    def BlueVial_1(self, x):
        if x == '1':
            Potions['Milo'] = 'Blue'
        elif x == '2':
            Potions['User'] = 'Blue'
            Choices['TakeFakePotion'] = True
        else:
            print('\nPERCIVAL: Come on, this is no time to play around.\n')
            x = input()
            self.BlueVial_1(x)

    def BlueVial_2(self, x):
        if x == '1':
            Potions['Leo'] = 'Blue'
        elif x == '2':
            Potions['User'] = 'Blue'
            Choices['TakeFakePotion'] = True
        else:
            print('\nPERCIVAL: Come on, this is no time to play around.\n')
            x = input()
            self.BlueVial_2(x)

    def BlueVial_3(self, x):
        if x == '1':
            Potions['Leo'] = 'Blue'
        elif x == '2':
            Potions['Milo'] = 'Blue'
        else:
            print('\nPERCIVAL: Come on, this is no time to play around.\n')
            x = input()
            self.BlueVial_3(x)

    def BlueVial_4(self, x):
        if x == '1':
            Potions['Milo'] = 'Blue'
        elif x == '2':
            Potions['User'] = 'Blue'
            Choices['TakeFakePotion'] = True
        else:
            print('\nPERCIVAL: Come on, this is no time to play around.\n')
            x = input()
            self.BlueVial_4(x)

    def BlueVial_5(self, x):
        if x == '1':
            Potions['Percival'] = 'Blue'
        elif x == '2':
            Potions['User'] = 'Blue'
            Choices['TakeFakePotion'] = True
        else:
            print('\nPERCIVAL: Come on, this is no time to play around.\n')
            x = input()
            self.BlueVial_5(x)

    def BlueVial_6(self, x):
        if x == '1':
            Potions['Percival'] = 'Blue'
        elif x == '2':
            Potions['Milo'] = 'Blue'
        else:
            print('\nPERCIVAL: Come on, this is no time to play around.\n')
            x = input()
            self.BlueVial_6(x)

    def BlueVial_7(self, x):
        if x == '1':
            Potions['Leo'] = 'Blue'
        elif x == '2':
            Potions['User'] = 'Blue'
            Choices['TakeFakePotion'] = True
        else:
            print('\nPERCIVAL: Come on, this is no time to play around.\n')
            x = input()
            self.BlueVial_7(x)

    def BlueVial_8(self, x):
        if x == '1':
            Potions['Percival'] = 'Blue'
        elif x == '2':
            Potions['User'] = 'Blue'
            Choices['TakeFakePotion'] = True
        else:
            print('\nPERCIVAL: Come on, this is no time to play around.\n')
            x = input()
            self.BlueVial_8(x)

    def BlueVial_9(self, x):
        if x == '1':
            Potions['Percival'] = 'Blue'
        elif x == '2':
            Potions['Leo'] = 'Blue'
        else:
            print('\nPERCIVAL: Come on, this is no time to play around.\n')
            x = input()
            self.BlueVial_9(x)

    def BlueVial_10(self, x):
        if x == '1':
            Potions['Leo'] = 'Blue'
        elif x == '2':
            Potions['Milo'] = 'Blue'
        else:
            print('\nPERCIVAL: Come on, this is no time to play around.\n')
            x = input()
            self.BlueVial_10(x)

    def BlueVial_11(self, x):
        if x == '1':
            Potions['Percival'] = 'Blue'
        elif x == '2':
            Potions['Milo'] = 'Blue'
        else:
            print('\nPERCIVAL: Come on, this is no time to play around.\n')
            x = input()
            self.BlueVial_11(x)

    def BlueVial_12(self, x):
        if x == '1':
            Potions['Percival'] = 'Blue'
        elif x == '2':
            Potions['Leo'] = 'Blue'
        else:
            print('\nPERCIVAL: Come on, this is no time to play around.\n')
            x = input()
            self.BlueVial_12(x)

    def Dueling_1(self, x):
        if x == '1':
            print('\nLEO: Alright. Should I sacrifice myself or would you like to?', end='')
            input()
            print('\n[1] You can sacrifice yourself.\n'
                  '[2] I\'ll sacrifice myself.\n')
            x = input()
            if x == '1':
                self.dueling.leo = False
                print('\nLEO: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('\n~Rictusempra!~', end='')
                input()
                print('\n~Leo falls to the ground unconscious.~', end='')
                input()
            elif x == '2':
                self.dueling.user = False
                print('\nLEO: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('LEO: Rictusempra!', end='')
                input()
                print('\n~Everything around you turns to black.~', end='')
                input()
            else:
                self.dueling.user = False
                print('\nLEO: I\'m just going to assume you\'re okay with sacrificing yourself.', end='')
                input()
                print('LEO: Rictusempra!', end='')
                input()
                print('\n~Everything around you turns to black.~', end='')
                input()
        elif x == '2':
            print('\nMILO: Alright. Should I sacrifice myself or would you like to?', end='')
            input()
            print('\n[1] You can sacrifice yourself.\n'
                  '[2] I\'ll sacrifice myself.\n')
            x = input()
            if x == '1':
                self.dueling.milo = False
                print('\nMILO: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('\n~Rictusempra!~', end='')
                input()
                print('\n~Milo falls to the ground unconscious.~', end='')
                input()
            elif x == '2':
                self.dueling.user = False
                print('\nMILO: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('MILO: Rictusempra!', end='')
                input()
                print('\n~Everything around you turns to black.~', end='')
                input()
            else:
                self.dueling.user = False
                print('\nMILO: I\'m just going to assume you\'re okay with sacrificing yourself.', end='')
                input()
                print('MILO: Rictusempra!', end='')
                input()
                print('\n~Everything around you turns to black.~', end='')
                input()
            
        elif x == '3':
            print('\nLEO: Alright. Which one of us should sacrifice ourselves?', end='')
            input()
            print('\n[1] Leo\n'
                  '[2] Milo\n')
            x = input()
            if x == '1':
                self.dueling.leo = False
                print('\nLEO: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('\nMILO: Rictusempra!', end='')
                input()
                print('\n~Leo falls to the ground unconscious.~', end='')
                input()
            elif x == '2':
                self.dueling.milo = False
                print('\nLEO: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('LEO: Rictusempra!', end='')
                input()
                print('\n~Milo falls to the ground unconscious.~', end='')
                input()
            else:
                self.dueling.leo = False
                print('\nLEO: I\'m just going to sacrifice myself. Now Milo!', end='')
                input()
                print('\nMILO: Rictusempra!', end='')
                input()
                print('\n~Leo falls to the ground unconscious.~', end='')
                input()

        else:
            print('\nLEO: This is serious, now make up your mind.', end='')
            x = input()
            self.Dueling_1(x)

    def Dueling_2(self, x):
        if x == '1':
            print('\nPERCIVAL: Alright. Should I sacrifice myself or would you like to?', end='')
            input()
            print('\n[1] You can sacrifice yourself.\n'
                  '[2] I\'ll sacrifice myself.\n')
            x = input()
            if x == '1':
                self.dueling.percival = False
                print('\nPERCIVAL: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('\n~Rictusempra!~', end='')
                input()
                print('\n~Percival falls to the ground unconscious.~', end='')
                input()
            elif x == '2':
                self.dueling.user = False
                print('\nPERCIVAL: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('PERCIVAL: Rictusempra!', end='')
                input()
                print('\n~Everything around you turns to black.~', end='')
                input()
            else:
                self.dueling.user = False
                print('\nPERCIVAL: I\'m just going to assume you\'re okay with sacrificing yourself.', end='')
                input()
                print('PERCIVAL: Rictusempra!', end='')
                input()
                print('\n~Everything around you turns to black.~', end='')
                input()

        elif x == '2':
            print('\nMILO: Alright. Should I sacrifice myself or would you like to?', end='')
            input()
            print('\n[1] You can sacrifice yourself.\n'
                  '[2] I\'ll sacrifice myself.\n')
            x = input()
            if x == '1':
                self.dueling.milo = False
                print('\nMILO: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('\n~Rictusempra!~', end='')
                input()
                print('\n~Milo falls to the ground unconscious.~', end='')
                input()
            elif x == '2':
                self.dueling.user = False
                print('\nMILO: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('MILO: Rictusempra!', end='')
                input()
                print('\n~Everything around you turns to black.~', end='')
                input()
            else:
                self.dueling.user = False
                print('\nMILO: I\'m just going to assume you\'re okay with sacrificing yourself.', end='')
                input()
                print('MILO: Rictusempra!', end='')
                input()
                print('\n~Everything around you turns to black.~', end='')
                input()

        elif x == '3':
            print('\nPERCIVAL: Alright. Which one of us should sacrifice ourselves?', end='')
            input()
            print('\n[1] Percival\n'
                  '[2] Milo\n')
            x = input()
            if x == '1':
                self.dueling.percival = False
                print('\nPERCIVAL: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('\nMILO: Rictusempra!', end='')
                input()
                print('\n~Percival falls to the ground unconscious.~', end='')
                input()
            elif x == '2':
                self.dueling.milo = False
                print('\nPERCIVAL: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('PERCIVAL: Rictusempra!', end='')
                input()
                print('\n~Milo falls to the ground unconscious.~', end='')
                input()
            else:
                self.dueling.percival = False
                print('\nPERCIVAL: I\'m just going to sacrifice myself. Now Milo!', end='')
                input()
                print('\nMILO: Rictusempra!', end='')
                input()
                print('\n~PERCIVAL falls to the ground unconscious.~', end='')
                input()
                
        else:
            print('\nPERCIVAL: This is serious, now make up your mind.', end='')
            x = input()
            self.Dueling_2(x)

    def Dueling_3(self, x):
        if x == '1':
            print('\nPERCIVAL: Alright. Should I sacrifice myself or would you like to?', end='')
            input()
            print('\n[1] You can sacrifice yourself.\n'
                  '[2] I\'ll sacrifice myself.\n')
            x = input()
            if x == '1':
                self.dueling.percival = False
                print('\nPERCIVAL: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('\n~Rictusempra!~', end='')
                input()
                print('\n~Percival falls to the ground unconscious.~', end='')
                input()
            elif x == '2':
                self.dueling.user = False
                print('\nPERCIVAL: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('PERCIVAL: Rictusempra!', end='')
                input()
                print('\n~Everything around you turns to black.~', end='')
                input()
            else:
                self.dueling.user = False
                print('\nPERCIVAL: I\'m just going to assume you\'re okay with sacrificing yourself.', end='')
                input()
                print('PERCIVAL: Rictusempra!', end='')
                input()
                print('\n~Everything around you turns to black.~', end='')
                input()

        elif x == '2':
            print('\nLEO: Alright. Should I sacrifice myself or would you like to?', end='')
            input()
            print('\n[1] You can sacrifice yourself.\n'
                  '[2] I\'ll sacrifice myself.\n')
            x = input()
            if x == '1':
                self.dueling.leo = False
                print('\nLEO: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('\n~Rictusempra!~', end='')
                input()
                print('\n~Leo falls to the ground unconscious.~', end='')
                input()
            elif x == '2':
                self.dueling.user = False
                print('\nLEO: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('LEO: Rictusempra!', end='')
                input()
                print('\n~Everything around you turns to black.~', end='')
                input()
            else:
                self.dueling.user = False
                print('\nLEO: I\'m just going to assume you\'re okay with sacrificing yourself.', end='')
                input()
                print('LEO: Rictusempra!', end='')
                input()
                print('\n~Everything around you turns to black.~', end='')
                input()

        elif x == '3':
            print('\nPERCIVAL: Alright. Which one of us should sacrifice ourselves?', end='')
            input()
            print('\n[1] Percival\n'
                  '[2] Leo\n')
            x = input()
            if x == '1':
                self.dueling.percival = False
                print('\nPERCIVAL: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('\nLEO: Rictusempra!', end='')
                input()
                print('\n~Percival falls to the ground unconscious.~', end='')
                input()
            elif x == '2':
                self.dueling.leo = False
                print('\nPERCIVAL: Okay. I\'ll see you when all of this is done.', end='')
                input()
                print('PERCIVAL: Rictusempra!', end='')
                input()
                print('\n~Leo falls to the ground unconscious.~', end='')
                input()
            else:
                self.dueling.percival = False
                print('\nPERCIVAL: I\'m just going to sacrifice myself. Now Leo!', end='')
                input()
                print('\nLEO: Rictusempra!', end='')
                input()
                print('\n~PERCIVAL falls to the ground unconscious.~', end='')
                input()

        else:
            print('\nPERCIVAL: This is serious, now make up your mind.', end='')
            x = input()
            self.Dueling_3(x)

    def YouCanDoThis(self):
        print('\n~Y~')
        time.sleep(0.2)
        print('~Yo~')
        time.sleep(0.2)
        print('~You~')
        time.sleep(0.2)
        print('~You c~')
        time.sleep(0.2)
        print('~You ca~')
        time.sleep(0.2)
        print('~You can~')
        time.sleep(0.2)
        print('~You can d~')
        time.sleep(0.2)
        print('~You can do~')
        time.sleep(0.2)
        print('~You can do t~')
        time.sleep(0.2)
        print('~You can do th~')
        time.sleep(0.2)
        print('~You can do thi~')
        time.sleep(0.2)
        print('~You can do this~')
        time.sleep(0.2)
        print('~You can do this!~', end='')
        input()

    def YouCantDoThis(self):
        print('~You can\'t do this!~')
        time.sleep(0.2)
        print('~You can\'t do this~')
        time.sleep(0.2)
        print('~You can\'t do thi~')
        time.sleep(0.2)
        print('~You can\'t do th~')
        time.sleep(0.2)
        print('~You can\'t do t~')
        time.sleep(0.2)
        print('~You can\'t do~')
        time.sleep(0.2)
        print('~You can\'t d~')
        time.sleep(0.2)
        print('~You can\'t~')
        time.sleep(0.2)
        print('~You can\'~')
        time.sleep(0.2)
        print('~You can~')
        time.sleep(0.2)
        print('~You ca~')
        time.sleep(0.2)
        print('~You c~')
        time.sleep(0.2)
        print('~You~')
        time.sleep(0.2)
        print('~Yo~')
        time.sleep(0.2)
        print('~Y~', end='')
        input()

    def DecideTreasure_1(self, x):
        if self.player.house != 'Slytherin':
            if x == '1':
                self.choices.take_full_credit = True
                print('\nPERCIVAL: Are you sure about that?', end='')
                input()
                print('PERCIVAL: Well Milo\'s not going to be happy about this.', end='')
                input()
                print('PERCIVAL: Once we get out, I\'ll go to Professor McGonagall first thing, I\'ll let\n'
                    'her know about Leo and Milo, and then I\'ll hand the box off to her.', end='')
                input()
                print('PERCIVAL: We did it. Both of us.', end='')
                input()
            elif x == '2':
                self.choices.give_full_credit = True
                print('\nPERCIVAL: But why would you do that?', end='')
                input()
                print('PERCIVAL: We were the ones who...', end='')
                input()
                print('PERCIVAL: Wait...', end='')
                input()
                print('PERCIVAL: Of course!', end='')
                input()
                print('PERCIVAL: When Merlin referred to his descendants, he meant Slytherin!', end='')
                input()
                print('PERCIVAL: That must have been what was driving Milo.', end='')
                input()
                print('PERCIVAL: Once we get out, I\'ll go to Professor McGonagall first thing, I\'ll let\n'
                    'her know about Leo and Milo, and then I\'ll hand the box off to her, and I\'ll tell\n'
                    'her to hand it off to Snape.', end='')
                input()
                print('PERCIVAL: We did it. Both of us.', end='')
                input()
            elif x == '3':
                self.choices.split_credit = True
                print('\nPERCIVAL: That only seems fair.', end='')
                input()
                print('PERCIVAL: Once we get out, I\'ll go to Professor McGonagall first thing, I\'ll let\n'
                    'her know about Leo and Milo, and then I\'ll hand the box off to her.', end='')
                input()
                print('PERCIVAL: We did it. Both of us.', end='')
                input()
            else:
                print('\nPERCIVAL: This is too important to be messing around.\n')
                x = input()
                self.DecideTreasure_1(x)
        else:
            #SLYTHERIN PATH HERE
            pass

    def DecideTreasure_2(self, x):
        if self.player.house != 'Slytherin':
            if x == '1':
                self.choices.take_full_credit = True
                print('\nLEO: Are you sure about that?', end='')
                input()
                print('LEO: Well Milo\'s not going to be happy about this.', end='')
                input()
                print('LEO: Once we get out, I\'ll go to Professor McGonagall first thing, I\'ll let\n'
                    'her know about Percival and Milo, and then I\'ll hand the box off to her.', end='')
                input()
                print('LEO: We did it. Both of us.', end='')
                input()
            elif x == '2':
                self.choices.give_full_credit = True
                print('\nLEO: But why would you do that?', end='')
                input()
                print('LEO: We were the ones who...', end='')
                input()
                print('LEO: Wait...', end='')
                input()
                print('LEO: Of course!', end='')
                input()
                print('LEO: When Merlin referred to his descendants, he meant Slytherin!', end='')
                input()
                print('LEO: That must have been what was driving Milo.', end='')
                input()
                print('LEO: Once we get out, I\'ll go to Professor McGonagall first thing, I\'ll let\n'
                    'her know about Percival and Milo, and then I\'ll hand the box off to her, and I\'ll tell\n'
                    'her to hand it off to Snape.', end='')
                input()
                print('LEO: We did it. Both of us.', end='')
                input()
            elif x == '3':
                self.choices.split_credit = True
                print('\nLEO: That only seems fair.', end='')
                input()
                print('LEO: Once we get out, I\'ll go to Professor McGonagall first thing, I\'ll let\n'
                    'her know about Percival and Milo, and then I\'ll hand the box off to her.', end='')
                input()
                print('LEO: We did it. Both of us.', end='')
                input()
            else:
                print('\nLEO: This is too important to be messing around.\n')
                x = input()
                self.DecideTreasure_2(x)
        else:
            #SLYTHERIN PATH HERE
            pass

    def DecideTreasure_3(self, x):
        if self.player.house != 'Slytherin':
            if x == '1':
                self.choices.give_full_credit = True
                print('\nMILO: Are you sure about that?', end='')
                input()
                print('MILO: You\'ve worked so hard to get here.', end='')
                input()
                print('MILO: Well, I suppose it is your choice.', end='')
                input()
                print('MILO: Once we get out, I\'ll go to Professor Snape first thing, I\'ll let\n'
                    'him know about Percival and Leo, and then I\'ll hand the box off to him.', end='')
                input()
                print('MILO: We did it. Both of us.', end='')
                input()
            elif x == '2':
                self.choices.split_credit = True
                print('\nMILO: That only seems fair.', end='')
                input()
                print('MILO: Once we get out, I\'ll go to Professor Snape first thing, I\'ll let\n'
                    'him know about Percival and Leo, and then I\'ll hand the box off to him.', end='')
                input()
                print('MILO: We did it. Both of us.', end='')
                input()
            else:
                print('\nMILO: This is too important to be messing around.\n')
                x = input()
                self.DecideTreasure_3(x)
        else:
            #SLYTHERIN PATH HERE
            pass

    def HospitalWing(self):
        #OPTIMIZE FOR HOUSE PATHS
        print('\n~ You can see a blinding light as you open your eyes... ~', end='')
        input()
        print('\n~ You\'re in the Hospital Wing. ~', end='')
        input()
        print(f"\n~ {self.player.companion} is sitting on the bed next to you. ~", end='')
        input()
        print(f"\n{self.player.companion.upper()}: Welcome back to the land of the living.", end='')
        input()
        print(
            '\n[1] Where\'s Leo?\n'
            f"[2] Where\'s {self.player.rival}?\n"
            '[3] Did we get the treasure?\n'
        )
        x = input()
        if x == '1':
            print(f"\n{self.player.companion.upper()}: He made it out just fine. We all did.", end='')
            input()
        elif x == '2':
            print(f"\n{self.player.companion.upper()}: He made it out just fine. We all did.", end='')
            input()
        elif x == '3':
            print(f"\n{self.player.companion.upper()}: All in good time.", end='')
            input()
        else:
            print(f"\n{self.player.companion.upper()}: I can see you\'re still a bit disoriented.", end='')
            input()
        print(f"{self.player.companion.upper()}: I went to Dumbledore and let him know about what happened down there.", end='')
        input()
        print(f"{self.player.companion.upper()}: As it turns out, you were the last one of us to be nursed back to health.", end='')
        input()
        self.choices.split_credit = True
        print(f'{self.player.companion.upper()}: We all got to talking and we agreed that it would be best if we shared\n'
              f'the treasure with {self.player.rival}.', end='')
        input()
        print(f'{self.player.companion.upper()}: And speaking of which...', end='')
        input()
        print(f'\n~ {self.player.companion} reaches for an object sitting behind him... ~', end='')
        input()
        print('\n~ It\'s a small, silver box. ~', end='')
        input()
        print(f"\n{self.player.companion.upper()}: Merlin left us a note. Do you want to read it?", end='')
        input()
        print(
            '\n[1] Accept\n'
            '[2] Decline\n'
        )
        x = input()
        if x == '1':
            print('\nDearest Adventurer,\n\n'
                  'If you\'re reading this right now, then I applaud your efforts. In case you were wondering\n'
                  'what lies inside the box in front of you, that is unfortunately a secret that will be buried\n'
                  'in my grave. I offer this box to you in the hopes that a generation far from now will remember\n'
                  'everything I\'ve done for them and their school. Although my great seal will keep the box closed\n'
                  'forever, my final wish is for it to be given to the school and to my descendants.\n\n'
                  'Best wishes,~\n'
                  'Merlin~', end='')
            input()
            print('')
        else:
            print('\nPERCIVAL: I understand. I appreciate what you did for us down there, though.', end='')
            input()
        print(f'{self.player.companion.upper()}: I held onto it long enough to show you, but I\'m about to hand it off to Professor\n'
              'Dumbledore once we\'re done.', end='')
        input()
        print(f"{self.player.companion.upper()}: We couldn\'t have done it without you. Remember that.", end='')
        input()

Branch = Dialogue()

class Potions():
    def __init__(self):
        self.orange = 'Default'
        self.pink = 'Default'
        self.blue = 'Default'

Potion = Potions()

class Dueling():
    def __init__(self):
        self.user = False
        self.percival = False
        self.milo = False
        self.leo = False

Duel = Dueling()

class Chapter():
    def __init__(self, User, Decide, Branch, Potion, Duel):
        self.player = User
        self.choices = Decide
        self.dialogue = Branch
        self.potions = Potion
        self.dueling = Duel

    def Execute_Main(self):
        print('')
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
        print(' ~     CHAPTER 9: INTO THE DARK    ~ ')
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
        input()
        print('\n~You and your friends stand before the Room of Requirement, but all you see is a blank wall.~', end='')
        input()
        print('\nPERCIVAL: Now remember, you need to think about how much you need to find the treasure for\n'
              'the door to appear.', end='')
        input()
        print('\n[1] I need to show that Milo.\n'
              '[2] I need to earn Percival\'s respect.\n'
              '[3] I need to restore Merlin\'s Legacy.\n')
        user_input = input()
        self.dialogue.Branch_1(user_input)
        print('\n~Before you a grand, arched door begins to form.~', end='')
        input()
        print(f"\nPERCIVAL: I think you did it, {self.player.first_name}!", end='')
        input()

        #ROOM 1: THE BOGGART
        print('\n~The four of you step inside a small, dimly lit room with a musty smell.~', end='')
        input()
        print('\n~All that stands in front of you is a wardrobe.~', end='')
        input()
        print('\nLEO: What do you think this is?', end='')
        input()
        print('\n[1] I know exactly what this is.\n'
              '[2] I haven\'t the faintest clue.\n')
        user_input = input()
        self.dialogue.Branch_2(user_input)
        print('\n~You approach the wardrobe, wand in your hand, prepared to face your fear.~', end='')
        input()
        print('\n~The door to the wardrobe slowly beings to open...~', end='')
        input()
        if self.player.fear == 'being rejected by others':
            print('\n~~', end='')
            input()
        elif self.player.fear == 'feeling powerless':
            print('\n~You can see into a completely setting: A dark and foggy woods.~', end='')
            input()
            print('\n~You are engaged in battle with a wizard, his face obscured by darkness.~', end='')
            input()
            print('\n~He casts a muffled incantation and you drop to the ground as you write in anguish.~', end='')
            input()
            print('\n~You know this to be the Cruciatus Curse: The most unimaginable pain one could undergo.~', end='')
            input()
        elif self.player.fear == 'being alone':
            print('\n~You can see into a completely different room and a cold breeze takes over you.~', end='')
            input()
            print('\n~It\'s a prison cell. One of the most isolated and secure cells that Azkaban prison\n'
                  'has to offer.~', end='')
            input()
            print('\n~Inside the cell is a person bound by a straight-jacket, struggling to break free.~', end='')
            input()
            print('\n~That person is you.~', end='')
            input()
        elif self.player.fear == 'failing those around you':
            print('\n~You can see into a completely different room that looks like the Great Hall.~', end='')
            input()
            print('\n~You are in the middle of your O.W.L. exams when something goes wrong...~', end='')
            input()
            print('\n~You attempt to cast a spell but your magic is gone.~', end='')
            input()
            print('\n~You are no longer a wizard.~', end='')
            input()
        else:
            print('\n~What sorcery is this? You have no fear? This can\'t be right~', end='')
            input()
        print(f"\nPERCIVAL: Of course, you told the Sorting Hat that your deepest fear was {self.player.fear}.", end='')
        input()
        print('PERCIVAL: You have to fight it!', end='')
        input()
        print('\n~Press R to resist your fear!~\n')
        x = input()
        if x == 'r' or x == 'R':
            self.dialogue.YouCanDoThis()
        else:
            self.dialogue.YouCantDoThis()
        print('\n~Press G to gather your courage!~\n')
        x = input()
        if x == 'g' or x == 'G':
            self.dialogue.YouCanDoThis()
        else:
            self.dialogue.YouCantDoThis()
        print('\n~Press X to cast the spell!~\n')
        x = input()
        if x == 'x' or x == 'X':
            print('\n~ Riddikulus! ~', end='')
            input()
            print('\n~ Your fear transforms into a tap-dancing gorilla. Under other circumstances you would find it amusing. ~', end='')
            input()
            print(f"\nPERCIVAL: You had me worried there for a moment, {self.player.first_name}. Great job!", end='')
            input()
        else:
            print('\n~ Your fear begins to consume you when... ~')
            input()
            print('\nPERCIVAL: Riddikulus!')
            input()
            print('\n~ Your fear transforms into a tap-dancing gorilla. Under other circumstances you would find it amusing. ~', end='')
            input()
            print('\nPERCIVAL: Sorry about that. You weren\'t doing anything and so I had to.', end='')
            input()
        print('\nMILO: Come on, the way to the next room is open now.', end='')
        input()
        print('\n~ Sure enough, the wardrobe and the gorilla have both disappeared and a wooden door has now appeared. ~', end='')
        input()
        print('\n~ You walk on through to find... ~', end='')
        input()

        #ROOM 2: THE POTION
        print('\n~ This next room is no bigger than the last and a small wooden table sits in the center. ~', end='')
        input()
        print('\n~ On the table are three glass tubes being held in place, each one containing a different potion. ~', end='')
        input()
        print('\nPERCIVAL: There\'s a note on the table. What does it say?', end='')
        input()
        print('\nLEO: "Two shall pass. One shall remain."', end='')
        input()
        print('\nPERCIVAL: So each of us need to choose a vial and one of the them will leave that person behind, but you didn\'t\n'
              'think there would be four of us, now did you Merlin?', end='')
        input()
        print(f"PERCIVAL: In that case, I\'ll let you decide how we go about this, {self.player.first_name}.", end='')
        input()

        #DECIDE ORANGE
        print('PERCIVAL: There\'s an orange, pink, and blue vial. Who gets orange?', end='')
        input()
        print('\n[1] Percival\n'
              '[2] Leo\n'
              '[3] Milo\n'
              '[4] Me\n')
        x = input()
        self.dialogue.OrangeVial(x)

        #DECIDE PINK
        print('\nPERCIVAL: Alright, now who gets pink?', end='')
        input()
        if self.potions.orange == 'Percival':
            print('\n[1] Leo\n'
                  '[2] Milo\n'
                  '[3] Me\n')
            x = input()
            self.dialogue.PinkVial_1(x)
        elif self.potions.orange == 'Leo':
            print('\n[1] Percival\n'
                  '[2] Milo\n'
                  '[3] Me\n')
            x = input()
            self.dialogue.PinkVial_2(x)
        elif self.potions.orange == 'Milo':
            print('\n[1] Percival\n'
                  '[2] Leo\n'
                  '[3] Me\n')
            x = input()
            self.dialogue.PinkVial_3(x)
        elif self.potions.orange == 'User':
            print('\n[1] Percival\n'
                  '[2] Leo\n'
                  '[3] Milo\n')
            x = input()
            self.dialogue.PinkVial_4(x)

        #DECIDE BLUE
        print('\nPERCIVAL: Finally, who will get the blue?', end='')
        input()
        if self.potions.orange == 'Percival' and self.potions.pink == 'Leo':
            print('\n[1] Milo\n'
                  '[2] Me\n')
            x = input()
            self.dialogue.BlueVial_1(x)
        elif self.potions.orange == 'Percival' and self.potions.pink == 'Milo':
            print('\n[1] Leo\n'
                  '[2] Me\n')
            x = input()
            self.dialogue.BlueVial_2(x)
        elif self.potions.orange == 'Percival' and self.potions.orange == 'User':
            print('\n[1] Leo\n'
                  '[2] Milo\n')
            x = input()
            self.dialogue.BlueVial_3(x)
        elif self.potions.orange == 'Leo' and self.potions.pink == 'Percival':
            print('\n[1] Milo\n'
                  '[2] Me\n')
            x = input()
            self.dialogue.BlueVial_4(x)
        elif self.potions.orange == 'Leo' and self.potions.pink == 'Milo':
            print('\n[1] Percival\n'
                  '[2] Me\n')
            x = input()
            self.dialogue.BlueVial_5(x)
        elif self.potions.orange == 'Leo' and self.potions.pink == 'User':
            print('\n[1] Percival\n'
                  '[2] Milo\n')
            x = input()
            self.dialogue.BlueVial_6(x)
        elif self.potions.orange == 'Milo' and self.potions.pink == 'Percival':
            print('\n[1] Leo\n'
                  '[2] Me\n')
            x = input()
            self.dialogue.BlueVial_7(x)
        elif self.potions.orange == 'Milo' and self.potions.pink == 'Leo':
            print('\n[1] Percival\n'
                  '[2] Me\n')
            x = input()
            self.dialogue.BlueVial_8(x)
        elif self.potions.orange == 'Milo' and self.potions.pink == 'User':
            print('\n[1] Percival\n'
                  '[2] Leo\n')
            x = input()
            self.dialogue.BlueVial_9(x)
        elif self.potions.orange == 'User' and self.potions.pink == 'Percival':
            print('\n[1] Leo\n'
                  '[2] Milo\n')
            x = input()
            self.dialogue.BlueVial_10(x)
        elif self.potions.orange == 'User' and self.potions.pink == 'Leo':
            print('\n[1] Percival\n'
                  '[2] Milo\n')
            x = input()
            self.dialogue.BlueVial_11(x)
        elif self.potions.orange == 'User' and self.potions.pink == 'Milo':
            print('\n[1] Percival\n'
                  '[2] Leo\n')
            x = input()
            self.dialogue.BlueVial_12(x)
        
        print('\nPERCIVAL: Well, altogether on three now...', end='')
        input()
        print('PERCIVAL: 3...', end='')
        time.sleep(1)
        print('\nPERCIVAL: 2...', end='')
        time.sleep(1)
        print('\nPERCIVAL: 1...', end='')
        time.sleep(1)
        print('\n\n~Sip~', end='')
        input()
        if self.potions.orange == 'Percival':
            print('\nPERCIVAL: Oh...', end='')
            input()
            print('PERCIVAL: I think I\'m feeling a bit drowsy at the moment...', end='')
            input()
            print('\n~Percival falls on the stone-hard floor unconscious.~', end='')
            input()
            print('\nLEO: It was a sleeping solution. I should have known.', end='')
            input()
            print('\nMILO: Come on. We\'ve got one more room to go.', end='')
            input()
            print('\n~A door appears that was not there before, and you continue on...~', end='')
            input()
        elif self.potions.orange == 'Leo':
            print('\nLEO: Oh...', end='')
            input()
            print('LEO: I think I\'m feeling a bit drowsy at the moment...', end='')
            input()
            print('\n~Leo falls on the stone-hard floor unconscious.~', end='')
            input()
            print('\nPERCIVAL: It was a sleeping solution. I should have known.', end='')
            input()
            print('\nMILO: Come on. We\'ve got one more room to go.', end='')
            input()
            print('\n~A door appears that was not there before, and you continue on...~', end='')
            input()
        elif self.potions.orange == 'Milo':
            print('\nMILO: Oh...', end='')
            input()
            print('MILO: I think I\'m feeling a bit drowsy at the moment...', end='')
            input()
            print('\n~Milo falls on the stone-hard floor unconscious.~', end='')
            input()
            print('\nPERCIVAL: It was a sleeping solution. I should have known.', end='')
            input()
            print('\nLEO: Come on. We\'ve got one more room to go.', end='')
            input()
            print('\n~A door appears that was not there before, and you continue on...~', end='')
            input()
        elif self.potions.orange == 'User':
            print('\n~You begin to feel drowsy...~', end='')
            input()
            print('\n~Your eyes grow heavier until...~', end='')
            input()

        if self.potions.orange != 'User':
            #ROOM 3: THE DUEL
            print('\n~The next room is completely empty aside from two runic markings on the ground,\n'
                  'both opposing each other.~', end='')
            input()

            #PERCIVAL IS UNCONSCIOUS
            if self.potions.orange == 'Percival':
                self.dueling.leo = True
                self.dueling.milo = True
                self.dueling.user = True
                print('\nLEO: I know what this is...', end='')
                input()
                print('LEO: Two of us have to duel our way to the treasure.', end='')
                input()
                print('LEO: The only question is which two?', end='')
                input()
                print('\n[1] Me and Leo\n'
                      '[2] Me and Milo\n'
                      '[3] Leo and Milo\n')
                x = input()
                self.dialogue.Dueling_1(x)

            #LEO IS UNCONSCIOUS
            elif self.potions.orange == 'Leo':
                self.dueling.percival = True
                self.dueling.milo = True
                self.dueling.user = True
                print('\nPERCIVAL: I know what this is...', end='')
                input()
                print('PERCIVAL: Two of us have to duel our way to the treasure.', end='')
                input()
                print('PERCIVAL: The only question is which two?', end='')
                input()
                print('\n[1] Me and Percival\n'
                      '[2] Me and Milo\n'
                      '[3] Percival and Milo\n')
                x = input()
                self.dialogue.Dueling_2(x)

            #MILO IS UNCONSCIOUS
            elif self.potions.orange == 'Milo':
                self.dueling.percival = True
                self.dueling.leo = True
                self.dueling.user = True
                print('\nPERCIVAL: I know what this is...', end='')
                input()
                print('PERCIVAL: Two of us have to duel our way to the treasure.', end='')
                input()
                print('PERCIVAL: The only question is which two?', end='')
                input()
                print('\n[1] Me and Percival\n'
                      '[2] Me and Leo\n'
                      '[3] Percival and Leo\n')
                x = input()
                self.dialogue.Dueling_3(x)
                
            else:
                print('\n~Wait, what\'s going on? You shouldn\'t be here!~', end='')
                input()
            
            if self.dueling.user != False:
                print('\n~The two of you that remain continue into the newly materialized room.~', end='')
                input()
                print('\n~The treasure is so close now...~', end='')
                input()

                #ROOM 4: THE TREASURE
                #MAKE SURE THAT ALL HOUSE PATHS WORK!!!
                if self.dueling.user == True and self.dueling.percival == True:
                    print('\n~Sitting on a pedestal at the end of the room is a small, silver box.~', end='')
                    input()
                    print('\nPERCIVAL: There\'s a note. What does it say?', end='')
                    input()
                    print('PERCIVAL: "Dearest Adventurer..."', end='')
                    input()
                    print('PERCIVAL: "If you\'re reading this right now, then I applaud your efforts."', end='')
                    input()
                    print('PERCIVAL: "In case you were wondering what lies inside the box in front of you, that\n'
                          'is unfortunately a secret that will be buried in my grave."', end='')
                    input()
                    print('PERCIVAL: "I offer this box to you in the hopes that a generation far from now will\n'
                          'remember everything I\'ve done for them and their school."', end='')
                    input()
                    print('PERCIVAL: "Although my great seal will keep the box closed forever, my final wish is\n'
                          'for it to be given to the school and to my descendants."', end='')
                    input()
                    print('PERCIVAL: "Best wishes, Merlin."', end='')
                    input()
                    print('PERCIVAL: His descendants? Merlin never had any children. What did he mean by that?', end='')
                    input()
                    print('PERCIVAL: Anyway, what are we going to do about the treasure?', end='')
                    input()
                    if self.player.house != 'Slytherin':
                        print(f"\n[1] Give full credit to {self.player.house}\n"
                            '[2] Give full credit to Slytherin\n'
                            f"[3] Split credit between {self.player.house} and Slytherin\n")
                    else:
                        print('[1] Give full credit to Gryffindor\n'
                            f"[2] Split credit between Slytherin and Gryffindor\n")
                    x = input()
                    self.dialogue.DecideTreasure_1(x)

                elif self.dueling.user == True and self.dueling.leo == True:
                    print('\n~Sitting on a pedestal at the end of the room is a small, silver box.~', end='')
                    input()
                    print('\nLEO: There\'s a note. What does it say?', end='')
                    input()
                    print('LEO: "Dearest Adventurer..."', end='')
                    input()
                    print('LEO: "If you\'re reading this right now, then I applaud your efforts."', end='')
                    input()
                    print('LEO: "In case you were wondering what lies inside the box in front of you, that\n'
                          'is unfortunately a secret that will be buried in my grave."', end='')
                    input()
                    print('LEO: "I offer this box to you in the hopes that a generation far from now will\n'
                          'remember everything I\'ve done for them and their school."', end='')
                    input()
                    print('LEO: "Although my great seal will keep the box closed forever, my final wish is\n'
                          'for it to be given to the school and to my descendants."', end='')
                    input()
                    print('LEO: "Best wishes, Merlin."', end='')
                    input()
                    print('LEO: His descendants? Merlin never had any children. What did he mean by that?', end='')
                    input()
                    print('LEO: Anyway, what are we going to do about the treasure?', end='')
                    input()
                    if self.player.house != 'Slytherin':
                        print(f"\n[1] Give full credit to {self.player.house}\n"
                            '[2] Give full credit to Slytherin\n'
                            f"[3] Split credit between {self.player.house} and Slytherin\n")
                    else:
                        print('[1] Give full credit to Gryffindor\n'
                            f"[2] Split credit between Slytherin and Gryffindor\n")
                    x = input()
                    self.dialogue.DecideTreasure_2(x)

                elif self.dueling.user == True and self.dueling.milo == True:
                    print('\n~Sitting on a pedestal at the end of the room is a small, silver box.~', end='')
                    input()
                    print('\nMILO: There\'s a note. What does it say?', end='')
                    input()
                    print('MILO: "Dearest Adventurer..."', end='')
                    input()
                    print('MILO: "If you\'re reading this right now, then I applaud your efforts."', end='')
                    input()
                    print('MILO: "In case you were wondering what lies inside the box in front of you, that\n'
                          'is unfortunately a secret that will be buried in my grave."', end='')
                    input()
                    print('MILO: "I offer this box to you in the hopes that a generation far from now will\n'
                          'remember everything I\'ve done for them and their school."', end='')
                    input()
                    print('MILO: "Although my great seal will keep the box closed forever, my final wish is\n'
                          'for it to be given to the school and to my descendants."', end='')
                    input()
                    print('MILO: "Best wishes, Merlin."', end='')
                    input()
                    print('MILO: His descendants? Merlin never had any children. What did he mean by that?', end='')
                    input()
                    print('MILO: Anyway, what are we going to do about the treasure?', end='')
                    input()
                    if self.player.house != 'Slytherin':
                        print('[1] Give full credit to Slytherin\n'
                            f"[2] Split credit between {self.player.house} and Slytherin\n")
                    else:
                        print(f"\n[1] Give full credit to Gryffindor\n"
                            '[2] Give full credit to Slytherin\n'
                            f"[3] Split credit between Gryffindor and Slytherin\n")
                    x = input()
                    self.dialogue.DecideTreasure_3(x)

                else:
                    print('\n~ Wait, what\'s going on? You shouldn\'t be here! ~', end='')
                    input()

            else:
                self.choices.sacrifice_self = True
                self.dialogue.HospitalWing()


        else:
            self.choices.take_real_potion = True
            self.dialogue.HospitalWing()