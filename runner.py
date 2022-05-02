#!/usr/bin/env python
import argparse
import glob
import re
import requests


parser = argparse.ArgumentParser(description="project euler runner")
parser.add_argument(
    "-s",
    "--solve",
    dest="solve",
    type=int,
    required=False,
    nargs=1,
    action="store",
    help="problem number",
)

parser.add_argument(
    "-e",
    "--explicit",
    dest="explicit",
    type=int,
    required=False,
    nargs=1,
    action="store",
    help="explicit file to solve",
)

parser.add_argument(
    "-i",
    "--input",
    dest="input",
    type=str,
    required=False,
    nargs=1,
    action="store",
    help="input file",
)

parser.add_argument(
    "-v",
    "--verbose",
    dest="verbose",
    action="store_true",
    required=False,
    help="print verbose result",
)

parser.add_argument(
    "-p",
    "--prepare",
    dest="prepare",
    type=int,
    required=False,
    nargs=1,
    action="store",
    help="problem number",
)

args = parser.parse_args()

if args.solve:
    file = glob.glob(f"problems/p{args.solve[0]}.py")
    if len(file) > 1 and not args.explicit:
        parser.error(
            "There is multiple files for this problem, please use --explicit flag to explicitly name the required file"
        )
    elif args.explicit:
        file = glob.glob(f"problems/p{args.explicit[0]}.py")

    problem = __import__(
        file[0].split(".")[0].replace("/", "."), fromlist=[None]  # type: ignore
    ).Main
    if problem.requires_input() and not args.input:
        parser.error(
            f"Problem #{args.problem[0]} requires an input file. Use --input flag."
        )

    problem.solve(verbose=args.verbose)


if args.prepare:
    problem = re.search(
        r'<div class="problem_content" role="problem">((.*\s)*?)</div>',
        requests.get(f"https://projecteuler.net/problem={args.prepare[0]}").text,
    )
    paragraphs = re.findall(r"<p.*?>(.+)</p>", problem.group(1))

    with open(f"problems/p{args.prepare[0]}.py", "w") as template, open(
        "utils/_template.py", "r"
    ) as _template:
        template.write(f"# Problem number {args.prepare[0]}.\n#\n# ")
        for count, paragraph in enumerate(paragraphs):
            counter = 2
            for word in paragraph.split(" "):
                if counter + len(word) > 88:
                    counter = 3 + len(word)
                    template.write(f"\n# {word} ")
                else:
                    counter += len(word)
                    template.write(word)
                    if counter < 88:
                        template.write(" ")
                        counter += 1
            template.write("\n")
            if not count == len(paragraphs) - 1:
                template.write("#\n# ")

        for line in _template.readlines():
            template.write(line.replace("# type: ignore", ""))
