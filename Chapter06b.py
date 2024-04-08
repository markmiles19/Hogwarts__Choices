#IMPORTED DICTIONARIES
from Common import Player
from Common import AddHousePoints
from Common import HousePointTotals
import time
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)

class Subchapter():
      def __init__(self):
            self.name = 'Chapter 6b'

      #BEGIN TRANSFIGURATION
      def Transfiguration(self):
            print('\n~You nearly get lost on your way to Transfiguration with Professor McGonagall, but you manage to\n'
                  'make it just in time.~', end='')
            input()
            print('\nMCGONAGALL: Take a seat everyone! We\'ll being momentarily.', end='')
            input()
            print('MCGONAGALL: Mr. Davies please put that sneakoscope away.', end='')
            input()
            print('MCGONAGALL: Thank you.', end='')
            input()
            print('MCGONAGALL: Now we will begin with today\'s lesson on Avifors, the spell that will allow you\n'
                  'to transform everyday objects into birds.', end='')
            input()
            print('MCGONAGALL: To demonstrate the spell, each of you will cast the Avifors spell on your chairs.', end='')
            input()
            print('MCGONAGALL: Now you may begin!', end='')
            input()
            print('\n~To cast Avifors, you must unscramble each anagram.~', end='')
            input()
            print('\n~ GDEIHW ~\n')
            x = input()
            if x == 'Hedwig' or x == 'hedwig' or x == 'HEDWIG':
                  AddHousePoints(10)
            else:
                  print('\n~ GDEIHW ~', end='')
                  time.sleep(0.3)
                  print('\n~ HGDEIW ~', end='')
                  time.sleep(0.3)
                  print('\n~ HEGDIW ~', end='')
                  time.sleep(0.3)
                  print('\n~ HEDGIW ~', end='')
                  time.sleep(0.3)
                  print('\n~ HEDWGI ~', end='')
                  time.sleep(0.3)
                  print('\n~ HEDWIG ~', end='')
                  input()
            print('\n~ SLBGNIO ~\n')
            x = input()
            if x == 'Goblins' or x == 'goblins' or x == 'GOBLINS':
                  AddHousePoints(10)
            else:
                  print('\n~ SLBGNIO ~', end='')
                  time.sleep(0.3)
                  print('\n~ GSLBNIO ~', end='')
                  time.sleep(0.3)
                  print('\n~ GOSLBNI ~', end='')
                  time.sleep(0.3)
                  print('\n~ GOBSLNI ~', end='')
                  time.sleep(0.3)
                  print('\n~ GOBLSNI ~', end='')
                  time.sleep(0.3)
                  print('\n~ GOBLISN ~', end='')
                  time.sleep(0.3)
                  print('\n~ GOBLINS ~', end='')
                  input()
            print('\n~ ICXLSIELFFIE ~\n')
            x = input()
            if x == 'Felix Felicis' or x == 'felix felicis' or x == 'FELIX FELICIS' or x == 'FelixFelicis' or x == 'felixfelicis' or x == 'FELIXFELICIS':
                  AddHousePoints(20)
            else:
                  print('\n~ ICXLSIELFFIE ~', end='')
                  time.sleep(0.3)
                  print('\n~ FICXLSIELFIE ~', end='')
                  time.sleep(0.3)
                  print('\n~ FEICXLSILFIE ~', end='')
                  time.sleep(0.3)
                  print('\n~ FELICXSILFIE ~', end='')
                  time.sleep(0.3)
                  print('\n~ FELIXCSILFIE ~', end='')
                  time.sleep(0.3)
                  print('\n~ FELIXFCSILIE ~', end='')
                  time.sleep(0.3)
                  print('\n~ FELIXFECSILI ~', end='')
                  time.sleep(0.3)
                  print('\n~ FELIXFELCSII ~', end='')
                  time.sleep(0.3)
                  print('\n~ FELIXFELICSI ~', end='')
                  time.sleep(0.3)
                  print('\n~ FELIXFELICIS ~', end='')
                  input()
            print('\n~Avifors!~', end='')
            input()
            print('\n~You have successfully transformed your chair into a hummingbird.~', end='')
            input()
            print(f"\nMCGONAGALL: Well done, {playerDict['firstName']}!", end='')
            input()
            print('MCGONAGALL: Be sure to continue practicing the Avifors spell in your own time.', end='')
            input()
            print('MCGONAGALL: Class dismissed!', end='')
            input()
            #END TRANSFIGURATION



      #BEGIN HERBOLOGY
      def Herbology(self):
            print('\n~You travel out to the herbology greenhouses on the Hogwarts grounds, where you meet Professor Sprout!~', end='')
            input()
            print('\nSPROUT: Good morning, everyone!', end='')
            input()
            print('SPROUT: I hope you all brought your dragon-hide gloves because we\'re getting right to business.', end='')
            input()
            print('SPROUT: Today\'s lesson will be on Chinese Chomping Cabbages, a plant with a vicious appetite.', end='')
            input()
            print('SPROUT: Now I would like for you collect six carrots from around the room and return with them to\n'
                  'your cabbage.', end='')
            input()
            print('SPROUT: Off you go now!', end='')
            input()

            MissedCount = 0
            MissedDict = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six'}

            print('\n~For every letter that spells out the word CARROT type PICK.~', end='')
            input()
            print('\n~ A ~\n')
            x = input()
            if x == 'Pick' or x == 'pick' or x == 'PICK':
                  AddHousePoints(-5)
            else:
                  pass
            print('\n~ C ~\n')
            x = input()
            if x == 'Pick' or x == 'pick' or x == 'PICK':
                  AddHousePoints(5)
            else:
                  MissedCount += 1
                  AddHousePoints(-5)
            print('\n~ A ~\n')
            x = input()
            if x == 'Pick' or x == 'pick' or x == 'PICK':
                  AddHousePoints(5)
            else:
                  MissedCount += 1
                  AddHousePoints(-5)
            print('\n~ P ~\n')
            x = input()
            if x == 'Pick' or x == 'pick' or x == 'PICK':
                  AddHousePoints(-5)
            else:
                  pass
            print('\n~ R ~\n')
            x = input()
            if x == 'Pick' or x == 'pick' or x == 'PICK':
                  AddHousePoints(5)
            else:
                  MissedCount += 1
                  AddHousePoints(-5)
            print('\n~ O ~\n')
            x = input()
            if x == 'Pick' or x == 'pick' or x == 'PICK':
                  AddHousePoints(-5)
            else:
                  pass
            print('\n~ R ~\n')
            x = input()
            if x == 'Pick' or x == 'pick' or x == 'PICK':
                  AddHousePoints(5)
            else:
                  MissedCount += 1
                  AddHousePoints(-5)
            print('\n~ Q ~\n')
            x = input()
            if x == 'Pick' or x == 'pick' or x == 'PICK':
                  AddHousePoints(-5)
            else:
                  pass
            print('\n~ O ~\n')
            x = input()
            if x == 'Pick' or x == 'pick' or x == 'PICK':
                  AddHousePoints(5)
            else:
                  MissedCount += 1
                  AddHousePoints(-5)
            print('\n~ T ~\n')
            x = input()
            if x == 'Pick' or x == 'pick' or x == 'PICK':
                  AddHousePoints(5)
            else:
                  MissedCount += 1
                  AddHousePoints(-5)
            print('\nSPROUT: Time\'s up!', end='')
            input()
            if MissedCount == 0:
                  print('SPROUT: Now that you have all six carrots, you will feed them to your cabbage.', end='')
                  input()
            elif MissedCount > 0 and MissedCount < 6:
                  print(f"SPROUT: Unfortunately you missed {MissedDict[str(MissedCount)]} carrots, but I\'m sure we\'ll manage.", end='')
                  input()
                  print('SPROUT: Now you will feed them to your cabbage.', end='')
                  input()
            else:
                  print('SPROUT: Well it appears that you were unable to collect any carrots at all.', end='')
                  input()
                  print('SPROUT: I\'m honestly astounded.', end='')
                  input()
                  print('SPROUT: I\'m afraid I\'ll have to deduct even more points for that.', end='')
                  input()
                  AddHousePoints(-10)
            if MissedCount < 6:
                  print('\n~Press F to feed the cabbages.~\n')
                  x = input()
                  def FeedCabbages(x):
                        if x == 'f' or x == 'F':
                              for _ in range(6 - MissedCount):
                                    print('\nCHOMP', end='')
                                    time.sleep(1)
                              input()
                        else:
                              print('\n~Eh-hem, I said press F to feed the cabbages.~\n')
                              x = input()
                              FeedCabbages(x)
                  FeedCabbages(x)     
            else:
                  pass
            print('\nSPROUT: I hope today\'s lesson has been helpful. You may go now.', end='')
            input()
            #END HERBOLOGY



      #BEGIN CARE FOR MAGICAL CREATURES
      def MagicalCreatures(self):
            print('\n~You make your way over to an open clearing right outside the Forbidden Forest where other students\n'
                  'are gathered around.~', end='')
            input()
            print('\n~You come face to face with Professor Kettleburn, an old man decorated in prosthetic limbs with a\n'
                  'bandage covering an eye. Next to him sits a large tortoise-like creature in a cage.~', end='')
            input()
            print('\nKETTLEBURN: Thank you everyone for attending class today. We\'ll be learning about a very fascinating\n'
                  'type of creature today, the fire crab.', end='')
            input()
            print('KETTLEBURN: The fire crab is know for its protective shell and ability to project fire from its rear,\n'
                  'making it an especially dangerous creature to handle.', end='')
            input()
            print('KETTLEBURN: Often they are bred with a manticore to produce a far more formidable foe...', end='')
            input()
            print('KETTLEBURN: The blast-ended skrewt.', end='')
            input()
            print('KETTLEBURN: That\'s why today we will be learning the spell Rictusempra, which is the only known spell\n'
                  'to stun the crab.', end='')
            input()
            print('KETTLEBURN: Follow my wand movement like so.', end='')
            input()
            print('\n~ertfcvb~\n')
            x = input()
            if x == 'ertfcvb':
                  AddHousePoints(10)
            else:
                  print('\nKETTLEBURN: You can do better than that.', end='')
                  input()
            print('\n~ertyugcvbnm~\n')
            x = input()
            if x == 'ertyugcvbnm':
                  AddHousePoints(10)
            else:
                  print('\nKETTLEBURN: You can do better than that.', end='')
                  input()
            print('\n~qweszxc~\n')
            x = input()
            if x == 'qweszxc':
                  AddHousePoints(10)
            else:
                  print('\nKETTLEBURN: You can do better than that.', end='')
                  input()
            print('\n~You hear the sound of crunching wood...~', end='')
            input()
            print('\n~The fire crab has broken free!~', end='')
            input()
            print('\n~Quick! Press R to cast Rictusempra!~\n')
            x = input()
            if x == 'r' or x == 'R':
                  print('\n~Rictusempra!~', end='')
                  input()
                  print('\n~You manage to stun the fire crab before it could harm Kettleburn.~', end='')
                  input()
                  print(f"\nKETTLEBURN: Excellent casting, {playerDict['firstName']}.", end='')
                  input()
                  print('KETTLEBURN: You saved me from purchasing yet another leg replacement.', end='')
                  input()
                  print(f"KETTLEBURN: Fifteen points to {playerDict['House']} for your bravery!", end='')
                  input()
                  AddHousePoints(15)
            else:
                  print('\n~The fire crab sears off Kettleburn\'s wooden leg as he struggles to fan out the flame.~', end='')
                  input()
                  print('\nKETTLEBURN: Aguamenti!', end='')
                  input()
                  print('\n~The water-making spell douses the fire in an instant.~', end='')
                  input()
                  print('\nKETTLEBURN: Well it seems that will make thirteen legs now.', end='')
                  input()
            print('\nKETTLEBURN: I suppose that\'s more than enough for one day. Class dismissed.', end='')
            input()
            #END HERBOLOGY