#원형 리스트


class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    if current.link == None:
        return
    print(current.data,end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()




def insertNodes(find_data,insert_data):
    global memory, head, current,pre


    if head.data==find_data:                    # 첫번째 노드 삽입
        node=Node()
        node.data=insert_data
        node.link=head
        last=head
        while last.link!=head:
            last=last.link
        last.link=node
        head=node
        return

    current=head
    while current.link!=head:                        # 중간 노드 삽입
        pre=current
        current=current.link
        if current.data==find_data:
            node=Node()
            node.data=insert_data
            node.link=current
            pre.link=node
            return


    node=Node()                                 # 마지막에 노드 삽입
    node.data=insert_data
    node.link=head
    current.link=node




memory=[]
head,current,pre=None,None,None
dataArray=["다현","정연","쯔위","사나","지효"]


if __name__ =="__main__":

    node=Node()
    node.data=dataArray[0]  #첫번쨰 노드
    head=node
    node.link=head  # (단순연결에서는 없었던 부분)
    memory.append(node)

    for data in dataArray[1:]:
        pre=node
        node=Node()
        node.data=data
        pre.link=node
        node.link=head
        memory.append(node)


    printNodes(head)

    insertNodes("다현","화사")
    printNodes(head)

    insertNodes("사나", "솔라")
    printNodes(head)

    insertNodes("재남", "문별")
    printNodes(head)
