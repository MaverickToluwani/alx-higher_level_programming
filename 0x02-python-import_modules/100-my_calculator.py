#!/usr/bin/python3
import sys
from calculator_1 import add, sub, div, mul

if __name__ == "__main__":
    def calculator():
        usg = "Usage: ./100-my_calculator.py <a> <operator> <b>\n"
        msg = "Unknown operator. Available operators: +, -, * and /\n"
        if len(sys.argv)-1 != 3:
            sys.stderr.write(usg)
            sys.exit(1)

        a = int(sys.argv[1])
        b = int(sys.argv[3])
        sign = sys.argv[2]
        if sign == "+":
            return"{} {} {} = {} ".format(a, sign, b, add(a, b))
        elif sign == "-":
            return "{} {} {} = {} ".format(a, sign, b, sub(a, b))
        elif sign == "":
            return "{} {} {} = {} ".format(a, sign, b, mul(a, b))
        elif sign == "/":
            return "{} {} {} = {} ".format(a, sign, b, div(a, b))
        else:
            sys.stderr.write(msg)
            sys.exit(1)

    print(calculator())
