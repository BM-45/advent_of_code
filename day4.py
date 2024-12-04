def dfs(start, matrix):

    directions = [(0,1),(0,-1),(1,0),(1,-1),(1,1),(-1,-1),(-1,1),(-1,0)]
    result = 0
    for x,y in directions:
        if check_direction(start[0], start[1], x, y, matrix):
                    result += 1
        
    return result

def check_direction(r, c, dr, dc, matrix):
        rows, cols = len(matrix), len(matrix[0])
        if 0 <= r < rows and 0 <= c < cols and \
           0 <= r + 3*dr < rows and 0 <= c + 3*dc < cols:
            return matrix[r][c] == 'X' and \
                   matrix[r+dr][c+dc] == 'M' and \
                   matrix[r+2*dr][c+2*dc] == 'A' and \
                   matrix[r+3*dr][c+3*dc] == 'S'
        return False

def read_matrix_from_file(filename):
    # Open the file and read it.
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            row = list(line)
            matrix.append(row)
    return matrix

def pattern_part2(start, matrix):
     
    if matrix[start[0]][start[1]] == 'A':
         if matrix[start[0]-1][start[1]-1] == 'M' and matrix[start[0]-1][start[1]+1] == 'M' and matrix[start[0]+1][start[1]-1] == 'S' and matrix[start[0]+1][start[1]+1] == 'S': return 1
         elif matrix[start[0]-1][start[1]-1] == 'S' and matrix[start[0]-1][start[1]+1] == 'M' and matrix[start[0]+1][start[1]-1] == 'S' and matrix[start[0]+1][start[1]+1] == 'M': return 1
         elif matrix[start[0]-1][start[1]-1] == 'S' and matrix[start[0]-1][start[1]+1] == 'S' and matrix[start[0]+1][start[1]-1] == 'M' and matrix[start[0]+1][start[1]+1] == 'M': return 1
         elif matrix[start[0]-1][start[1]-1] == 'M' and matrix[start[0]-1][start[1]+1] == 'S' and matrix[start[0]+1][start[1]-1] == 'M' and matrix[start[0]+1][start[1]+1] == 'S': return 1

    return 0
          

def main():
    # Get text from the file and store it in a matrix.
    matrix = read_matrix_from_file("day4.txt")
    print(len(matrix), len(matrix[0]))
    result = 0
    for i in range(1,len(matrix)-1):
        for j in range(1,len(matrix[0])-1):
            # perform dfs.
            if matrix[i][j] == 'A':
                result += pattern_part2((i,j), matrix)


    print(result)

if __name__ == "__main__":
    main()


