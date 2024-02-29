def Chapter02():
    #IMPORTED LISTS
    from Common import blacklist

    #IMPORTED DICTIONARIES
    from Common import playerDict

    #TESTING STATEMENTS
    #playerDict['fullName'] = 'Mark Miles'
    #playerDict['fullName'] = 'Harry Potter'
    #playerDict['House'] = 'Gryffindor'
    #playerDict['House'] = 'Hufflepuff'
    #playerDict['House'] = 'Ravenclaw'
    #playerDict['House'] = 'Slytherin'

    #IMPORTED ETC
    import colorama
    from colorama import Back, Fore, Style
    colorama.init(autoreset=True)

    #BRANCH FUNCTIONS
    def branch1(x):
        if x == '1':
            if playerDict['fullName'].upper() in blacklist:
                print('\nPERCIVAL: ~Laughs~ You’re really quite the comedian, you are.', end='')
                input()
            else:
                print('\nPERCIVAL: Oh, I remember now! I heard your name called out during the Sorting Ceremony.\n'
                    'I probably should have mentioned before that I’m actually a second year.', end='')
                input()
        elif x == '2':
            print('\nPERCIVAL: Are you sure you’re in the right house? I guess it doesn’t matter anyway...', end='')
            input()
        elif x == '3':
            print('\nPERCIVAL: So you\'re the silent type, huh? Interesting.', end='')
            input()
        else:
            print('\nPERCIVAL: Sorry, could you repeat that?\n')
            x = input()
            branch1(x)

    def branch2(x):
        if x == '1':
            print('\nPERCIVAL: Meet me in the library tomorrow whenever you have the chance. I always go there whenever\n'
                'I have a free period, not just so I can read, but also to think.', end='')
            input()
            print('PERCIVAL: Then I’ll tell you everything about our quest.', end='')
            input()
        elif x == '2':
            print('\nPERCIVAL: If you meet me in the library tomorrow, I’ll tell you everything about our quest.', end='')
            input()
        else:
            print('\nPERCIVAL: What was that?\n')
            x = input()
            branch2(x)

    def branch3(x):
        if x == '1':
            if playerDict['fullName'].upper() in blacklist:
                print('\nLEANNA: Are you really sure about that?', end='')
                input()
            else:
                print(f"\nLEANNA: Pleased to meet you, {playerDict['firstName']}.", end='')
                input()
        elif x == '2':
            print('\nLEANNA: Sorry. I didn’t mean to upset you. I only wanted to talk to you very briefly.', end='')
            input()
        elif x == '3':
            print('\nLEANNA: Silent but deadly. You seem like exactly the type that I’m looking for.', end='')
            input()
        else:
            print('\nLEANNA: What was that?\n')
            x = input()
            branch3(x)

    def branch4(x):
        if x == '1':
            print('\nLEANNA: Excellent! We’ll be meeting very soon.', end='')
            input()
        elif x == '2':
            print('\nLEANNA: Well I’ll be there once you’ve made up your mind.', end='')
            input()
        elif x == '3':
            print('\nLEANNA: That’s alright, but if you have a change of heart I’ll still be there.', end='')
            input()
        else:
            print('\nWhat was that?\n')
            x = input()
            branch4(x)
        
    def branch5(x):
        if x == '1':
            if playerDict['fullName'].upper() in blacklist:
                print('\nALIYA: Hilarious. Anyway...', end='')
                input()
            else:
                print('\nALIYA: Happy to make your acquaintance.', end='')
                input()
        elif x == '2':
            print('\nALIYA: I do in fact see that.', end='')
            input()
        elif x == '3':
            print('\nALIYA: Don’t worry. I used to be shy as well when I first started here.', end='')
            input()
        else:
            print('\nALIYA: What was that?\n')
            x = input()
            branch5(x)

    def branch6(x):
        if x == '1':
            playerDict['WizardsChess'] = 'Yes'
            print('\nALIYA: Then you’re just who I’ve been looking for!', end='')
            input()
            print('ALIYA: You see, I’ve been tasked with recruiting first-years for the Hogwarts Wizard’s Chess Club,\n'
                    'and you seem to be just who we need.', end='')
            input()
            print('ALIYA: Of course, you’ll have to defeat one of our current members in order to join, but they tend\n'
                    'to be more lenient towards newcomers.', end='')
            input()
        elif x == '2':
            print('\nALIYA: It’s not terribly different from the version of Chess in the muggle world.', end='')
            input()
            print('ALIYA: The only real difference is that you tell the pieces where to move and they come to life and\n'
                    'move on their own.', end='')
            input()
            print('ALIYA: Believe me, I’ve only ever played muggle Chess once and I’ll never understand how they can stand\n'
                    'such a boring game.', end='')
            input()
            print('ALIYA: The reason I asked is because I’ve been tasked with recruiting first-years for the Hogwarts Wizard’s\n'
                    'Chess Club, such as yourself.', end='')
            input()
            print('ALIYA: Although if you intend to join, you’ll have to defeat one of our current members, but they tend to be\n'
                    'more lenient towards newcomers.', end='')
            input()
            print('ALIYA: So what do you say?', end='')
            input()
            print(
            '\n[1] You can count me in.\n'
            '[2] I’ll have to think about it.\n'
            '[3] No thanks.\n'
            )
            x = input()
            branch7(x)
        elif x == '3':
            playerDict['WizardsChess'] = 'No'
            print('\nALIYA: Oh, I see.', end='')
            input()
            print('ALIYA: The reason I asked is because I’ve been tasked with recruiting first-years for the Hogwarts Wizard’s\n'
                    'Chess Club, although that hardly seems like the kind of thing that would interest you.', end='')
            input()
            print('ALIYA: If you ever change your mind, however, I’ll be there.', end='')
            input()
        elif x == '4':
            print('\nALIYA: I’ve been tasked with recruiting first-years for the Hogwarts Wizard’s Chess Club, such as yourself.', end='')
            input()
            print('ALIYA: Although if you intend to join, you’ll have to defeat one of our current members, but they tend to be\n'
                    'more lenient towards newcomers.', end='')
            input()
            print('ALIYA: So what say you?', end='')
            input()
            print(
            '\n[1] You can count me in.\n'
            '[2] I’ll have to think about it.\n'
            '[3] No thanks.\n'
            )
            x = input()
            branch7(x)
        else:
            x = input()
            branch6(x)

    def branch7(x):
        if x == '1':
            playerDict['WizardsChess'] = 'Yes'
            print('\nALIYA: I hoped you would say that!', end='')
            input()
        elif x == '2':
            playerDict['WizardsChess'] = 'Maybe'
            print('\nALIYA: Take your time. Once you make up your mind, I’ll be there.', end='')
            input()
        elif x == '3':
            playerDict['WizardsChess'] = 'No'
            print('\nALIYA: I understand. That’s perfectly fine.', end='')
            input()
            print('ALIYA: If you ever change your mind, however, I’ll be there.', end='')
            input()
        else:
            print('\nALIYA: What was that?\n')
            x = input()
            branch7(x)

    def branch8(x):
            if x == '1':
                if playerDict['fullName'].upper() in blacklist:
                    print('\nMILO: Oh you think you’re being funny, do you? That’s fine, I didn’t want to know your real name anyway.', end='')
                    input()
                else:
                    print('\nMILO: Interesting.', end='')
                    input()
            elif x == '2':
                print('\nMILO: I would watch the attitude if I were you.', end='')
                input()
            elif x == '3':
                print('\nMILO: Okay, I guess that was too much to ask.', end='')
                input()
            else:
                print('\nMILO: What was that?\n')
                x = input()
                branch8(x)

    def branch9(x):
            if x == '1':
                print('\nMILO: It would be best to talk details tomorrow whenever you have the time. You can meet me down by the boathouse,\n'
                      'since it’s a nice place where I like to get away.', end='')
                input()
            elif x == '2':
                print('\nMILO: Alright then. You can meet me down by the boathouse tomorrow and we’ll talk about it then.', end='')
                input()
            else:
                print('\nMILO: What was that?\n')
                x = input()
                branch9(x)



    print('')
    print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
    print(Back.WHITE + Fore.BLACK + ' ~   CHAPTER 2: NEW FRIENDS, NEW BEGINNINGS    ~ ')
    print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
    input()
    print(f"\n~You settle into the {playerDict['House']} common room and you couldn’t feel more at home.~", end='')
    input()
    print('\n~A student approaches you as you return from unpacking.~', end='')
    input()



    #GRYFFINDOR PATH
    if playerDict['House'] == 'Gryffindor':
        print('\nPERCIVAL: I don’t believe we’ve officially met. I’m Percival, by the way...', end='')
        input()
        print(
        f"\n[1] I’m {playerDict['firstName']}. {playerDict['fullName']}.\n"
        '[2] Can’t you see that I’m busy right now.\n'
        '[3] ~Say nothing~\n'
        )
        x = input()
        branch1(x)
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
        x = input()
        branch2(x)
        print('PERCIVAL: Anyway, classes start in the morning. I just hope that you’re prepared.', end='')
        input()



    #HUFFLEPUFF PATH
    if playerDict['House'] == 'Hufflepuff':
        print('\nLEANNA: You must be one of the new first years. My name is Leanna.', end='')
        input()
        print(
        f"\n[1] I’m {playerDict['firstName']}. {playerDict['fullName']}.\n"
        '[2] Can’t you see that I’m busy right now.\n'
        '[3] ~Say nothing~\n'
        )
        x = input()
        branch3(x)
        print('\nLEANNA: I know this may seem a little sudden, but I’m going to let you in on something...', end='')
        input()
        print('LEANNA: I’m actually the Hufflepuff Quidditch captain, and although first-years are never\n'
            'allowed on the team, I’m always looking to train first years who may be interested in joining later.', end='')
        input()
        print('LEANNA: So what do you say?', end='')
        input()
        print(
        '\n[1] I’ve wanted to play Quidditch my whole life!\n'
        '[2] I’ll have to think about it.\n'
        '[3] Sorry, not a chance.\n'
        )
        x = input()
        branch4(x)
        print('LEANNA: In the meantime, you best prepare yourself for classes starting tomorrow.', end='')
        input()



    #RAVENCLAW PATH
    if playerDict['House'] == 'Ravenclaw':
        print('\nALIYA: I don’t believe we’ve met before, have we? My name is Aliya.', end='')
        input()
        print(
        f"\n[1] I’m {playerDict['firstName']}. {playerDict['fullName']}.\n"
        '[2] Can’t you see that I’m busy right now.\n'
        '[3] ~Say nothing~\n'
        )
        x = input()
        branch5(x)
        print('ALIYA: Do you like Wizard’s Chess? Or even just normal muggle Chess?', end='')
        input()
        print(
        '\n[1] Absolutely!\n'
        '[2] There’s Chess for wizards?\n'
        '[3] Not particularly, no.\n'
        '[4] Why do you ask?\n'
        )
        x = input()
        branch6(x)
        print('ALIYA: We best settle in for the night. Classes start early in the morning.', end='')
        input()



    #SLYTHERIN PATH
    if playerDict['House'] == 'Slytherin':
        print('\nMILO: So you\'re one of the new ones around here. Mind telling me your name?', end='')
        input()
        print(
        f"\n[1] I’m {playerDict['firstName']}. {playerDict['fullName']}.\n"
        '[2] Can’t you see that I’m busy right now.\n'
        '[3] ~Say nothing~\n'
        )
        x = input()
        branch8(x)
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
        x = input()
        branch9(x)
        print('MILO: I won’t keep you any longer. You’ll need your rest for classes tomorrow.', end='')
        input()

    print('...', end='')
    input()



    #DEBUG PATH
    if playerDict['House'] == 'Default':
        print('\nYou need to be assigned to a Hogwarts house in order to progress.', end='')



#RUN CHAPTER
#Chapter02()