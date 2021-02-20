from auto_name_enum import AutoNameEnum


class Dice(AutoNameEnum):
    """
    Six sided classic dice.
    ⚀ ⚁ ⚂ ⚃ ⚄ ⚅
    """
    one = auto()
    two = auto()
    three = auto()
    four = auto()
    five = auto()
    six = auto()


dice_characters = {
    Dice.one: "⚀",
    Dice.two: "⚁",
    Dice.three: "⚂",
    Dice.four: "⚃",
    Dice.five: "⚄",
    Dice.six: "⚅",
}
