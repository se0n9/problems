nums = list(map(int, input().split()))
sq_sum = 0
for i in range(len(nums)):
    sq_sum += (nums[i] * nums[i])
print(sq_sum % 10)