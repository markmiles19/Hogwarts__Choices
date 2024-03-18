def Chapter03():
    #IMPORTED DICTIONARIES
    from Common import playerDict

    #IMPORTED FUNCTIONS
    from Chapter03b import Charms
    from Chapter03b import Potions
    from Chapter03b import Flying

    #IMPORTED CLASSES
    from Common import Lessons
    Day_1 = Lessons(False, False, False)

    #TESTING STATEMENTS
    #playerDict['House'] = 'Gryffindor'
    #playerDict['House'] = 'Hufflepuff'
    #playerDict['House'] = 'Ravenclaw'
    #playerDict['House'] = 'Slytherin'
    #playerDict['Companion'] = 'Percival'
    #playerDict['Companion'] = 'Leanna'
    #playerDict['Companion'] = 'Aliya'
    #playerDict['Companion'] = 'Milo'

    #IMPORTED ETC
    import colorama
    from colorama import Back, Fore, Style
    colorama.init(autoreset=True)

    #BRANCH FUNCTIONS
    def branch1(x):
        if x == '1':
            print(f"\n{playerDict['Companion'].upper()}: Optimism. I can appreciate that.", end='')
            input()
        elif x == '2':
            print(f"\n{playerDict['Companion'].upper()}: Everyone’s like that on their first day. It’s nothing to worry about.", end='')
            input()
        elif x == '3':
            print(f"\n{playerDict['Companion'].upper()}: Can’t say that I blame you.", end='')
            input()
        else:
            print(f"{playerDict['Companion'].upper()}: Come on. Be honest with me, now.\n")
            x = input()
            branch1(x)

    def branch2(x):
        if x == '1':
            if playerDict['House'] == 'Ravenclaw':
                print('\nALIYA: Excellent choice! Professor Flitwick is the head of Ravenclaw and you’ll learn so many\n'
                    'useful spells from him.', end='')
                input()
            else:
                print(f"\n{playerDict['Companion'].upper()}: Interesting choice. You won’t see me in your classes since I’m not a first-year, but I hope it\n"
                'goes well for you.', end='')
                input()
            print('...', end='')
            input()
            Charms()
            Day_1.Attend1 = True
                
        elif x == '2':
            if playerDict['House'] == 'Gryffindor':
                print('\nPERCIVAL: Really? Potions with Snape? Everyone in Gryffindor hates him.', end='')
                input()
                print('PERCIVAL: Well, I suppose it is your choice. Just don’t say that I didn’t give you a fair warning.', end='')
                input()
            elif playerDict['House'] == 'Slytherin':
                print('\nMILO: Despite what some may say, potions is one of my favorite subjects.',end='')
                input()
                print('MILO: Professor Snape on the other hand is a complete slimeball.',end='')
                input()
                print('MILO: What’s worse is that he’s the head of Slytherin house, but I wouldn’t let that get in the way of\n'
                    'learning if I were you.', end='')
                input()
            else:
                print(f"\n{playerDict['Companion'].upper()}: Interesting choice. You won’t see me in your classes since I’m not a first-year, but I hope it\n"
                'goes well for you.', end='')
                input()
            print('...', end='')
            input()
            Potions()
            Day_1.Attend2 = True
            

        elif x == '3':
            if playerDict['House'] == 'Hufflepuff':
                print('LEANNA: The class that started it all for me so very long ago. My only hope is that it takes on with\n'
                    'you the same way it did for me.', end='')
                input()
            else:
                print(f"\n{playerDict['Companion'].upper()}: Interesting choice. You won’t see me in your classes since I’m not a first-year, but I hope it\n"
                'goes well for you.', end='')
                input()
            print('...', end='')
            input()
            Flying()
            Day_1.Attend3 = True
        else:
            print(f"\n{playerDict['Companion'].upper()}: Come on, now. You\'ve got to pick one.", end='')
            x = input()
            branch2(x)

    def branch3(x):
        if x == '1':
            Potions()
            Day_1.Attend2 = True
        elif x == '2':
            Flying()
            Day_1.Attend3 = True
        else:
            print('\n~You\'re not getting out of this one so easy...~\n')
            x = input()
            branch3(x)

    def branch4(x):
        if x == '1':
            Charms()
            Day_1.Attend1 = True
        elif x == '2':
            Flying()
            Day_1.Attend3 = True
        else:
            print('\n~You\'re not getting out of this one so easy...~\n')
            x = input()
            branch4(x)

    def branch5(x):
        if x == '1':
            Charms()
            Day_1.Attend1 = True
        elif x == '2':
            Potions()
            Day_1.Attend2 = True
        else:
            print('\n~You\'re not getting out of this one so easy...~\n')
            x = input()
            branch5(x)

    def branch6():
        if Day_1.Attend1 == True:
            print(
            '\n[1] Potions\n'
            '[2] Flying\n'
            )
            x = input()
            branch3(x)
        elif Day_1.Attend2 == True:
            print(
            '\n[1] Charms\n'
            '[2] Flying\n'
            )
            x = input()
            branch4(x)
        elif Day_1.Attend3 == True:
            print(
            '\n[1] Charms\n'
            '[2] Potions\n'
            )
            x = input()
            branch5(x)



    #BEGIN COMMON ROOM
    print('')
    print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
    print(Back.WHITE + Fore.BLACK + ' ~    CHAPTER 3: READY TO BEGIN    ~ ')
    print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
    input()
    print('\n~You wake up early to watch the sunrise from your dormitory window, ready to start your classes.~', end='')
    input()
    print(f"\n~{playerDict['Companion']} stops to talk to you in the common room.~", end='')
    input()
    print(f"\n{playerDict['Companion'].upper()}: Feeling alright there, {playerDict['firstName']}?", end='')
    input()
    print(
    '\n[1] Feeling ready to learn is more like it.\n'
    '[2] I just hope I’m ready for this.\n'
    '[3] ~Shrug~\n'
    )
    x = input()
    branch1(x)
    print(f"{playerDict['Companion'].upper()}: If you take a look at the notice board you’ll see the schedule for first-years.", end='')
    input()
    print(f"{playerDict['Companion'].upper()}: Remember, this year you can choose the order in which you attend classes.", end='')
    input()
    print(f"{playerDict['Companion'].upper()}: It looks like today will be Charms, Potions, and Flying for you.", end='')
    input()
    print(f"{playerDict['Companion'].upper()}: So which class will you start the day with?", end='')
    input()
    print(
    '\n[1] Charms\n'
    '[2] Potions\n'
    '[3] Flying\n'
    )
    x = input()
    branch2(x)
    print('\n~Now with that out of the way, where would you like to go next?~', end='')
    input()
    branch6()
    print('\n~You\'ve finished two of your classes for the day, leaving just one more...~', end='')
    input()
    if Day_1.Attend1 == True and Day_1.Attend2 == True:
        Flying()
        Day_1.Attend3 = True
    elif Day_1.Attend2 == True and Day_1.Attend3 == True:
        Charms()
        Day_1.Attend1 = True
    elif Day_1.Attend1 == True and Day_1.Attend3 == True:
        Potions()
        Day_1.Attend2 = True



#RUN CHAPTER
#Chapter03()