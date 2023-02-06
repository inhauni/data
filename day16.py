## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printNodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()

def insertNode(findData, insertData) :
	global memory, head, current, pre

	if head.data == findData :      # 첫 번째 노드 삽입
		node = Node()
		node.data = insertData
		node.link = head
		head = node
		return

	current = head
	while current.link != None :    # 중간 노드 삽입
		pre = current
		current = current.link
		if current.data == findData :
			node = Node()
			node.data = insertData
			node.link = current
			pre.link = node
			return

	node = Node()                   # 마지막 노드 삽입
	node.data = insertData
	current.link = node

def deleteNode(deleteData) :
	global memory, head, current, pre

	if head.data == deleteData :
        current = head
		head = head.link
		del(current)
        return



	current = head                          # 첫 번째  외 노드 삭제
	while current.link != None :
		pre = current
		current = current.link
		if current.data == deleteData :
# 삭제 할 데이터 못 찾는 경우 코드 종료
			pre.link = current.link
			del(current)
			return



## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["피카츄", "라이츄", "파이리", "꼬부기", "버터풀"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	node = Node()			# 첫 번째 노드
	node.data = dataArray[0]
	head = node
	memory.append(node)

	for data in dataArray[1:] :		# 두 번째 노드부터
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		memory.append(node)


insertNode("피카츄","잠만보")
printNodes(head)
insertNode("버터풀","어니부기")
printNodes(head)
deleteNode("잠만보")
printNodes(head)
deleteNode("어니부기")
printNodes(head)
deleteNode("야도란")
printNodes(head)  # 변화 없음