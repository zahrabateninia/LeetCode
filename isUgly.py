#!/usr/bin/env python3

# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.

import sys

def is_ugly(n: int) -> bool:
    if n <= 0:
        return False

    for factor in (2, 3, 5):
        while n % factor == 0:
            n //= factor

    return n == 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./isUgly.py <number>")
        sys.exit(1)

    n = int(sys.argv[1])
    print(is_ugly(n))
