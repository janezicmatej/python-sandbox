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
