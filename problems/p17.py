# Problem number 17
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
# there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of
# "and" when writing out numbers is in compliance with British usage.
from fwk.solution import Problem
import inflect


class Main(Problem):
    @classmethod
    def solution(cls) -> int:
        p = inflect.engine()
        lengths_sum = 0
        for i in range(1, 1001):
            word = p.number_to_words(i)
            if not isinstance(word, str):
                continue
            lengths_sum += len(word.replace(" ", "").replace("-", ""))

        return lengths_sum
