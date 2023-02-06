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

def deleteNodes(deleteData):
    global memory,head,current,pre

    if head.data==deleteData:       # 첫번째 노드 삭제
        current=head
        head=head.link
        last= head
        while last.link!=current:
            last=last.link
        last.link=head
        del(current)
        return

    current=head
    while current.link!=head:
        pre=current
        current=current.link
        if current.data==deleteData:
            pre.link=current.link
            del(current)
            return
    print(f"{deleteData}는 존재하지 않는 이름입니다 \n수정결과 : ")


def is_find(findData):
    '''
    연결 리스트 안에서 원소 존재 여부 판정
    :param findData: 찾고자 하는 원소 .srt
    :return: 연결 리스트 안에서 원소가 존재하면 True 아니면 False 리턴
    '''

    global memory, head, current, pre
    current=head
    if current.data==findData:
        return current
    while current.link != head:
       current=current.link
       if current.data == findData:
           return current

    return Node()




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

    deleteNodes("화사")
    printNodes(head)

    deleteNodes("솔라")
    printNodes(head)

    deleteNodes("이나")
    printNodes(head)

    fNode=is_find("이나")
    print(fNode.data)
    fNode = is_find("다현")
    print(fNode.data)