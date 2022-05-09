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
        print(f"#{problem_number} - time: {'{:f}'.format(time)}ms, result: {result}")
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

    max_len = len(str(max([i[0] for i in ordered_results])))
    for p_n, r, t in sorted(ordered_results):
        p_n_str = "0" * (max_len - len(str(p_n))) + str(p_n)
        print(f"#{p_n_str} - time: {'{:f}'.format(t)}ms, result: {r}")
