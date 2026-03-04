nums = [int(input()) for _ in range(9)]
best = max(nums)
print(best)
print(nums.index(best) + 1)