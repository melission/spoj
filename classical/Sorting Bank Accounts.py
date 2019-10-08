# https://www.spoj.com/problems/SBANK/

import sys

bank_acc = {}
for line in sys.stdin:
    if len(line) > 30:
        if line not in bank_acc:
            bank_acc[line] = 1
        if line in bank_acc:
            bank_acc[line] += 1
    if len(line) == 0:

