# https://www.youtube.com/watch?v=rfscVS0vtbw&t=10033s

number_grid = [ # 2D List. Sort of like a grid of numbers
    [0, 1],
    [2, 3],
    [4, 5],
    [6, 7],
    [8, 9]
]

print(number_grid[0][1]) # Prints 1

for row in number_grid: # Loops each "row"
    print(f"row: {row}")
    for col in row: # Loops each "column"
        print(f"col: {col}")