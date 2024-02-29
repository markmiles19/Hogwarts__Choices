def Chapter06():
    #IMPORTED DICTIONARIES
    from Common import playerDict
    from Common import Choices

    #IMPORTED FUNCTIONS
    from Chapter06b import Transfiguration
    from Chapter06b import Herbology
    from Chapter06b import MagicalCreatures
    from Common import HousePointTotals
    from Common import EndDayTwo

    #IMPORTED ETC
    import colorama
    from colorama import Back, Fore, Style
    colorama.init(autoreset=True)

    #TESTING STATEMENTS
    #playerDict['House'] = 'Gryffindor'
    #playerDict['House'] = 'Hufflepuff'
    #playerDict['House'] = 'Ravenclaw'
    #playerDict['House'] = 'Slytherin'
    #playerDict['Companion'] = 'Percival'
    #playerDict['Companion'] = 'Leanna'
    #playerDict['Companion'] = 'Aliya'
    #playerDict['Companion'] = 'Milo'

    #BRANCH FUNCTIONS
    def DecideClassOne(x):
        print(f"{playerDict['Companion'].upper()}: See you later, {playerDict['firstName']}.", end='')
        input()
        if x == '1':
            Transfiguration()
        elif x == '2':
            Herbology()
        elif x == '3':
            MagicalCreatures()
        else:
            print(f"\n{playerDict['Companion'].upper()}: Come on, now. Pick one!\n")
            x = input()
            DecideClassOne(x)

    def DecideClassTwo():
        def SubDecideOne(x):
            if x == '1':
                Herbology()
            elif x == '2':
                MagicalCreatures()
            else:
                print('\n~You\'re not getting out of this one so easy...~\n')
                x = input()
                SubDecideOne(x)
        def SubDecideTwo(x):
            if x == '1':
                Transfiguration()
            elif x == '2':
                MagicalCreatures()
            else:
                print('\n~You\'re not getting out of this one so easy...~\n')
                x = input()
                SubDecideTwo(x)
        def SubDecideThree(x):
            if x == '1':
                Transfiguration()
            elif x == '2':
                Herbology()
            else:
                print('\n~You\'re not getting out of this one so easy...~\n')
                x = input()
                SubDecideThree(x)
        if playerDict['AttendTransfig'] == True:
            print(
            '\n[1] Herbology\n'
            '[2] Care for Magical Creatures\n'
            )
            x = input()
            SubDecideOne(x)
        elif playerDict['AttendHerb'] == True:
            print(
            '\n[1] Transfiguration\n'
            '[2] Care for Magical Creatures\n'
            )
            x = input()
            SubDecideTwo(x)
        elif playerDict['AttendCare'] == True:
            print(
            '\n[1] Transfiguration\n'
            '[2] Herbology\n'
            )
            x = input()
            SubDecideThree(x)
    #END BRANCH FUNCTIONS



    #BEGIN COMMON ROOM
    print('')
    print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
    print(Back.WHITE + Fore.BLACK + ' ~   CHAPTER 6: CHAIRS, CABBAGES, AND CRABS    ~ ')
    print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
    input()

    #BEGIN GRYFFINDOR PATH
    if playerDict['House'] == 'Gryffindor':
        print('~Following the exciting events from last night, you struggle to adjust to start\n'
              'of a new day as you meet Percival in the common room.~', end='')
        input()
        print('PERCIVAL: I just hope that by the end of the day I\'ll have pinpointed to location\n'
              'to the next clue.', end='')
        input()
        if Choices['Compromise'] == True:
            print('PERCIVAL: As much as I disagree with bringing Milo along, it looks like i have\n'
                  'no choice but to let him know when I get the chance.', end='')
        else:
            print('PERCIVAL: And hopefully Milo will learn to keep his fat nose out of our business.', end='')
        #END GRYFFINDOR PATH

    #BEGIN HUFFLEPUFF PATH
    if playerDict['House'] == 'Hufflepuff':
        pass
        #END HUFFLEPUFF PATH

    #BEGIN HUFFLEPUFF PATH
    if playerDict['House'] == 'Ravenclaw':
        pass
        #END RAVENCLAW PATH

    #BEGIN SLYTHERIN PATH
    if playerDict['House'] == 'Slytherin':
        print('~Following the exciting events from last night, you struggle to adjust to start\n'
              'of a new day as you meet Percival in the common room.~', end='')
        input()
        #END SLYTHERIN PATH


    #CONTINUE COMMON ROOM
    print(f"{playerDict['Companion'].upper()}: Anyway, which class do you think you're going to first?", end='')
    input()
    print(
    '\n[1] Transfiguration\n'
    '[2] Herbology\n'
    '[3] Care for Magical Creatures\n'
    )
    x = input()
    DecideClassOne(x)
    print('\n~Now with that out of the way, where would you like to go next?~', end='')
    input()
    DecideClassTwo()
    print('\n~You\'ve finished two of your classes for the day, leaving just one more...~', end='')
    input()
    if playerDict['AttendTransfig'] == True and playerDict['AttendHerb'] == True:
        MagicalCreatures()
    if playerDict['AttendHerb'] == True and playerDict['AttendCare'] == True:
        Transfiguration()
    if playerDict['AttendTransfig'] == True and playerDict['AttendCare'] == True:
        Herbology()
    EndDayTwo()
    HousePointTotals()



#RUN CHAPTER
#Chapter06()