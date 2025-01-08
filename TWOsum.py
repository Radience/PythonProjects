print("----------TWO SUM--------------")

nums = [3,2,4]
target = 6
for x in range(len(nums)):
    if target - nums[x] in nums[x+1:len(nums)]:
        print([x, nums.index(target - nums[x], x+1, len(nums))])
        break

outputList = [[x, nums.index(target - nums[x], x+1, len(nums))] for x in range(len(nums)) if target - nums[x] in nums[x+1:len(nums)]]
print(outputList)

print("-------------------------------")
