import sys
n = int(input())
if n < 1 or n > 4000:
    sys.exit()
else:
    if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
        print(1)
    else:
        print(0)