# # 5장 01
# import random
# import math
#
# class Node():
#     def __init__(self):
#         self.data=None
#         self.link=None
#
#
# def printNode(start):
#     current=start
#     if current==None:
#         return
#     print(f'{current.data[0]} 편의점 , 거리 : {current.data[1]}', end='\n')
#     while current.link != head:
#         current=current.link
#         print(f'{current.data[0]} 편의점 , 거리 : {current.data[1]}', end=' \n')
#     print()
#
# def arrayConv(store):
#
#     global memory, current, head, pre
#
#     node=Node()
#     node.data=store
#
#     memory.append(node)
#
#     if head == None:
#         head=node
#         node.link=head
#
#         return
#
#
#
#     if head.data[1]>store[1]:
#         node.link=head
#         last=head
#         while last.link!=head:
#             last=last.link
#         last.link=node
#         head=node
#
#         return
#
#     current=head
#     while current.link != head:
#         pre=current
#         current=current.link
#         if current.data[1] > store[1]:
#             pre.link = node
#             node.link = current
#             return
#
#     current.link = node
#     node.link=head
#
#
#
#
# memory=[]
# head, pre, current = None, None, None
#
# alph=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#
# if __name__ == "__main__":
#
#     convs=[]
#     for i in alph:               # 편의점 객체들 생성
#         convName = i
#         conx=random.randint(1,100)
#         cony=random.randint(1,100)
#         conDist=math.sqrt(conx*conx+cony*cony)
#         conv = convName,conDist
#         convs.append(conv)
#
#
#     for store in convs:
#         arrayConv(store)
#
#     printNode(head)



## 5장 2
#
# class Node():
#     def __init__(self):
#         self.data=None
#         self.flink=None
#         self.blink=None
#
#
# def printNode(start):
#
#     current=start
#     if current==None:
#         return
#     print('정방향 : ', current.data, end=' ')
#     while current.blink != None:
#         current=current.blink
#         print(current.data, end=' ')
#     print('\n역방향 : ', current.data, end=' ')
#     while current.flink != None:
#         current=current.flink
#         print(current.data, end=' ')
#     print()
#
#
# memory=[]
# head, pre, current = None, None, None
# dataArray=["다현","정연","쯔위","사나","지효"]
#
# if __name__ == "__main__":
#
#     node=Node()
#     node.data=dataArray[0]
#     head=node
#     memory.append(node)
#
#     for data in dataArray[1:]:
#         pre=node
#         node = Node()
#         node.data=data
#         pre.blink = node
#         node.flink = pre
#         memory.append(node)
#
#     printNode(head)

def isStackFull():
    global SIZE, top, stack
    if top>=SIZE-1:

        return True
    return False

def isStackEmpty():
    global SIZE, top, stack
    if top==-1:
        return True
    return False

def push(data):
    global SIZE, top, stack
    if isStackFull():
        print("Stack is full.")
        return
    top+=1
    stack[top]=data

def pop():
    global SIZE, top, stack
    if isStackEmpty():
        print("Stack is empty!")
        return
    temp=stack[top]
    stack[top]=None
    top-=1
    return temp

def peek():
    global SIZE, top, stack
    if isStackEmpty():
        return None
    return stack[top]

SIZE=7
top=-1
stack=[None for _ in range(SIZE)]


if __name__ == "__main__":

    stone=["빨강","주황","노랑","초록","파랑","남색","보라"]

    print('가는길 : 우리집 ->' ,end=' ')
    for go in stone:
        push(go)
        print(go,"->",end=' ')
    print('과자집')

    print('오는길 : 과자집 ->',end=' ')
    for back in stack:
        print(pop(), '->', end=' ')
    print('우리집')

