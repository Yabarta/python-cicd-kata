import random


def get_dice_roll() -> int:
    return random.randint(1, 6) + 4  # noqa: S311
