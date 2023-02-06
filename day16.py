#Stack
import random

stack =[None for i in range(5)]
top=-1

top+=1
stack[top]="커피"
top+=1
stack[top]="녹차"
top+=1
stack[top]="꿀물"

for i in range(len(stack)-1,-1,-1):
    print(stack[i])
print("---------------")
data=stack[top]
stack[top]=None
top -= 1
print(f'pop -> {data}')

data=stack[top]
stack[top]=None
top -= 1
print(f'pop -> {data}')

data=stack[top]
stack[top]=None
top -= 1
print(f'pop -> {data}')
print("---------------")
for i in range(len(stack)-1,-1,-1):
    print(stack[i])

