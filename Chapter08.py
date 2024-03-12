def Chapter08():
    #IMPORTED DICTIONARIES
    from Common import playerDict

    #IMPORTED FUNCTIONS
    from Chapter08b import Defense
    from Chapter08b import Divination
    from Chapter08b import Astronomy
    from Common import HousePointTotals
    from Common import EndDayThree

    #IMPORTED ETC
    import colorama
    from colorama import Back, Fore, Style
    colorama.init(autoreset=True)

    #BRANCH FUNCTIONS
    def DecideClassOne(x):
        if x == '1':
            Defense()
        elif x == '2':
            Divination()
        elif x == '3':
            Astronomy()
        else:
            print(f"\n{playerDict['Companion'].upper()}: Come on, now. Pick one!\n")
            x = input()
            DecideClassOne(x)

    def DecideClassTwo():
        def SubDecideOne(x):
            if x == '1':
                Divination()
            elif x == '2':
                Astronomy()
            else:
                print('\n~You\'re not getting out of this one so easy...~\n')
                x = input()
                SubDecideOne(x)
        def SubDecideTwo(x):
            if x == '1':
                Defense()
            elif x == '2':
                Astronomy()
            else:
                print('\n~You\'re not getting out of this one so easy...~\n')
                x = input()
                SubDecideTwo(x)
        def SubDecideThree(x):
            if x == '1':
                Defense()
            elif x == '2':
                Divination()
            else:
                print('\n~You\'re not getting out of this one so easy...~\n')
                x = input()
                SubDecideThree(x)
        if playerDict['AttendDefense'] == True:
            print(
            '\n[1] Divination\n'
            '[2] Astronomy\n'
            )
            x = input()
            SubDecideOne(x)
        elif playerDict['AttendDiv'] == True:
            print(
            '\n[1] Defense Against the Dark Arts\n'
            '[2] Astronomy\n'
            )
            x = input()
            SubDecideTwo(x)
        elif playerDict['AttendAstro'] == True:
            print(
            '\n[1] Defense Against the Dark Arts\n'
            '[2] Divination\n'
            )
            x = input()
            SubDecideThree(x)
    #END BRANCH FUNCTIONS



    #BEGIN COMMON ROOM
    print('')
    print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
    print(Back.WHITE + Fore.BLACK + ' ~     CHAPTER 8: The Beyond     ~ ')
    print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
    input()



    #BEGIN GRYFFINDOR PATH
    if playerDict['House'] == 'Gryffindor':
        print('\n~You\'ve nearly recovered from your great battle yesterday, and now you must return\n'
              'your mind to your studies.~', end='')
        input()
        print('\nPERCIVAL: I don\'t know how I\'m supposed to pay attention in Ancient Runes today\n'
              'knowing that the treasure it so close now.', end='')
        input()
    #END GRYFFINDOR PATH



    #BEGIN HUFFLEPUFF PATH
    elif playerDict['House'] == 'Hufflepuff':
        pass
    #END GRYFFINDOR PATH



    #BEGIN RAVENCLAW PATH
    elif playerDict['House'] == 'Ravenclaw':
        pass
    #END GRYFFINDOR PATH



    #BEGIN SLYTHERIN PATH
    elif playerDict['House'] == 'Slytherin':
        pass
    #END GRYFFINDOR PATH



    #CONT COMMON ROOM
    print(f"{playerDict['Companion'].upper()}: Anyway, I think you know the drill by now.", end='')
    input()
    print(
    '\n[1] Defense Against the Dark Arts\n'
    '[2] Divination\n'
    '[3] Astronomy\n'
    )
    x = input()
    DecideClassOne(x)

    #FIRST CLASS ATTENDED

    print('\n~Now with that out of the way, where would you like to go next?~', end='')
    input()
    DecideClassTwo()

    #SECOND CLASS ATTENDED

    print('\n~You\'ve finished two of your classes for the day, leaving just one more...~', end='')
    input()
    if playerDict['AttendDefense'] == True and playerDict['AttendDiv'] == True:
        Astronomy()
    elif playerDict['AttendDiv'] == True and playerDict['AttendAstro'] == True:
        Defense()
    elif playerDict['AttendDefense'] == True and playerDict['AttendAstro'] == True:
        Divination()

    #THIRD CLASS ATTENDED

    EndDayThree()
    HousePointTotals()



#RUN CHAPTER
#Chapter08()