
from linkedList import Linked_list
from module import Printf


x = Linked_list()


# * add value
x.append("world")
x.push("hello")
x.indexing("zobaer" , 1)
x.append(1)



def detectLoop(h):
 
    while (h != None):
        # If this node is already traverse
        # it means there is a cycle
        # (Because you we encountering the
        # node for the second time).
        if (h.flag == 1):
            return True
  
        # If we are seeing the node for
        # the first time, mark its flag as 1
        h.flag = 1
        h = h.next
    return False



print(detectLoop(x.head))

