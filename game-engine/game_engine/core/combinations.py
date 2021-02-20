from typing import Any, List, Optional
from enum import Enum, auto, unique
from collections import Counter

from .auto_name_enum import AutoNameEnum
from .dice import Roll, Dice


class Combinations(Enum):
    pass


@unique
class UpperSectionCombinations(int, Combinations):
    """
    ones: The sum of all dice showing the number 1.
    twos: The sum of all dice showing the number 2.
    threes: The sum of all dice showing the number 3.
    fours: The sum of all dice showing the number 4.
    fives: The sum of all dice showing the number 5.
    sixes: The sum of all dice showing the number 6.
    If a player manages to score at least 63 points
    (an average of three of each number) in the upper section,
    they are awarded a bonus of 50 points.
    """

    ones = 1
    twos = 2
    threes = 3
    fours = 4
    fives = 5
    sixes = 6


class LowerSectionCombinations(AutoNameEnum, Combinations):
    """
    One Pair: Two dice showing the same number. Score: Sum of those two dice.
    Two Pairs: Two different pairs of dice. Score: Sum of dice in those two pairs.
    Three of a Kind: Three dice showing the same number. Score: Sum of those three dice.
    Four of a Kind: Four dice with the same number. Score: Sum of those four dice.
    Small Straight: The combination 1-2-3-4-5. Score: 15 points (sum of all the dice).
    Large Straight: The combination 2-3-4-5-6. Score: 20 points (sum of all the dice).
    Full House: Any set of three combined with a different pair. Score: Sum of all the dice.
    Chance: Any combination of dice. Score: Sum of all the dice.
    Yatzy: All five dice with the same number. Score: 50 points.
    """

    one_pair = auto()
    two_pairs = auto()
    three_of_a_kind = auto()
    four_of_a_kind = auto()
    small_straight = auto()
    large_straight = auto()
    full_house = auto()
    chance = auto()
    yatzy = auto()


def count_die(dice: Roll, kind_count: int, combination_count: int) -> bool:
    return (
        len([count for count in Counter(dice).values() if count > kind_count])
        >= combination_count
    )


def has_upper_section(dice: Roll, kind: Dice) -> bool:
    return kind in dice


def has_one_pair(dice: Roll) -> bool:
    return count_die(dice, 2, 1)


def has_two_pairs(dice: Roll) -> bool:
    return count_die(dice, 2, 2)


def has_three_pairs(dice: Roll) -> bool:
    return count_die(dice, 2, 3)


def has_three_of_a_kind(dice: Roll):
    return count_die(dice, 3, 1)


def has_four_of_a_kind(dice: Roll):
    return count_die(dice, 4, 1)


def has_yatzy(dice: Roll):
    return count_die(dice, 5, 1)


def has_full_house(dice: Roll):
    return count_die(dice, 2, 1) and count_die(dice, 3, 1)


def has_small_straight(dice: Roll):
    return sorted(dice) == (1, 2, 3, 4, 5)


def has_large_straight(dice: Roll):
    return sorted(dice) == (2, 3, 4, 5, 6)


def has_chance(dice: Roll):
    return True
