from my_array import Array

def run():
    menu = Array(5) 
    for i in range(len(menu)):
        menu[i] = i+1
    print(menu.__len__())
    print(menu.__str__())
    print(menu.__iter__())
    print(menu.__getitem__(2))
    # menu.__setitem__(2,100)
    
    menu.__addRandomItems__()
    print(menu)
    print(menu.__addAll__())
    
    
if __name__=="__main__":
    run()