from collections import defaultdict

def part1(matrix):
    uniquePositions = set()
    freq = defaultdict(list)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != '.':
                freq[matrix[i][j]].append((i,j))
    
    for char, positions in freq.items():
        #print(char, len(positions))
        for i in range(len(positions)):
            for j in range(i+1, len(positions)):

                x = positions[i][0] - positions[j][0]
                y = positions[i][1] - positions[j][1]
                uniquePositions.add((positions[i]))
                uniquePositions.add(positions[j])
                for k in range(1, 100):
                    newX, newY = positions[i][0] + k*x, positions[i][1] + k*y
                    new1X, new1Y = positions[j][0] - k*x, positions[j][1] - k*y

                    if (0 <= newX < len(matrix) and 0 <= newY < len(matrix[0])):
                        uniquePositions.add((newX, newY))
                    if (0 <= new1X < len(matrix) and 0 <= new1Y < len(matrix[0])):
                        uniquePositions.add((new1X, new1Y))
    
    return len(uniquePositions)

def part2(data):
    # Solve part 2
    return part1(data)
    

matrix = []

def main():
    # Read input from file
    with open('day8.txt', 'r') as file:
        for line in file:
            row = list(line.strip())  # Split line into characters
            matrix.append(row)
    
    
    # Solve part 1
    result1 = part1(matrix)
    print(f"Part 1 result: {result1}")
    
    # Solve part 2
    result2 = part2(matrix)
    print(f"Part 2 result: {result2}")

if __name__ == "__main__":
    main()