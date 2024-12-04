def isItSafe(nums, safe=3):
    if nums[0] > nums[1]:
        for i in range(len(nums)-1):
            if not (1 <= (nums[i] - nums[i+1]) <= safe):
                return False
    else:
        if nums[0] < nums[1]:
            for i in range(len(nums)-1):
                if not (1 <= (nums[i+1] -  nums[i]) <= safe):
                    return False
        else:
            return False
    return True

def isItSafeWithTweak(nums, safe=3):
    for i in range(0, len(nums)):
            if isItSafe(nums[:i] + nums[i+1:]) == True:
                return True
    return False


with open("day2.txt",'r') as file:
    result = 0
    for line in file:
        line = line.strip()
        if isItSafe([int(i) for i in line.split()]) or isItSafeWithTweak([int(i) for i in line.split()]):
            result += 1

    print(result)
        
        

