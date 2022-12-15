from linkedList import Linked_list
from module import *


a = Linked_list()


# * adding values
a.append("h")
a.append("e")
a.append("l")
a.append("l")
a.append("o")

a.append(1)
a.append(3)
a.append(6)
a.append(10)
a.append(20)



# * oparetion

a.print()
print("---")
a.delete("o")
a.print()
print("---")
a.delete("1")
a.print()
print("---")
a.delete("l")
a.print()
print("---")
a.delete("3")
a.print() 
a.delete("h")
a.print()

