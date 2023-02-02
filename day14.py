

class Pokemon:

    def __init__(self, name, owner, skills): # name이라는 매개변수
        self.name = name # 받은 name을 속성.name에 저장
        # print(f'포켓몬 {name} 객체 생성됨')
        self.owner = owner # 받은 owner변수를 속성.owner에 저장
        self.skills = skills.split('/')
    def info(self):
        print(f'{self.owner}의 포켓몬은 {self.name}입니다.')
        for skill in self.skills:
            print(skill,end=' ')

#<상속>
class Pikachu(Pokemon): # 상속(inheritance) : 부모 class 는 pokemon / 자식 class는 pickchu
    pass

p1=Pokemon('피카츄','지우','백만 볼트/몸통박치기/전광속화') # 객체 생성
p2=Pokemon('꼬부기','이슬이','물대포/몸통박치기')

pi1 =Pikachu('피카츄','덴트','번개')
pi1.info()
