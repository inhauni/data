class Node():

    def __init__(self):
        self.data=None
        self.link=None

def makeNameAndEmail():
    name = input('이름 : ')
    if name == '\n':
        return
    email = input('이메일 : ')
    return name,email


def printNodes(start):

    current=start
    if current==None:
        return
    print(current.data,end=' ')
    while current.link != None:
        current=current.link
        print(current.data,end=' ')

    print()


memory=[]
head,current,pre=None, None, None

## 첫번째 노드 생성

node=Node()
node.data=(makeNameAndEmail())
head= node
memory.append(node)
printNodes(head)
while True:

    node = Node()
    node.data = (makeNameAndEmail())
    memory.append(node)

    if head==None:
        head=node
        continue

    if head.data[1]>node.data[1] :
        node.link=head
        head=node
        continue

    current= head
    while current.link != None:
        pre=current
        current=node
        if current.data[1]>node.data[1]:
            node.link=current
            pre.link=node
            break

    current.link=node
    printNodes(head)




