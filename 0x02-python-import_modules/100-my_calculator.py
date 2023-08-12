#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    ac = len(sys.argv) - 1
    if ac != 3:
        print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
        exit(1)
    operator = {"+":add, "-":sub, "*":mul, "/":div}
    if sys.argv[2] not in operator.keys():
        print(f"Unknown operator. Available operators: +, -, *, /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = operator[sys.argv[2]](a, b)
    print(f"{a} {sys.argv[2]} {b} = {result}")
