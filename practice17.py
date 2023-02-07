# 8 - 1


import random

class Node():
    def __init__(self):
        self.left=None
        self.data=None
        self.right=None


## 전역 변수 생성

memory=[]
root=None
storeAry=['레쓰비 캔커피', '레쓰비 캔커피', '레쓰비 캔커피', '도시락','도시락', '삼각김밥',
          '삼각김밥','삼각김밥','삼각김밥','코카콜라', '코카콜라', '츄파츕스','츄파츕스','츄파츕스', '삼다수']

random.shuffle(storeAry)

#   storeAry=random.choice(storeAry) for _ in range(20) -> 이런 식으로도 가능


print(f'오늘 판매될 물건(중복O) --> {storeAry}\n')

#이진 탐색 함수 생성

node=Node()
node.data=storeAry[0]
root=node
memory.append(node)

for store in storeAry[1:]:

    node=Node()
    node.data=store

    current=root

    while True:
        if store == current.data:
            break
        if current.data>store:
            if current.left==None:
                current.left=node
                break
            current=current.left
        else:
            if current.right==None:
                current.right=node
                break
            current=current.right

    memory.append(node)


print('이진 탐색 트리 구성 완료!\n')



## 탐색하여 중복값 제외

# 이진 트리 후위 순회

sellAry=[]
def postorder(node):

    if node==None:
        return
    postorder(node.left)
    postorder(node.right)
    # print(node.data, end=' ')
    sellAry.append(node.data)


postorder(root)
print(f'오늘 판매된 종류(중복X) --> {sellAry}',end='')






