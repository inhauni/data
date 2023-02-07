# 7 - 1
import random


def isQueueEmpty():
    global rear, front, queue, SIZE
    if rear==front:
        return True
    return False

def isQueueFull():
    global rear, front, queue, SIZE

    if rear==SIZE-1:
        return True
    return False

def enQueue(data):
    global rear, front, queue, SIZE

    if isQueueFull():
        print("Queue is FUll")
        return
    rear+=1
    queue[rear]=data


def deQueue():
    global rear, front, queue, SIZE

    if isQueueEmpty():
        print("Queue is Empty")
        return None

    front += 1
    temp = queue[front]
    queue[front]=None
    for i in range(front+1,rear+1):
        queue[i-1]=queue[i]
        queue[i]=None
    rear -=1
    front-=1

    return temp

def peekQueue():
    if isQueueEmpty():
        return None
    return queue[front+1]

SIZE=7
rear=front=-1
queue=[None for _ in range(SIZE)]

BTS=['정국','지민','뷔','진','슈가','RM','제이홉']
random.shuffle(BTS)

for member in BTS:
    enQueue(member)

while True:
    print(f'\n대기 줄 상태 : {queue}')
    if queue.count(None)==SIZE:
        print('식당 영업 종료!')
        break
    print(f'{deQueue()} 님 식당에 들어감')
