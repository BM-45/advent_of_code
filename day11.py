

def part1(nums):
    # Solve part 1
    
    newList = []

    for i in nums:
        if i == 0:
            newList.append(1)
        elif len(str(i)) % 2 == 0:
            data = str(i)
            num1 = int(str(i)[:len(data)//2])
            num2 = int(str(i)[len(data)//2:])
            newList.append(num1)
            newList.append(num2)
        else:
            newList.append(i*2024)
    
    return newList

def part2(stones):
    # Solve part 2
    new_stones = {}
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] = new_stones.get(1, 0) + count
        elif len(str(stone)) % 2 == 0:
            half = len(str(stone)) // 2
            left = int(str(stone)[:half])
            right = int(str(stone)[half:])
            new_stones[left] = new_stones.get(left, 0) + count
            new_stones[right] = new_stones.get(right, 0) + count
        else:
            transformed = stone * 2024
            new_stones[transformed] = new_stones.get(transformed, 0) + count
    return new_stones

def main():
    # Read input from file
    parsed_data = ""
    with open('input.txt', 'r') as file:
        listNumbers = file.read()
        parsed_data = [int(i) for i in listNumbers.split(" ")]
    
    
    # Solve part 1
    k = 0
    data = parsed_data.copy()
    while k < 25:
        data = part1(data)
        k += 1

    print(f"Part 1 result: {len(data)}")
    
    # Solve part 2
    stones = {stone: parsed_data.count(stone) for stone in set(parsed_data)}
    for _ in range(75):
        stones = part2(stones)
    print(f"Part 2 result: {sum(stones.values())}")

if __name__ == "__main__":
    main()
