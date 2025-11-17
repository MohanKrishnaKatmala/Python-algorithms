"""
The sudoku solver is the solving the 9*9 grid that has the unique numbers in rows,columns and subgrid also.
Initial all take as the 0 values and then update one by one.
Here taking was the input as 0 so here many solutions can occur.
By pressing enter you can get more solutions.
conditions:
All rows has unique numbers.
All columns has the unique numbers.
The subgrid also has the unique numbers.
Output:
Give the sudoku solver.
"""
def sudoku_solver():
    import numpy as np
    grid=[[0 for a in range(9) ]for a in range(9)]
    def possibility(row,column,number):
        # Rows values check.
        for a in range(9):
            if(grid[row][a]==number):
                return False
        # Column values check.   
        for a in range(9):
            if(grid[a][column]==number):
                return False
        # Subgrid values check.
        sub_row=(row//3)*3
        sub_column=(column//3)*3
        for a in range(3):
            for b in range(3):
                if(grid[a+sub_row][b+sub_column]==number):
                    return False
        return True
    def solve():
        for row in range(9):
            for column in range(9):
                if(grid[row][column]==0):
                    for number in range(1,10):
                        if(possibility(row,column,number)):
                            grid[row][column]=number
                            solve()
                            grid[row][column]=0
                    return
        print(np.matrix(grid))
        input("More solutions exists as of all are initial was 0 take.So press enter to get another sudoku solver solution.")
    solve()
sudoku_solver()
