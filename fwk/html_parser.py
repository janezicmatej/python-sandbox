import glob
import requests
from string import Template
from bs4 import BeautifulSoup


def prepare_solution_file(
    problem_number: int, forced: bool = False, input_subclass: bool = False
) -> None:
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
        "parent_classes": "Problem"
        if not (href or input_subclass)
        else "Problem, Input",
    }

    lines: list[str] = []
    for line in problem_body.text.split("\n"):
        if len(line) < 86:
            lines.append(line)
            continue
        current_line: list[str] = []
        for word in line.split():
            if len(" ".join(current_line + [word])) > 86:
                lines.append(" ".join(current_line))
                current_line = [word]
            else:
                current_line += [word]
        lines.append(" ".join(current_line))

    if not lines[-1]:
        lines = lines[:-1]

    with open(f"problems/p{problem_number}.py", "w") as template, open(
        "fwk/main_template.txt", "r"
    ) as _template, open("fwk/input_template.txt", "r") as input_template:
        print(f"# Problem number {problem_number}", file=template)
        for line in lines:
            if line:
                print("# " + line, file=template)
            else:
                print("#", file=template)

        src = Template(_template.read())
        result = src.substitute(template_dict)
        print(result, file=template)

        if href or input_subclass:
            print(file=template)
            input_src = Template(input_template.read())
            input_result = input_src.substitute(template_dict)
            print(input_result, file=template)
