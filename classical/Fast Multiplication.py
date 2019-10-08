# https://www.spoj.com/problems/MUL/
import sys

miltcount = int(input())
for line in sys.stdin:
    frst, scnd = line.split()
    print(int(frst)*int(scnd))
