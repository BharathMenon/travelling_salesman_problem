"""
run program
"""
from tsp import run_interactive, run
from sys import argv

if len(argv) > 1 and argv[1] == "--interactive":
    run_interactive()
else:
    run()
