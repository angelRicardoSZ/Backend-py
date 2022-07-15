from node import Node

def run():

   
    node2 = Node("A", None)
    node3 = Node("B", node2)
    node1 = Node("C", node3)
    print("Node 1.next.data")
    print(node1.next.data)
    
    print("Node 2:")
    print(node2)
    print("Node 2 data:")
    print(node2.data)
    
    print("Node 3:")
    print(node3.next.data)
    
    head = None
    for i in range(1,5):
        head = Node(i,head)
    while head != None:
        print(head.data)
        head = head.next
    
if __name__=="__main__":
    run()