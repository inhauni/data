class Graph:
    def __init__(self,size):
        self.size=size
        self.graph=[[0 for _ in range(size)] for _ in range(size)]

    def printGraph(self,array):

        if array is None:
            for row in range(self.size):
                for col in range(self.size):
                    print(self.graph[row][col], end='')
                print()
        else:
            print('\t',end='')
            for name in array:
                print(name,end=' ')
            print()
            for row in range(self.size):
                print(array[row],' ',end='')
                for col in range(self.size):
                    print(self.graph[row][col], end='   ')
                print()

## 전역변수 설정

G1=None
NameAry=['화사', '문별', '휘인', '솔라']
stack=[]
visited=[]

## 그래프 생성

g1=Graph(4)
g1.graph[0][3]=1;
g1.graph[1][2]=1;g1.graph[1][3]=1;
g1.graph[2][1]=1;
g1.graph[3][0]=1;g1.graph[3][1]=1;

print('----생성된 그래프----\n')
g1.printGraph(NameAry)


# 깊이 우선 탐색 구현 (DFS)

current=0
root=current
stack.append(0)
visited.append(0)


while len(stack) != 0:

    next=None
    for vertex in range(g1.size):
        if g1.graph[current][vertex]==1:
                if vertex in visited:
                    pass
                else:
                    next = vertex
                    break

    if next is not None:
        current=next
        stack.append(current)
        visited.append(current)

    else:
        current=stack.pop()


print(f'\n방문순서 : ',end=' ')
for visit in visited:
    visit=NameAry[visit]
    print(visit,end=' ')
