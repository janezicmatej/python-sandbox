# Problem number 22
#
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing
# over five-thousand first names, begin by sorting it into alphabetical order. Then
# working out the alphabetical value for each name, multiply this value by its
# alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3
# + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score
# of 938 × 53 = 49714.
# What is the total of all the name scores in the file?
from fwk.solution import Problem, Input


class Main(Problem, Input):
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    @classmethod
    def solution(cls) -> int:
        translator = {k: v for v, k in enumerate(cls.ALPHABET.upper(), 1)}
        count = 0
        for place, word in enumerate(sorted(cls.parse_input(22)[0]), 1):
            count += place * sum([translator[i] for i in word])
        return count

    @classmethod
    def parse_line(cls, line: str) -> list[str]:
        return line.replace('"', "").split(",")
