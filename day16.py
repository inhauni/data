class Node():
    def __init__(self):
        self.data=None
        self.link=None

def printNodes(start):
    current = start
    if current ==None:
        return
    print(current.data,end='')
    while current.link != None:
        current=current.link
        print(current.data,end='')
    print()

def makeSimpleLinkedList(namePhone):
    global memory, head, current,pre
    printNodes(head)

    node =Node()    # 새 노드 추가
    node.data =namePhone
    memory.append(node)

    if head ==None:     # 첫번째 노드일 때
        head=node
        return
    if head.data[0]>namePhone[0]:  #첫번째 노드보다 작을 때
        node.link=head
        head=node
        return

    current=head
    while current.link != None:  # 중간에 삽입
        pre=current
        current =current.link
        if current.data[0]>namePhone[0]:
            pre.link=node
            node.link=current
            return

    current.link=node # 삽입하는 노드의 값이 가장 큰 경우

s
memory=[]
head,current,pre=None,None,None
dataArray=[["지민","010-1111-1111"],["정국","010-2222-2222"],["뷔","010-3333-3333"],["슈가","010-4444-4444"],["진","010-5555-5555"]]

if __name__ =="__main__":
    for data in dataArray:
        makeSimpleLinkedList(data)

    printNodes(head)