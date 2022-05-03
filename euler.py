#!/usr/bin/env python
import argparse
import webbrowser
from fwk import solver, html_parser


parser = argparse.ArgumentParser(description="project euler cli")
parser.add_argument("--debug", action="store_true", help="print debug info")

subparsers = parser.add_subparsers(dest="command")

solve = subparsers.add_parser("solve", help="solve problem")
solve.add_argument(
    "problem", metavar="n", type=int, nargs=1, help="solve problem with given problem"
)
solve.add_argument(
    "-v", "--verbose", dest="verbose", action="store_true", help="print verbose result"
)
solve.add_argument(
    "-o", "--open", dest="open", action="store_true", help="open problem page"
)
solve.add_argument(
    "-c", "--copy", dest="copy", action="store_true", help="copy solution to clipboard"
)

prepare = subparsers.add_parser("prepare", help="prepare solution file")
prepare.add_argument(
    "problem", metavar="n", type=int, nargs=1, help="prepare file with given problem"
)
prepare.add_argument(
    "-f", "--force", dest="force", action="store_true", help="override solution file"
)

open_page = subparsers.add_parser("open", help="open problem page")
open_page.add_argument(
    "problem", metavar="n", type=int, nargs=1, help="open page with given problem"
)

args = parser.parse_args()

match args.command:
    case "solve":
        solver.solve(
            problem_number=args.problem[0],
            verbose=args.verbose,
            copy=args.copy,
            open_page=args.open,
        )

    case "prepare":
        try:
            html_parser.prepare_solution_file(
                problem_number=args.problem[0], forced=args.force
            )
        except FileExistsError as e:
            parser.error(str(e))

    case "open":
        webbrowser.open(f"https://projecteuler.net/problem={args.problem[0]}")
