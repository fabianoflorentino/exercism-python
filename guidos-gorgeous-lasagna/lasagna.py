"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(pass_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - pass_time


def preparation_time_in_minutes(layers):
    """Calculate the preparation time.

    :param layers: int - number of layers of lasagna.
    :return: int - preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers of lasagna as an argument and
    returns how many minutes the lasagna needs to be prepared based on the
    'PREPARATION_TIME' per layer.
    """
    return PREPARATION_TIME * layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time.

    :param number_of_layers: int - the number of layers added to the lasagna.
    :param elapsed_bake_time: int - the number of minutes the lasagna has been
                                    baking in the oven

    :return: int - the total number of minutes you've been cooking

    This function should return the total number of minutes you've been cooking,
    or the sum of your preparation time and the time the lasagna has already
    spent baking in the oven.
    """
    return (PREPARATION_TIME * number_of_layers) + elapsed_bake_time
