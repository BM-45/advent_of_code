from collections import defaultdict
import re

def part1(buttons):
    # Solve part 1
    tokens = 450
    # Did brute force approach, but this problem is finding the intersection of
    # two lines and if the intersection coordintaes or of integers then print.
    # Generally if there are more than 2 or 3 variables go for dp(memorization).
    for i in range(1,101):
        for j in range(1,101):
            aButton = [i*x for x in buttons[0]]
            bButton = [j*x for x in buttons[1]]
            finalDestination = buttons[2]

            if aButton[0] + bButton[0] == finalDestination[0] and aButton[1] + bButton[1] == finalDestination[1]:
                tokens = min(tokens, 3*i + j)
    
    return 0 if tokens == 450 else tokens


def part2(buttons):
    # Solve part 2
    aButton = buttons[0]
    bButton = buttons[1]
    finalDestination = buttons[2]
    
    # check if parallel lines.
    if aButton[0]*bButton[1] == aButton[1]*bButton[0]:
        return 0
    
    # If intersection is integer co-ordinates.
    y = ((finalDestination[0]*aButton[1] - finalDestination[1]*aButton[0])/(bButton[0]*aButton[1] - bButton[1]*aButton[0]))
    if isinstance(y, int) or (isinstance(y, float) and y.is_integer()):
        x = (finalDestination[0]-bButton[0]*y)/aButton[0]
        if isinstance(x, int) or (isinstance(x, float) and x.is_integer()):
            return 3*x + y
        
    return 0

    

matrix = []

def main():
    result1 = 0
    result2 = 0
    buttons = []
    # Read input from file
    with open('input.txt', 'r') as file:
        for line in file:
            if len(str(line)) < 2:
                # Solve part 1
                result1 += part1(buttons)

                # Solve part 2
                buttons[2] = [x+10000000000000 for x in buttons[2]]
                result2 += part2(buttons)

                buttons.clear()
            else:
                # Take input.
                numbers = re.findall(r'[-+]?\d+', line)
                buttons.append([int(i) for i in numbers])

        result1 += part1(buttons)
        buttons[2] = [x+10000000000000 for x in buttons[2]]
        result2 += part2(buttons)
            
    
    
    
    print(f"Part 1 result: {result1}")
    print(f"Part 2 result: {result2}")

if __name__ == "__main__":
    main()