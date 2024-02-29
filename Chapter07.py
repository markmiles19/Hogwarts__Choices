def Chapter07():
    #IMPORTED DICTIONARIES
    from Common import playerDict
    from Common import Choices
    
    #IMPORTED ETC
    import colorama
    from colorama import Back, Fore, Style
    colorama.init(autoreset=True)



    #BEGIN GRYFFINDOR PATH
    if playerDict['House'] == 'Gryffindor':
        print('')
        print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
        print(Back.WHITE + Fore.BLACK + ' ~   CHAPTER 7: OUT OF BOUNDS    ~ ')
        print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
        input()
        if Choices['Compromise'] == True:
            print('\n~You set out from the castle with Percival, Leo, and Milo at nightfall, navigating\n'
                  'hills, ponds, and swamps for what feels like hours.~', end='')
            input()
            print('\n~Finally, you come to a decent-sided cave.~', end='')
            input()
            print('\nPERCIVAL: We need to be prepared for whatever we find in there, so have your wands\n'
                  'at the ready.', end='')
            input()
            print('\nMILO: There\'s nothing scary at all about this.', end='')
            input()
        else:
            print('\n~You set out from the castle with Percival and Leo at nightfall, navigating hills,\n'
                  'ponds, and swamps for what feels like hours.~', end='')
            input()
            print('\n~Finally, you come to a decent-sided cave.~', end='')
            input()
            print('\nPERCIVAL: We need to be prepared for whatever we find in there, so have your wands\n'
                  'at the ready.', end='')
            input()
            print('\nLEO: I\'m not sure I like this.', end='')
            input()
            print('\n~Before you manage to set foot in the cave, you hear a rustling sound behind you.~', end='')
            input()
            print('\nPERCIVAL: What was that?', end='')
            input()
            print('\n~Everything around you is dead quiet until...~', end='')
            input()
            print('PERCIVAL: Revelio!', end='')
            input()
            print('~From out of the foliage stumbles a newly materialized Milo.~', end='')
            input()
            print('\nPERCIVAL: I know a disillusionment charm when I see one, now leave us.', end='')
            input()
            print('\nMILO: Like I said, the treasure belongs with Slytherin.', end='')
            input()
    #END GRYFFINDOR PATH



    #BEGIN HUFFLEPUFF PATH
    elif playerDict['House'] == 'Hufflepuff':
        print('')
        print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
        print(Back.WHITE + Fore.BLACK + ' ~   CHAPTER 7: TBD    ~ ')
        print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
        input()
    #END HUFFLEPUFF PATH



    #BEGIN RAVENCLAW PATH
    elif playerDict['House'] == 'Ravenclaw':
        print('')
        print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
        print(Back.WHITE + Fore.BLACK + ' ~   CHAPTER 7: TBD    ~ ')
        print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
        input()
    #END RAVENCLAW PATH



    #BEGIN SLYTHERIN PATH
    elif playerDict['House'] == 'Slytherin':
        print('')
        print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
        print(Back.WHITE + Fore.BLACK + ' ~   CHAPTER 7: OUT OF BOUNDS    ~ ')
        print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
        input()
    #END SLYTHERIN PATH



#RUN CHAPTER
#Chapter07()