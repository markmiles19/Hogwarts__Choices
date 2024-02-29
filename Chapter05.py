def Chapter05():   
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
    def branch1(x):
        if x == '1':
            print('\nPERCIVAL: Sorry about that. Like I said, Ancient Runes was a big mistake.', end='')
        elif x == '2':
            print('\nPERCIVAL: Thanks for waiting up for me.', end='')
        else:
            print('PERCIVAL: Did you say something?\n')
            x = input()
            branch1(x)

    def branch2(x):
        if x == '1':
            print('\nPERCIVAL: Well what are you waiting for? Cast Reducto on the glass.', end='')
            input()
        elif x == '2':
            print('\nPERCIVAL: Flitwick taught you both Reducto AND Reparo, right?', end='')
            input()
            print('PERCIVAL: As long as we repair the glass after we\'re done, no one will ever know.', end='')
            input()
            print('PERCIVAL: Now go on...', end='')
            input()
        else:
            print('PERCIVAL: Are you going to cast Reducto or not?\n')
            x = input()
            branch2(x)

    def branch3(x):
        if x == '1':
            print(f"\nPERCIVAL: Not the time, {playerDict['firstName']}!", end='')
        elif x == '2':
            pass
        else:
            pass

    def Reducto(x):
        if x == 'd' or x == 'D':
            print('\n~Reducto!~', end='')
            input()
        else:
            print('\nPERCIVAL: Just cast the flippin\' spell already!\n')
            x = input()
            Reducto(x)

    def FiltchIsComing():
        print(f"\n{playerDict['Companion']}: Filtch is coming! Hide!", end='')
        input()
        print('\n~Press H to hide behind a trophy case.~\n')
        x = input()
        if x == 'h' or x == 'H':
            print('\n~The door slowly creeps open and you see the figure of Mr. Filtch holding his cat, Mrs. Norris.~', end='')
            input()
            print('\nFILTCH: Who\'s in here?', end='')
            input()
            print('\n~After what seems like an eternity, he leaves the room.~', end='')
            input()
            print('\n~Now back to what you were doing.~', end='')
            input()
            Section1()
        else:
            print('\n~You accidentally knock over something, alerting Filtch to your presence.~', end='')
            input()
            AddHousePoints(-15)
            print('\nFILTCH: Looks like it\'s down to the dungeons with you!', end='')
            input()
            print('\n~After another day of classes and a grueling evening serving detention, you start over again...~', end='')
            input()
            Chapter05()

    def Section3():
        print(
            '\n[<] ~PREV~\n'
            '[1] Zacharias Mumps, 1368\n'
            '[2] TBD\n'
            '[3] Jonathan Able, 1034\n'
            '[4] TBD\n')
        x = input()
        if x == '<':
            Section2()
        elif x == '3':
            pass
        else:
            FiltchIsComing()

    def Section2():
        print(
            '\n[<] ~PREV~\n'
            '[1] Bowman Wright, 1506\n'
            '[2] R. J. H. King, 1968\n'
            '[3] TBD\n'
            '[4] TBD\n'
            '[>] ~NEXT~\n')
        x = input()
        if x == '<':
            Section1()
        elif x == '>':
            Section3()
        else:
            FiltchIsComing()

    def Section1():
        print(
            '\n[1] M. G. McGonagall, 1971\n'
            '[2] Elfrida Clagg, 1345\n'
            '[3] James Potter, 1973\n'
            '[4] Kennilworthy Whisp, 1954\n'
            '[>] ~NEXT~\n')
        x = input()
        if x == '>':
            Section2()
        else:
            FiltchIsComing()

    def Standstill(x):
        if x == '1':
            print('\nPERCIVAL: No!')
            print('MILO: No!\n')
            x = input()
            Standstill(x)
        elif x == '2':
            Choices['Compromise'] = True
            print('\n~You tell Milo that he can join the rest of you to the next location.~', end='')
            input()
            print('\nMILO: Alright. I\'ll help the three of you for the time being, but once we find the\n'
                  'treasure, it\'s mine!', end='')
            input()
            print('\nPERCIVAL: I guess that\'s settled then.', end='')
            input()
            print('\nMILO: Okay.', end='')
            input()
            print('\nPERCIVAL: Okay.', end='')
            input()
            print('\n~You dodge patrolling prefects as you return to the Gryffindor Common room with\n'
                  'Percival and Leo, and you all turn in after an exhausting night.~', end='')
            input()
        elif x == '3':
            print('\n~You cast the stunning spell, Stupefy, and dash out of the room with the trophy,\n'
                  'your friends trailing behind you.~')
            input()
        elif x == '4':
            print('\nMILO: If that\'s what you want, then so be it.', end='')
            input()
            print('MILO: Stupefy!', end='')
            input()
            print('\n~Press D to dodge.~', end='')
            x = input()
            if x == 'd' or x == 'D':
                pass
            else:
                pass
        else:
            print('\n~This could turn ugly real fast. Now it\'s time to intervene.~\n')
            x = input()
            Standstill(x)

    def Standstill_S(x):
        if x == '1':
            print('\MILO: No!')
            print('PERCIVAL: No!\n')
            x = input()
            Standstill_S(x)
        elif x == '2':
            print('\n~You tell Percival that he can join the two of you to the next location.~', end='')
            input()
            print('\nPERCIVAL: Alright. I\'ll help the two of you for the time being, but don\'t think for\n'
                  'a second that I\'ll hand over the treasure to some slimy Slytherin.', end='')
            input()
            print('\MILO: I guess that\'s settled then.', end='')
            input()
            print('\nPERCIVAL: Okay.', end='')
            input()
            print('\nMILO: Okay.', end='')
            input()
        elif x == '3':
            print('~You cast the stunning spell, Stupefy, and dash out of the room with the trophy,\n'
                  'your friends trailing behind you.~')
            input()
        elif x == '4':
            pass
        else:
            print('\n~This could turn ugly real fast. Now it\'s time to intervene.~\n')
            x = input()
            Standstill_S(x)
    #END BRANCH FUNCTIONS



    #GRYFFINDOR PATH
    if playerDict['House'] == 'Gryffindor':
        print('')
        print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
        print(Back.WHITE + Fore.BLACK + ' ~   CHAPTER 5: THE LOST SEEKER    ~ ')
        print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
        input()
        print('\n~Tonight is the night! You wait patiently in the third floor corridor for Percival to arrive.~', end='')
        input()
        print('\n~Finally he approaches you with his younger brother, Leo.~', end='')
        input()
        print(
            '\n[1] What took you so long?\n'
            '[2] I\'m ready when you are.\n'
        )
        x = input()
        branch1(x)
        input()
        print('PERCIVAL: The good news is that the trophy room is open to students at all times.', end='')
        input()
        print('LEO: The only downside is that the caretaker Mr. Filtch stops by every so often to make sure\n'
            'there aren\'t any students getting up to no good.', end='')
        input()
        print('PERCIVAL: And as you could imagine that will be a problem for us.', end='')
        input()
        print('PERCIVAL: Just remember before we go in, Merlin attended Hogwarts around the turn of the 11th century,\n'
            'so we need to find a trophy that was issued to a student around the same time.', end='')
        input()
        print('\n~Without another moment\'s hesitation, Percival slowly opens the door...~', end='')
        input()
        print('\n~You step foot into a vast assortment of shining silver and gold, making an otherwise small and crowded\n'
            'room feel much bigger in reality.~', end='')
        input()
        print('\nPERCIVAL: I\'ll look over here in the Wizard\'s Chess section.', end='')
        input()
        print('\nLEO: I\'ll check out the Dueling Club section.', end='')
        input()
        print(f"LEO: I guess that leaves you with the Quidditch trophies, {playerDict['firstName']}.", end='')
        input()
        print('\nPERCIVAL: We\'ll meet back up here once we\'re done.', end='')
        input()
        print('\n~You inch towards a trophy case in the far back, and scan its contents.~', end='')
        input()
        Section1()
        print('\n~You found it!~', end='')
        input()
        print('\n~You let Percival and Leo know and they dart over to the trophy.~', end='')
        input()
        print('\nPERCIVAL: That\'s great! All we need to do now is break through the glass case.', end='')
        input()
        print(
            '\n[1] That shouldn\'t be too hard.\n'
            '[2] Wouldn\'t that be vandalism?\n'
        )
        x = input()
        branch2(x)
        print('\n~Press D to cast Reducto.~\n')
        x = input()
        Reducto(x)
        print('\n~The class case shatters into a million pieces. Thank Merlin none of them landed on\n'
              'the three of you.~', end='')
        input()
        print('\nPERCIVAL: Let\'s see what all the fuss is about with you, Jonathan Able.', end='')
        input()
        print('\n~Percival examines the Golden Snitch recreated in fine detail, perched atop the trophy.~', end='')
        input()
        print('\nPERCIVAL: There seems to be some sort of markings on the Snitch\'s wings. If I\'m not mistaken...', end='')
        input()
        print('PERCIVAL: Of course! They\'re coordinates.', end='')
        input()
        print('PERCIVAL: And they seem to lead off somewhere into the Highlands.', end='')
        input()
        print('PERCIVAL: We\'re going to need to hold onto this for the moment so that I can study the coordinates\n'
              'and pinpoint the location.', end='')
        input()
        print('\n???: I\'m afraid I can\'t let you do that.', end='')
        input()
        print('\n~Out from behind a trophy case, a Slytherin boy reveals himself.~', end='')
        input()
        print('\nPERCIVAL: Get lost, Milo! This has nothing to do with you.', end='')
        input()
        print('\nMILO: This has EVERYTHING to do with me.', end='')
        print(
            '\n[1] Who\'s this guy?\n'
            '[2] ~Stay silent~\n'
        )
        x = input()
        branch3(x)
        print('PERCIVAL: We found the trophy first. You can leave now.', end='')
        input()
        print('\nMILO: I\'m not leaving without that trophy!', end='')
        input()
        print('\nPERCIVAL: What does it matter to you, anyway?', end='')
        input()
        print('\nMILO: The treasure belongs to Slytherin. It always has and it always will.', end='')
        input()
        print('\n~Percival and Milo are at a standstill. What are you going to do about it?~', end='')
        input()
        print(
            '\n[1] I\'m sure if we just talk about it we can come to a mutual understanding.\n'
            '[2] ~Compromise~\n'
            '[3] ~Stun and run~\n'
            '[4] ~Wizard\'s duel~\n'
        )
        x = input()
        Standstill(x)



    #HUFFLEPUFF PATH
    if playerDict['House'] == 'Hufflepuff':
        pass


    #RAVENCLAW PATH
    if playerDict['House'] == 'Ravenclaw':
        pass


    #SLYTHERIN PATH
    if playerDict['House'] == 'Slytherin':
        print('')
        print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
        print(Back.WHITE + Fore.BLACK + ' ~   CHAPTER 5: THE LOST SEEKER    ~ ')
        print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
        input()
        print('\n~You accompany Milo to the third floor corridor late into the night once everyone is in bed~', end='')
        input()
        print('\nMILO: Now remember, Merlin attended Hogwarts around the 11th century, so the trophy we\'re looking for\n'
              'was issued around the same time.', end='')
        input()
        print('\n~As the two of you prepare to turn a corner, you catch a glimpse of Mr. Filtch blocking the entrance\n'
              'to the trophy room.~', end='')
        input()
        print('\n[1] What do we do now?\n'
              '[2] ~Scan the room~\n')
        def EncounterFiltch(x):
            if x == 1:
                pass
            elif x == 2:
                pass
            else:
                pass
        x = input()
        EncounterFiltch(x)
        print('\n~Without another moment\'s hesitation, Milo slowly opens the door...~', end='')
        input()
        print('\n~You step foot into a vast assortment of shining silver and gold, making an otherwise small and crowded\n'
            'room feel much bigger in reality.~', end='')
        input()
        print('\nMILO: I\'ll keep watch at the door while you search the Quidditch trophies.', end='')
        input()
        print('\n~You inch towards a trophy case in the far back, and scan its contents.~', end='')
        input()
        Section1()
        print('\n~You found it!~', end='')
        input()
        print('\n~You let Milo know and he darts over to the trophy.~', end='')
        input()
        print('\MILO: That\'s great! All we need to do now is break through the glass case.', end='')
        input()
        print('~Suddenly you and Milo hear talking outside the room.~', end='')
        input()
        print('MILO: Quick! Find something to hide behind!', end='')
        input()
        print('\n~Press H to hide behind a trophy case.~\n')
        def PercivalIsComing(x):
            if x == 'h' or x == 'H':
                print('\n~You hide behind the nearest trophy case as you watch two Gryffindors enter the room...~', end='')
                input()
                print('\n???: I\'ll look over here in the Wizard\'s Chess section.', end='')
                input()
                print('\n???: I\'ll check out the Dueling Club section.', end='')
                input()
                print('~You stay hidden for what seems like ages, and then finally you hear the younger of the two speak...~', end='')
                input()
                print('???: I\'ve found it', end='')
                input()
                print('\n???: Let\'s see what all the fuss is about with you, Jonathan Able.', end='')
                input()
                print('???: There seems to be some sort of markings on the Snitch\'s wings. If I\'m not mistaken...', end='')
                input()
                print('???: Of course! They\'re coordinates.', end='')
                input()
                print('???: And they seem to lead off somewhere into the Highlands.', end='')
                input()
                print('???: We\'re going to need to hold onto this for the moment so that I can study the coordinates\n'
                    'and pinpoint the location.', end='')
                input()
                print('\nMILO: I\'m afraid I can\'t let you do that.', end='')
                input()
            else:
                print('\n~You failed to hide in time! The Gryffindors have spotted you.~', end='')
                input()
        x = input()
        PercivalIsComing(x)
        print('\n~Milo reveals himself.~', end='')
        input()
        print('\nMILO: It\'s too late Percival. We\'ve found the next clue.', end='')
        input()
        print('\nPERCIVAL: Get lost, Milo! This has nothing to do with you.', end='')
        input()
        print('MILO: This has everything to do with us!', end='')
        input()
        print('\nPERCIVAL: What does it matter to you, anyway?', end='')
        input()
        print('\nMILO: The treasure belongs to Slytherin. It always has and it always will.', end='')
        input()
        print('\n~Milo and Percival are at a standstill. What are you going to do about it?~', end='')
        input()
        print(
            '\n[1] I\'m sure if we just talk about it we can come to a mutual understanding.\n'
            '[2] ~Compromise~\n'
            '[3] ~Stun and run~\n'
            '[4] ~Wizard\'s duel~\n'
        )
        x = input()
        Standstill_S(x)
        print('\n~You dodge patrolling prefects as you return to the Slytherin Common room with\n'
                  'Milo, and you turn in after an exhausting night.~', end='')
        input()
        #END SLYTHERIN PATH



#RUN CHAPTER
#Chapter05()