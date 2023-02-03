# Pokemons = []  # 빈 배열
 # 전체 소스코드의 특정 변수이름을 한번에 바꾸고 싶을땐 마우스 오른쪽 버튼에 refactors-> rename 사용!!


## <데이터 추가 코드>
#
# def add_data(pokemon):
#     Pokemons.append(None)
#     # Pokemons[len(Pokemons) - 1] = pokemon
#     Pokemons[- 1] = pokemon  # 맨끝에 집어넣는 방법
#
#
# add_data('피카추')
# add_data('라이츄')
# add_data('파이리')
# add_data('꼬부기')
# add_data('버터풀')
#
# print(Pokemons)
#


Pokemons = ["피카츄", "라이츄", "파이리", "꼬부기", "버터풀"]



# <데이터 삽입 코드>
def insert_data(position, pokemon):
    if position < 0 or position > len(Pokemons):
        print("Out of range.")
        return

    Pokemons.append(None)  # 빈칸 추가
    len_pokemon = len(Pokemons)  # 배열의 현재 크기

    for i in range(len_pokemon - 1, position, -1):  # 맨끝에 데이터 삽입시 이 코드 안 돌아감
        Pokemons[i] = Pokemons[i - 1]
        Pokemons[i - 1] = None

    Pokemons[position] = pokemon  # 지정한 위치에 친구 추가

# <데이터 삭제 코드>
def delete_data(idx):

    if idx < 0 or idx > len(Pokemons)-1:
        print("Out of range")
        return

    len_pokemons = len(Pokemons)
    Pokemons[idx] = None  # 데이터 삭제

    for i in range(idx + 1, len_pokemons):
        Pokemons[i - 1] = Pokemons[i]
        Pokemons[i] = None  # 배열의 맨 마지막 위치 삭제

    del (Pokemons[len_pokemons - 1])

# < idx 뒤의 데이터 전부 삭제>
# def delete_data(idx):
#
#     len_pokemons = len(Pokemons)
#
#     if idx < 0 or idx > len(Pokemons)-1:
#         print("Out of range")
#         return
#
#     for i in range(len_pokemons-1, idx-1, -1):
#         del (Pokemons[i])

 # 메인으로 지정
if __name__ == "__main__":

    insert_data(4, '어니부기')
    print(Pokemons)
    insert_data(5, '거북왕')
    print(Pokemons)
    delete_data(7)
    print(Pokemons)
    delete_data(4)
    print(Pokemons)
