import time
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)

#LISTS
blacklist = ['HARRY POTTER', 'RON WEASLEY', 'HERMIONE GRANGER', 'NEVILLE LONGBOTTOM', 'ALBUS DUMBLEDORE',
             'SEVERUS SNAPE', 'SIRIUS BLACK', 'DRACO MALFOY', 'TOM RIDDLE', 'GILDEROY LOCKHART',
             'DOLORES UMBRIDGE', 'BATHILDA BAGSHOT', 'BELLATRIX LESTRANGE', 'SUSAN BONES', 'LAVENDER BROWN',
             'CHO CHANG', 'COLIN CREEVY', 'VERNON DURSLEY', 'LUNA LOVEGOOD', 'RUBEUS HAGRID']


#DICTIONARIES
playerDict = {'firstName':'Default',
              'lastName':'Default',
              'fullName':'Default',
              'Fear':'Default',
              'House':'Default',
              'HouseColor':'Default',
              'Companion':'Default',
              'Quidditch':'Default',
              'WizardsChess':'Default',
              'AttendCharms': False,
              'AttendPotions': False,
              'AttendFlying': False,
              'Reducto':'Default',
              'Reparo':'Default',
              'AttendTransfig': False,
              'AttendHerb': False,
              'AttendCare': False,
              'AttendDefense': False,
              'AttendDiv': False,
              'AttendAstro': False,
              'WinHouseCup': False}

Choices = {'Compromise': False,
           'HelpCompanion': False,
           'HelpRival': False,
           'TakeFakePotion': False,
           'TakeRealPotion': False,
           'SacrificeSelf': False,
           'TakeFullCredit': False,
           'GiveFullCredit': False,
           'SplitCredit': False}

sortingDict = {'Red':0,
               'Yellow':0,
               'Blue':0,
               'Green':0}

housePts = {'Gryffindor':0,
            'Hufflepuff':0,
            'Ravenclaw':0,
            'Slytherin':0}

Potions = {'User': 'None',
           'Percival': 'None',
           'Leo': 'None',
           'Milo': 'None'}

Dueling = {'User': False,
           'Percival': False,
           'Leo': False,
           'Milo': False}


#FUNCTIONS
def storeName(name):
    tokens = name.split()
    if len(tokens) == 2:
        if tokens[0].isalpha and tokens[1].isalpha():
            playerDict['firstName'] = tokens[0]
            playerDict['firstName'] = playerDict['firstName'][0].upper() + playerDict['firstName'][1:].lower()
            playerDict['lastName'] = tokens[1]
            playerDict['lastName'] = playerDict['lastName'][0].upper() + playerDict['lastName'][1:].lower()
            playerDict['fullName'] = playerDict['firstName'] + ' ' + playerDict['lastName']
        else:
            print('\n~Preferably first and last name AND NO SYMBOLS.~\n')
            playerName = input()
            storeName(playerName)
    elif len(tokens) < 2:
        print('\n~Preferably first AND last name.~\n')
        playerName = input()
        storeName(playerName)
    elif len(tokens) > 2:
        print('\n~Preferably first and last name ONLY.~\n')
        playerName = input()
        storeName(playerName)

def sortingHat1(user_input):
    if user_input == '1':
        sortingDict['Green'] += 1
    elif user_input == '2':
        sortingDict['Yellow'] += 1
    elif user_input == '3':
        sortingDict['Red'] += 1
    elif user_input == '4':
        sortingDict['Blue'] += 1
    else:
        print('\nSORTING HAT: I beg your pardon?', end='')
        user_num = input()
        sortingHat1(user_num)

def sortingHat2(user_input):
    if user_input == '1':
        sortingDict['Red'] += 1
    elif user_input == '2':
        sortingDict['Blue'] += 1
    elif user_input == '3':
        sortingDict['Yellow'] += 1
    elif user_input == '4':
        sortingDict['Green'] += 1
    else:
        print('\nSORTING HAT: I beg your pardon?', end='')
        user_num = input()
        sortingHat2(user_num)

def sortingHat3(user_input):
    if user_input == '1':
        sortingDict['Blue'] += 1
    elif user_input == '2':
        sortingDict['Yellow'] += 1
    elif user_input == '3':
        sortingDict['Green'] += 1
    elif user_input == '4':
        sortingDict['Red'] += 1
    else:
        print('\nSORTING HAT: I beg your pardon?', end='')
        user_num = input()
        sortingHat3(user_num)

def sortingHat4(user_input):
    if user_input == '1':
        sortingDict['Green'] += 1
    elif user_input == '2':
        sortingDict['Red'] += 1
    elif user_input == '3':
        sortingDict['Blue'] += 1
    elif user_input == '4':
        sortingDict['Yellow'] += 1
    else:
        print('\nSORTING HAT: I beg your pardon?', end='')
        user_num = input()
        sortingHat4(user_num)

def sortingHat5(user_input):
    if user_input == '1':
        sortingDict['Yellow'] += 1
        playerDict['Fear'] = 'being rejected by others'
    elif user_input == '2':
        sortingDict['Green'] += 1
        playerDict['Fear'] = 'feeling powerless'
    elif user_input == '3':
        sortingDict['Red'] += 1
        playerDict['Fear'] = 'being alone'
    elif user_input == '4':
        sortingDict['Blue'] += 1
        playerDict['Fear'] = 'failing those around you'
    else:
        print('\nSORTING HAT: I beg your pardon?', end='')
        user_num = input()
        sortingHat5(user_num)

def finalizeSort():
    keymax = max(zip(sortingDict.values(), sortingDict.keys()))[1]
    if keymax == 'Red':
        playerDict['House'] = 'Gryffindor'
        playerDict['Companion'] = 'Percival'
        playerDict['HouseColor'] = 'RED'
    elif keymax == 'Yellow':
        playerDict['House'] = 'Hufflepuff'
        playerDict['Companion'] = 'Leanna'
        playerDict['HouseColor'] = 'YELLOW'
    elif keymax == 'Blue':
        playerDict['House'] = 'Ravenclaw'
        playerDict['Companion'] = 'Aliya'
        playerDict['HouseColor'] = 'BLUE'
    elif keymax == 'Green':
        playerDict['House'] = 'Slytherin'
        playerDict['Companion'] = 'Milo'
        playerDict['HouseColor'] = 'GREEN'

def AddHousePoints(x):
    housePts[playerDict['House']] += int(x)
    if playerDict['House'] == 'Gryffindor':
        print(Fore.RED + '\n+' + str(x) + '*', end='')
        time.sleep(0.5)
        print()
    elif playerDict['House'] == 'Hufflepuff':
        print(Fore.YELLOW + '\+' + str(x) + '*', end='')
        time.sleep(0.5)
        print()
    elif playerDict['House'] == 'Ravenclaw':
        print(Fore.BLUE + '\n+' + str(x) + '*', end='')
        time.sleep(0.5)
        print()
    elif playerDict['House'] == 'Slytherin':
        print(Fore.GREEN + '\n+' + str(x) + '*', end='')
        time.sleep(0.5)
        print()
    else:
        print('\n~Wait, are you unsorted? What are you doing here?~', end='')
        time.sleep(0.5)
        print()

def EndDayOne():
    if playerDict['House'] == 'Gryffindor':
        housePts['Hufflepuff'] += 70
        housePts['Ravenclaw'] += 75
        housePts['Slytherin'] += 110
    elif playerDict['House'] == 'Hufflepuff':
        housePts['Gryffindor'] += 75
        housePts['Ravenclaw'] += 70
        housePts['Slytherin'] += 110
    elif playerDict['House'] == 'Ravenclaw':
        housePts['Gryffindor'] += 75
        housePts['Hufflepuff'] += 70
        housePts['Slytherin'] += 110
    elif playerDict['House'] == 'Slytherin':
        housePts['Gryffindor'] += 110
        housePts['Hufflepuff'] += 70
        housePts['Ravenclaw'] += 75

def EndDayTwo():
    if playerDict['House'] == 'Gryffindor':
        housePts['Hufflepuff'] += 60
        housePts['Ravenclaw'] += 65
        housePts['Slytherin'] += 80
    elif playerDict['House'] == 'Hufflepuff':
        housePts['Gryffindor'] += 65
        housePts['Ravenclaw'] += 60
        housePts['Slytherin'] += 80
    elif playerDict['House'] == 'Ravenclaw':
        housePts['Gryffindor'] += 65
        housePts['Hufflepuff'] += 60
        housePts['Slytherin'] += 80
    elif playerDict['House'] == 'Slytherin':
        housePts['Gryffindor'] += 80
        housePts['Hufflepuff'] += 60
        housePts['Ravenclaw'] += 65

def EndDayThree():
    if playerDict['House'] == 'Gryffindor':
        housePts['Hufflepuff'] += 60
        housePts['Ravenclaw'] += 65
        housePts['Slytherin'] += 80
    elif playerDict['House'] == 'Hufflepuff':
        housePts['Gryffindor'] += 65
        housePts['Ravenclaw'] += 60
        housePts['Slytherin'] += 80
    elif playerDict['House'] == 'Ravenclaw':
        housePts['Gryffindor'] += 65
        housePts['Hufflepuff'] += 60
        housePts['Slytherin'] += 80
    elif playerDict['House'] == 'Slytherin':
        housePts['Gryffindor'] += 80
        housePts['Hufflepuff'] += 60
        housePts['Ravenclaw'] += 65

def HousePointTotals():
    print('\n~The house point totals are being calculated.~', end='')
    input()
    print(Fore.RED + f"\n~Gryffindor: {housePts['Gryffindor']}~", end='')
    input()
    print(Fore.YELLOW + f"~Hufflepuff: {housePts['Hufflepuff']}~", end='')
    input()
    print(Fore.BLUE + f"~Ravenclaw: {housePts['Ravenclaw']}~", end='')
    input()
    print(Fore.GREEN + f"~Slytherin: {housePts['Slytherin']}~", end='')
    input()
    keymax = max(zip(housePts.values(), housePts.keys()))[1]
    if keymax == 'Gryffindor':
        print(Fore.RED + '\n~Gryffindor is in the lead!~', end='')
        input()
    elif keymax == 'Hufflepuff':
        print(Fore.YELLOW + '\n~Hufflepuff is in the lead!~', end='')
        input()
    elif keymax == 'Ravenclaw':
        print(Fore.BLUE + '\n~Ravenclaw is in the lead!~', end='')
        input()
    elif keymax == 'Slytherin':
        print(Fore.GREEN + '\n~Slytherin is in the lead!~', end='')
        input()