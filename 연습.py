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
NameAry=['춘천', '서울', '속초', '대전', '광주', '부산']
춘천,서울,속초,대전,광주,부산=0,1,2,3,4,5  # 도시를 전역변수로 설정

## 그래프 생성

g=Graph(6)
g.graph[춘천][서울] = 10; g.graph[춘천][속초] = 15
g.graph[서울][춘천] = 10; g.graph[서울][속초] = 40; g.graph[서울][대전] = 11; g.graph[서울][광주] = 50
g.graph[속초][춘천] = 15; g.graph[속초][서울] = 40; g.graph[속초][대전] = 12
g.graph[대전][서울] = 11; g.graph[대전][속초] = 12; g.graph[대전][광주] = 20; g.graph[대전][부산] = 30
g.graph[광주][서울] = 50; g.graph[광주][대전] = 20; g.graph[광주][부산] = 25
g.graph[부산][대전] = 30; g.graph[부산][광주] = 25

print('----생성된 그래프----\n')
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

edges=sorted(edges,key=itemgetter(0),reverse=True)

newedges=[]
for i in range(0,len(edges),2):
    newedges.append(edges[i])


## 가중치가 높은 간선부터 제거

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


print('----최소비용으로 생성된 그래프----\n')
g.printGraph(NameAry)
print()