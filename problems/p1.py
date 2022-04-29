from utils.problem import Problem


class Main(Problem):

    input_file: bool = True

    @staticmethod
    def solution() -> int:
        return sum([x if x % 3 == 0 or x % 5 == 0 else 0 for x in range(1, 1000)])
