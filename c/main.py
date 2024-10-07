from util import *

def draw_meters_to_feet_form():

    try:

        num = input('Introduce la cifra a convertir de metros a pies: ')

        num = int(num)

        res = num * 3.281

        print(f'Conversion: {res}')
    except ValueError:

        print('ERR: Introduce una eleccion valida')

def draw_feet_to_meters_form():
    try:

        num = input('Introduce la cifra a convertir de pies a metros: ')

        num = int(num)

        res = num / 3.281

        print(f'Conversion: {res}')
    except ValueError:

        print('ERR: Introduce una eleccion valida')

def draw_distance_form():

    form = [

        ('Metros a pies', draw_meters_to_feet_form),
        ('Pies a metros', draw_feet_to_meters_form)
    ]

    draw(form)

    ask(form, 'Introduce a que forma convertir: ')

def draw_kilograms_to_pounds_form():

    try:

        num = input('Introduce la cifra a convertir de kilogramos a libras: ')

        num = int(num)

        res = num * 2.205

        print(f'Conversion: {res}')
    except ValueError:

        print('ERR: Introduce una eleccion valida')

def draw_pounds_to_kilograms_form():

    try:

        num = input('Introduce la cifra a convertir de libras a kilogramos: ')

        num = int(num)

        res = num / 2.205

        print(f'Conversion: {res}')
    except ValueError:

        print('ERR: Introduce una eleccion valida')

def draw_weight_form():

    form = [

        ('Kilogramos a libras', draw_kilograms_to_pounds_form),
        ('Libras a kilogramos', draw_pounds_to_kilograms_form)
    ]

    draw(form)

    ask(form, 'Introduce a que forma convertir: ')

def draw_cubic_centimeters_to_ounces_form():

    try:

        num = input('Introduce la cifra a convertir de onzas a centimetros cubicos: ')

        num = int(num)

        res = num * 29.574

        print(f'Conversion: {res}')
    except ValueError:

        print('ERR: Introduce una eleccion valida')

def draw_ounces_to_cubic_centimeters_form():

    try:

        num = input('Introduce la cifra a convertir de centimetros cubicos a onzas: ')

        num = int(num)

        res = num / 29.574

        print(f'Conversion: {res}')
    except ValueError:

        print('ERR: Introduce una eleccion valida')

def draw_volume_form():

    form = [

        ('Centimetros cubicos a onzas', draw_cubic_centimeters_to_ounces_form),
        ('Onzas a centimetros cubicos', draw_ounces_to_cubic_centimeters_form)
    ]

    draw(form)

    ask(form, 'Introduce a que forma convertir: ')

def draw_celsius_to_fahrenheit_form():

    try:

        num = input('Introduce la cifra a convertir de celsius a fahrenheit: ')

        num = int(num)

        res = num * (9 / 5)

        res = res + 32

        print(f'Conversion: {res}')
    except ValueError:

        print('ERR: Introduce una eleccion valida')

def draw_fahrenheit_to_celsius_form():
    try:

        num = input('Introduce la cifra a convertir de celsius a fahrenheit: ')

        num = int(num)

        res = num - 32

        res = res * (5 / 9)

        print(f'Conversion: {res}')
    except ValueError:

        print('ERR: Introduce una eleccion valida')

def draw_temperature_form():

    form = [

        ('Celsius a fahrenheit', draw_celsius_to_fahrenheit_form),
        ('Fahrenheit a celsius', draw_fahrenheit_to_celsius_form)
    ]

    draw(form)

    ask(form, 'Introduce a que forma convertir: ')

while True:

    form = [

        ('DISTANCIA', draw_distance_form),
        ('PESO', draw_weight_form),
        ('VOLUMEN', draw_volume_form),
        ('TEMPERATURA', draw_temperature_form)
    ]

    draw(form)

    ask(form, 'Introduce el modo a convertir: ')
