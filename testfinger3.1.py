#!/usr/bin/env python3
from findARoot import findARoot

def check(value, answer):
    assert(findARoot(value) == answer)

check(49,[7,2])
check(0, [0,2])
check(1, [1,2])
check(2, [])
check(3, [])
check(4, [2,2])
check(5, [])
check(6, [])
check(7, [])
check(8, [2,3])
check(9, [3,2])
check(-1, [-1,3])
check(-2, [])
check(-3, [])
check(-4, [])
check(-5, [])
check(-6, [])
check(-7, [])
check(-8, [-2,3])
check(-9, [])
check(-32, [-2,5])
check(64, [4,3])



print('All pass')