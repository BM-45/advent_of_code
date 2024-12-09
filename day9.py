from collections import defaultdict

def parse_input(data):
    return list(data.strip())

def part1(data):
    nums = []
    empty = []
    fid = 0
    pos = 0
    
    # Build initial array
    for i, val in enumerate(data):
        blocks = int(val)
        if i % 2 == 0:
            nums.extend([fid] * blocks)
            pos += blocks
            fid += 1
        else:
            nums.extend([-1] * blocks)
            empty.extend(range(pos, pos + blocks))
            pos += blocks
    
    result = 0
    max_idx = len(nums) - 1
    empty_idx = 0
    
    
    while empty_idx < len(empty) and empty[empty_idx] < max_idx:
        if nums[max_idx] != -1:
            result += empty[empty_idx] * nums[max_idx]
            empty_idx += 1
        max_idx -= 1
    
    # Add remaining positions in one pass
    result += sum(i * nums[i] for i in range(max_idx + 1) if nums[i] != -1)
    
    return result

def part2(data):
    blocks = []
    file_id = 0
    for i in range(0, len(data), 2):
        file_length = int(data[i])
        free_space = int(data[i+1]) if i+1 < len(data) else 0
        blocks.extend([file_id] * file_length)
        blocks.extend(['.'] * free_space)
        file_id += 1
    
    for current_file_id in range(file_id - 1, -1, -1):
        file_positions = [i for i, block in enumerate(blocks) if block == current_file_id]
        if not file_positions:
            continue
        
        file_length = len(file_positions)
        start_pos = min(file_positions)
        
        leftmost_space = -1
        free_count = 0
        for i in range(start_pos):
            if blocks[i] == '.':
                free_count += 1
                if free_count == file_length:
                    leftmost_space = i - file_length + 1
                    break
            else:
                free_count = 0
        
        if leftmost_space != -1:
            for pos in reversed(file_positions):
                blocks[pos] = '.'
            for i in range(file_length):
                blocks[leftmost_space + i] = current_file_id
    
    return sum(i * block for i, block in enumerate(blocks) if block != '.')

def main():
    with open('day9.txt') as f:
        data = f.read().strip()
    
    parsed = parse_input(data)
    print(part1(parsed))
    print(part2(parsed))

if __name__ == "__main__":
    main()