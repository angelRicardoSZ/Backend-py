# Data structures

## Node

Each node will store a value and each node has a pointer that will take you to another node

### Implementation of a Node :

```python
class Node():
    def __init__(self, data, next= None):
        self.data = data
        self.next = next
```

### Example: we will create series of 5 nodes

```python
head = None
for i in range(1,6):      		 
	head = Node(i,head)	  	       
```

### Explanation

1st step: i =1

head =  Node_1: data = 1, next => None

2nd step: i = 2

head =  Node_2: data = 2, next => Node_1: data = 1, next => None

3rd step: i = 3

head =  Node_3: data = 3, next => Node_2: data = 2, next => Node_1: data = 1, next => None

4th step: i = 4

head =  Node_4: data = 4, next => Node_3: data = 3, next => Node_2: data = 2, next => Node_1: data = 1, next => None

5th step: i = 5

head =  Node_5: data = 5, next => Node_4: data = 4, next => Node_3: data = 3, next => Node_2: data = 2, next => Node_1: data = 1, next => None

### Showing all nodes

```python
while head != None:
	print(head.data)
    head = head.next       
```

Singly linked list

A linked list is created by using the node class. We pass the appropriate values through the node object to point the to the next data elements

```python
from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0
        
    def append(self, data):
        node = Node(data)   # Creation of node
        
        if(self.tail == None): # if there is no node  at the end
            self.tail = node   # then, it is assigned in tail
        
        else:
            current = self.tail  # take the current tail
            while current.next:  # while the current node points to another node 
                current = current.next # reassings the node
            current.next = node  # when current.next = None, the new node is assigned
            
        self.size += 1  # when the node is added, the length of the list is incrimented by 1
    
    def size(self): 
        return str(self.size) # Convert the length of the list to string
    
    def iter(self): # method to explore their values
        current = self.tail # method to explore their values
        while current: # while a node exists
            val = current.data # takes the value of the node
            current.data = current.next #  reassings the node
            yield val # values generator
    
    # explanation of delete method with a fake linked list
    # linked_list : 
    #    tail: 
    #    	node1: 
    #			data = data1
    #            next: node2:
    #				data = data2
    #                 next: node3:
    #						data = data3
	#    					next: None
    #    size = 3
    # 
    
    # Case 1
    # when the delete method is called with data = data3
	# linked_list.delete(data3)    
    #  initial conditions
    #   current =
    #			node1: 
    #			data = data1
    #            next:
    #				node2:
    #				 data = data2
    #                  next: node3:
    #						data = data3
	#    					next: None
    # 	previuous =
    #			node1: 
    #			data = data1
    #            next:
    #				node2:
    #				 data = data2
    #                  next: node3:
    #						data = data3
	#    					next: None
    #  while loop
    #  node1.data = data1 is different to  data3 
    #  then  => 
    #     previuous =
    #			node1: 
    #			data = data1
    #            next:
    #				node2:
    #				 data = data2
    #                  next: node3:
    #						data = data3
	#    					next: None
    # 	AND 
    #   current =
    #				node2:
    #				 data = data2
    #                  next: node3:
    #						data = data3
	#    					next: None
    #   COMPARE current.data with the input = data3
    #   because are different,
   	#     previuous =
    #				node2:
    #				 data = data2
    #                  next: node3:
    #						data = data3
	#    					next: None
    # 	AND 
    #   current =
    #				node3:
    #						data = data3
	#    					next: None
    #  COMPARE current.data = data3 with the input = data3
    #  in this case are equal, then continue with the next validation
    #  current == self.tail, because is FALSE continues to the ELSE statment
    #  previous in this case is equal to node2, then 
    #  previuous.next is equals to 
    #				node2:
    #				 data = c
    #                  next: None
    #  because current.next = node3.next = None
    #  finally self.size -= 1
    #  returns data3
    #  because current = None, ends the method
        
    def delete(self, data): 
        current = self.tail
        previuous = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previuous.next = current.next
                    self.size -=1
                    return current.data
                
            previuous = current
            current = current.next
    def search(self,data):
        for node in self.iter(): 
            if data == node:
                print(f"Data {data} found")
                
    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0
```

