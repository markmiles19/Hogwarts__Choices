class Chapter():
    def __init__(self, User, Pts, Decide):
        self.player = User
        self.choices = Decide
        self.house_pts = Pts
        
    def Execute_Main(self):
        print('')
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
        print(' ~   CHAPTER 7: OUT OF BOUNDS    ~ ')
        print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
        input()
        if self.choices.compromise:
            print('\n~ You set out from the castle with Percival, Leo, and Milo at nightfall, navigating\n'
                  'hills, ponds, and swamps for what feels like hours. ~', end='')
            input()
            print('\n~ Finally, you come to a decent-sided cave. ~', end='')
            input()
            print('\nPERCIVAL: We need to be prepared for whatever we find in there, so have your wands\n'
                  'at the ready.', end='')
            input()
            print('\nMILO: There\'s nothing scary at all about this.', end='')
            input()
        else:
            print('\n~ You set out from the castle with Percival and Leo at nightfall, navigating hills,\n'
                  'ponds, and swamps for what feels like hours. ~', end='')
            input()
            print('\n~ Finally, you come to a decent-sided cave. ~', end='')
            input()
            print('\nPERCIVAL: We need to be prepared for whatever we find in there, so have your wands\n'
                  'at the ready.', end='')
            input()
            print('\nLEO: I\'m not sure I like this.', end='')
            input()
            print('\n~ Before you manage to set foot in the cave, you hear a rustling sound behind you. ~', end='')
            input()
            print('\nPERCIVAL: What was that?', end='')
            input()
            print('\n~ Everything around you is dead quiet until... ~', end='')
            input()
            print('\nPERCIVAL: Revelio!', end='')
            input()
            print('\n~ From out of the foliage stumbles a newly materialized Milo. ~', end='')
            input()
            print('\nPERCIVAL: I know a disillusionment charm when I see one, now leave us.', end='')
            input()
            print('\nMILO: Like I said, the treasure belongs with Slytherin.', end='')
            input()
            print('\nLEO: ~ Sigh ~', end='')
            input()
            print('LEO: I guess we have no choice.', end='')
            input()
            print('LEO: He\'s with us now.', end='')
            input()
            print('\nPERCIVAL: Fine.', end='')
            input()

        print('\n~ The four of you enter the cave as the Lumos spell provides illumination from the tip\n'
              'of your wand. ~', end='')
        input()
        print('\n~ There seems to be a faint, growling sound coming from the back walls. ~', end='')
        input()
        print('\nMILO: What was that?', end='')
        input()
        print('\nPERCIVAL: If I\'m right then I\'m afraid to say...', end='')
        input()
        print('\n~ From out of the darkness emerges a creature like a fire crab, but bigger... ~', end='')
        input()
        print('\nPERCIVAL: Blast-ended skrewt!', end='')
        input()
        print('\n~ He manages to dodge just as the skrewt shoots fire. ~', end='')
        input()
        print('\n~ It\'s time to put what you\'ve learned into practice. ~', end='')
        input()

        HitPoints = 0
        def Blackout():
            print('\n~ Before you can react, you get hit and become unconscious. ~', end='')
            input()
            print('\n~ Next thing that you know, you are lying on a bed in the hospital wing,\n'
                  'Madame Pomfrey towering over you. ~', end='')
            input()
            print('\n~ POMFREY: You\'re lucky we were able to find you all the way outside the castle! ~', end='')
            input()
            print('POMFREY: Wandering about the castle at night is bad enough, but leaving the castle...', end='')
            input()
            if self.player.house == 'Gryffindor':
                print('POMFREY: I\'ve spoken to your head of house and they have deducted fifty points\n'
                      f'from {self.player.house}.', end='')
                input()
                self.house_pts.Add_House_Points(-50)
            elif self.player.house == 'Slytherin':
                print('POMFREY: I\'ve spoken to Professor Snape and he has deducted fifty points\n'
                      'from Gryffindor.', end='')
                input()
                self.house_pts.Add_House_Points(-50)
            print('~That does not stop you. Once you get out of here, you\'ll finish what you started.~', end='')
            input()
            self.Execute_Main()
                
        print('\nLEO: We\'ve got to find a way to distract him that way we can get in a hit.', end='')
        input()
        print('\nMILO: And one of us needs to get the angle on it.', end='')
        input()
        print('\nLEO: Who should lure it away?', end='')
        input()
        print(
            '\n[1] LEO\n'
            '[2] MILO\n'
        )
        x = input()
        if x == '1':
            print('\nLEO: Good thinking!', end='')
            input()
            print(f"\nMILO: I\'ll help you out, {self.player.first_name}.", end='')
            input()
        elif x == '2':
            print('\nMILO: Good thinking!', end='')
            input()
            print(f"\nLEO: I\'ll help you out, {self.player.first_name}.", end='')
            input()
        else:
            HitPoints += 1
            print('\n~ You take too long and the beast sears your clothing as you dodge out of the way. ~', end='')
            input()
        print('\n~ Cast the incantations indicated... ~', end='')
        input()
        print('\n~ Incendio! ~\n')
        x = input()
        if x == 'Incendio' or x == 'incendio' or x == 'INCENDIO':
            pass
        else:
            HitPoints += 1
            print('\n~ Ouch! ~', end='')
            input()
        print('\n~ Confringo! ~\n')
        x = input()
        if x == 'Confringo' or x == 'confringo' or x == 'CONFRINGO':
            pass
        else:
            HitPoints += 1
            if HitPoints >= 3:
                Blackout()
            else:
                print('\n~ Ouch! ~', end='')
                input()
        print('\n~ Rictusempra! ~\n')
        x = input()
        if x == 'Rictusempra' or x == 'rictusempra' or x == 'RICTUSEMPRA':
            print('\n~ That\'s done it! Keep going! ~', end='')
            input()
        else:
            HitPoints += 1
            if HitPoints >= 3:
                Blackout()
            else:
                print('\n~ Ouch! ~', end='')
                input()
        print('\n~ It\'s coming at you now! Dodge with D. ~\n')
        x = input()
        if x == 'd' or x == 'D':
            pass
        else:
            HitPoints += 1
            if HitPoints >= 3:
                Blackout()
            else:
                print('\n~ Ouch! ~', end='')
                input()
        print('\n~ You are now separated from your helper. ~', end='')
        input()
        print('\n~ You\'re strength is beginning to give, but you are determined. ~', end='')
        input()
        print('\n~ Rctsmpr ~\n')
        x = input()
        if x == 'Rctsmpr' or x == 'rctsmpr' or x == 'RCTSMPR':
            pass
        else:
            HitPoints += 1
            if HitPoints >= 3:
                Blackout()
            else:
                print('\n~ Ouch! ~', end='')
                input()
        print('\n~ Crfngo ~\n')
        x = input()
        if x == 'Crfngo' or x == 'crfngo' or x == 'CRFNGO':
            pass
        else:
            HitPoints += 1
            if HitPoints >= 3:
                Blackout()
            else:
                print('\n~ Ouch! ~', end='')
                input()
        print('\n~ Ineio ~\n')
        x = input()
        if x == 'Ineio' or x == 'ineio' or x == 'INEIO':
            pass
        else:
            HitPoints += 1
            if HitPoints >= 3:
                Blackout()
            else:
                print('\n~ Ouch! ~', end='')
                input()
        print('\n~You\'ve managed to fend of against the skrewt, but now it has both Percival cornered at\n'
              'its pincers and Milo at its rear.~', end='')
        input()
        print(
            '\n[1] Save Percival\n'
            '[2] Save Milo\n'
        )
        def SaveDecision(x):
            if x == '1':
                if self.player.house != 'Slytherin':
                    self.choices.help_companion = True
                else:
                    self.choices.help_rival = True
                print('\n~ You rush in at Percival and push him out of the way just as... ~', end='')
                input()
                print('\n~ Rictusempra! ~', end='')
                input()
                print('\n~ You cast the spell and it dissolves away into nothing. ~', end='')
                input()
                print('\nMILO: Don\'t worry! I\'m perfectly fine over here.', end='')
                input()
                print('\n~ He pats out a waning flame on his robes. ~', end='')
                input()
            elif x == '2':
                if self.player.house != 'Slytherin':
                    self.choices.help_rival = True
                else:
                    self.choices.help_companion = True
                print('\n~ You rush in at Milo and push him out of the way just as... ~', end='')
                input()
                print('\n~ Rictusempra! ~', end='')
                input()
                print('\n~ You cast the spell and it dissolves away into nothing. ~', end='')
                input()
                print('\nPERCIVAL: That was a close one!', end='')
                input()
            else:
                Blackout()
        x = input()
        SaveDecision(x)
        print('\n~ You notice a strange piece of parchment now lying on the ground. ~', end='')
        input()
        print('\nPERCIVAL: That\'s odd.', end='')
        input()
        print('\n~ He inches towards it and begins to read... w~', end='')
        input()
        print('\nPERCIVAL: "In the place that cannot be seen..."', end='')
        input()
        print('PERCIVAL: "The final resting place will be."', end='')
        input()
        print('PERCIVAL: Oh, of course!', end='')
        input()
        print('PERCIVAL: Merlin hid the treasure away in the Room of Requirement!', end='')
        input()
        print(
            '\n[1] The what?\n'
            '[2] ~Stay Silent~\n'
        )
        x = input()
        if x == '1':
            print('\nPERCIVAL: It\'s a room that only appears when you have real need of it.', end='')
            input()
            print('PERCIVAL: Only the room alters its appearance to fit the person\'s needs.', end='')
            input()
        else:
            pass
        print('\nPERCIVAL: Merlin hid the treasure away in there so that only someone who completed every\n'
                'step of the quest can access it.', end='')
        input()
        print('\nMILO: Well we can\'t very well do it tonight.', end='')
        input()
        print('MILO: By the time we return to the castle the sun will be coming up.', end='')
        input()
        print('\nPERCIVAL: I guess you\'re right.', end='')
        input()
        print('PERCIVAL: Tomorrow night, we meet at the seventh floor corridor.', end='')
        input()