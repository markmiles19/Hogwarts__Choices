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

    #IMPORTED CLASSES
    from Common import Lessons
    from Common import EndOfDay
    Day_2 = Lessons(False, False, False)

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
        print(f"\n{playerDict['Companion'].upper()}: See you later, {playerDict['firstName']}.", end='')
        input()
        if x == '1':
            Transfiguration()
            Day_2.Attend1 = True
        elif x == '2':
            Herbology()
            Day_2.Attend2 = True
        elif x == '3':
            MagicalCreatures()
            Day_2.Attend3 = True
        else:
            print(f"\n{playerDict['Companion'].upper()}: Come on, now. Pick one!\n")
            x = input()
            DecideClassOne(x)

    def DecideClassTwo():
        def SubDecideOne(x):
            if x == '1':
                Herbology()
                Day_2.Attend2 = True
            elif x == '2':
                MagicalCreatures()
                Day_2.Attend3 = True
            else:
                print('\n~You\'re not getting out of this one so easy...~\n')
                x = input()
                SubDecideOne(x)
        def SubDecideTwo(x):
            if x == '1':
                Transfiguration()
                Day_2.Attend1 = True
            elif x == '2':
                MagicalCreatures()
                Day_2.Attend3 = True
            else:
                print('\n~You\'re not getting out of this one so easy...~\n')
                x = input()
                SubDecideTwo(x)
        def SubDecideThree(x):
            if x == '1':
                Transfiguration()
                Day_2.Attend1 = True
            elif x == '2':
                Herbology()
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
        print('\n~Following the exciting events from last night, you struggle to adjust to start\n'
              'of a new day as you meet Percival in the common room.~', end='')
        input()
        print('\nPERCIVAL: I was just looking for you.', end='')
        input()
        print('PERCIVAL: You\'ll be happy to hear that I did a bit of research earlier and I now\n'
              'know exactly where the next step in our journey will take us.', end='')
        input()
        print('PERCIVAL: Mind you that it will be several miles of walking distance, and should anything\n'
              'go wrong or one of us gets hurt, it\'ll be points from Gryffindor.', end='')
        input()
        if Choices['Compromise'] == True:
            print('PERCIVAL: As much as I disagree with bringing Milo along, it looks like i have\n'
                  'no choice but to let him know when I get the chance.', end='')
            input()
        else:
            print('PERCIVAL: And hopefully Milo will learn to keep his fat nose out of our business.', end='')
            input()
        #END GRYFFINDOR PATH



    #BEGIN HUFFLEPUFF PATH
    if playerDict['House'] == 'Hufflepuff':
        print('WORK IN PROGRESS', end='')
        input()
        #END HUFFLEPUFF PATH



    #BEGIN HUFFLEPUFF PATH
    if playerDict['House'] == 'Ravenclaw':
        print('WORK IN PROGRESS', end='')
        input()
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
    if Day_2.Attend1 == True and Day_2.Attend2 == True:
        MagicalCreatures()
        Day_2.Attend3 = True
    elif Day_2.Attend2 == True and Day_2.Attend3 == True:
        Transfiguration()
        Day_2.Attend1 = True
    elif Day_2.Attend1 == True and Day_2.Attend3 == True:
        Herbology()
        Day_2.Attend2 = True



    if playerDict['House'] == 'Gryffindor':
        EndOfSecondDay = EndOfDay(0, 60, 65, 80)
    elif playerDict['House'] == 'Hufflepuff':
        EndOfSecondDay = EndOfDay(65, 0, 60, 80)
    elif playerDict['House'] == 'Ravenclaw':
        EndOfSecondDay = EndOfDay(65, 60, 0, 80)
    elif playerDict['House'] == 'Slytherin':
        EndOfSecondDay = EndOfDay(80, 60, 65, 0)

    EndOfSecondDay.DisplayPoints()



#RUN CHAPTER
#Chapter06()