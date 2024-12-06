from itertools import permutations
import math
import copy

matrix = []
with open("day6.txt") as file:
    for line in file:
        row = list(line.strip())  # Split line into characters
        matrix.append(row)

print(len(matrix), len(matrix[0]))

# Part I
# distinct positions along the path.

# find the starting position.
startX, startY = 0, 0

for i in range(len(matrix)):
    for j in range(len(matrix[1])):
        if matrix[i][j] == '^':
            startX, startY = i, j
            break
iniX, iniY = startX, startY
print(startX, startY)


directions = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}
direction = 0
distinct = set()
distinct.add((startX, startY))
#matrix[startX][startY] = 'X'
positions = 1
#obstructions = set()

while 0 <= startX < len(matrix) and 0 <= startY < len(matrix[0]):
    newX, newY = startX + directions[direction][0], startY + directions[direction][1]
    if 0 <= newX < len(matrix) and 0 <= newY < len(matrix[0]):
        if matrix[newX][newY] == '#':
            direction = (direction +1)%4
            #obstructions.add((newX, newY))
            
        else:
            if (newX, newY) not in distinct:
                positions += 1
                distinct.add((newX, newY))
                #matrix[newX][newY] = 'X'
            startX, startY = newX, newY
    else:
        break

    
print("No of unique positions",positions)


print("------------------------------------------------------------------------------------------------------------------------------")



# Part II.
# Dumb solution
##########################

count = 0
def inLoop(matrix):
    
    startX, startY = iniX, iniY
    newX, newY = 0, 0
    direction = 0
    countconsecutiveObstacle = 0
    visitedNodes = set()
    # Run the simulation.

    while 0 <= startX < len(matrix) and 0 <= startY < len(matrix[0]):
        newX, newY = startX + directions[direction][0], startY + directions[direction][1]
        if 0 <= newX < len(matrix) and 0 <= newY < len(matrix[0]):
            if matrix[newX][newY] == '#':
                direction = (direction +1)%4
                
            else:
                if (newX, newY) not in visitedNodes:
                    visitedNodes.add((newX, newY))
                    
                else:
                    if countconsecutiveObstacle > 10000:
                        return True
                    countconsecutiveObstacle += 1
                startX, startY = newX, newY
        else:
            break
    return False



for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] != '#':
            temp = matrix[i][j]
            matrix[i][j] = '#'
            if inLoop(matrix):
                count += 1
            matrix[i][j] = temp

print("Total possible obstacles",count)


print("----------------------------------------------------------------------------------------------------------------------------------------")

# find the obstructions position.
#for i in range(len(matrix)):
#    for j in range(len(matrix[1])):
#        if matrix[i][j] == '#':
#            obstruction.append((i,j))

# Thought loops means rectangle only. Time waste. 
"""
obstruction = list(obstructions)

def is_rectangle_with_X_boundary(coords):
    if len(coords) != 4:
        return False

    x_coords = sorted(set(coord[0] for coord in coords))
    y_coords = sorted(set(coord[1] for coord in coords))

    if len(x_coords) != 2 or len(y_coords) != 2:
        return False


    x_min, x_max = x_coords
    y_min, y_max = y_coords
    for x in range(x_min, x_max + 1):
        if matrix[x][y_min] != 'X' or matrix[x][y_max] != 'X':
            return False

    for y in range(y_min, y_max + 1):
        if matrix[x_min][y] != 'X' or matrix[x_max][y] != 'X':
            return False 


    return True


def isLoop(x1, x2, x3, x4):
    
    changes = [(0,1), (0,-1), (1,0), (-1,0)]
    perm = list(permutations(changes))
    x = [x1, x2, x3, x4]
    p = []
    for permutation in perm:
        p = [(a + c, b + d) for (a, b), (c, d) in zip(x, permutation)]
        #print("Checking the rectangle coordinates",p)
        if is_rectangle_with_X_boundary(p):
            return True
        
    return False

#Math formula P4 = P1 + P3 - P2.
def find4point(x1, x2, x3):
    # find the 4th point.
    if (abs(x2[0] - x3[0]) == 1 and abs(x1[1] - x3[1]) == 1) or (abs(x1[0] - x3[0]) == 1 and abs(x2[1] - x3[1]) == 1):
        x1, x2, x3 = x1, x3, x2
    else:
        if (abs(x1[0] - x2[0]) == 1 and abs(x1[1] - x3[1]) == 1) or (abs(x1[0] - x3[0]) == 1 and abs(x1[1] - x2[1]) == 1):
            x1, x2, x3 = x3, x1, x2
        else:
            if (abs(x2[0] - x3[0]) == 1 and abs(x1[1] - x2[1]) == 1) or (abs(x1[0] - x2[0]) == 1 and abs(x2[1] - x3[1]) == 1):
                x1, x2, x3 = x1, x2, x3
            else:
                return False

    fourthPoint = (x1[0] + x3[0] - x2[0], x1[1] + x3[1] - x2[1])
    if (0 <= fourthPoint[0] < len(matrix)) and (0 <= fourthPoint[1] < len(matrix[0])):
        if (matrix[fourthPoint[0]][fourthPoint[1]] in ('X' , '.')):
            if isLoop(x1, x2, x3, fourthPoint):
                print(x1, x2, x3, fourthPoint)
                return True
    return False

count = 0
print(obstruction)
#find 3 pairs forming a parallelogram.
for i in range(len(obstruction)):
    for j in range(i+1, len(obstruction)):
        for k in range(j+1, len(obstruction)):

            # Finding the 4th point and also checking if path has loop.
            if find4point(obstruction[i], obstruction[j], obstruction[k]):
                count += 1

print(count)
"""

"""
for i in matrix:
    print(i)

"""




            



