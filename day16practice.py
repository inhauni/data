
# 6-2
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

Note="진달래꽃\n나 보기가 역겨워\n가실 때에는\n말없이 고이 보내드리오리다."
SIZE=len(Note)
print(SIZE)
top=-1
stack=[None for _ in range(SIZE)]


if __name__ == "__main__":

    print('-------원본-------')
    for letter in Note:
        push(letter)
        print(letter,end='')
    print('\n-------거꾸로 처리된 결과-------')
    for rletter in stack:
        print(pop(),end='')



