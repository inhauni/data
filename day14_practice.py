print('<10. 1>\n')
class Thing():
    pass                    # java에서는 {}이용해서 class 생성

print(Thing)  # <class '__main__.Thing'> : (main 내의 class) Thing의 타입 출력

example=Thing()
print(example) # <__main__.Thing object at 0x00000080B9662FD0> : thing클래스를 복사한 example객체의 할당된 주소 출력

print('\n<10. 2>\n')

class Thing2:
    letters='abc' #문자열

print(Thing2.letters)
#  Thing2 class 내부의 letters 멤버변수 출력

print('\n<10. 3>\n')

class Thing3:
    def __init__(self, letters):     # 파이썬의 생성자함수 __init__(self)    *java는 -> public 클래스이름(){} 이런식으로 가능
                                      # 이때 self는 java의 this와 같은 역할 (할당된 주소정보를 가지고 있는 변수) 다만 java에선 숨겨진채로 함께 이동했고
                                    #  python에서는 드러낸 채로 같이 이동. 'self.변수'는 호출한 객체의 주소 정보를 가지고 있는, 객체가 복사한 stack에 존재하는 멤버변수를 의미함
        self._hletters = letters
                    #property의 영향으로 멤버변수 letters의 형태가 변한다 (ex hletters, _letters, __letters etc...)

    def info(self):
        print(self.letters)

    @property
    def letters(self):
        print('inside the getter', end=' ')
        return self._hletters  # __두개는 private , _한개는 protected 변수 지정 (다만 그 구속이 강제적인 것은 아니다)


t3=Thing3('xyz')  # t3 = Thing3 생성자를 불러내어 Thing3 class를 복사하여 만든 객체. 이때, _letters 변수에 xyz를 대입

print(t3)
t3.info()       # @property 아래의 letters를 출력하는 메서드 -> inside the getter를 먼저 print하고 self._letters를 return한 값을 print한다


# t3.letters      # -> info()메서드 안의 self.letters를 호출 : inside the getter만 출력

# t3.letters='zyx'    # if letters 멤버 변수를 property를 이용해서 READ ONLY로 바꾸면-> 오류 발생
                        # Because 외부 접근이 차단, 변수로 직접 접근이 불가능해짐 (멤버변수의 이름이 바뀌기 때문)

# t3.hletters='zyx'     # (멤버 변수가 public일 경우만 변경 가능)
# t3._hletters = 'zyx'  # 값 직접 변경 가능 (protected)  (멤버 변수가 protected일 경우만 직접 변경 가능)
# t3.__hletters='zyx' # 값 직접 변경 불가 (private)   (멤버 변수가 어떤 타입 이든 변경 불가능)


# t3=Thing3('zyx') #t3에 새로운 주소를 배정 받은 new 객체를 다시 할당한 것. 기존의 t3과는 다르다

# print(t3)  # 위의 문장에 대한 증명 : 첫번째 t3과 주소 값이 다름 (=새로운 별도의 객체 주소에 'zyx' 를 넣은 후, t3변수가 가리 키게 한 것)
t3.info()   # @property 아래의 letters를 출력 하여 inside the getter 출력 후 return 값인 self.letters('zyx')를 출력

print('\n<10. 4, 10. 5>\n')

class Element:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number

    def dump(self):
        print(f'{self.name} 원소의 약칭은 {self.symbol}이고, 원소번호는 {self.number} 입니다.')


e1=Element('Hydrogen','H',1) # 객체 생성

el_dict={keyz:vals for keyz,vals in zip(('name','symbol','number'), (e1.name,e1.symbol,e1.number))}

print(el_dict) # dic 생성

# hydrogen=Element(el_dict['name'],el_dict['symbol'],el_dict['number'])
hydrogen=Element(**el_dict) # **kwargs는 함수 외부에서 딕셔너리 kwargs를 이름=값 형태의 인수(키워드 인수)로 분해한다.
                            # 따라서, name=Hydrogen라는 키워드 인수가 Element 클래스에 대입됨.

print(f'이름 : {hydrogen.name}, symbol : {hydrogen.symbol}, 순서 : {hydrogen.number}')

print('\n<10. 6>\n')

hydrogen.dump()

print('\n<10. 7>\n')

print(hydrogen)  # 객체를 출력하면 클랙스가 복사되며 배당된 고유 주소값이 출력됨

class Element2(Element):            # Element를 상속받는 자식 class
    def __init__(self,name,symbol,number):
        super().__init__(name,symbol,number) # name symbol number를 매개변수로 받는 상위 클래스인 Element의 생성자 호출 (상속의 취지 =코드의 중복 최소화)


    def __str__(self):
        return f'{self.name} 원소의 약칭은 {self.symbol}이고, 원소번호는 {self.number} 입니다.'

hydrogen2=Element2(**el_dict)
print(hydrogen2) # __str__ 이 반환됨 (내부함수이기 때문??)


print('\n<10. 8>\n')


# <name 속성만 private로 바꿔본 예시>

print(f'1] getter / setter method\n')


class Element:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number

    def dump(self):
        print(f'{self.name} 원소의 약칭은 {self.symbol}이고, 원소번호는 {self.number} 입니다.')

    def get_name(self):
        print('inside the getter',end=' ')
        return self.name
    def set_name(self, name):
        print('inside the setter')
        self.name = name

e2=Element('ox','O',8)
print(e2.get_name())
e2.set_name('oxygen')
print(e2.get_name())


print(f'\n2-1] Use property (name 구문 이용)\n')

class Element:
    def __init__(self,input_name,symbol,number):
        self.hidden_name=input_name
        self.symbol=symbol
        self.number=number

    def dump(self):
        print(f'{self.hidden_name} 원소의 약칭은 {self.symbol}이고, 원소번호는 {self.number} 입니다.')


    def get_name(self):
        print('inside the getter',end=' ')
        return self.hidden_name

    def set_name(self, name):
        print('inside the setter')
        self.hidden_name = name

    name = property(get_name, set_name)

e3=Element('Helyum','He',2)

print(e3.name)  # getter에 접근 (속성처럼 name에 접근 가능)
e3.name='Helium'  # setter에 접근
print(e3.name)

print(f'\n2-2] Use property (decorator 사용)\n')

class Element:
    def __init__(self,input_name,symbol,number):
        self.hidden_name=input_name
        self.symbol=symbol
        self.number=number

    def dump(self):
        print(f'{self.hidden_name} 원소의 약칭은 {self.symbol}이고, 원소번호는 {self.number} 입니다.')

    @property
    def name(self):
        print('inside the getter',end=' ')
        return self.hidden_name

    @name.setter
    def name(self, name):
        print('inside the setter')
        self.hidden_name = name

e4=Element('리튬','Li',3)

print(e4.name)
e4.name='Lithium'
print(e4.name)


print(f'\n 10. 8 예시\n')

class Element:
    def __init__(self,input_name,symbol,number):
        self.hidden_name=input_name
        self.hidden_symbol=symbol
        self.hidden_number=number


    @property
    def name(self):
        print('inside the getter',end=' ')
        return self.hidden_name

    @property
    def symbol(self):
        print('inside the getter', end=' ')
        return self.hidden_symbol

    @property
    def number(self):
        print('inside the getter', end=' ')
        return self.hidden_number

    # @name.setter  -> 속성에 대한 setter 프로퍼티를 명시하지 않을 경우 외부로부터 속성 설정 불가 : 읽기 전용이 된다 (READ ONLY)
    # def name(self, name):
    #     print('inside the setter')
    #     self.hidden_name = name
    #
    # @symbol.setter
    # def symbol(self, symbol):
    #     print('inside the setter')
    #     self.hidden_symbol = symbol
    #
    # @number.setter
    # def numberset(self, number):
    #     print('inside the setter')
    #     self.hidden_number = number


e5=Element('베릴륨','Be',4)

print(e5.name)
# e5.name ='Beryllium' -> 오류 발생 : can't set attribute (Setter가 지정되지 않아 이런 형식으로는 외부에서 속성을 건들 수 없다)



print('\n<10. 9>\n')

#   class가 직접 대입됨
class Bear:

    @classmethod
    def eats(cls):
        # print(cls) # -> <class '__main__.Bear'> 라는 타입이 출력
        return f'\'berries\' ({cls.__name__})'

class Rabbit:

    @classmethod
    def eats(cls):
        return f'\'clover\' ({cls.__name__})'

class Octothorpe:

    @classmethod
    def eats(cls):
        return f'\'campers\' ({cls.__name__})'

# print(Bear) # -> <class '__main__.Bear'> 이 출력되고 이는 cls의 출력값과 같다. 따라서 cls는 class 자기자신이다

print(Bear.eats(),Rabbit.eats(),Octothorpe.eats(),"\n")

# -> 'berries' (Bear) 'clover' (Rabbit) 'campers' (Octothorpe) 출력

#객체의 주소가 self에 대입됨
class Bear:

    def eats(self):
        # print(self) # -> <__main__.Bear object at 0x00000066F7BDE970> 라는 객체의 주소가 출력
        return 'berries'

class Octothorpe:

    def eats(self):
        return 'campers'

class Rabbit:


    def eats(self):
        return 'clovers'

bear=Bear()
# print(bear) # -> <__main__.Bear object at 0x00000057E626E970> 이 객체의 주소는 위와 동일하다. 따라서 self = 복사된 객체의 주소값을 저장하는 변수

rabbit=Rabbit()
octothorpe=Octothorpe()

print(bear.eats(),rabbit.eats(),octothorpe.eats(),"\n")


print('\n<10. 10>\n')

class Laser:
    def does(self):
        return 'disintegrate'


class Claw:
    def does(self):
        return 'crush'


class Smartphone:
    def does(self):
        return 'ring'

class Robot:
    # def __init__(self,laser,claw,smart):
        # self.laser=laser
        # self.claw=claw
        # self.smart=smart
    def __init__(self):
        self.laser=Laser()  # 여기서 바로 self.laser를 Laser class의 객체로 생성
        self.claw=Claw()
        self.smart=Smartphone()
    def does(self):
        return f'Laser : {self.laser.does()}, Claw : {self.claw.does()}, Smartphone : {self.smart.does()}\n'
         # -> self.laser가 객체이므로 바로 does() 함수 호출 가능


# l=Laser()
# c=Claw()
# s=Smartphone()
# r=Robot(l.does(),c.does(),s.does())
# r.does()

robbie=Robot()
print(robbie.does())



