from collections import Counter


list1 = []
list2 = []
result = 0
def total_distance(list1,list2):
    list1.sort()
    list2.sort()
    distance = 0
    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i])

    return distance

def similarity_score(list1, list2):
    freq = Counter(list2)
    score = 0
    for i in list1:
        score += i*freq[i]

    return score


with open("day1.txt") as file:
    for line in file:
        nums = line.split()
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))
    
result = total_distance(list1, list2)
result1 = similarity_score(list1, list2)
print(result)
print(result1)

