## 9-2


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



##  누락요소 확인 (DFS와 유사)

def findVertex(g,findV):

    stack=[]
    visited=[]

    current=0
    stack.append(0)
    visited.append(0)


    while len(stack) != 0:

        next=None
        for vertex in range(g.size):
            if g.graph[current][vertex]!=0:
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

    if findV in visited:
        return True
    return False

## 전역변수 설정

g=None
NameAry=['서울','뉴욕', '런던','북경','방콕','파리']
서울,뉴욕,런던,북경,방콕,파리=0,1,2,3,4,5  # 도시를 전역변수로 설정

## 그래프 생성

g=Graph(6)
g.graph[북경][서울] = 10; g.graph[북경][뉴욕] = 40;g.graph[북경][방콕] = 50;
g.graph[서울][뉴욕] = 80; g.graph[서울][북경] = 10;
g.graph[뉴욕][방콕] = 70; g.graph[뉴욕][서울] = 80; g.graph[뉴욕][북경] = 40
g.graph[방콕][뉴욕] = 70; g.graph[방콕][북경] = 50; g.graph[방콕][런던] = 30; g.graph[방콕][파리] = 20
g.graph[런던][방콕] = 30; g.graph[런던][파리] = 60;
g.graph[파리][방콕] = 20; g.graph[파리][런던] = 60

print('## 해저 케이블 연결을 위한 전체 연결도 ##\n')
g.printGraph(NameAry)
print()



# 가중치 간선 목록



## 중복 없는 가중치 & 간선 목록 생성
edges=[]

for i in range(g.size):
    for k in range(g.size):
        if g.graph[i][k]!=0:
            edges.append([g.graph[i][k],i,k])

from operator import itemgetter

edges=sorted(edges,key=itemgetter(0),reverse=False)

newedges=[]
for i in range(0,len(edges),2):
    newedges.append(edges[i])


## 가중치가 낮은 간선부터 제거

index=0

while len(newedges) >g.size-1:
    start=newedges[index][1]
    end=newedges[index][2]
    save=newedges[index][0]

    g.graph[start][end]=0
    g.graph[end][start]=0

    startYN=findVertex(g,start)
    endYN=findVertex(g,end)

    if startYN and endYN:
        del(newedges[index])
    else:

        g.graph[start][end] = save
        g.graph[end][start] = save

        index += 1


print('## 가장 효율적인 해저 케이블 연결도 ##\n')
g.printGraph(NameAry)
print()