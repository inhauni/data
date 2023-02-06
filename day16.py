#원형 리스트
import random


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

def countOddEven():
    global memory,head,current,pre

    odd,even=0,0

    if head==None:
        return False

    current=head
    while True:
        if current.data%2==0:
            even +=1
        else:
            odd +=1

        if current.link==head:
            break
        current=current.link

    return odd, even


def makeMinus(odd,even):
    if odd>even:
        reminder = 1
    else:
        reminder =0

    current=head
    while True:

        if current.data%2 == reminder:
            current.data *= -1
        if current.link == head:
            break

        current=current.link



memory=[]
head,current,pre=None,None,None


if __name__ =="__main__":

    dataArray=[]
    for i in range(7):
        dataArray.append(random.randint(1,100))

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


    oddcount, evencount =countOddEven()
    print(f'홀수 --> {oddcount}, 짝수 --> {evencount}')
    makeMinus(oddcount,evencount)
    printNodes(head)



