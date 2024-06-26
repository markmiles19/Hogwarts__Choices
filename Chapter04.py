class Dialogue():
    def __init__(self, User):
        self.player = User

    def Branch_1(self, user_input):
            if user_input == '1':
                print('\nPERCIVAL: I can see you’re as eager as I am.', end='')
                input()
            elif user_input == '2':
                print('\nPERCIVAL: This here is “Hogwarts: A History” by Bathilda Bagshot, and it’s part of the reason I\n'
                    'asked you here in the first place.', end='')
                input()
            else:
                print('\nPERCIVAL: Sorry, could you repeat that?\n')
                user_input = input()
                self.Branch_1(user_input)

    def Branch_2(self, user_input):
            if user_input == '1':
                print('\nPERCIVAL: There’s only one way to find out, and I think I know just where to look.')
                input()
            elif user_input == '2':
                print('\nPERCIVAL: To many it may seem that way. I’m willing to bet it’s the reason it’s been\n'
                    'safely preserved in the library for nearly a thousand years. Any common person would pay\n'
                    'it no mind and excuse it for a placeholder to be passed around from book to book.', end='')
                input()
                print('PERCIVAL: But as for us true explorers on the other hand...', end='')
                input()
            else:
                print('\nPERCIVAL: Come again?\n')
                user_input = input()
                self.Branch_2(user_input)

    def Branch_3(self, user_input):
            if user_input == '1':
                print('\nPERCIVAL: The stars DO glitter like gold at night, but that’s not what I’m looking for.\n')
                user_input = input()
                self.Branch_3(user_input)
            elif user_input == '2':
                print('\nPERCIVAL: That’s really funny, but no.\n')
                user_input = input()
                self.Branch_3(user_input)
            elif user_input == '3':
                print('\nPERCIVAL: Exactly. If we can somehow find the clue Merlin left for us, it would bring us one\n'
                    'step closer to his treasure.', end='')
                input()
                print('PERCIVAL: Unfortunately I’ve got too much homework on my hands at the moment, partly due to the\n'
                    'mistake of taking Ancient Runes, so the best time to go would be at night. What do you say?', end='')
                input()
            else:
                print('\nPERCIVAL: Come on, give me a REAL guess.\n')
                user_input = input()
                self.Branch_3(user_input)

    def Branch_4(self, user_input):
            if user_input == '1':
                print('\nPERCIVAL: You have absolutely nothing to worry about. I’ve done this dozens of times, and Leo can vouch for me.', end='')
                input()
                print('PERCIVAL: As a matter of fact, next time I see him, I’ll let him know of our plans.', end='')
                input()
            elif user_input == '2':
                print('\nPERCIVAL: I like your spirit! Next time I see Leo, I’ll let him know of our plans.', end='')
                input()
            else:
                print('\nPERCIVAL: Come on, give me a REAL guess.\n')
                user_input = input()
                self.Branch_4(user_input)

    def Branch_5(self, user_input):
            if user_input == '1':
                print('\nMILO: Several days ago I checked this book out from the library since I’m an avid reader\n'
                    'and I\'ve always wanted to read “Quidditch Through the Ages.”', end='')
                input()
            elif user_input == '2':
                print('\nMILO: At the moment I’m reading “Quidditch Through the Ages” by Kennilworthy Whisp. I never\n'
                    'cared too much for Quidditch, but it has a fascinating history.', end='')
                input()
            else:
                print('\nMILO: Could you speak up?\n')
                user_input = input()
                self.Branch_5(user_input)

    def Branch_6(self, user_input):
            if user_input == '1':
                print('\nMILO: You have nothing to worry about since it doesn’t mean what you think.', end='')
                input()
            elif user_input == '2':
                print('\nMILO: It’s a riddle.', end='')
                input()
            else:
                (print('\nMILO: Could you speak up?\n'))
                user_input = input()
                self.Branch_6(user_input)

    def Branch_7(self, user_input):
            if user_input == '1':
                print('\nMILO: We could have found him there if it weren’t for the fact that he’s dead.\n')
                user_input = input()
                self.Branch_7(user_input)
            elif user_input == '2':
                print('\nMILO: What would a thousand-year old seeker be doing in the dungeons?\n')
                user_input = input()
                self.Branch_7(user_input)
            elif user_input == '3':
                print('\nMILO: My thoughts exactly. If we can find the trophy that belonged to this seeker, it would bring us closer to\n'
                    'finding the treasure and restoring Merlin’s legacy.', end='')
                input()
            else:
                print('\nMILO: What?\n')
                user_input = input()
                self.Branch_7(user_input)

    def Branch_8(self, user_input):
            if user_input == '1':
                print('\nMILO: Only if we get caught. I’ve done this maybe once or twice, so it should all work out in the end.', end='')
                input()
            elif user_input == '2':
                print('')
            else:
                print('\nMILO: Sorry?\n')
                user_input = input()
                self.Branch_8(user_input)

class Chapter():
    def __init__(self, User, Pts):
        self.player = User
        self.dialogue = Dialogue(User)
        self.house_pts = Pts
        
    def Execute_Main(self):
        #GRYFFINDOR/HUFFLEPUFF/RAVENCLAW PATH
        if self.player.house != 'Slytherin':
            print('')
            print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
            print(' ~    CHAPTER 4: MERLIN\'S LEGACY     ~ ')
            print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ', end=' ')
            input()

            print('\n~After a long day of classes, you go to the library to look for Percival. It doesn’t take you too long to find him\n'
                'sitting at a long table looking earnestly at the contents of a book.~', end='')
            input()
            print('\nPERCIVAL: Ah, I was wondering when you would show up.', end='')
            input()
            print(
            '\n[1] So what’s the deal with this quest you were talking about?\n'
            '[2] What’s that you’re reading?\n'
            )
            user_input = input()
            self.dialogue.Branch_1(user_input)
            print('\nPERCIVAL: You see, I’ve been an explorer my whole life. One of the things I looked forward to the most when\n'
                'I first came to Hogwarts was being able to explore every square-inch of the castle.', end='')
            input()
            print('PERCIVAL: Unfortunately, it seems that no matter how much of the castle you think you’ve seen, there will always\n'
                'be something hidden out of sight.', end='')
            input()
            print('PERCIVAL: I had to learn this the hard way when I gave up on my search for the Chamber of Secrets, but just as\n'
                'that door closed, another one opened.', end='')
            input()
            print('PERCIVAL: I was reading a chapter in “Hogwarts: A History” about a hidden treasure inside the castle, laid away by\n'
                'Merlin himself. Wedged between the pages was this withered parchment that appears to be torn at the bottom. As you\n'
                'can see it says...', end='')
            input()
            print('PERCIVAL: “In the place where all that glitters is gold...”', end='')
            input()
            print('PERCIVAL: “The next step in your journey will be told”', end='')
            input()
            print(
            '\n[1] Do you really think THE Merlin wrote this riddle?\n'
            '[2] It’s a cryptic message in a book. So what?\n'
            )
            user_input = input()
            self.dialogue.Branch_2(user_input)
            print(
            '\n[1]: So where do we start?\n'
            '[2]: ~Say nothing~\n'
            )
            input()
            print('\nPERCIVAL: Think about it. What’s the one place in Hogwarts where “all that glitters is gold?”', end='')
            input()
            print(
            '\n[1] The Astronomy Tower\n'
            '[2] The Girl’s Bathroom\n'
            '[3] The Trophy Room\n'
            )
            user_input = input()
            self.dialogue.Branch_3(user_input)
            print(
            '\n[1] Seems a little dangerous wandering the castle at night.\n'
            '[2] What do we have to lose?\n'
            )
            user_input = input()
            self.dialogue.Branch_4(user_input)
            print('PERCIVAL: We\'ll both see you tonight.', end='')
            input()
            #END PATH



        #SLYTHERIN PATH
        if self.player.house == 'Slytherin':
            print('')
            print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
            print(' ~    CHAPTER 4: MERLIN\'S LEGACY    ~ ')
            print(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
            input()
            print('\n~After a long day of classes, you go to the boathouse where you meet Milo sitting down on the\n'
                'edge of the dock with his feet in the water. He holds a book in his hands.~', end='')
            input()
            print(f"MILO: I’ve been expecting you, {self.player.first_name}. Doesn’t all of your stress just float away when you\n"
                'look out on the water?\n')
            input()
            print(
            '\n[1] So what’s the deal with this quest you were talking about?\n'
            '[2] What’s that you’re reading?\n'
            )
            user_input = input()
            self.dialogue.Branch_5(user_input)
            print('\nMILO: Although of course I didn’t bring you out here to discuss books, but rather the secrets\n'
                'that can be found within. Particularly this parchment that appears to be torn at the top.\n'
                'Here’s what it reads:', end='')
            input()
            print('MILO: “Only an able-bodied should you seek...”', end='')
            input()
            print('MILO: “And all will be revealed with one small peek”', end='')
            input()
            print(
            '\n[1] Sounds vaguely menacing.\n'
            '[2] What am I supposed to make of this?\n'
            )
            user_input = input()
            self.dialogue.Branch_6(user_input)
            print('MILO: If my suspicions are correct, this is a clue that will guide us to Merlin’s hidden treasure inside this very castle.', end='')
            input()
            print('MILO: I always looked up to Merlin as my hero. There are some who forget that he was part of Slytherin house, and he went on\n'
                'to become the greatest sorcerer the world has ever seen.', end='')
            input()
            print('...', end='')
            input()
            print('MILO: Slytherin isn’t what it used to be, and I want to do my part in restoring its legacy by bringing to light what Merlin\n'
                'left behind for us.', end='')
            input()
            print('MILO: I had to come out here to think for a bit, and then it finally came to me and I understood what Merlin was trying to tell us.', end='')
            input()
            print('MILO: He wants us to “seek” something, but he doesn’t say what, except he did since it’s in the word, if you follow me.', end='')
            input()
            print('MILO: If you didn’t know already, the seeker in Quidditch is responsible for catching the Golden Snitch, typically winning the game.', end='')
            input()
            print('MILO: The clue just so happens to be in a book about Quidditch, which tells us that what we need to seek...', end='')
            input()
            print('MILO: Is a seeker.', end='')
            input()
            print('...')
            input()
            print('MILO: Are you still with me after all of this?', end='')
            input()
            print(
            '\n[1] Yeah, sure.\n'
            '[2] Not at all.\n'
            '[3] ~Shrug~\n'
            )
            input()
            print('MILO: What I’m trying to say is that the clue has to do with a seeker who went to Hogwarts around the same time as Merlin.', end='')
            input()
            print('MILO: Where do you think we could possibly find this person?', end='')
            input()
            print(
            '\n[1] The Quidditch Pitch\n'
            '[2] The Dungeons\n'
            '[3] The Trophy Room\n'
            )
            user_input = input()
            self.dialogue.Branch_7(user_input)
            print('MILO: The only tricky bit is that I was banned from the Trophy Room. I won’t get into it at the moment,\n'
                'but none of it was my fault. He had it coming.', end='')
            input()
            print('MILO: This means that we’ll have to go at night.', end='')
            input()
            print(
            '\n[1] Wouldn’t we get into trouble for staying out late?\n'
            '[2] I’m ready if you are.\n'
            )
            user_input = input()
            self.dialogue.Branch_8(user_input)
            print('MILO: Alright. Our quest begins tonight.')
            input()
            #END PATH



        if self.player.house == 'Gryffindor':
            self.house_pts.Add_Gryffindor(0)
            self.house_pts.Add_Hufflepuff(70)
            self.house_pts.Add_Ravenclaw(75)
            self.house_pts.Add_Slytherin(110)
        elif self.player.house == 'Hufflepuff':
            self.house_pts.Add_Gryffindor(75)
            self.house_pts.Add_Hufflepuff(0)
            self.house_pts.Add_Ravenclaw(70)
            self.house_pts.Add_Slytherin(110)
        elif self.player.house == 'Ravenclaw':
            self.house_pts.Add_Gryffindor(75)
            self.house_pts.Add_Hufflepuff(70)
            self.house_pts.Add_Ravenclaw(0)
            self.house_pts.Add_Slytherin(110)
        elif self.player.house == 'Slytherin':
            self.house_pts.Add_Gryffindor(110)
            self.house_pts.Add_Hufflepuff(70)
            self.house_pts.Add_Ravenclaw(75)
            self.house_pts.Add_Slytherin(0)

        self.house_pts.Display_Points()