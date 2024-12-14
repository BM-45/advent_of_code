from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import re

def part1(tall, wide, robotspecs, iterations):
    # Solve part 1
    firstQuadrant, secondQuadrant, thirdQuadrant, fourthQuadrant = 0, 0, 0, 0

    for i in robotspecs:
        location = (i[0], i[1])
        velocity = (i[2], i[3])

        for j in range(iterations):
            location = (  (location[0] + velocity[0])%wide, (location[1] + velocity[1])%tall )

        if location[0] < wide//2:
            xlesshalf = True
        elif location[0] > wide//2:
            xlesshalf = False
        else:
            continue

        if location[1] < tall//2:
            ylesshalf = True
        elif location[1] > tall//2:
            ylesshalf = False
        else:
            continue


        if xlesshalf and ylesshalf:
            firstQuadrant += 1
        elif not xlesshalf and ylesshalf:
            secondQuadrant += 1
        elif xlesshalf and not ylesshalf:
            thirdQuadrant += 1
        else:
            fourthQuadrant += 1

        #print(firstQuadrant, secondQuadrant, thirdQuadrant, fourthQuadrant)
    return firstQuadrant* secondQuadrant * thirdQuadrant * fourthQuadrant

# Didn't understand the question itself, worst question framing.
def part2(tall, wide, robotSpecs, iterations=10000):
    # Solve part 2
    matrix = [[0 for x in range(wide)] for y in range(tall)]

    locations, velocity = [], []
    for i in robotSpecs:
        locations.append((i[0], i[1]))
        velocity.append((i[2], i[3]))

    # Animating the robot locations.
    animate_robot_movements(tall, wide, velocity, locations, iterations)

    # visuvalize the locations in matrix grid. Checking the whether getting the matrix or not.
    visualize_matrix(tall, wide, locations, velocity, 7892)



# Got this code from chatgpt, need to understand it.
def animate_robot_movements(tall, wide, velocities, locations, iterations=10000):

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, wide)
    ax.set_ylim(0, tall)
    scat = ax.scatter([], [], s=100)
    iteration_text = ax.text(0.02, 0.98, '', transform=ax.transAxes, verticalalignment='top')

    def init():
        scat.set_offsets(np.empty((0, 2)))
        iteration_text.set_text('')
        return scat, iteration_text

    def update(frame):
        nonlocal locations
        locations = [((loc[0] + vel[0]) % wide, (loc[1] + vel[1]) % tall) for loc, vel in zip(locations, velocities)]
        scat.set_offsets(np.array(locations))
        iteration_text.set_text(f'Iteration: {frame}')
        return scat, iteration_text

    ani = animation.FuncAnimation(fig, update, frames=iterations, init_func=init, blit=True, repeat=False, interval=50)
    plt.show()

def visualize_matrix(tall, wide, locations, velocity, iteration):
    matrix = np.zeros((tall, wide))
    for i in range(len(locations)):
        locations[i] =  (  (locations[i][0] + velocity[i][0]*iteration)%wide, (locations[i][1] + velocity[i][1]*iteration )%tall )
    for x, y in locations:
        matrix[y, x] = 1  # Mark robot positions

    plt.imshow(matrix, cmap='Greys', interpolation='nearest')
    plt.title(f'Robot Positions at Iteration {iteration}')
    plt.xlabel('Width')
    plt.ylabel('Height')
    plt.show()

def main():
    tall, wide = 103, 101
    robotSpecs = []
    # Read input from file
    with open('input.txt', 'r') as file:
        for line in file:
            numbers = re.findall(r'-?\d+', line)
            loc_speed = [int(num) for num in numbers]
            robotSpecs.append(loc_speed)

    
    # Solve part 1
    result1 = part1(tall, wide, robotSpecs, 100)
    print(f"Part 1 result: {result1}")
    
    # Solve part 2
    result2 = part2(103, 101, robotSpecs)

if __name__ == "__main__":
    main()