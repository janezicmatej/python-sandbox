import glob
import importlib
import webbrowser
import pyperclip


def solve(problem_number: int, verbose: bool, copy: bool, open_page: bool) -> None:
    file = glob.glob(f"problems/p{problem_number}.py")
    problem = getattr(
        importlib.import_module(
            file[0].split(".")[0].replace("/", "."),
        ),
        "Main",
    )
    result, time = problem.solve().values()
    if verbose:
        print(f"The result {result} was calculated in {time}ms time.")
    else:
        print(f"{result}, {time}ms")
    if copy:
        pyperclip.copy(result)
    if open_page:
        webbrowser.open(f"https://projecteuler.net/problem={problem_number}")


def solve_all() -> None:
    files = glob.glob(f"problems/p*.py")
    problems = [
        getattr(
            importlib.import_module(
                file.split(".")[0].replace("/", "."),
            ),
            "Main",
        )
        for file in files
    ]
    results = [problem.solve().values() for problem in problems]
    ordered_results = []
    for (result, time), file in zip(results, files):
        problem_number = int(file.split("/")[-1][1:-3])
        ordered_results.append([problem_number, result, time])

    for problem_number, result, time in sorted(ordered_results):
        print(
            f"The result to problem number {problem_number} was {result}. "
            f"It was calculated in {time}ms time."
        )
