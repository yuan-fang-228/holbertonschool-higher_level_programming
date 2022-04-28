#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            print(f"{a} + {b} = {add(a, b)}")
            exit(0)
        if sys.argv[2] == "-":
            print(f"{a} - {b} = {sub(a, b)}")
            exit(0)
        if sys.argv[2] == "*":
            print(f"{a} * {b} = {mul(a, b)}")
            exit(0)
        if sys.argv[2] == "/":
            print(f"{a} / {b} = {div(a, b)}")
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
