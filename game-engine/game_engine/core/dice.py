from typing import Tuple
from enum import IntEnum


class Dice(IntEnum):
    """
    Six sided classic dice.
    ⚀ ⚁ ⚂ ⚃ ⚄ ⚅
    """

    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6


Roll = Tuple[
    Dice, Dice, Dice, Dice, Dice,
]

dice_characters = {
    Dice.one: "⚀",
    Dice.two: "⚁",
    Dice.three: "⚂",
    Dice.four: "⚃",
    Dice.five: "⚄",
    Dice.six: "⚅",
}
