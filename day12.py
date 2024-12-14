def find_regions(matrix):
    rows, cols = len(matrix), len(matrix)
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    regions = []
    
    def dfs(r, c, char, region):
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or matrix[r][c] != char:
            return
        visited[r][c] = True
        region.append((r, c))
        # Explore neighbors
        dfs(r + 1, c, char, region)
        dfs(r - 1, c, char, region)
        dfs(r, c + 1, char, region)
        dfs(r, c - 1, char, region)
    
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                region = []
                dfs(r, c, matrix[r][c], region)
                if region:
                    regions.append(region)
    return regions

# If it is part of the region.
def isValidCell(matrix, x, y, region):
    return (0 <= x < len(matrix)) and (0 <= y < len(matrix[0])) and ((x,y) in region)

def part1(matrix, regions):
    result = 0

    # Iterate through the region and find the perimeter(degree of the node).
    directions = [(0,1), (0,-1), (1,0),(-1,0)]
    
    for i in regions:
        area = len(i)
        TotalPerimeter = 0
        for j in i:
            # check four nodes.
            perimeter = 4
            for dir in directions:
                newX, newY = j[0] + dir[0], j[1] + dir[1]
                if isValidCell(matrix, newX, newY, i):
                    perimeter -= 1
            TotalPerimeter += perimeter
            
        result += area* TotalPerimeter

    return result

def part2(matrix, regions):
    result = 0

    # Iterate through the region and find the perimeter(degree of the node).
    hordirections = [(1,0),(-1,0)]
    verdirections = [(0,1), (0,-1)]
    diadirections = [(1,1),(1,-1),(-1,1),(-1,-1)]
    directions = [hordirections, verdirections]
    
    for i in regions:
        area = len(i)
        cornerPoints = 0
        char = matrix[i[0][0]][i[0][1]]
        for x, y in i:
            
            count = 0
            # One element has 4 corners. Dead end road. Has 2 corners.
            for k in directions:
                for dx, dy in k:
                    if not isValidCell(matrix, x + dx, y + dy, i):
                        count += 1

            if count == 4:
                cornerPoints += 4
            elif count == 3:
                cornerPoints += 2
            elif count <= 2:
                isDiscontinuity = True
                # discontinuity in x direction and y direction.
                for a, b in directions:
                    if isValidCell(matrix, x + a[0], y + a[1], i) and isValidCell(matrix, x + b[0], y + b[1], i):
                        isDiscontinuity = False

                if isDiscontinuity:
                    cornerPoints += 1
                # check for interior corners.
                for dx, dy in diadirections:
                    if not isValidCell(matrix,x + dx, y + dy,i):
                        if isValidCell(matrix,x + dx, y, i) and isValidCell(matrix, x, y + dy, i):
                            cornerPoints += 1
            #print(f" For ({x}, {y}) co ordinate has {cornerPoints}")

        #print(f"For {char} the area is {area} and sides are {cornerPoints}")
        result += area * cornerPoints

    return result

def main():
    # Read input from file
    matrix = []
    with open('input.txt', 'r') as file:
        for line in file:
            row = list(line.strip())
            matrix.append(row)
    
    # Create a list of regions.
    regions = find_regions(matrix)
    
    # Solve part 1
    result1 = part1(matrix, regions)
    print(f"Part 1 result: {result1}")
    
    # Solve part 2
    result2 = part2(matrix, regions)
    print(f"Part 2 result: {result2}")

if __name__ == "__main__":
    main()
