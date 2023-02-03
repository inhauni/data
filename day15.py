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

def printPoly(p_x):

    term = len(p_x)-1  # 최고차항 차수

    polyStr = "P(x) = "

    for i in range(len(p_x)):

        coef = p_x[i]  # 계수

        if coef == 0:
            term = term-1
            continue
        if coef>=0:
            polyStr += "+"

        polyStr += f'{coef}x^{term} '
        term -= 1
    return polyStr


def calcPoly(xVal, p_x):
    retValue = 0
    term = len(p_x) - 1 # 차수
    for i in range(len(p_x)):
        coef = p_x[i]  # 계수
        retValue += coef * xValue ** term
        term -= 1

    return retValue


    ## 전역 변수 선언 부분 ##

# tx = [300, 20, 0]
px = [7, -4, 0, 5]

    ## 메인 코드 부분 ##
if __name__ == "__main__":
    pStr = printPoly(px)
    print(pStr)

    xValue = int(input("X 값-->"))

    pxValue = calcPoly(xValue, px)
    print(pxValue)

