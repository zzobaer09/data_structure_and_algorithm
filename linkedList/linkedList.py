
from module import *



# node here
class Node():
    def __init__(self , data) -> None:
        self.data = data
        self.next = None





# TODO: make a linked list which can -----> add data after a another✅; add data before✅; add data by index✅;
class Linked_list():

    # * constructor
    def __init__(self) -> None:
        
        self.head = None
        self.tail = None
        self.size = 0

    # * val add after
    def append(self , data):
        node = Node(data)
        
        curr = self.head
        if self.head is None: 
            self.head = node
            self.size += 1
        else:
            while curr.next:
                curr = curr.next
            curr.next = node
            self.size += 1
    
    #  * val add before
    def push(self , data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.size += 1
        else:
            current = self.head
            self.head = node
            self.head.next =  current
            self.size += 1
            
    # * delete value by index 
    def deleteVal(self, val):

        # todo: delete the given value 
        # given value is the current value
        # if the head is the current value then current value's next will be the head
        # get track of the previous value of the current value
        # previous value's next will be the current value's next 
        # then free the current value


        try:
            val = int(val)
        except:
            pass

        curr = self.head
        
        if self.head.data == val:

            self.head = curr.next
            curr = None
            self.size -= 1

        while curr:

            if curr.data is val:

                pre.next = curr.next
                self.size -= 1
                curr = None
                break

            pre = curr
            curr = curr.next


    def delete(self):

        current = self.head
        while current:
            prev = current.next  # move next node
 
            # delete the current node
            del current.data
 
            # set current equals prev node
            current = prev

    def delIndex(self , index:int):

        curr = self.head

        if self.head is None: return
        if index > self.size: return "Index Out Of range"

        if index == 0:

            self.head = self.head.next
            self.size -= 1
            return



        pre = self.head
        count = 0

        while curr:

            if count == index-1:
                pre = curr
                try:

                    pre.next = curr.next.next
                    self.size -= 1
                except:
                    pass
                curr = None
                return

            curr = curr.next
            count += 1






    # * add val by index
    def indexing(self , data , index:int):

        if index < 0 or index > self.size:
            raise Exception("index is not valid")
        if index == 0:
            self.push(data)

        current = self.head
        count = 0

        node = Node(data)

        while current:
            if count == index - 1:
                node.next = current.next
                current.next = node
                self.size += 1

            current = current.next
            count += 1



    # * print val
    def print(self):

        current = self.head
        data = ""

        while current:

            if current.next is None:
                data += str(current.data) + " ---> (null)"
            else:
                data += str(current.data) +  " ---> "


            current = current.next

        print(data)
        return data
        print("size of list is {}".format(self.size))



