import math
import os
import random
import re
import sys


def countSwaps(a):
    # Write your code here
    swap = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap += 1
    print("Array is sorted in " + str(swap) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
