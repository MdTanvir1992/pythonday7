

# word_list = ["advark", "baboon", "camel"]
# import random
# chosen_word = random.choice(word_list)
# guess = input("Guess a letter: ").lower()
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")
#



# word_list = ["advark", "baboon", "camel"]
# import random
# chosen_word = random.choice(word_list)
# print(f'Pssst, the solution is {chosen_word}.')
# guess = input("Guess a letter: ").lower()
# display = []
# word_length = len(chosen_word)
# for _ in range(word_length):
#     display += "_"
# print(display)
# for position in range(word_length):
#     letter = chosen_word[position]
#     if letter == guess:
#         display[position] = letter
# print(display)




#
# word_list = ["advark", "baboon", "camel"]
#
# import random
# chosen_word = random.choice(word_list)
# print(f'Pssst, the solution is {chosen_word}.')
#
# display = []
# word_length = len(chosen_word)
# for _ in range(word_length):
#         display += "_"
#
# end_of_game = False
#
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#
#
#     for position in range(word_length):
#         letter = chosen_word[position]
#         # print(f"Current position: {position}\n"
#         #       f"Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#     print(display)
#
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")


#
#
#
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
#
# word_list = ["advark", "baboon", "camel"]
#
# import random
# chosen_word = random.choice(word_list)
# print(f'Pssst, the solution is {chosen_word}.')
# lives = 6
# display = []
# word_length = len(chosen_word)
# for _ in range(word_length):
#         display += "_"
#
# end_of_game = False
#
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#
#
#     for position in range(word_length):
#         letter = chosen_word[position]
#         # print(f"Current position: {position}\n"
#         #       f"Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#
#     if guess not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")
#
#     print(f"{' '.join(display)}")
#
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
#     print(stages[lives])
#
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


word_list = [
'abruptly',
'absurd',
'abyss',
'affix',
'askew',
'avenue',
'awkward',
'axiom',
'azure',
'bagpipes',
'bandwagon',
'banjo',
'bayou',
'beekeeper',
'bikini',
'blitz',
'blizzard',
'boggle',
'bookworm',
'boxcar',
'boxful',
'buckaroo',
'buffalo',
'buffoon',
'buxom',
'buzzard',
'buzzing',
'buzzwords',
'caliph',
'cobweb',
'cockiness',
'croquet',
'crypt',
'curacao',
'cycle',
'daiquiri',
'dirndl',
'disavow',
'dizzying',
'duplex',
'dwarves',
'embezzle',
'equip',
'espionage',
'euouae',
'exodus',
'faking',
'fishhook',
'fixable',
'fjord',
'flapjack',
'flopping',
'fluffiness',
'flyby',
'foxglove',
'frazzled',
'frizzled',
'fuchsia',
'funny',
'gabby',
'galaxy',
'galvanize',
'gazebo',
'giaour',
'gizmo',
'glowworm',
'glyph',
'gnarly',
'gnostic',
'gossip',
'grogginess',
'haiku',
'haphazard',
'hyphen',
'iatrogenic',
'icebox',
'injury',
'ivory',
'ivy',
'jackpot',
'jaundice',
'jawbreaker',
'jaywalk',
'jazziest',
'jazzy',
'jelly',
'jigsaw',
'jinx',
'jiujitsu',
'jockey',
'jogging',
'joking',
'jovial',
'joyful',
'juicy',
'jukebox',
'jumbo',
'kayak',
'kazoo',
'keyhole',
'khaki',
'kilobyte',
'kiosk',
'kitsch',
'kiwifruit',
'klutz',
'knapsack',
'larynx',
'lengths',
'lucky',
'luxury',
'lymph',
'marquis',
'matrix',
'megahertz',
'microwave',
'mnemonic',
'mystify',
'naphtha',
'nightclub',
'nowadays',
'numbskull',
'nymph',
'onyx',
'ovary',
'oxidize',
'oxygen',
'pajama',
'peekaboo',
'phlegm',
'pixel',
'pizazz',
'pneumonia',
'polka',
'pshaw',
'psyche',
'puppy',
'puzzling',
'quartz',
'queue',
'quips',
'quixotic',
'quiz',
'quizzes',
'quorum',
'razzmatazz',
'rhubarb',
'rhythm',
'rickshaw',
'schnapps',
'scratch',
'shiv',
'snazzy',
'sphinx',
'spritz',
'squawk',
'staff',
'strength',
'strengths',
'stretch',
'stronghold',
'stymied',
'subway',
'swivel',
'syndrome',
'thriftless',
'thumbscrew',
'topaz',
'transcript',
'transgress',
'transplant',
'triphthong',
'twelfth',
'twelfths',
'unknown',
'unworthy',
'unzip',
'uptown',
'vaporize',
'vixen',
'vodka',
'voodoo',
'vortex',
'voyeurism',
'walkway',
'waltz',
'wave',
'wavy',
'waxy',
'wellspring',
'wheezy',
'whiskey',
'whizzing',
'whomever',
'wimpy',
'witchcraft',
'wizard',
'woozy',
'wristwatch',
'wyvern',
'xylophone',
'yachtsman',
'yippee',
'yoked',
'youthful',
'yummy',
'zephyr',
'zigzag',
'zigzagging',
'zilch',
'zipper',
'zodiac',
'zombie',
]







import random

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []

for _ in range(word_length):
        display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()
    if guess is display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        game_is_finished = True
        print("You win.")
    print(stages[lives])