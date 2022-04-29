#!/usr/bin/env python
import argparse
import glob


parser = argparse.ArgumentParser(description="project euler runner")
parser.add_argument(
    "-n",
    "--number",
    dest="problem",
    type=int,
    required=True,
    nargs=1,
    action="store",
    help="problem number",
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
    "-pr",
    "--print-result",
    dest="print",
    action="store_true",
    required=False,
    help="print the result",
)

args = parser.parse_args()
file = glob.glob(f"problems/p{args.problem[0]}.py")
if len(file) > 1:
    parser.error(
        "There is multiple files for this problem, please use -e flag to explicitly name the required file"
    )

problem = __import__(file[0].split(".")[0].replace("/", "."), fromlist=[None]).Main  # type: ignore
if problem.requires_input() and not args.input:
    parser.error(
        f"Problem #{args.problem[0]} requires an input file. Use -i INPUT flag."
    )

result = problem.solution()
if args.print:
    print(f"Solution to problem #{args.problem[0]} is: " + str(result))
