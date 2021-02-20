from typing import Any, List, Optional
from enum import Enum, auto, unique

from .auto_name_enum import AutoNameEnum



class Combinations(AutoNameEnum): pass

@unique
class UpperSectionCombinations(Combinations):
    """
    ones: The sum of all dice showing the number 1.
    twos: The sum of all dice showing the number 2.
    threes: The sum of all dice showing the number 3.
    fours: The sum of all dice showing the number 4.
    fives: The sum of all dice showing the number 5.
    sixes: The sum of all dice showing the number 6.
    If a player manages to score at least 63 points (an average of three of each number) in the upper section, they are awarded a bonus of 50 points.
    """
    ones = auto()
    twos = auto()
    threes = auto()
    fours = auto()
    fives = auto()
    sixes = auto()

class LowerSectionCombinations(Combinations):
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
