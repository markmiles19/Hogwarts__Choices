class Chapter():
    def __init__(self, User, Decide, Pts):
        self.player = User
        self.choices = Decide
        self.house_pts = Pts

    def Execute_Main(self):
            print('')
            print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
            print(' ~     CHAPTER 10: END OF TERM     ~ ')
            print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
            input()

            print('\n~ The term has concluded and Dumbledore makes an announcement at the feast in the Great Hall. ~', end='')
            input()
            print('\nDUMBLEDORE: Another year has concluded, and now the time has come to award the House Cup.', end='')
            input()
            print(f"DUMBLEDORE: Currently standing with {self.house_pts.gryffindor} points...", end='')
            input()
            print("DUMBLEDORE: Gryffindor!", end='')
            input()
            print('\n~ Applause ~', end='')
            input()
            print(f"\nDUMBLEDORE: Currently standing with {self.house_pts.hufflepuff} points...", end='')
            input()
            print("DUMBLEDORE: Hufflepuff!", end='')
            input()
            print('\n~ Applause ~', end='')
            input()
            print(f"\nDUMBLEDORE: Currently standing with {self.house_pts.ravenclaw} points...", end='')
            input()
            print("DUMBLEDORE: Ravenclaw!", end='')
            input()
            print('\n~ Applause ~', end='')
            input()
            print(f"\nDUMBLEDORE: Finally, currently standing with {self.house_pts.slytherin} points...", end='')
            input()
            print(f"DUMBLEDORE: Slytherin!", end='')
            input()
            print('\n~ Applause ~', end='')
            input()
            print(f"\nDUMBLEDORE: Well done! However, recent events must be taken into account.", end='')
            input()

            if self.choices.compromise == True:
                print('\nDUMBLEDORE: It takes nothing short of humility to help the ones who oppose you which is\n'
                    f"why I now award 25 points to {self.player.house}.", end='')
                input()
                self.house_pts.Add_House_Points(25)
                print('\n~ Applause ~', end='')
                input()
            else:
                pass

            if self.choices.help_companion == True:
                print('\nDUMBLEDORE: A true friend is willing to come to one\'s aid in the face of almost\n'
                    f"certain death, and so now I award 10 points to {self.player.house}.", end='')
                input()
                self.house_pts.Add_House_Points(10)
                print('\n~ Applause ~', end='')
                input()
            elif self.choices.help_rival == True:
                print('\nDUMBLEDORE: While being ready to rescue your friends from imminent harm is\n'
                    'a noble service alone, true nobility can be seen in saving one\'s enemy, and\n'
                    f"so now I award {self.player.house} house with 25 points.", end='')
                input()
                self.house_pts.Add_House_Points(25)
                print('\n~ Applause ~', end='')
                input()
            else:
                pass

            if self.choices.take_fake_potion == True:
                print('\nDUMBLEDORE: For making a self-less sacrifice that could have cost themselves\n'
                    f"dearly, I award 25 points to {self.player.house}.", end='')
                input()
                self.house_pts.Add_House_Points(25)
                print('\n~Applause~', end='')
                input()
            elif self.choices.take_real_potion == True:
                print('\nDUMBLEDORE: For making a self-less sacrifice that cost themselves dearly, I\n'
                    f"award 50 points to {self.player.full_name}.", end='')
                input()
                self.house_pts.Add_House_Points(50)
                print('\n~ Applause ~', end='')
                input()
            else:
                pass

            if self.choices.take_full_credit == True:
                print('\nDUMBLEDORE: Long before any one of you were born, there was a great sorcerer\n'
                    'who sat at the very same tables as you.', end='')
                input()
                print('DUMBLEDORE: His name was Merlin.', end='')
                input()
                print(f"DUMBLEDORE: I now award 25 points to {self.player.house} for the discovery of\n"
                    'a treasure that none thought would every see the light of day.', end='')
                input()
                self.house_pts.Add_House_Points(25)
                print('\n~ Applause ~', end='')
                input()
            elif self.choices.give_full_credit == True:
                print('\nDUMBLEDORE: Long before any one of you were born, there was a great sorcerer\n'
                    'who sat at the very same tables as you.', end='')
                input()
                print('DUMBLEDORE: His name was Merlin.', end='')
                input()
                if self.player.house != 'Slytherin':
                    print(f'DUMBLEDORE: I now award 50 points to both {self.player.house} and Slytherin for the discovery\n'
                        'of a treasure that none thought would every see the light of day.', end='')
                    input()
                else:
                    print(f'DUMBLEDORE: I now award 50 points to both Slytherin and Gryffindor for the discovery\n'
                        'of a treasure that none thought would every see the light of day.', end='')
                    input()
                self.house_pts.Add_House_Points(50)
                print('\n~ Applause ~', end='')
                input()
            elif self.choices.split_credit == True:
                print('\nDUMBLEDORE: Long before any one of you were born, there was a great sorcerer\n'
                    'who sat at the very same tables as you.', end='')
                input()
                print('DUMBLEDORE: His name was Merlin.', end='')
                input()
                if self.player.house != 'Slytherin':
                    print(f'DUMBLEDORE: I now award 25 points to both {self.player.house} and Slytherin for the discovery\n'
                        'of a treasure that none thought would every see the light of day.', end='')
                    input()
                else:
                    print(f'DUMBLEDORE: I now award 25 points to both Slytherin and Gryffindor for the discovery\n'
                        'of a treasure that none thought would every see the light of day.', end='')
                    input()
                self.house_pts.Add_House_Points(25)
                print('\n~ Applause ~', end='')
                input()
            else:
                pass


            HP_Dict = {'Gryffindor': self.house_pts.gryffindor,
                       'Hufflepuff': self.house_pts.hufflepuff,
                       'Ravenclaw': self.house_pts.ravenclaw,
                       'Slytherin:': self.house_pts.slytherin}
            keymax = max(zip(HP_Dict.values(), HP_Dict.keys()))[1]

            print('\nDUMBLEDORE: And so now without further ado...', end='')
            input()
            print('DUMBLEDORE: I would like to award the house cup to ' + keymax + '!', end='')
            input()

            if keymax == self.player.house:
                self.player.house = True
                print(f"\n~All of your friends in {self.player.house} cheer with you!~", end='')
                input()
                print('\n~ You\'ve never felt happier in your life! ~', end='')
                input()
            else:
                print('\n~ Even though you didn\'t win, you still cheer anyway. ~', end='')
                input()
                print('\n~ Of course, there\'s always next time... ~', end='')
                input()

            #GRYFFINDOR/HUFFLEPUFF/RAVENCLAW ENDINGS
            if self.player.house != 'Slytherin':
                print('\n~ As you make your way out of the Great Hall with Percival and Leo, you make\n'
                    'eye contact with Milo. You approach him. ~', end='')
                input()

                #BAD ENDING
                if self.choices.take_full_credit == True:
                    print('\nMILO: After all that we\'ve been through, did it really mean nothing\n'
                        'to you?', end='')
                    input()
                    if self.choices.compromise == True:
                        print('MILO: After you offered to help...', end='')
                        input()
                    if self.choices.help_rival == True:
                        print('MILO: After you saved my life...', end='')
                        input()
                    if self.player.win_house_cup == True:
                        print('MILO: I hope you\'re happy that you won the House Cup, knowing that you\n'
                            'lied and cheated to get where you are.', end='')
                        input()
                    else:
                        print('MILO: Not to mention you didn\'t even win the House Cup. What was it all\n'
                            'for then?', end='')
                        input()
                    print('MILO: They say that all wizards from Slytherin go bad eventually. I guess you\'re\n'
                        'no different.', end='')
                    input()
                    print('MILO: Don\'t bother keeping in touch.', end='')
                    input()
                    print('\n~ You watch as he leaves you far behind. There are no words. ~', end='')
                    input()

                #BEST ENDING
                elif self.choices.give_full_credit == True:
                    print('\nMILO: I had no idea Dumbledore was going to award you as well. I didn\'t even\n'
                        'mention a word about you like you asked.', end='')
                    input()
                    print('MILO: Although from what I hear, that man has his ways.', end='')
                    input()
                    print('MILO: Oh, and by the way, I wanted to say thank you...', end='')
                    input()
                    if self.choices.compromise == True:
                        print('MILO: For offering to help...', end='')
                        input()
                    if self.choices.help_rival == True:
                        print('MILO: For saving my life...', end='')
                        input()
                    if self.player.win_house_cup == True:
                        print('MILO: I may not have won the House Cup, but I think I\'ve already been awarded\n'
                            'enough.', end='')
                        input()
                    else:
                        print('MILO: You may not have won the House Cup, but you\'ve won my respect.', end='')
                        input()
                    print('MILO: I look forward to whatever adventure we get ourselves tangled up in next year.', end='')
                    input()
                    print('\n~ You follow Milo out of the school, Percival and Leo at your side. ~', end='')
                    input()

                #GOOD ENDING
                elif self.choices.split_credit == True:
                    print('\nMILO: I\'m glad we got to share this journey together.', end='')
                    input()
                    print('MILO: I wanted to say thank you...', end='')
                    input()
                    if self.choices.compromise == True:
                        print('MILO: For offering to help...', end='')
                        input()
                    if self.choices.help_rival == True:
                        print('MILO: For saving my life...', end='')
                        input()
                    if self.player.win_house_cup == True:
                        print('MILO: I may not have won the House Cup, but I think I\'ve already been awarded\n'
                            'enough.', end='')
                        input()
                    else:
                        print('MILO: You may not have won the House Cup, but you\'ve won my respect.', end='')
                        input()
                    print('MILO: I look forward to whatever adventure we get ourselves tangled up in next year.', end='')
                    input()
                    print('\n~ You follow Milo out of the school, Percival and Leo at your side. ~', end='')
                    input()
                else:
                    pass


            #SLYTHERIN ENDINGS
            else:
                print('\n~ As you make your way out of the Great Hall with Milo, you make\n'
                    'eye contact with Percival. You approach him. ~', end='')
                input()

                #BAD ENDING
                if self.choices.take_full_credit == True:
                    print('\nPERCIVAL: After all that we\'ve been through, did it really mean nothing\n'
                        'to you?', end='')
                    input()
                    if self.choices.compromise == True:
                        print('PERCIVAL: After you offered to help...', end='')
                        input()
                    if self.choices.help_rival == True:
                        print('PERCIVAL: After you saved my life...', end='')
                        input()
                    if self.player.win_house_cup == True:
                        print('PERCIVAL: I hope you\'re happy that you won the House Cup, knowing that you\n'
                            'lied and cheated to get where you are.', end='')
                        input()
                    else:
                        print('PERCIVAL: Not to mention you didn\'t even win the House Cup. What was it all\n'
                            'for then?', end='')
                        input()
                    print('PERCIVAL: They say that all wizards from Slytherin go bad eventually. I guess they\n'
                        'were right.', end='')
                    input()
                    print('PERCIVAL: Don\'t bother keeping in touch.', end='')
                    input()
                    print('\n~ You watch as he leaves you far behind. There are no words. ~', end='')
                    input()

                #BEST ENDING
                elif self.choices.give_full_credit == True:
                    print('\nPERCIVAL: I had no idea Dumbledore was going to award you as well. I didn\'t even\n'
                        'mention a word about you like you asked.', end='')
                    input()
                    print('PERCIVAL: Although from what I hear, that man has his ways.', end='')
                    input()
                    print('PERCIVAL: Oh, and by the way, I wanted to say thank you...', end='')
                    input()
                    if self.choices.compromise == True:
                        print('PERCIVAL: For offering to help...', end='')
                        input()
                    if self.choices.help_rival == True:
                        print('PERCIVAL: For saving my life...', end='')
                        input()
                    if self.player.win_house_cup == True:
                        print('PERCIVAL: I may not have won the House Cup, but I think I\'ve already been awarded\n'
                            'enough.', end='')
                        input()
                    else:
                        print('PERCIVAL: You may not have won the House Cup, but you\'ve won my respect.', end='')
                        input()
                    print('PERCIVAL: I look forward to whatever adventure we get ourselves tangled up in next year.', end='')
                    input()
                    print('\n~ You follow Percival out of the school, Milo and Leo at your side. ~', end='')
                    input()

                #GOOD ENDING
                elif self.choices.split_credit == True:
                    print('\nPERCIVAL: I\'m glad we got to share this journey together.', end='')
                    input()
                    print('PERCIVAL: I wanted to say thank you...', end='')
                    input()
                    if self.choices.compromise == True:
                        print('PERCIVAL: For offering to help...', end='')
                        input()
                    if self.choices.help_rival == True:
                        print('PERCIVAL: For saving my life...', end='')
                        input()
                    if self.player.win_house_cup == True:
                        print('PERCIVAL: I may not have won the House Cup, but I think I\'ve already been awarded\n'
                            'enough.', end='')
                        input()
                    else:
                        print('PERCIVAL: You may not have won the House Cup, but you\'ve won my respect.', end='')
                        input()
                    print('PERCIVAL: I look forward to whatever adventure we get ourselves tangled up in next year.', end='')
                    input()
                    print('\n~ You follow Percival out of the school, Milo and Leo at your side. ~', end='')
                    input()
                else:
                    pass
            


            #END OF GAME
            print('\n~ Thank you for playing Hogwarts: Choices... ~', end='')
            input()
            print('\n~ But there still remains so much to be done! ~', end='')
            input()
            print('\n~ Replay the game as a different Hogwarts house and view every story path. ~', end='')
            input()
            print('\nCREDITS', end='')
            input()
            print('\nMARK MILES\nSTORY/CODING', end='')
            input()
            print('\nMICHAEL MARTIN\nPLANNING', end='')
            input()
            print('\nJ.K. ROWLING\nIDEAS/CHARACTERS', end='')
            input()
            print('\nEND OF PROGRAM', end='')