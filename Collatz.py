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

# Populate cache with cycle length of 1 (1) 
# Because the while loop will not execute with a value of 1
maxes_dict = {1: 1}

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

    # Confirm inputs are positive
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

    # Store all cycle lengths in interval
    lengths_list = []

    for x in range(i, j+1):

        assert x > 0

        y = x

        opti_check = optimize(x)

        # Use values stored in cache if possible
        if opti_check:
            lengths_list.append(maxes_dict[x])

        else:
            
            # Store all instances of y in loop
            # The total number of instances is the cycle length
            cycle_list = [y]
            
            while y != 1:
            
                if y % 2 == 0:
                    y = y / 2
                    cycle_list.append(y)
            
                else:
                    y = (3 * y) + 1
                    cycle_list.append(y)

            # Confirm cycle length is greater than zero
            assert len(cycle_list) > 0
            length = len(cycle_list)
            lengths_list.append(length)

            # Store cycle length of x in cache
            if len(maxes_dict) < 10000:
                maxes_dict[x] = length

    # Return greatest cycle length in interval
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
