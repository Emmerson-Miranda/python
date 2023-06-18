"""
PCAP-31-03 1.2 – Perform evaluations using the math module

    functions: ceil(), floor(), trunc(), factorial(), hypot(), sqrt()
"""
import math


def main():
    print("math.ceil", math.ceil(4.3), math.ceil(4.6))
    print("math.floor", math.floor(4.3), math.floor(4.6))
    print("math.trunc", math.trunc(4.3), math.trunc(4.6))
    print("math.factorial", math.factorial(4))
    print("math.hypot", math.hypot(4, 16))
    print("math.sqrt", math.sqrt(144))
    print("math.pow", math.pow(12,2))

    f = math.cos(math.pi / 4)
    print("math.cos", f)
    print("math.pi", math.pi)


if __name__ == '__main__':
    main()
