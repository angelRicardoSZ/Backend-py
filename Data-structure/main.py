from node import Node

def run():

    head = None

    for count in range(1,4):
        head = Node(count,head)

    #   i = 1
    #   head:
    #     data = 1
    #     next: None

    #   i = 2
    #   head:
    #     data = 2
    #     next: 
    #       data = 1
    #       next: None

    #   i = 3
    #   head:
    #     data = 3
    #     next: 
    #       data = 2
    #       next: 
    #           data = 1
    #           next: None

        
        
    while head != None:
        print(head.data)
        head = head.next
        
    probe = head
    
    print("probe")
    while probe != None:
        
        print(probe.data)
        probe = probe.next
        
    target_item = 2
    
    while probe != None and target_item != probe.data:
        probe = probe.next
    
    if probe != None: 
        print(f"Target item {target_item} has been found")

if __name__=="__main__":
    run()