from typing import Callable

ROCK_CHOICE = "PIEDRA"
PAPER_CHOICE = "PAPEL"
SCISSORS_CHOICE = "TIJERA"

CHOICES = [

    ROCK_CHOICE,
    PAPER_CHOICE,
    SCISSORS_CHOICE
]

COMPARATIVE = {

    ROCK_CHOICE: {

        ROCK_CHOICE: "EMPATAS",
        PAPER_CHOICE: "PIERDES",
        SCISSORS_CHOICE: "GANAS"
    },

    PAPER_CHOICE: {

        ROCK_CHOICE: "GANAS",
        PAPER_CHOICE: "EMPATAS",
        SCISSORS_CHOICE: "PIERDES"
    },

    SCISSORS_CHOICE: {

        ROCK_CHOICE: "PIERDES",
        PAPER_CHOICE: "GANAS",
        SCISSORS_CHOICE: "EMPATAS"
    }
}

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
