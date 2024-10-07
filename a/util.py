import random

WORDS = ["saludo", "arroz", "cielo", "aire", "fuego"]

HUMAN = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
    '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========
''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
]

def generate():
    word = random.choice(WORDS)

    mask = ''

    for latter in word:

        match random.randint(0, 1):

            case 0:

                mask += latter

            case 1:

                mask += '_'

    return word, mask
