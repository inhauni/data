import webbrowser
import time



def is_stackFull():
    if top>=SIZE-1:
        print("stack is full")
        return True
    return False

def is_stackEmpty():
    if top == -1:
        print("stack is empty")
        return True
    return False

def push(data):
    global SIZE,stack,top

    if is_stackFull():
      return

    top += 1
    stack[top]= data


def pop():
    global SIZE, stack, top
    if is_stackEmpty():
        return
    temp =stack[top]
    stack[top]=None
    top -=1
    return temp

def peek():
    global SIZE, stack, top
    if is_stackEmpty():
        return None   #peek했지만 top에 아무것도 없는 경우
    return stack[top]



SIZE= 100
stack =[None for _ in range(SIZE)]
top=-1  # top의 초기값

if __name__ == "__main__":

    urls=["inha.ac.kr","harvard.edu","seoul.edu"]

    for url in urls:
        push(url)
        webbrowser.open('http://'+url)
        print(url,end=' ')
        time.sleep(1)

    print("방문 종료")
    time.sleep(5)

    while True:
        url =pop()
        if url == None:
            break
        webbrowser.open('http://'+url)
        print(url, end=' ')
        time.sleep(1)

    print("방문 종료")
