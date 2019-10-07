import sys

for num in sys.stdin:
    if int(num) == 42:
        break
    else:
        print(num)
