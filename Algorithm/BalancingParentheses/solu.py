import math
import os
import random
import re
import sys


def getMin(s):
    stack = []
    table = {')': '('}

    length = 0
    for char in s:
        if char not in table:
            stack.append(char)
        elif len(stack) == 0:
            length += 1
        else:
            stack.pop()

    return len(stack) + length


if __name__ == '__main__':
    with open('test_input.txt', 'r') as input_file:
        test_case = int(input_file.readline())
        for _ in range(test_case):
            parenthesis = input_file.readline().strip()
            print(getMin(parenthesis))

