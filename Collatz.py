#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

global maxes_dict

maxes_dict = {1: 1}     # Populate with cycle length for 1 because while loop will not execute for 1

def optimize(num):
    if num in maxes_dict:
        return True
    else:
        return False


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()

    assert int(a[0]) > 0        # Confirm inputs are positive
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

    lengths_list = []   # Store all cycle lengths in interval

    for x in range(i, j+1):

        assert x > 0

        y = x

        opti_check = optimize(x)

        if opti_check:      # Use values stored in cache if possible
            lengths_list.append(maxes_dict[x])

        else:
            
            cycle_list = [y]    # The length of cycle_list will be the cycle length
            
            while y != 1:
            
                if y % 2 == 0:
                    y = y / 2
                    cycle_list.append(y)
            
                else:
                    y = (3 * y) + 1
                    cycle_list.append(y)

            assert len(cycle_list) > 0      # Confirm cycle length is greater than zero
            length = len(cycle_list)
            lengths_list.append(length)

            if len(maxes_dict) < 10000:     # Store cycle length for x in cache
                maxes_dict[x] = length

    return max(lengths_list)    # Return greatest cycle length in interval
   
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
