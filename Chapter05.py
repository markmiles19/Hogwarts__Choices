from Common import Player
from Common import Choices
from Common import HousePts

class Chapter():
    class Dialogue():
        def Branch_1(self, user_input):
            if user_input == '1':
                print('\nPERCIVAL: Sorry about that. Like I said, Ancient Runes was a big mistake.', end='')
            elif user_input == '2':
                print('\nPERCIVAL: Thanks for waiting up for me.', end='')
            else:
                print('PERCIVAL: Did you say something?\n')
                user_input = input()
                Chapter.Dialogue.Branch_1(user_input)

        def Branch_2(self, user_input):
            if user_input == '1':
                print('\nPERCIVAL: Well what are you waiting for? Cast Reducto on the glass.', end='')
                input()
            elif user_input == '2':
                print('\nPERCIVAL: Flitwick taught you both Reducto AND Reparo, right?', end='')
                input()
                print('PERCIVAL: As long as we repair the glass after we\'re done, no one will ever know.', end='')
                input()
                print('PERCIVAL: Now go on...', end='')
                input()
            else:
                print('PERCIVAL: Are you going to cast Reducto or not?\n')
                user_input = input()
                Chapter.Dialogue.Branch_2(user_input)

        def Branch_3(self, user_input):
            if user_input == '1':
                print(f"\nPERCIVAL: Not the time, {Player.first_name}!", end='')
                input()
            elif user_input == '2':
                print('')
            else:
                print('')

        def Reducto(self, user_input):
            if user_input == 'd' or user_input == 'D':
                print('\n~ Reducto! ~', end='')
                input()
            else:
                print('\nPERCIVAL: Just cast the flippin\' spell already!\n')
                x = input()
                Chapter.Dialogue.Reducto(x)

        def FiltchIsComing():
            print(f"\n{Player.companion}: Filtch is coming! Hide!", end='')
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
                HousePts.Add_House_Points(-15)
                print('\nFILTCH: Looks like it\'s down to the dungeons with you!', end='')
                input()
                print('\n~After another day of classes and a grueling evening serving detention, you start over again...~', end='')
                input()
                Chapter.Execute_Main()

        def Section_3(self):
            print(
                '\n[<] ~PREV~\n'
                '[1] Zacharias Mumps, 1368\n'
                '[2] Gladys Boothby, 1901\n'
                '[3] Jonathan Able, 1034\n'
                '[4] Katie Rayknolls, 1728\n')
            x = input()
            if x == '<':
                Chapter.Dialogue.Section_2()
            elif x == '3':
                pass
            else:
                Chapter.Dialogue.FiltchIsComing()

        def Section_2(self):
            print(
                '\n[<] ~PREV~\n'
                '[1] Bowman Wright, 1506\n'
                '[2] R. J. H. King, 1968\n'
                '[3] Jocunda Sykes, 1921\n'
                '[4] Modesty Rabnott, 1269\n'
                '[>] ~NEXT~\n')
            x = input()
            if x == '<':
                Chapter.Dialogue.Section_1()
            elif x == '>':
                Chapter.Dialogue.Section_3()
            else:
                Chapter.Dialogue.FiltchIsComing()

        def Section_1(self):
            print(
                '\n[1] M. G. McGonagall, 1971\n'
                '[2] Elfrida Clagg, 1345\n'
                '[3] James Potter, 1973\n'
                '[4] Kennilworthy Whisp, 1954\n'
                '[>] ~NEXT~\n')
            x = input()
            if x == '>':
                Chapter.Dialogue.Section2()
            else:
                Chapter.Dialogue.FiltchIsComing()

        def Standstill(self, user_input):
            if user_input == '1':
                print('\nPERCIVAL: No!')
                print('MILO: No!\n')
                user_input = input()
                Chapter.Dialogue.Standstill(user_input)
            elif user_input == '2':
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
            elif user_input == '3':
                print('\n~You cast the stunning spell, Stupefy, and dash out of the room with the trophy,\n'
                    'your friends trailing behind you.~')
                input()
                print('\n~After dodging patrolling prefects on your return to the Gryffindor Common room,\n'
                    'you all turn in after an exhausting night.~', end='')
                input()
            elif user_input == '4':
                print('\nMILO: If that\'s what you want, then so be it.', end='')
                input()
                print('MILO: Stupefy!', end='')
                input()
                print('\n~Press D to dodge.~', end='')
                user_input = input()
                if user_input == 'd' or user_input == 'D':
                    pass
                else:
                    print('\n~Milo stunned you in your right arm.~', end='')
                    input()
                print('\n~You are hidden behind a column. Will you attack from the left or the right?~', end='')
                input()
                print(
                    '\n[1] Left\n'
                    '[2] Right\n'
                )
                user_input = input()
                if user_input == '1':
                    print('\n~You manage to graze his left knee.~', end='')
                    input()
                    print('\nMILO: You\'ll have to do better than that if you want me to yield!', end='')
                    input()
                elif user_input == '2':
                    print('\n~You manage to graze his right knee.~', end='')
                    input()
                    print('\nMILO: You\'ll have to do better than that if you want me to yield!', end='')
                    input()
                else:
                    print('\n~You sneak a look around the corner...~', end='')
                    input()
                    print('\nMILO: Stupefy!', end='')
                    input()
                    print('\n~He blinds your sight temporarily.~', end='')
                    input()
                    print('\nMILO: It\'s never too late to yield!', end='')
                    input()
                print('\n~You leave your cover and open fire on him.~', end='')
                input()
                print('~Press S to cast stupefy.~', end='')
                user_input = input()
                if user_input == 's' or user_input == 'S':
                    pass
                else:
                    print('~OUCH~', end='')
                    input()
                print('~Press S to cast stupefy.~', end='')
                user_input = input()
                if user_input == 's' or user_input == 'S':
                    pass
                else:
                    print('~OUCH~', end='')
                    input()
                print('~Press P to defend with Protego.~', end='')
                user_input = input()
                if user_input == 'p' or user_input == 'P':
                    pass
                else:
                    print('~OUCH~', end='')
                    input()
                print('\n~Milo is on the ground now, completely defenseless. What will you do?~', end='')
                input()
                print(
                    '\n[1] Disarm him\n'
                    '[2] Let him go\n'
                )
                def MiloFate(x):
                    if x == '1':
                        print('\n~Expelliarmus!~', end='')
                        input()
                        print('\n~Milo\'s wand flies out of his hand and hits the floor.~', end='')
                        input()
                        print('\nMILO: Alright! Alright I yield now.', end='')
                        input()
                        print('MILO: Just take your trophy and go.', end='')
                        input()
                        print('\n~MILO trudges out of the room, his pride in shambles.~', end='')
                        input()
                        print('\n~After dodging patrolling prefects on your return to the Gryffindor Common room,\n'
                        'you all turn in after an exhausting night.~', end='')
                        input()
                    elif x == '2':
                        print('\n~You pocket your want and help him back up on his feet.~', end='')
                        input()
                        print('\n~He dashed to the exit, turns back to you briefly, and then disappears.~', end='')
                        input()
                        print('\n~After dodging patrolling prefects on your return to the Gryffindor Common room,\n'
                        'you all turn in after an exhausting night.~', end='')
                        input()
                    else:
                        print('\nYou have an important decision to make. Now choose!', end='')
                        x = input()
                        MiloFate(x)
                x = input()
                MiloFate(x)
            else:
                print('\n~This could turn ugly real fast. Now it\'s time to intervene.~\n')
                user_input = input()
                Chapter.Dialogue.Standstill(user_input)

    def __init__(self):
        self.name = 'Chapter 5'
        
    def Execute_Main(self):
        #GRYFFINDOR/RAVENCLAW/HUFFLEPUFF PATH
        if Player.house != 'Slytherin':
            print('')
            print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
            print(' ~   CHAPTER 5: THE LOST SEEKER    ~ ')
            print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
            input()
            print('\n~Tonight is the night! You wait patiently in the third floor corridor for Percival to arrive.~', end='')
            input()
            print('\n~Finally he approaches you with his younger brother, Leo.~', end='')
            input()
            print(
                '\n[1] What took you so long?\n'
                '[2] I\'m ready when you are.\n'
            )
            user_input = input()
            Chapter.Dialogue.Branch_1(user_input)
            input()
            print('PERCIVAL: The good news is that the trophy room is open to students at all times.', end='')
            input()
            print('\nLEO: The only downside is that the caretaker Mr. Filtch stops by every so often to make sure\n'
                'there aren\'t any students getting up to no good.', end='')
            input()
            print('\nPERCIVAL: And as you could imagine that will be a problem for us.', end='')
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
            print(f"LEO: I guess that leaves you with the Quidditch trophies, {Player.first_name}.", end='')
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
            print('\n~The glass case shatters into a million pieces. Thank Merlin none of them landed on\n'
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
            print('\nMILO: This has everything to do with me.', end='')
            input()
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


        #SLYTHERIN PATH
        if Player.house == 'Slytherin':
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
                    print('\nMILO: I\'ll make a ')
                elif x == 2:
                    print('~You find three objects in the room you can use to your advantage: ~')
                else:
                    print()
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
            user_input = input()
            Chapter.Dialogue.Standstill(user_input)
            print('\n~You dodge patrolling prefects as you return to the Slytherin Common room with\n'
                    'Milo, and you turn in after an exhausting night.~', end='')
            input()
            #END SLYTHERIN PATH



#RUN CHAPTER
