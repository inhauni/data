## 9 -1


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
            print(' ',end=' ')
            for name in array:
                print("%9s" % name[0], end=' ')
            print()
            for row in range(self.size):
                print("%9s" % array[row][0] ,end=' ')
                for col in range(self.size):
                    print("%8d" % self.graph[row][col], end=' ')
                print()




## 전역변수 설정

g=None
NameAry=[['GS25',30], ['CU',60], ['Seven11',10], ['MiniStop',90], ['Emart24',40]]

GS25,CU,Seven11,MiniStop,Emart24= 0,1,2,3,4

## 그래프 생성

g=Graph(5)
g.graph[GS25][CU] = 1; g.graph[GS25][Seven11] = 1
g.graph[CU][GS25] = 1; g.graph[CU][Seven11] = 1; g.graph[CU][MiniStop] = 1;
g.graph[Seven11][GS25] = 1; g.graph[Seven11][CU] = 1; g.graph[Seven11][MiniStop] = 1
g.graph[MiniStop][CU] = 1; g.graph[MiniStop][Seven11] = 1; g.graph[MiniStop][Emart24] = 1;
g.graph[Emart24][MiniStop] = 1;


print('----생성된 그래프----\n')
g.printGraph(NameAry)
print()


## 허버칩이 많은 순서대로 나열하여 리스트 생성


stack = []
visited = []


current = 0
maxstore=current
maxcount=NameAry[current][1]
stack.append(0)
visited.append(0)

while len(stack) != 0:

    next = None
    for vertex in range(g.size):
        if g.graph[current][vertex] != 0:
            if vertex in visited:
                pass
            else:
                next = vertex
                break

    if next is not None:
        current = next
        stack.append(current)
        visited.append(current)

        if maxcount<NameAry[current][1]:
            maxstore=current
            maxcount=NameAry[current][1]

    else:
        current = stack.pop()


print(f'허니버터칩 최대 보유 편의점(개수) --> {NameAry[maxstore][0]}({NameAry[maxstore][1]}개)')