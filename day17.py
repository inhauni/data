

def is_queueFull():
    global SIZE,queue,rear,front

    if (rear+1) % SIZE == front:
        return True
    return False

def is_queueEmpty():
    global SIZE,queue,rear,front

    if rear == front:
        return True
    return False

def enQueue(data):
    global SIZE,queue,rear,front

    if is_queueFull():
        print("Queue is Full")
        return
    rear = (rear+1) % SIZE
    queue[rear]= data


def deQueue():
    global SIZE,queue,rear,front
    if is_queueEmpty():
        print("Queue is Empty")
        return
    front=(front+1) % SIZE
    data =queue[front]
    queue[front]=None
    return data

def peek():
    global SIZE,queue,rear,front
    if is_queueEmpty():
        print("Queue is Empty")
        return None
    return queue[(front+1) % SIZE]




SIZE= 5
queue =[None for _ in range(SIZE)]
rear= front = 0  # top의 초기값

if __name__ == "__main__":

    select = input("삽입(I)/추출(E)/확인(V)/종료(X)/ 중 하나를 선택 ==> ")

    while True:

        if select == 'X' or select == 'x':
            print("프로그램 종료")
            break
        elif select == 'I' or select == 'i':
            data = input("입력할 데이터 => ")
            enQueue(data)
            print("스택 상태 : ", queue, "\n")
            select = input("삽입(I)/추출(E)/확인(V)/종료(X)/ 중 하나를 선택 ==> ")
        elif select == 'E' or select == 'e':
            data = deQueue()
            print("추출된 데이터 : ", data)
            print("스택 상태 : ", queue, "\n")
            select = input("삽입(I)/추출(E)/확인(V)/종료(X)/ 중 하나를 선택 ==> ")
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터 : ", data)
            print("스택 상태 : ", queue, "\n")
            select = input("삽입(I)/추출(E)/확인(V)/종료(X)/ 중 하나를 선택 ==> ")
        else:
            print("올바른 코드를 입력하시오\n")
            select = input("삽입(I)/추출(E)/확인(V)/종료(X)/ 중 하나를 선택 ==> ")
            


