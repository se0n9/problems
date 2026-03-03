import sys
N = int(input())
if N < 1 or N > 9:
    sys.exit()
else:
    for i in range(9):
        result = N * (i+1)
        print(f"{N} * {i+1} = {result}")