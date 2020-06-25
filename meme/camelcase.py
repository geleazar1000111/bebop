import click
import random

random.seed()


def change_letter(char, state):
    if state == 0:
        return char.upper()
    else:
        return char.lower()


def switch_state(state):
    if state == 0:
        return 1
    else:
        return 0


def get_char_state(char):
    if char.islower():
        return 0 * random.randint(0, 1) + random.randint(0, 1)
    else:
        return 1 * random.randint(0, 1)


@click.command()
@click.argument('input_string')
def generate_camelcase(input_string):
    camel_word = ""
    init_state = get_char_state(input_string[0])
    camel_word += change_letter(input_string[0], init_state)
    state = switch_state(init_state)
    for char in input_string[1:]:
        if char.isalpha():
            char = change_letter(char, state)
            state = switch_state(state)
        camel_word += char
    print(camel_word)
    return camel_word


if __name__ == "__main__":
    generate_camelcase()
