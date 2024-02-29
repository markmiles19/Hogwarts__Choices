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
    print('TEACHER: Now boggarts can be banished through a simple spell...', end='')
    input()
    print('TEACHER: Riddikulus.', end='')
    input()
    print('')
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

    print('\nTRELAWNEY: I\'m afraid that\'s all of the time we have for today.', end='')
    input()
    print('TRELAWNEY: You may go now.', end='')
    #END DIVINATION CLASS



#BEGIN ASTRONOMY CLASS
def Astronomy():
    print('\n~~')
    input()
    #END ASTRONOMY CLASS



