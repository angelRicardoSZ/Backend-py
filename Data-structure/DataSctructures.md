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

