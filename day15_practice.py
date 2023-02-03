def array_hp(dicname):

    hparray = [[name, hp] for name,hp in zip((dicname.keys()), (dicname.values()))]
    hparray.sort(key=lambda x:-x[1])
    return_dic=dict(hparray)
    return return_dic

def insert_pokemon (position, pokemon):

    new_list = list(pokemons.items())


    if position < 0 or position > len(new_list):
        print("Out of range.")
        return

    new_list.append(None)  # 빈칸 추가

      # 배열의 현재 크기

    for i in range(len(new_list) - 1, position, -1):  # 맨끝에 데이터 삽입시 이 코드 안 돌아감
        new_list[i] = new_list[i - 1]
        new_list[i - 1] = None


    new_list[position] = pokemon
    print(dict(new_list))




def add_pokemon(name, hp):
    '''

    :param name: 포켓몬 이름
    :param hp: 체력
    :return: 체력을 내림차순으로 정렬하여 pokemons 리스트에 새 친구 추가
    '''

    new_list = list(pokemons.items())

    len_pokemons = len(new_list)

    for i in range(len_pokemons):

        if new_list[i][1] <= hp:
            insert_pokemon(i, (name, hp))
            break
        if i == len_pokemons -1:
            insert_pokemon(len_pokemons, (name, hp))


if __name__ == "__main__":


    pokemons = {'피카츄': 100, '라이츄': 150, '파이리': 110, '꼬부기': 80, '버터풀': 145}

    pokemons=array_hp(pokemons)
    print(pokemons)
    pname = input("추가할 포켓몬 = ")
    p_hp = int(input("남은 체력 --> "))
    add_pokemon(pname,p_hp)
