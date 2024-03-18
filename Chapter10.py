def Chapter10():
    #IMPORTED DICTIONARIES
    from Common import playerDict
    from Common import Choices
    from Common import housePts
    
    #IMPORTED FUNCTIONS
    from Common import AddHousePoints

    #IMPORTED ETC
    import colorama
    from colorama import Back, Fore, Style
    colorama.init(autoreset=True)

    print('')
    print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
    print(Back.WHITE + Fore.BLACK + ' ~     CHAPTER 10: END OF TERM     ~ ')
    print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
    input()

    print('\n~The term has concluded and Dumbledore makes an announcement at the feast in the Great Hall.~', end='')
    input()
    print('\nDUMBLEDORE: Another year has concluded, and now the time has come to award the House Cup.', end='')
    input()
    print(f"DUMBLEDORE: Currently standing with {housePts['Gryffindor']} points...", end='')
    input()
    print("DUMBLEDORE: Gryffindor!", end='')
    input()
    print('\n~Applause~', end='')
    input()
    print(f"\nDUMBLEDORE: Currently standing with {housePts['Hufflepuff']} points...", end='')
    input()
    print("DUMBLEDORE: Hufflepuff!", end='')
    input()
    print('\n~Applause~', end='')
    input()
    print(f"\nDUMBLEDORE: Currently standing with {housePts['Ravenclaw']} points...", end='')
    input()
    print("DUMBLEDORE: Ravenclaw!", end='')
    input()
    print('\n~Applause~', end='')
    input()
    print(f"\nDUMBLEDORE: Finally, currently standing with {housePts['Slytherin']} points...", end='')
    input()
    print(f"DUMBLEDORE: Slytherin!", end='')
    input()
    print('\n~Applause~', end='')
    input()
    print(f"\nDUMBLEDORE: Well done! However, recent events must be taken into account.", end='')
    input()

    if Choices['Compromise'] == True:
        print('\nDUMBLEDORE: It takes nothing short of humility to help the ones who oppose you which is\n'
              f"why I now award 25 points to {playerDict['House']}.", end='')
        input()
        AddHousePoints(25)
        print('\n~Applause~', end='')
        input()
    else:
        pass

    if Choices['HelpCompanion'] == True:
        print('\nDUMBLEDORE: A true friend is willing to come to one\'s aid in the face of almost\n'
              f"certain death, and so now I award 10 points to {playerDict['House']}.", end='')
        input()
        AddHousePoints(10)
        print('\n~Applause~', end='')
        input()
    elif Choices['HelpRival'] == True:
        print('\nDUMBLEDORE: While being ready to rescue your friends from imminent harm is\n'
              'a noble service alone, true nobility can be seen in saving one\'s enemy, and\n'
              f"so now I award {playerDict['House']} house with 25 points.", end='')
        input()
        AddHousePoints(25)
        print('\n~Applause~', end='')
        input()
    else:
        pass

    if Choices['TakeFakePotion'] == True:
        print('\nDUMBLEDORE: For making a self-less sacrifice that could have cost themselves\n'
              f"dearly, I award 25 points to {playerDict['fullName']}.", end='')
        input()
        AddHousePoints(25)
        print('\n~Applause~', end='')
        input()
    elif Choices['TakeTruePotion'] == True:
        print('\nDUMBLEDORE: For making a self-less sacrifice that cost themselves dearly, I\n'
              f"award 50 points to {playerDict['fullName']}.", end='')
        input()
        AddHousePoints(50)
        print('\n~Applause~', end='')
        input()
    else:
        pass

    if Choices['TakeFullCredit'] == True:
        print('\nDUMBLEDORE: Long before any one of you were born, there was a great sorcerer\n'
              'who sat at the very same tables as you.', end='')
        input()
        print('DUMBLEDORE: His name was Merlin.', end='')
        input()
        print(f"DUMBLEDORE: I now award 25 points to {playerDict['House']} for the discovery of\n"
              'a treasure that none thought would every see the light of day.', end='')
        input()
        AddHousePoints(25)
        print('\n~Applause~', end='')
        input()
    elif Choices['GiveFullCredit'] == True:
        print('\nDUMBLEDORE: Long before any one of you were born, there was a great sorcerer\n'
              'who sat at the very same tables as you.', end='')
        input()
        print('DUMBLEDORE: His name was Merlin.', end='')
        input()
        print('DUMBLEDORE: I now award 50 points to both Gryffindor and Slytherin for the discovery\n'
              'of a treasure that none thought would every see the light of day.', end='')
        input()
        AddHousePoints(50)
        print('\n~Applause~', end='')
        input()
    elif Choices['SplitCredit'] == True:
        print('\nDUMBLEDORE: Long before any one of you were born, there was a great sorcerer\n'
              'who sat at the very same tables as you.', end='')
        input()
        print('DUMBLEDORE: His name was Merlin.', end='')
        input()
        print('DUMBLEDORE: I now award 25 points to both Gryffindor and Slytherin for the discovery\n'
              'of a treasure that none thought would every see the light of day.', end='')
        input()
        AddHousePoints(25)
        print('\n~Applause~', end='')
        input()
    else:
        pass

    keymax = max(zip(housePts.values(), housePts.keys()))[1]

    print('\nDUMBLEDORE: And so now without further ado...', end='')
    input()
    print('DUMBLEDORE: I would like to award the house cup to ' + keymax + '!', end='')
    input()

    if keymax == playerDict['House']:
        playerDict['WinHouseCup'] = True
        print(f"\n~All of your friends in {playerDict['House']} cheer with you!~", end='')
        input()
        print('\n~You\'ve never felt happier in your life!~', end='')
        input()
    else:
        print('\n~Even though you didn\'t win, you still cheer anyway.~', end='')
        input()
        print('\n~Of course, there\'s always next time...~', end='')
        input()

    #GRYFFINDOR ENDINGS
    if playerDict['House'] == 'Gryffindor':
        print('\n~As you make your way out of the Great Hall with Percival and Leo, you make\n'
              'eye contact with Milo. You approach him.~', end='')
        input()

        #BAD ENDING
        if Choices['TakeFullCredit'] == True:
            print('\nMILO: After all that we\'ve been through, did it really mean nothing\n'
                  'to you?', end='')
            input()
            if Choices['Compromise'] == True:
                print('MILO: After you offered to help...', end='')
                input()
            if Choices['HelpRival'] == True:
                print('MILO: After you saved my life...', end='')
                input()
            if playerDict['WinHouseCup'] == True:
                print('MILO: I hope you\'re happy that you won the House Cup, knowing that you\n'
                      'lied and cheated to get where you are.', end='')
                input()
            else:
                print('MILO: Not to mention you didn\'t even win the House Cup. What was it all\n'
                      'for then?', end='')
                input()
            print('MILO: They say that all wizards from Slytherin go bad eventually. I guess you\n'
                  'Gryffindors are no different.', end='')
            input()
            print('MILO: Don\'t bother keeping in touch.', end='')
            input()
            print('\n~You watch as he leaves you far behind. There are no words.~', end='')
            input()

        #BEST ENDING
        elif Choices['GiveFullCredit'] == True:
            print('\nMILO: I had no idea Dumbledore was going to award you as well. I didn\'t even\n'
                  'mention a word about you like you asked.', end='')
            input()
            print('MILO: Although from what I hear, that man has his ways.', end='')
            input()
            print('MILO: Oh, and by the way, I wanted to say thank you...', end='')
            input()
            if Choices['Compromise'] == True:
                print('MILO: For offering to help...', end='')
                input()
            if Choices['HelpRival'] == True:
                print('MILO: For saving my life...', end='')
                input()
            if playerDict['WinHouseCup'] == True:
                print('MILO: I may not have won the House Cup, but I think I\'ve already been awarded\n'
                      'enough.', end='')
                input()
            else:
                print('MILO: You may not have won the House Cup, but you\'ve won my respect.', end='')
                input()
            print('MILO: I look forward to whatever adventure we get ourselves tangled up in next year.', end='')
            input()
            print('\n~You follow Milo out of the school, Percival and Leo at your side.~', end='')
            input()

        #GOOD ENDING
        elif Choices['SplitCredit'] == True:
            print('\nMILO: I\'m glad we got to share this journey together.', end='')
            input()
            print('MILO: I wanted to say thank you...', end='')
            input()
            if Choices['Compromise'] == True:
                print('MILO: For offering to help...', end='')
                input()
            if Choices['HelpRival'] == True:
                print('MILO: For saving my life...', end='')
                input()
            if playerDict['WinHouseCup'] == True:
                print('MILO: I may not have won the House Cup, but I think I\'ve already been awarded\n'
                      'enough.', end='')
                input()
            else:
                print('MILO: You may not have won the House Cup, but you\'ve won my respect.', end='')
                input()
            print('MILO: I look forward to whatever adventure we get ourselves tangled up in next year.', end='')
            input()
            print('\n~You follow Milo out of the school, Percival and Leo at your side.~', end='')
            input()
        else:
            pass



    #HUFFLEPUFF ENDINGS
    if playerDict['House'] == 'Hufflepuff':
        pass
    


    #RAVENCLAW ENDINGS
    if playerDict['House'] == 'Ravenclaw':
        pass



    #SLYTHERIN ENDINGS
    if playerDict['House'] == 'Slytherin':
        print('\n~As you make your way out of the Great Hall with Milo, you make\n'
              'eye contact with Percival. You approach him.~', end='')
        input()

        #BAD ENDING
        if Choices['TakeFullCredit'] == True:
            print('\nPERCIVAL: After all that we\'ve been through, did it really mean nothing\n'
                  'to you?', end='')
            input()
            if Choices['Compromise'] == True:
                print('PERCIVAL: After you offered to help...', end='')
                input()
            if Choices['HelpRival'] == True:
                print('PERCIVAL: After you saved my life...', end='')
                input()
            if playerDict['WinHouseCup'] == True:
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
            print('\n~You watch as he leaves you far behind. There are no words.~', end='')
            input()

        #BEST ENDING
        elif Choices['GiveFullCredit'] == True:
            print('\nPERCIVAL: I had no idea Dumbledore was going to award you as well. I didn\'t even\n'
                  'mention a word about you like you asked.', end='')
            input()
            print('PERCIVAL: Although from what I hear, that man has his ways.', end='')
            input()
            print('PERCIVAL: Oh, and by the way, I wanted to say thank you...', end='')
            input()
            if Choices['Compromise'] == True:
                print('PERCIVAL: For offering to help...', end='')
                input()
            if Choices['HelpRival'] == True:
                print('PERCIVAL: For saving my life...', end='')
                input()
            if playerDict['WinHouseCup'] == True:
                print('PERCIVAL: I may not have won the House Cup, but I think I\'ve already been awarded\n'
                      'enough.', end='')
                input()
            else:
                print('PERCIVAL: You may not have won the House Cup, but you\'ve won my respect.', end='')
                input()
            print('PERCIVAL: I look forward to whatever adventure we get ourselves tangled up in next year.', end='')
            input()
            print('\n~You follow Percival out of the school, Milo and Leo at your side.~', end='')
            input()

        #GOOD ENDING
        elif Choices['SplitCredit'] == True:
            print('\nPERCIVAL: I\'m glad we got to share this journey together.', end='')
            input()
            print('PERCIVAL: I wanted to say thank you...', end='')
            input()
            if Choices['Compromise'] == True:
                print('PERCIVAL: For offering to help...', end='')
                input()
            if Choices['HelpRival'] == True:
                print('PERCIVAL: For saving my life...', end='')
                input()
            if playerDict['WinHouseCup'] == True:
                print('PERCIVAL: I may not have won the House Cup, but I think I\'ve already been awarded\n'
                      'enough.', end='')
                input()
            else:
                print('PERCIVAL: You may not have won the House Cup, but you\'ve won my respect.', end='')
                input()
            print('PERCIVAL: I look forward to whatever adventure we get ourselves tangled up in next year.', end='')
            input()
            print('\n~You follow Percival out of the school, Milo and Leo at your side.~', end='')
            input()
        else:
            pass
    


    #END OF GAME
    print('\n~Thank you for playing Hogwarts: Choices...~', end='')
    input()
    print('\n~But there still remains so much to be done!~', end='')
    input()
    print('\n~Replay the game as each of the other Hogwarts houses in order to view every story path.~', end='')
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



#RUN CHAPTER
#Chapter10()