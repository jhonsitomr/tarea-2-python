from util import *

fail = 0

word, mask = generate()

while True:

    print(HUMAN[fail])

    response = input(f'Introduce una letra (palabra: {mask} letras): ')

    for a, b in zip(response, word):

        if a == b:

            print(f'"{a}" si se encuentra en la palabra')
        else:

            print(f'"{a}" no se encuentra en la palabra')

            fail += 1

            break

    if fail > len(HUMAN):

        print('PIERDES')

        break

    if response == word:

        print('GANAS')

        break
