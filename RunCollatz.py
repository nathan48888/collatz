#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C)
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

from Collatz import collatz_solve

# ----
# main
# ----

if __name__ == "__main__":
    collatz_solve(sys.stdin, sys.stdout)

""" #pragma: no cover
$ cat RunCollatz.in
1 10
100 200
201 210
900 1000



$ python RunCollatz.py < RunCollatz.in > RunCollatz.out

$ cat RunCollatz.out
1 10 1
100 200 1
201 210 1
900 1000 1



$ python -m pydoc -w Collatz"
# That creates the file Collatz.html
"""
         

'''
                                                    cProfile output

         3 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 Collatz.py:15(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''


