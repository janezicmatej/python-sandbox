import glob
import requests
from string import Template
from bs4 import BeautifulSoup


def prepare_solution_file(problem_number: int, forced: bool = False) -> None:
    if glob.glob(f"problems/p{problem_number}.py") and not forced:
        raise FileExistsError("There is already a file for that problem")
    parsed_html = BeautifulSoup(
        requests.get(f"https://projecteuler.net/problem={problem_number}").content,
        features="html.parser",
    )
    problem_body = parsed_html.body.find("div", attrs={"class", "problem_content"})
    href = problem_body.find("a", href=True)
    if href:
        with open(f"inputs/p{problem_number}.txt", "w") as problem_input:
            problem_input.write(
                requests.get(f"https://projecteuler.net/{href['href']}").text
            )

    template_dict: dict[str, str] = {
        "return_type": "int",
        "parent_classes": "Problem" if not href else "Problem, Input",
    }
    with open(f"problems/p{problem_number}.py", "w") as template, open(
        "fwk/template.txt", "r"
    ) as _template:
        print(f"# Problem number {problem_number}", file=template)
        for line in problem_body.text.split("\n"):
            print("# " + line, file=template)
        src = Template(_template.read())
        result = src.substitute(template_dict)
        print(result, file=template)
