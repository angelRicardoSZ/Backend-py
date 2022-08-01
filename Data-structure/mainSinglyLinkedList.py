from linked_list import SinglyLinkedList

def run():

    words = SinglyLinkedList()
    words.append("eg")
    words.append("jam")
    words.append("spam")
    current = words.tail
    while current:
        print(current.data)
        current=current.next
    for word in words.iter():
        print(word)
    
    
if __name__=="__main__":
    run()