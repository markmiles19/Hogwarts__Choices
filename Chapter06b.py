#IMPORTED DICTIONARIES
from Common import playerDict

#IMPORTED FUNCTIONS
from Common import AddHousePoints
from Common import HousePointTotals

#IMPORTED ETC
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)

#BEGIN TRANSFIGURATION
def Transfiguration():
    playerDict['AttendTransfig'] = True
    #END TRANSFIGURATION



#BEGIN HERBOLOGY
def Herbology():
    playerDict['AttendHerb'] = True
    #END HERBOLOGY



#BEGIN CARE FOR MAGICAL CREATURES
def MagicalCreatures():
    print('\n~You make your way over to an open clearing right outside the Forbidden Forest where other students\n'
          'are gathered around.~', end='')
    input()
    print('\nYou come face to face with Professor Kettleburn, an old man decorated in prosthetic limbs with a\n'
          'bandage covering an eye. Next to him sits a large tortoise-like creature in a cage.', end='')
    input()
    print('KETTLEBURN: Thank you everyone for attending class today. We\'ll be learning about a very fascinating\n'
          'type of creature today, the fire crab.', end='')
    input()
    print('KETTLEBURN: The fire crab is know for its protective shell and ability to project fire from its rear\n,'
          'making it an especially dangerous creature to handle.', end='')
    input()
    print('KETTLEBURN: That\'s why today we will be learning the spell Rictusempra, which can be used to disable ')
    input()
    playerDict['AttendCare'] = True
    print('KETTLEBURN: I suppose that\'s more than enough for one day. Class dismissed.', end='')
    input()
    #END HERBOLOGY