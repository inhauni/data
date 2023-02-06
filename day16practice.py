class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

n1 = Node('Pikachu')
n1.link=n1
head=n1

n2= Node('Raichu')
n1.link=n2
n2.link=head

n3=Node('pyrii')
n2.link=n3
n3.link=head

current=head
print(current.data, end=' ')
while current.link!=head:
    current=current.link
    print(current.data,end=' ')
