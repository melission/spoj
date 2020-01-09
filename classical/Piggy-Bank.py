# https://www.spoj.com/problems/PIGBANK/
import sys
test_cases = int(input().strip())

for _ in range(test_cases):
    e, f = input().split()
    e, f = int(e), int(f)
    mass = f - e
    coins = {}
    numcoins = int((input().strip()))
    for _ in range(numcoins):
        for line in sys.stdin:
