def pyramid_sum(lower, upper, margin=0):
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0) 
        return 0
    else:
        result = lower + pyramid_sum(lower+1, upper, margin + 4)
        print(blanks, result)
        return result
    
#  pyramid_sum( 1 , 4 )    
#  _1 4
#  result = 1 + rec1
#  rec1 = pyreamid_sum(2,4,4) = result2
#  result2 = 2 + rec2 
#  rec2 = pyramid_sum(3,4, 8)
if __name__ == "__main__":
    pyramid_sum(1,4)
    
    
# Output    
#  1 4
#      2 4
#          3 4
#              4 4
#                  5 4
#                  0
#              4
#          7
#      9
#  10