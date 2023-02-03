# Pokemons = []  # 빈 배열
 # 전체 소스코드의 특정 변수이름을 한번에 바꾸고 싶을땐 마우스 오른쪽 버튼에 refactors-> rename 사용!!


## <데이터 추가 코드>

# def add_data(pokemon):
#     pokemons.append(None)
#     # Pokemons[len(Pokemons) - 1] = pokemon
#     pokemons[- 1] = pokemon  # 맨끝에 집어넣는 방법
#
#
# # Pokemons = ["피카츄", "라이츄", "파이리", "꼬부기", "버터풀"]
#
# # <데이터 삽입 코드>
# def insert_data (position, pokemon):
#
#     if position < 0 or position > len(pokemons):
#         print("Out of range.")
#         return
#
#     pokemons.append(None)  # 빈칸 추가
#     len_pokemon = len(pokemons)  # 배열의 현재 크기
#
#     for i in range(len_pokemon - 1, position, -1):  # 맨끝에 데이터 삽입시 이 코드 안 돌아감
#         pokemons[i] = pokemons[i - 1]
#         pokemons[i - 1] = None
#
#     pokemons[position] = pokemon  # 지정한 위치에 친구 추가
#
# # <데이터 삭제 코드>
# def delete_data(idx):
#
#     if idx < 0 or idx > len(pokemons):
#         print("Out of range")
#         return
#
#     len_pokemons = len(pokemons)
#     pokemons[idx] = None  # 데이터 삭제
#
#     for i in range(idx + 1, len_pokemons):
#         pokemons[i - 1] = pokemons[i]
#         pokemons[i] = None  # 배열의 맨 마지막 위치 삭제
#
#     del (pokemons[len_pokemons - 1])

#< idx 뒤의 데이터 전부 삭제>

#def delete_data(idx):
#     len_pokemons = len(Pokemons)
#
#     if idx < 0 or idx > len(Pokemons)-1:
#         print("Out of range")
#         return
#
#     for i in range(len_pokemons-1, idx-1, -1):
#         del (Pokemons[i])

 # 메인으로 지정

    # pokemons = []
    # select = -1
    # if __name__ == "__main__":
    # insert_data(4, '어니부기')
    # print(Pokemons)
    # insert_data(5, '거북왕')
    # print(Pokemons)
    # delete_data(7)
    # print(Pokemons)
    # delete_data(4)
    # print(Pokemons)

# 포켓몬 추가 삽입 삭제

#     while select != 4:
#
#         select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> "))
#
#         if (select == 1):
#             data = input("추가할 데이터--> ")
#             add_data(data)
#             print(pokemons)
#         elif (select == 2):
#             idx = int(input("삽입할 위치--> "))
#             data = input("추가할 데이터--> ")
#             insert_data(idx, data)
#             print(pokemons)
#         elif (select == 3):
#             idx = int(input("삭제할 위치--> "))
#             delete_data(idx)
#             print(pokemons)
#         elif (select == 4):
#             print(pokemons)
#             exit
#         else:
#             print("1~4 중 하나를 입력하세요.")
#             continue

    ## 함수 선언 부분 ##

# def printPoly(t_x,p_x):
#     '''
#
#     :param p_x: 계수를 원소로 가지는 list
#     :return: 다항식 형태 출력
#     '''
#
#
#
#     polyStr = "P(x) = "
#
#     for i in range(len(p_x)):
#         term = t_x[i]
#         coef = p_x[i]  # 계수
#
#
#         if coef == 0:
#             i += 1
#             continue
#
#         if i > 0 and coef > 0:  # 첫항의 +는 빼주기
#             polyStr += "+"
#
#         polyStr += f'{coef}x^{term} '
#
#     return polyStr
#
#
# def calcPoly(xVal,t_x, p_x):
#
#     '''
#     다항식의 산술연산을 하는 함수
#     :param xVal: x에 대입할 값
#     :param p_x: 계수를 원소로 가지는 list
#     :return: 다항식 계산 결과 값
#     '''
#
#     retValue = 0
#      # 차수
#     for i in range(len(p_x)):
#         term = t_x[i]
#         coef = p_x[i]  # 계수
#         retValue += coef * xVal ** term
#
#
#     return retValue
#
#
#     ## 전역 변수 선언 부분 ##
#
# tx = [300, 20, 0]
# px = [7, 0, 5]
#
#     ## 메인 코드 부분 ##
# if __name__ == "__main__":
#     pStr = printPoly(tx, px)
#     print(pStr)
#
#     xValue = int(input("X 값-->"))
#
#     pxValue = calcPoly(xValue, tx, px)
#     print(pxValue)
#
#
# # <카톡 친구 자동 삽입>
# def insert_data (position, friend):
#
#     len_friends = len(friends)
#
#     if position < 0 or position > len_friends:
#         print("Out of range.")
#         return
#
#     friends.append(None)  # 빈칸 추가
#       # 배열의 현재 크기
#
#     for i in range(len_friends - 1, position, -1):  # 맨끝에 데이터 삽입시 이 코드 안 돌아감
#         friends[i] = friends[i - 1]
#         friends[i - 1] = None
#
#     friends[position] = friend
#
# def add_friends(name,num):
#     '''
#
#     :param name: 친구 이름
#     :param num: 연락 횟수
#     :return: 연락 횟수를 내림차순으로 정렬하여 friends 리스트에 새 친구 추가
#     '''
#
#     len_friends = len(friends)
#
#     for i in range(len_friends):
#
#         if friends[i][1]<=num:
#             insert_data(i, (name,num))
#             break
#         if i == len_friends -1:
#             insert_data(len_friends, (name,num))
#
#
#
#
# friends = [('다현',200), ('정연',150), ('쯔위',90), ('사나',30), ('지효',15)]
#
# fname = input("추가할 친구 --> ")
# number = int(input("카톡 횟수 --> "))
# add_friends(fname, number)
# print(friends)

## 클래스와 함수 선언 부분 ##

class Node:    # 노드 클래스 생성
	def __init__ (self) :
	    self.data = None
	    self.link = None

def printNodes(start):
	current = start     # 헤드를 받아서 current에 넣음
	if current == None :
		return
	print(current.data, end = ' ') # head의 데이터 우선 출력

	while current.link != None:  # 마지막 노드의 링크에 닿기 전까지 진행
		current = current.link
		print(current.data, end = ' ')  # 마지막 노드의 데이터까지 출력하고 종료
	print()  # current == None 일경우 return하는 None값을 print

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	node = Node()		# 첫 번째 노드
	node.data = dataArray[0]
	head = node    # head로 지정
	memory.append(node)  # 메모리 안에 노드 저장

	for data in dataArray[1:] :	# 두 번째 이후 노드
		pre = node  # 이전 노드를 pre로 지정
		node = Node()   # 새 노드 생성
		node.data = data
		pre.link = node   # 이전 노드의 link를 새 노드의 주소로 지정
		memory.append(node)  # 메모리에 새 노드 삽입

	printNodes(head)   # 첫번째 노드를 함수에 대입
