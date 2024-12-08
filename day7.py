def newOperator(num1, num2):
    return int(str(num1) + str(num2))

def isAchievable(target, nums):
    if len(nums) == 0:
        return target == 0
    
    if len(nums) == 1:
        return target == nums[0]
    
    num1 = nums[-1]
    num2 = nums[-2]
    sumVar = num1 + num2
    productVar = num1 * num2
    newOper = newOperator(num1, num2)


    nums_sum = nums[:-2] + [sumVar]
    nums_product = nums[:-2] + [productVar]
    nums_newOperator = nums[:-2] + [newOper]

    return isAchievable(target, nums_sum) or isAchievable(target, nums_product) or isAchievable(target, nums_newOperator)

result = 0
with open("day7.txt") as file:
    for line in file:
        data = line.strip().split(":")
        target = int(data[0])
        nums = [int(i) for i in reversed(data[1].split())]
        if isAchievable(target, nums):
            result += target

print(result)