# push pop peek

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

SIZE= int(input("Stack Size : "))
stack =[None for _ in range(SIZE)]
top=-1  # top의 초기값

if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X)/ 중 하나를 선택 ==> ")


    while True:

        if select == 'X' or select == 'x':
            print("프로그램 종료")
            break
        elif select=='I' or select == 'i':
            data = input("입력할 데이터 => ")
            push(data)
            print("스택 상태 : ",stack,"\n")
            select = input("삽입(I)/추출(E)/확인(V)/종료(X)/ 중 하나를 선택 ==> ")
        elif select=='E' or select == 'e':
            data =pop()
            print("추출된 데이터 : ",data)
            print("스택 상태 : ", stack,"\n")
            select = input("삽입(I)/추출(E)/확인(V)/종료(X)/ 중 하나를 선택 ==> ")
        elif select=='V' or select == 'v':
            data=peek()
            print("확인된 데이터 : ",data)
            print("스택 상태 : ", stack,"\n")
            select = input("삽입(I)/추출(E)/확인(V)/종료(X)/ 중 하나를 선택 ==> ")
        else:
            print("올바른 코드를 입력하시오\n")
            select = input("삽입(I)/추출(E)/확인(V)/종료(X)/ 중 하나를 선택 ==> ")

