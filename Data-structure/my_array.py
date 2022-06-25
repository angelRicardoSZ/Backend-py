"""
Array type class

Methods:
    1. Length
    2. String representation
    3. Membership
    4. Index.
    5. Replacement
    6. addRandomItems
    
Args:
    capacity (int): size of the array.
    fill_value (any, optional): value at each position. Defaults to None
"""
import random
from functools import reduce
class Array:
    
    def __init__(self, capacity, fill_value=None):
        self.capacity = capacity
        self.items = list()
        for i in range(self.capacity):
            self.items.append(fill_value)
    
    def __len__(self):
        """Returns capacity of the array."""
        return len(self.items)
    
    def __str__(self):
        """Returns string representation of the array"""
        return str(self.items)
    
    def __iter__(self):
        
        return iter(self.items)
    
    def __getitem__(self,index):
        """Subscrit operator for access at index."""
        return self.items[index]
    
    def __setitem__(self,index, new_item):
        """Subscript operator for replacement at index."""
        self.items[index] = new_item
        
    def __addRandomItems__(self, lower=0, upper=5):
        """Assign random numbers between lower and upper limits for each item"""
        self.items = [ random.randint(lower, upper)
                      for i in range(self.capacity)]
        
    def __addAll__(self):
        return reduce(lambda x, y: x + y, self.items)
        
        

        
        