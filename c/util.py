from typing import Callable

def draw(form: list[tuple[str, Callable]]):

    for ind, choice in enumerate(form):

        title, _ = choice

        print(f'{ind}. {title}')

def ask(form: list[tuple[str, Callable]], __prompt: object = ""):

    try:

        choice = input(__prompt)

        choice = int(choice)

        if 0 <= choice < len(form):

            _, callback = form[choice]

            callback(choice)

        else:

            print('ERR: Introduce una eleccion mostrada')
    except ValueError:

        print('ERR: Introduce una eleccion valida')
