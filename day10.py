
def isPath(matrix, i, j, target, depth):

    if i[0] == j[0] and i[1] == j[1] and depth == 9:
        return 1
    if depth > 10:
        return 0

    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    result = 0
    for k in directions:
        newX, newY = i[0] + k[0], i[1] + k[1]
        if 0 <= newX < len(matrix) and 0 <= newY < len(matrix[0]) and matrix[newX][newY] == target + 1:
            result +=  isPath(matrix, (newX, newY), j, target + 1, depth + 1)
    
    return result

def part1(matrix):
    # Solve part 1
    # Store the 0 and 9's.

    store0 = []
    store9 = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                store0.append((i,j))
            elif matrix[i][j] == 9:
                store9.append((i,j))

    result = 0
    for i in store0:
        for j in store9:
            # If there exists a path.
            if isPath(matrix, i, j, 0, 0):
                result += 1

    return result

def part2(matrix):
    # Solve part 2
    store0 = []
    store9 = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                store0.append((i,j))
            elif matrix[i][j] == 9:
                store9.append((i,j))

    result = 0
    for i in store0:
        for j in store9:
            # If there exists a path.
            sum = isPath(matrix, i, j, 0, 0)
            result += sum

    return result

def main():
    # Read input from file
    matrix = []
    with open('input.txt', 'r') as file:
        for line in file:
            row = [int(i) for i in list(line.strip())]
            matrix.append(row)
        
    # Solve part 1
    result1 = part1(matrix)
    print(f"Part 1 result: {result1}")
    
    # Solve part 2
    result2 = part2(matrix)
    print(f"Part 2 result: {result2}")

if __name__ == "__main__":
    main()