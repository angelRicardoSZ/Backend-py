from linked_list import SinglyLinkedList


def run():
	# array 
	array = ['hola', 'como','estas', '?']

	# Sinlgy linked list
	words = SinglyLinkedList()

	# transform to linked list
	for i in array:
		words.append(i)
	
	# print 
	current = words.tail
	while current:
		print(current.data)
		current = current.next

if __name__=="__main__":
    run()