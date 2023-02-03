Pokemons = []  # 빈 배열
 # 전체 소스코드의 특정 변수이름을 한번에 바꾸고 싶을땐 마우스 오른쪽 버튼에 refactors-> rename 사용!!
def add_data(pokemon):
    Pokemons.append(None)
    kLen = len(Pokemons)
    Pokemons[kLen - 1] = pokemon


add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

print(Pokemons)

Pokemons = ["다현", "정연", "쯔위", "사나", "지효"]


def insert_data(position, friend):
    if position < 0 or position > len(Pokemons):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    Pokemons.append(None)  # 빈칸 추가
    kLen = len(Pokemons)  # 배열의 현재 크기

    for i in range(kLen - 1, position, -1):
        Pokemons[i] = Pokemons[i - 1]
        Pokemons[i - 1] = None

    Pokemons[position] = friend  # 지정한 위치에 친구 추가


insert_data(2, '솔라')
print(Pokemons)
insert_data(6, '문별')
print(Pokemons)
