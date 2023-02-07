

def is_stackFull():
    if top>=SIZE-1:
        return True
    return False

def is_stackEmpty():
    if top == -1:
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


def checkBracket(expr):
    for ch in expr:
        if ch in '([{<':
            push(ch)
        elif ch in ')]}>':
            out = pop()
            if ch==')' and out =='(':
                pass
            elif ch==']' and out =='[':
                pass
            elif ch=='}' and out =='{':
                pass
            elif ch=='>' and out =='<':
                pass
            else:
                return False
        else: pass

    if is_stackEmpty():
        return True
    else:
        return False


SIZE= 100
stack =[None for _ in range(SIZE)]
top=-1  # top의 초기값

if __name__ == "__main__":

    exprAry=['()',')(','(()','(]','(<{}[]>)','(())']

    for expr in exprAry:
        top=-1  # 하나 검사 후 초기화
        print(expr, '==>', checkBracket(expr))

