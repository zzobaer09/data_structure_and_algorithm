


# * print the val of linked list
def Printf(head):
    curr = head

    data = ""
    while curr:
        if curr.next is None: data += str(curr.data) + " ---> (null)"
        else: data += str(curr.data) + " ---> "

        curr = curr.next 

    return data
# * return the sum of val
def Sum(head):

    curr = head
    sum = 0
    while curr:

        try:

            sum += curr.data

        except:
            pass
        curr = curr.next


    return sum






# * makes a list(arr)
def list_(head):

    curr = head
    arr = []

    while curr:

        arr.append(curr.data)
        curr = curr.next

    return arr








# * find the given val in linked list
def target(head , tar):

    # if head == None: return False

    # if head.data == tar: return True
    # return target(head.next , tar)




    # * while

    curr = head
    count = 0


    while curr:

        if curr.data == tar: return True , count
        curr = curr.next
        count += 1

    return False



# * find val in a given index


def find_in_index(head , index:int):

    # if head == None: return
    # if index == 0: return head.data
    # return find_in_index(head.next , index-1)


    count = 0

    curr = head

    while curr:

        if index == count: return "expected val: " ,  curr.data

        count += 1
        curr = curr.next




# * return the reversed linked list
def reversed(head):

    pre = None
    curr = head


    while curr:
        next = curr.next

        curr.next = pre
        pre = curr

        curr = next
    
    return pre