# pokemon game v0.5
# 중복코드 제거, getter setter

class Pokemon:

    count=0 # 클래스 변수
    def __init__(self, owner, skills):
        self.hidden_owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 생성 :", end=' ')
        # self.count += 1

    # built in decorator 사용
    @property
    def owner(self):
        return self.__hidden_owner

    @owner.setter
    def owner(self, owner):
        self.hidden_owner = owner


    def info(self):
        print(f"{self.hidden_owner}의 포켓몬이 사용 가능한 스킬")
        for i in range(len(self.skills)):
            print(f'{i+1} : {self.skills[i]}')

        # for skill in self.skills:
        #     print(f'{skill}')

    def attack(self, idx):
        print(f'{self.skills[idx]} 공격 시전!')


class Pikachu(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "피카츄"
        print(f"{self.name}")

    def attack(self, idx):  # override
        print(f'{self.hidden_owner}의 {self.name}가 {self.skills[idx]} 공격(전기) 시전!')


class Ggoboogi(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f"{self.name}")

    def attack(self, idx):  # override
        print(f'{self.hidden_owner}의 {self.name}가 {self.skills[idx]} 공격(물) 시전!')

    def swim(self):
        print(f'{self.name}가 수영을 합니다')


class Pairi(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "파이리"
        print(f"{self.name}")

    def attack(self, idx):  # override
        print(f'{self.hidden_owner}의 {self.name}가 {self.skills[idx]} 공격(불) 시전!')


while True:
    print(f'포켓몬 개수 :{Pokemon.count}')
    menu = input('1) 포켓몬 생성  2) 프로그램 종료 : ')
    if menu == '2':
        print('프로그램을 종료합니다')
        break
    elif menu == '1':
        pokemon = input('1) 피카츄  2) 꼬부기  3) 파이리 : ')
        n = input('플레이어 이름 입력 : ')
        s = input('사용 가능한 기술 입력(/로 구분하여 입력) :')
        if pokemon == '1':
            p = Pikachu(n, s)
            p.__hidden_owner="한지우" #hidden앞에 __를 두개 넣어주면 한지우가 반영되지 못한다
        #     p.owner="한지우" -> property가 setter로 동작
        elif pokemon == '2':
            p = Ggoboogi(n, s)
        elif pokemon == '3':
            p = Pairi(n, s)
        else:
            print('메뉴에서 골라 주세요')
        p.info()
        attack_menu = input('공격 번호 선택 : ')
        p.attack(int(attack_menu)-1)
    else:
        print('메뉴에서 골라 주세요')

    Pokemon.count += 1