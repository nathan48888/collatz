#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()

    assert int(a[0]) > 0
    assert int(a[1]) > 0

    lst = [int(a[0]), int(a[1])]
    
    return sorted(lst)

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    lengths_list = []

    for x in range(i, j+1):

        assert x > 0
        
        cycle_list = [x]
        
        while x != 1:
        
            if x % 2 == 0:
                x = x / 2
                cycle_list.append(x)
        
            else:
                x = (3 * x) + 1
                cycle_list.append(x)

        length = len(cycle_list)
        lengths_list.append(length)


    return max(lengths_list)

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
