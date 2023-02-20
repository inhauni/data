## 응용문제 13 -2
import random


def find_array(list, f_data):
    count =0
    for idx in range(len(list)):
        count +=1
        if list[idx]==f_data:
            return count
        if count == len(list):
            return f'{count} (목록에 존재하지 않는 정수)'



def find_binary(list, f_data):
    start=0
    end= len(list) - 1

    count =0

    while(start<=end):
        mid=(start+end) // 2
        count += 1
        if f_data == list[mid]:
            return count
        elif f_data > list[mid]:
            start = mid + 1
        else:
            end = mid -1

    return f'{count} (목록에 존재하지 않는 정수)'


r_list=random.choices(range(0,10000),k=1000000)
print(f'비정렬 배열(100만 개) --> {r_list[0:5]} ~~~ {r_list[-5:-1]}')

n_rlist=sorted(r_list)
print(f'정렬 배열(100만 개) --> {n_rlist[0:5]} ~~~ {n_rlist[-5:-1]}\n')

find_data=random.randrange(0,10000)
print(f'검색할 데이터 = {find_data}\n')
print(f'순차 검색(비정렬 데이터) --> {find_array(r_list,find_data)}회\n')
print(f'이진 검색(정렬 데이터) --> {find_binary(n_rlist,find_data)}회')

