def Chapter01():
      #IMPORTED DICTIONARIES
      from Common import playerDict

      #IMPORTED FUNCTIONS
      from Common import storeName
      from Common import sortingHat1
      from Common import sortingHat2
      from Common import sortingHat3
      from Common import sortingHat4
      from Common import sortingHat5
      from Common import finalizeSort

      #IMPORTED ETC
      import colorama
      from colorama import Back, Fore, Style
      colorama.init(autoreset=True)


      print('')
      print(Back.RED +                ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
      print(Back.YELLOW +             ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
      print(Back.WHITE + Fore.BLACK + ' ~ ~HOGWARTS: CHOICES~ ~ ')
      print(Back.BLUE +               ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
      print(Back.GREEN +              ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')

      print('\n~Before we begin, would you mind giving me your name? Preferably first AND last.~\n')

      playerName = input()
      storeName(playerName)

      print('\n~Excellent! We\'re ready to begin. (Press RETURN to continue.)~', end='')
      input()
      print(f"\nDear Mr/Ms. {playerDict['lastName']},\n"
            'We are pleased to inform you that you have been accepted at Hogwarts School of Witchcraft and Wizardry.\n'
            'Please find enclosed a list of all necessary books and equipment. Term begins on the first of September.\n'
            'We await your owl by no later than the thirty-first of July.\n'
            'Yours sincerely,\n'
            'Minerva McGonagall', end='')
      input()
      print('')
      print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
      print(Back.WHITE + Fore.BLACK + ' ~   CHAPTER 1: THE SORTING HAT    ~ ')
      print(Back.WHITE + Fore.BLACK + ' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
      input()
      print('\n~You meet the Hogwarts groundskeeper, Rubeus Hagrid, and the two of you travel to Diagon Alley to purchase\n'
            'a most unusual list of school supplies including a set of long black robes, an old-fashioned ink and quill,\n'
            'and a wand.~', end='')
      input()
      print('\n~Finally, you arrive at the Hogwarts entrance hall and he sees you off.~', end='')
      input()
      print('\nHAGRID: I ‘spect yeh know where ter go from ‘ere. Jus’ remember, yeh’re welcome to come visit me down at me\n'
            'hut whenever yeh want. I think Professor McGonagall’s waiting fer yeh just inside the Great Hall. Go on now,\n' 
            'don’t be shy!', end='')
      input()
      print('\n~You step inside the longest room you’ve ever seen in your life, filled with rows of students that stretch forever.\n'
            'A group of other first-years are huddled in front of Professor McGonagall.~', end='')
      input()
      print('\nMCGONAGALL: Welcome to Hogwarts! We are now ready to begin the Sorting Ceremony.', end='')
      input()
      print('MCGONAGALL: There are four houses: Gryffindor, Hufflepuff, Ravenclaw, and Slytherin.', end='')
      input()
      print('MCGONAGALL: While you are here, your house will be like your family. Succeeding in your classes and making the right\n'
            'choices will earn you points.', end='')
      input()
      print('MCGONAGALL: Failing to do so will lose you points.', end='')
      input()
      print('MCGONAGALL: The house with the most points by the end of term will be awarded the House Cup, so always do your best!', end='')
      input()
      print('MCGONAGALL: Now when I call your name, you will step forward and I will place the Sorting Hat on your head.', end='')
      input()
      print('...', end='')
      input()
      print('...', end='')
      input()
      print('MCGONAGALL: Earl Wormsby.', end='')
      input()
      print('...', end='')
      input()
      print('...', end='')
      input()
      print('SORTING HAT: Hufflepuff!', end='')
      input()
      print('\n~Applause~', end='')
      input()
      print('\nMCGONAGALL: Vera Flemming.', end='')
      input()
      print('...', end='')
      input()
      print('...', end='')
      input()
      print('SORTING HAT: Gryffindor!', end='')
      input()
      print('\n~Applause~', end='')
      input()
      print(f"\nMCGONAGALL: {playerDict['fullName']}.", end='')
      input()
      print('...', end='')
      input()
      print('...', end='')
      input()
      print('SORTING HAT: Hmm... Yes, I see. This one is particularly difficult. It seems this will require further inquiry.', end='')
      input()

      #Question #1
      print('SORTING HAT: Let’s say that you caught another student jinxing your closest friend outside on the grounds.\n'
            'Your friend repeatedly tells them to stop, but they refuse. How would you react?', end='')
      input()
      print(
      '\n[1] “You jinxed my friend, now I jinx you!”\n'
      '[2] “I’ll give you a chance to stop, then I’m going to get a teacher involved.”\n'
      '[3] ~Cast the counter and help him escape~\n'
      '[4] “Just be rational: You have nothing to gain from this.”\n'
      )

      user_num = input()
      sortingHat1(user_num)

      print('\nSORTING HAT: Interesting. Very interesting. Now let’s see...', end='')
      input()
      print('SORTING HAT: Ah, yes!', end='')
      input()

      #Question #2
      print('During your time at Hogwarts, you will have the opportunity to experience all kinds of activities outside the classroom.\n'
            'Which one appeals most to you?', end='')
      input()
      print(
      '\n[1] Quidditch.\n'
      '[2] Wizard’s Chess.\n'
      '[3] Exploding Snap.\n'
      '[4] Dueling.\n'
      )

      user_num = input()
      sortingHat2(user_num)

      print('\nSORTING HAT: I see...', end='')
      input()

      #Question #3
      print('SORTING HAT: If you could brew the perfect potion with whatever effect you so desired, what would it do?', end='')
      input()
      print(
      '\n[1] It would make me the smartest person in the world. (Wit-Sharpening Potion)\n'
      '[2] It would heal all kinds of injuries. (Wiggenweld Potion)\n'
      '[3] It would allow me to transform into anyone I want. (Polyjuice Potion)\n'
      '[4] It would make every single thing go my way. (Felix Felicis)\n'
      )

      user_num = input()
      sortingHat3(user_num)

      print('\nSORTING HAT: Very curious indeed...', end='')
      input()

      #Question #4
      print('SORTING HAT: The Mirror of Erised shows us nothing more than the deepest, most desperate desires of our hearts.', end='')
      input()
      print('SORTING HAT: When you look into the mirror, what do you see?', end='')
      input()
      print(
      '\n[1] I’m the most powerful sorcerer in the world!\n'
      '[2] I’m shaking hands with Dumbledore after winning the House Cup.\n'
      '[3] I’ve just been promoted to Minister for Magic.\n'
      '[4] Myself, just the way I am.\n'
      )

      user_num = input()
      sortingHat4(user_num)

      print('\nSORTING HAT: Hmm... how very quaint. Now finally...', end='')
      input()

      #Question #5
      print('SORTING HAT: What do you fear the most?', end='')
      input()

      print(
      '\n[1] Rejection.\n'
      '[2] Feeling powerless.\n'
      '[3] Being alone.\n'
      '[4] Failing those around me.\n'
      )

      user_num = input()
      sortingHat5(user_num)

      finalizeSort()

      print('\nSORTING HAT: Hmm... yes.', end='')
      input()
      print('SORTING HAT: I know just where to put you!', end='')
      input()
      print(f"SORTING HAT: {playerDict['House']}!", end='')
      input()
      print(f"\n~The students from the {playerDict['House']} table cheer for you and you sit down next to someone who welcomes you with a pat on the back.~", end='')
      input()
      print('\n~The last first-year has just been sorted and the headmaster Professor Dumbledore stands to speak to the school.~', end='')
      input()
      print('\nDUMBLEDORE: I have a few start of term announcements I wish to make...', end='')
      input()
      print('DUMBLEDORE: First-year students are to disregard any rumors of dragons living in the kitchens.', end='')
      input()
      print('DUMBLEDORE: Second, I am happy to announce that for the first time ever at Hogwarts, students will be offered a flexible schedule.', end='')
      input()
      print('DUMBLEDORE: What this means is that you may choose the order in which you attend your classes. If you would rather not take Charms\n'
            'first thing in the morning, you can leave it for the afternoon and take Potions instead.', end='')
      input()
      print('DUMBLEDORE: That is all for now. Off you trot!', end='')
      input()
      print('...', end='')
      input()

#RUN CHAPTER
#Chapter01()