#이진트리

import random
class TreeNode():
    def __init__(self):
        self.left=None
        self.data=None
        self.right=None


memory=[]
rootBook, rootAuth =None, None
bookAry=[['어린왕자', '쌩떽쥐베리'],['이방인', '까뮈'], ['부활', '톨스토이'],
		   ['신곡', '단테'], ['돈키호테', '세브반테스'], ['동물농장', '조지오웰'],
		   ['데미안','헤르만헤세'], ['파우스트', '괴테'], ['대지', '펄벅']]
random.shuffle(bookAry) # -> 매번 랜덤으로 배열


## 책이름 트리

node =TreeNode()
node.data=bookAry[0][0]
rootBook=node
memory.append(node)

# 이진 탐색 트리 생성
for book in bookAry[1:]:
    name=book[0]
    node=TreeNode()
    node.data=name

    current=rootBook

    while True:
        if name<current.data:
            if current.left==None:
                current.left=node
                break
            current=current.left
        else:
            if current.right ==None:
                current.right=node
                break
            current=current.right

    memory.append(node)


print("책 이름 트리 구성 완료!")




## 저자이름 트리

node =TreeNode()
node.data=bookAry[0][1]
rootAuth=node
memory.append(node)


# 이진 탐색 트리 생성

for book in bookAry[1:]:
    name = book[1]
    node = TreeNode()
    node.data = name

    current = rootAuth

    while True:
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right

    memory.append(node)

print("저자 이름 트리 구성 완료!")



## 책 이름 및 작가 이름 검색

bookOrauth=int(input('책검색(1), 작가검색(2) -->'))
findName=input('검색할 책 또는 작가 : ')

if bookOrauth == 1:
    root=rootBook
else:
    root=rootAuth

current=root

while True:
    if findName == current.data:
        print(f'{findName} 을(를) 찾음')
        break
    elif findName < current.data:
        if current.left == None:
            print(f'{findName} 이(가) 트리에 존재하지 않음')
            break
        current=current.left

    else:
        if current.right== None:
            print(f'{findName} 이(가) 트리에 존재하지 않음')
            break
        current=current.right

