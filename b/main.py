import random

from util import *

def draw_round_form(choice: int):

    user_choice = CHOICES[choice]

    bot_choice = random.choice(CHOICES)

    print(f"{user_choice} vs {bot_choice} (Bot) - {COMPARATIVE[user_choice][bot_choice]}")

while True:

    form = [

        (ROCK_CHOICE, draw_round_form),
        (PAPER_CHOICE, draw_round_form),
        (SCISSORS_CHOICE, draw_round_form)
    ]

    draw(form)

    ask(form, 'Introduce que mostrar: ')
