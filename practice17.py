# 7 - 2
import random



## 고객 정보 class

class Customer():
    def __init__(self,name):
        self.name=name
        self.time=None

    def setTime(self):
        if self.name == '사용':
            self.time = 9
        elif self.name == '고장':
            self.time = 3
        elif self.name == '환불':
            self.time = 4
        else:
            self.time = 1

        return self.time


## 원형 Queue
def isQueueEmpty():
    global rear, front, queue, SIZE
    if rear==front:
        return True
    return False

def isQueueFull():
    global rear, front, queue, SIZE

    if (rear+1)% SIZE == front:
        return True
    return False

def enQueue(data):
    global rear, front, queue, SIZE

    if isQueueFull():
        return
    rear = (rear+1) % SIZE
    queue[rear]=data

    if rear==5:
        print(f'귀하의 예상 대기시간은 {timeTotal(data[1])}분 입니다.\n최종 대기 콜 --> {queue}\n\n프로그램 종료!')
        return
    print(f'귀하의 예상 대기시간은 {timeTotal(data[1])}분 입니다.\n현재 대기 콜 ==> {queue}\n')


def deQueue():
    global rear, front, queue, SIZE

    if isQueueEmpty():
        print("Queue is Empty")
        return None

    front= (front+1) % SIZE
    temp = queue[front]
    queue[front] = None
    return temp

def peekQueue():
    if isQueueEmpty():
        return None
    return queue[(front+1)%SIZE]


## 시간 더하는 함수

def timeTotal(time):
    global total
    total += time
    return total


## 전역 변수 설정
SIZE=6
rear=front=0
queue=[None for _ in range(SIZE)]
total=0



## 임의의 queue 생성

rsns=['사용','환불','고장','기타문의']
reasons = [random.choice(rsns) for _ in range(SIZE-1)]


for reason in reasons:
    customer=Customer(reason)
    enQueue((reason,customer.setTime()))




