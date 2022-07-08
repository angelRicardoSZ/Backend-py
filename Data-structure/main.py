from grid import Grid

def run():
    matrix = Grid(3,3)
    print(matrix)
    for row in range(matrix.get_height()):
        for col in range(matrix.get_height()):
            matrix[row][col] = row * col
    print(matrix)
    
if __name__=="__main__":
    run()