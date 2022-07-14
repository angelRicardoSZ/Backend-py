from my_array import Array

"""
Two dimensional array type class

Methods:
    1. height
    2. Weight
    3. Get item
    4. String representation
    5. Add random items

    
Args:
    height (int): height of the array.
    width (int): width of the array.
    fill_value (any, optional): value at each position. Defaults to None
"""

class Grid():
    def __init__(self, rows, columns, fill_value=None) -> None:
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)
            
    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])
    
    def __getitem__(self,index):
        return self.data[index]
    
    def __str__(self):
        result = ""
        
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "
            result += "\n"
        
        return str(result)
    
    def __addRandomItems__(self, lower=0, upper=10):
        pass