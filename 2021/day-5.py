"""
--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

Your puzzle answer was 4993.

--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?

"""

# Ongoing
def trace_map(x1, y1, x2, y2, arrs):
    # P1(x1, y1), P2(x2, y2)
    # y = mx + b; m = slope
    rise = y2 - y1
    run = x2 -x1
    try:
        slope = rise / run
    except Exception as e:
        # print(e)
        if y1 == y2:
            if x2 > x1:
                for x in range(x1, x2 + 1):
                    arrs[x][y1] += 1
            else:
                for x in range(x2, x1 + 1):
                    arrs[x][y1] += 1
        elif x1 == x2:
            if y2 > y1:
                for y in range(y1, y2 + 1):
                    arrs[x1][y] += 1
            else:
                for y in range(y2, y1 + 1):
                    arrs[x1][y] += 1
    else:
        # points = []
        if slope > 0:
            if rise > 0 and run > 0:
                x = x1
                y = y1
                for x in range(x1, x2 + 1):
                    if y <= y2:
                        arrs[x][y] += 1
                        y += 1
                        # points.append((x, y))
            elif rise < 0 and run < 0:
                x = x2
                y = y2
                for x in range(x2, x1 + 1):
                    if y >= y1:
                        arrs[x][y] += 1
                        y += 1
        elif slope < 0:
            if rise > 0 and run < 0:
                x = x2
                y = y2
                for x in range(x2, x1 + 1):
                    if y >= y1:
                        arrs[x][y] += 1
                        # points.append((x, y))
                        y -= 1
            elif rise < 0 and run > 0:
                x = x1
                y = y1
                for x in range(x1, x2 + 1):
                    if y >= y2:
                        arrs[x][y] += 1
                        # points.append((x, y))
                        y -= 1
        elif slope == 0:
            if y1 == y2:
                if x2 > x1:
                    for x in range(x1, x2 + 1):
                        arrs[x][y1] += 1
                else:
                    for x in range(x2, x1 + 1):
                        arrs[x][y1] += 1
            elif x1 == x2:
                if y2 > y1:
                    for y in range(y1, y2 + 1):
                        arrs[x1][y] += 1
                else:
                    for y in range(y2, y1 + 1):
                        arrs[x1][y] += 1
    return arrs



def counter(arrs):
    i = 0
    for y in arrs:
        for x in y:
            if type(x) == str:
                pass
            elif x >= 2:
                i += 1
    return i


def main():
    f = open("day-5-input.txt", "r")
    f_list = f.readlines()
    all = [line.strip().split(" -> ") for line in f_list if line.strip()]
    print("all:", len(all))
    map = []
    for _ in range(999):  # x-coord
        row = [0 for _ in range(999)]  # y-coord
        map.append(row)

    for cmd in all:
        x1, y1 = cmd[0].split(",")
        x2, y2 = cmd[1].split(",")
        trace_map(int(x1), int(y1), int(x2), int(y2), map)

    total = counter(map)
    print("counter:", counter)
    print("total:", total)


if __name__ == "__main__":
    main()

data = open("day-5-input.txt").read().splitlines() 
x_data = []
for i in range(len(data)):
    x_data.append(int(data[i].replace(' ', ',').split(",")[0]))
    x_data.append(int(data[i].replace(' ', ',').split(",")[1]))
y_data = []
for i in range(len(data)):
    y_data.append(int(data[i].replace(' ', ',').split(",")[1]))
    y_data.append(int(data[i].replace(' ', ',').split(",")[4]))
nx = max(x_data)
ny = max(y_data)

"""
Part1 : At how many points do at least two lines overlap?
"""
print("====PART1====")
import numpy as np

diagram = np.zeros((nx+1, ny+1), dtype=np.int) # empty diagram

for i in range(len(data)):
    x1 = int(data[i].replace(' ', ',').split(",")[0])
    y1 = int(data[i].replace(' ', ',').split(",")[1])
    x2 = int(data[i].replace(' ', ',').split(",")[3])
    y2 = int(data[i].replace(' ', ',').split(",")[4])
    if x1==x2:
        diagram[y1][x1]+=1
        diagram[y2][x2]+=1
        y = y1-y2
        if y>1 : 
            for i in range(1,abs(y)):
                diagram[y1-i][x1]+=1
        else:
            for i in range(1,abs(y)):
                diagram[y1+i][x1]+=1
    if y1==y2:
        diagram[y1][x1]+=1
        diagram[y2][x2]+=1
        x = x1-x2
        if x>0 : 
            for i in range(1,abs(x)):
                diagram[y2][x2+i]+=1
        else:
            for i in range(1,abs(x)):
                diagram[y2][x2-i]+=1   
                
print("number of points where at least two lines overlap :",len(np.where(diagram >= 2)[0]))

"""
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.
Part2 : At how many points do at least two lines overlap?
"""
print("====PART2====")
diagram = np.zeros((nx+1, ny+1), dtype=np.int) # empty diagram


for i in range(len(data)):
    x1 = int(data[i].replace(' ', ',').split(",")[0])
    y1 = int(data[i].replace(' ', ',').split(",")[1])
    x2 = int(data[i].replace(' ', ',').split(",")[3])
    y2 = int(data[i].replace(' ', ',').split(",")[4])
    if x1==x2:
        diagram[y1][x1]+=1
        diagram[y2][x2]+=1
        y = y1-y2
        if y>1 : 
            for i in range(1,abs(y)):
                diagram[y1-i][x1]+=1
        else:
            for i in range(1,abs(y)):
                diagram[y1+i][x1]+=1
    if y1==y2:
        diagram[y1][x1]+=1
        diagram[y2][x2]+=1
        x = x1-x2
        if x>0 : 
            for i in range(1,abs(x)):
                diagram[y2][x2+i]+=1
        else:
            for i in range(1,abs(x)):
                diagram[y2][x2-i]+=1
    if x1>x2 and y1>y2:
        diagram[y1][x1]+=1
        diagram[y2][x2]+=1
        x = x1-x2
        y = y1-y2
        if abs(x)>abs(y):
            for i in range(1,abs(x)):
                diagram[y1-i][x1-i]+=1
        else:
            for i in range(1,abs(y)):
                diagram[y1-i][x1-i]+=1
    if x1<x2 and y1<y2:
        diagram[y1][x1]+=1
        diagram[y2][x2]+=1
        x = x1-x2
        y = y2-y1
        if abs(x)>abs(y):
            for i in range(1,abs(x)):
                diagram[y1+i][x1+i]+=1
        else:
            for i in range(1,abs(y)):
                diagram[y1+i][x1+i]+=1
    if x1>x2 and y1<y2:
        diagram[y1][x1]+=1
        diagram[y2][x2]+=1
        x = x1-x2
        y = y1-y2
        if abs(x)>abs(y):
            for i in range(1,abs(x)):
                diagram[y1+i][x1-i]+=1
        else:
            for i in range(1,abs(y)):
                diagram[y1+i][x1-i]+=1
    if x1<x2 and y1>y2:
        diagram[y1][x1]+=1
        diagram[y2][x2]+=1
        x = x1-x2
        y = y2-y1
        if abs(x)>abs(y):
            for i in range(1,abs(x)):
                diagram[y1-i][x1+i]+=1
        else :
            for i in range(1,abs(y)):
                diagram[y1-i][x1+i]+=1
print("number of points where at least two lines overlap :",len(np.where(diagram >= 2)[0]))
