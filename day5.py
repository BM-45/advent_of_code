ordering = set()

def isOrdered(nums):

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if (nums[j], nums[i]) in ordering:
                return False
            
    return True

def orderUpdate(nums):
    i = 0
    while i < len(nums):
        updated = False
        for j in range(i+1,len(nums)):
            if (nums[j], nums[i]) in ordering:
                nums[j], nums[i] = nums[i], nums[j]
                updated = True
        if updated == False:
            i += 1
    return nums[len(nums)//2]



with open("day5.txt") as file:
    count = 0
    for line in file:
        nums = line.split("|")
        ordering.add((int(nums[0]), int(nums[1])))

result = 0
result1 = 0
with open("day5_01.txt") as file:
    for line in file:
        nums = [int(i) for i in line.split(",")]
        if isOrdered(nums):
            result += nums[len(nums)//2]
        else:
            result1 += orderUpdate(nums)

print(result)
print(result1)

