
#  File: Triangle.py

#  Description:

#  Student Name: Yilin Wen

#  Student UT EID: yw22559

#  Partner Name: Jiaxi Wang

#  Partner UT EID: jw53499

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 03/03/2022

#  Date Last Modified:03/04/2022

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force(grid):
    sums = recursive_brute_force(grid,0,0)
    #print("sums:",sums)
    return max(sums)

# recursively search the whole grid
def recursive_brute_force(grid, row, col):
    # base case:
    if row == len(grid) -1:
        return [grid[row][col]]
    # recursive step
    temp_1 = recursive_brute_force(grid, row+1, col)
    #print("temp1:", temp_1)
    temp_2 = recursive_brute_force(grid, row+1, col+1)
    #print("temp2:", temp_2)
    sum_1 = [v + grid[row][col] for v in temp_1]
    sum_2 = [v + grid[row][col] for v in temp_2]
    sum_1.extend(sum_2)
    return sum_1


# returns the greatest path sum using greedy approach
def greedy(grid):
    row, col = 0, 0
    max_sum = grid[0][0]
    while row < len(grid) - 1:
        if grid[row+1][col] < grid[row+1][col+1]:
            max_sum += grid[row+1][col+1]
            #print(grid[row+1][col+1])
            col += 1
        else:
            max_sum += grid[row+1][col]
            #print(grid[row+1][col+1])
        row += 1
    return max_sum 
    

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer(grid):
    return recursive_divide_conquer(grid, 0, 0)

# recursively find the max sum
def recursive_divide_conquer(grid,row,col):
    # base case:
    if row >= len(grid) - 1:
        return grid[row][col]
    # recursive step
    sum_1 = recursive_divide_conquer(grid,row+1,col)
    sum_2 = recursive_divide_conquer(grid,row+1,col+1)
    if sum_1 > sum_2:
        return sum_1 + grid[row][col]
    return sum_2 + grid[row][col]


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    # this is basically a "reversed selection" which going from buttom to top
    # in this order, reconstruct the whole grid by swithing each element with the largest sum it can achieve
    row = len(grid) - 2
    while row >= 0:
        for col in range(row + 1):
            # the feasible max sum at one position is itself plus the larger of the max sum of positions it can reach
            grid[row][col] += max(grid[row+1][col], grid[row+1][col+1])
        row -= 1
    # now the top of grid is the largest feasible sum
    return grid[0][0]

# reads the file and returns a 2-D list that represents the triangle
def read_file():
    # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create an empty grid with 0's
    grid = [[0 for i in range(n)] for j in range(n)]

    # read each line in the input file and add to the grid
    for i in range(n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list(map(int, row))
        for j in range(len(row)):
            grid[i][j] = grid[i][j] + row[j]

    return grid


def main():
    # read triangular grid from file
    grid = read_file()

    # check that the grid was read in properly
    #print(grid)

    # output greatest path from exhaustive search
    print("The greatest path sum through exhaustive search is ")
    print(brute_force(grid))
    # print time taken using exhaustive search
    times = timeit('brute_force({})'.format(grid),
                   'from __main__ import brute_force', number=10)
    times = times / 10
    print("The time taken for exhaustive search in seconds is")
    print(times)
    print()


    # output greatest path from greedy approach
    print("The greatest path sum through greedy search is ")
    print(greedy(grid))
    # print time taken using greedy approach
    times = timeit('greedy({})'.format(grid),
                   'from __main__ import greedy', number=10)
    times = times / 10
    print("The time taken for greedy approach in seconds is")
    print(times)
    print()


    # output greatest path from divide-and-conquer approach
    print("The greatest path sum through recursive search is ")
    print(divide_conquer(grid))
    # print time taken using divide-and-conquer approach
    times = timeit('divide_conquer({})'.format(grid),
                   'from __main__ import divide_conquer', number=10)
    times = times / 10
    print("The time taken for recursive search in seconds is")
    print(times)
    print()


    # output greatest path from dynamic programming
    print("The greatest path sum through dynamic programming is ")
    print(dynamic_prog(grid))
    # print time taken using dynamic programming
    times = timeit('dynamic_prog({})'.format(grid),
                   'from __main__ import dynamic_prog', number=10)
    times = times / 10
    print("The time taken for dynamic programming in seconds is")
    print(times)
    print()


if __name__ == "__main__":
    main()


