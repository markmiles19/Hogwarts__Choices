from Common import playerDict
from Common import AddHousePoints

#BEGIN DEFENSE AGAINST THE DARK ARTS CLASS
def Defense():
    print('\n~You reach the Defense Against the Dark Arts Classroom. You don\'t even bother remembering'
          'the teacher\'s name since you know he\'ll be gone at the end of the year.~', end='')
    input()
    print('\nTEACHER: Good morning, class!', end='')
    input()
    print('TEACHER: We\'ll be learning about a most fascinating creature called a boggart.', end='')
    input()
    print('TEACHER: Now a boggart takes the shape of what one fears the most, and they often hide\n'
          'inside of everyday objects such as wardrobes or cabinets.', end='')
    input()
    print('TEACHER: They can be banished through a simple spell...', end='')
    input()
    print('TEACHER: Riddikulus.', end='')
    input()
    print('TEACHER: Now pay close attention to my movements and repeat the spell.', end='')
    input()
    print('\n~qazmlp~\n')
    x = input()
    if x == 'qazmlp':
        AddHousePoints(10)
        print('TEACHER: Very good!', end='')
        input()
    else:
        print('TEACHER: Ooh! Not good.', end='')
        input()
    print('\n~weiosdjkxcbn~\n')
    x = input()
    if x == 'weiosdjkxcbn':
        AddHousePoints(10)
        print('TEACHER: Very good!', end='')
        input()
    else:
        print('TEACHER: Ooh! Not good.', end='')
        input()
    print('\n~rfvbhuh~\n')
    x = input()
    if x == 'rfvbhuh':
        AddHousePoints(10)
        print('TEACHER: Very good!', end='')
        input()
    else:
        print('TEACHER: Ooh! Not good.', end='')
        input()
    print('~Riddikulus!~', end='')
    input()
    print('~Your spell disappears into thin air.~', end='')
    input()
    print('\nTEACHER: Unfortunately we won\'t be able to put the spell to practical\n'
          'use during this class period since all boggarts have been curiously displaced.', end='')
    input()
    playerDict['AttendDefense'] = True
    print('TEACHER: Alright, I won\'t hold you any longer. Off you go!', end='')
    input()
    #END DEFENSE AGAINST THE DARK ARTS CLASS



#BEGIN DIVINATION CLASS
def Divination():
    print('\n~You ascend into the highest levels of the castle until you find the Divination classroom.~', end='')
    input()
    print('\n~Professor Trelawney is the strangest person you have ever met.~', end='')
    input()
    print('\nTRELAWNEY: Today we will learn to cast ourselves into the future through the noble art of\n'
          'Divination.', end='')
    input()
    print('TRELAWNEY: Today\'s lesson will be on Tessomancy, which is the reading of tea leaves.', end='')
    input()
    print('TRELAWNEY: Now I will pass around these cups, and I want for you to tell me what you see.', end='')
    input()

    #QUESTION #1
    print('')
    print('@@@@@@@@@@@@@@@@BB@@@@@@@@@@@@\n'
          '@@@@@@@@&&##BBBPPB#&@@@@@@@@@@\n'
          '@@@@@&BP5Y55YJYJ?JY5PGB#@@@@@@\n'
          '@@@@B5YYYJJJJ??7?Y5PPP555B@@@@\n'
          '@@@5JYJJ7!!!!!!7Y555PPP55JP@@@\n'
          '@@B?JY?7!~~!7JYY555555PPP5J#@@\n'
          '@@P?JJJ?7!!!7YYYY555555PP5YG@@\n'
          '@@B7JJJ??????YYY5555555PPPYP@@\n'
          '@@@Y?JJJ?JJYJYYYY5555555P5YB@@\n'
          '@@@&J?JJJJJJJYYYYY555555555@@@\n'
          '@@@@@P?????JJJYYYYY5555555&@@@\n'
          '@@@@@@#5J??7?JJYYYY55555P&@@@@\n'
          '@@@@@@@@&G5JJJJYYY5555PB@@@@@@\n'
          '@@@@@@@@@@@&#GPPGGBB#&@@@@@@@@\n')
    print('[1] Acorn\n'
          '[2] Skull\n'
          '[3] Apple\n'
          '[4] Sun\n')
    x = input()
    if x == '3':
        AddHousePoints(10)
    else:
        print('\nTRELAWNEY: Oh are you sure you\'re using your inner eye?', end='')
        input()

    #QUESTION #2
    print('')
    print('@@@@@@@@@@@@@@&#@@@@@@@@@@@@@@\n'
          '@@@@@@@@@@@@@&###&@@@@@@@@@@@@\n'
          '@@@@@@@@@@@&######&@@@@@@@@@@@\n'
          '@@@@@@@@@&##########&@@@@@@@@@\n'
          '@@@@@@@&##############&@@@@@@@\n'
          '@@@@@&################B#&@@@@@\n'
          '@@@@#B#################BB#&@@@\n'
          '@@@#B###################BBB@@@\n'
          '@@&B###################BBBB#@@\n'
          '@@&B###########B#####BBBBBB&@@\n'
          '@@@#BB######B####BBBBBBBBB#@@@\n'
          '@@@@&#######&&B#@&#######&@@@@\n'
          '@@@@@@@@@@@@@##B#@@@@@@@@@@@@@\n'
          '@@@@@@@@@@@&BB##B#@@@@@@@@@@@@\n')
    print('[1] Club\n'
          '[2] Spade\n'
          '[3] Mountain\n'
          '[4] Kite\n')
    x = input()
    if x == '2':
        AddHousePoints(10)
    else:
        print('\nTRELAWNEY: Oh are you sure you\'re using your inner eye?', end='')
        input()

    #QUESTION #3
    print('')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
          '@@@@@@@@@@##@@@@@@@#&@@@@@@@@@\n'
          '@@@@@@@@@@&PB@&5@@#5@@@@@@@@@@\n'
          '@@@@@@@&G&@&J&#Y@#Y&@&B@@@@@@@\n'
          '@@@&B##&&GP57!!~!7Y#GG&@@&&@@@\n'
          '@@@@@&#GG5~^^~~~^^^~J#GGG#&@@@\n'
          '@@@@#B##G^~~~~~~~~~~^P###&@@@@\n'
          '@@@@@&##G~^~~~~~~~~~^G###&@@@@\n'
          '@@@#BGGG#5~^^^~^^^^~PBPB#&@@@@\n'
          '@@@&&@@&PG&5?7!!!?PPG&@&###@@@\n'
          '@@@@@@@#&@#Y&@Y&&J@@#G&@@@@@@@\n'
          '@@@@@@@@@@5&@@5&@BP@@@@@@@@@@@\n'
          '@@@@@@@@@#&@@@@@@@##@@@@@@@@@@\n'
          '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
    print('[1] Spider\n'
          '[2] Ferns\n'
          '[3] Hand\n'
          '[4] Sun\n')
    x = input()
    if x == '4':
        AddHousePoints(10)
    else:
        print('\nTRELAWNEY: Oh are you sure you\'re using your inner eye?', end='')
        input()

    #QUESTION #4
    print('')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
          '@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@\n'
          '@@@@@@@@@@@&@@&@@&@@@@@@@@@@@@\n'
          '@@@@@@@@@@@&&&@@@@@&@@@@@@@@@@\n'
          '@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@\n'
          '@@@@@@@@&@&#@@@@@@@@@@@@@@@@@@\n'
          '@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@\n'
          '@@@@@@@@@@@&&&&@@@&@@@@&&&@@@@\n'
          '@@@&@@&&#BBB#B###&&&@@@&&&@@@@\n'
          '@@@@@#BBB#@@@@@@&&@&@&@&@@@@@@\n'
          '@@@@@@@@@@@@@@@@@@@@@&@&@@@@@@\n'
          '@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@\n'
          '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
          '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
    print('[1] House\n'
          '[2] Grim\n'
          '[3] Fox\n'
          '[4] Hammer\n')
    x = input()
    if x == '2':
        AddHousePoints(10)
    else:
        print('\nTRELAWNEY: Oh are you sure you\'re using your inner eye?', end='')
        input()
    playerDict['AttendDiv'] = True
    print('\nTRELAWNEY: I\'m afraid that\'s all of the time we have for today.', end='')
    input()
    print('TRELAWNEY: You may go now.', end='')
    #END DIVINATION CLASS



#BEGIN ASTRONOMY CLASS
def Astronomy():
    print('\n~You gather with other students in the astronomy tower where you can see the\n'
          'entire grounds of Hogwarts all around you. Professor Sinistra stands before you.~', end='')
    input()
    print('\nSINISTRA: Settle down now, please!', end='')
    input()
    print('SINISTRA: I\'m sure many of you are eager to break out those telescopes you bought\n'
          'from Diagon Alley, but I thought I would warm all of you up a different way...', end='')
    input()
    print('SINISTRA: With a pop quiz!', end='')
    input()
    print('\n~Every one of you groan.~', end='')
    input()
    print('\nSINISTRA: Now I\'ll be a lot more forgiving with your grades since this is the first\n'
          'day, so let us begin.', end='')
    input()

    #QUESTION #1
    print('SINISTRA: Question #1: The constellation Ursa Major is often seen as either a bear, wagon,\n'
          'or ladle, but it is more commonly known by what other name?', end='')
    input()
    print(
        '\n[1] Big Dipper\n'
        '[2] Little Dipper\n'
        '[3] Plough\n'
        '[4] Polaris\n'
    )
    x = input()
    if x == '1':
        print('\nSINISTRA: Incorrect.', end='')
        input()
        print('SINISTRA: In the United Kingdom, Ursa Major is known as the Plough, whereas the name Big\n'
              'Dipper is used in the United States and Canada.', end='')
        input()
    elif x == '2':
        print('\nSINISTRA: Incorrect.', end='')
        input()
        print('SINISTRA: In the United Kingdom, Ursa Major is known as the Plough, whereas the name Little\n'
              'Dipper is used in the United States and Canada to refer to Ursa Minor.', end='')
        input()
    elif x == '3':
        AddHousePoints(5)
        print('\nSINISTRA: Correct.', end='')
        input()
        print('SINISTRA: In the United Kingdom, Ursa Major is known as the Plough.', end='')
        input()
    elif x == '4':
        print('\nSINISTRA: Incorrect.', end='')
        input()
        print('SINISTRA: In the United Kingdom, Ursa Major is known as the Plough, whereas Polaris is the\n'
              'star located at the tip of Ursa Minor.', end='')
        input()
    else:
        print('\nSINISTRA: Time\'s up!', end='')
        input()
        print('SINISTRA: In the United Kingdom, Ursa Major is known as the Plough.', end='')
        input()

    #QUESTION #2
    print('SINISTRA: Question #2: Which zodiac constellation is located between Cancer and Taurus?', end='')
    input()
    print(
        '\n[1] Taurus\n'
        '[2] Gemini\n'
        '[3] Leo\n'
        '[4] Virgo\n'
    )
    x = input()
    if x == '1':
        print('\nSINISTRA: Incorrect!', end='')
        input()
        print('SINISTRA: Taurus can be found between Aries and Gemini, however Leo is found between Cancer and Taurus.', end='')
        input()
    elif x == '2':
        print('\nSINISTRA: Incorrect!', end='')
        input()
        print('SINISTRA: Gemini can be found between Taurus and Cancer, however Leo is found between Cancer and Taurus.', end='')
        input()
    elif x == '3':
        AddHousePoints(5)
        print('\nSINISTRA: Correct!', end='')
        input()
        print('SINISTRA: Leo is found in the fifth position of the Zodiac constellations and appears in the\n'
              'sky from July 23 to August 22.', end='')
        input()
    elif x == '4':
        print('\nSINISTRA: Incorrect!', end='')
        input()
        print('SINISTRA: Virgo can be found between Leo and Libra, however Leo is found between Cancer and Taurus.', end='')
        input()
    else:
        print('\nSINISTRA: Time\'s up!', end='')
        input()
        print('SINISTRA: Leo is found in the fifth position of the Zodiac constellations and appears in the\n'
              'sky from July 23 to August 22.', end='')
        input()

    #QUESTION #3
    print('\nSINISTRA: Question #3: At what time of the year can Orion be seen?', end='')
    input()
    print(
        '\n[1] Summer\n'
        '[2] Winter\n'
        '[3] Spring\n'
        '[4] Fall\n'
    )
    x = input()
    if x == '1':
        print('\nSINISTRA: Incorrect!', end='')
        input()
        print('SINISTRA: The constellation Orion is visible during Winter, not Summer.', end='')
        input()
    elif x == '2':
        AddHousePoints(5)
        print('\nSINISTRA: Correct!', end='')
        input()
        print('SINISTRA: The constellation Orion is visible during Winter.', end='')
        input()
    elif x == '3':
        print('\nSINISTRA: Incorrect!', end='')
        input()
        print('SINISTRA: The constellation Orion is visible during Winter, not Spring.', end='')
        input()
    elif x == '4':
        print('\nSINISTRA: Incorrect!', end='')
        input()
        print('SINISTRA: The constellation Orion is visible during Winter, not Fall.', end='')
        input()
    else:
        print('\nSINISTRA: Time\'s up!', end='')
        input()
        print('SINISTRA: The constellation Orion is visible during Winter.', end='')
        input()
    playerDict['AttendAstro'] = True
    print('SINISTRA: Unfortunately that\'s all the time we have for today.', end='')
    input()
    print('SINISTRA: Class dismissed!', end='')
    input()
    #END ASTRONOMY CLASS



