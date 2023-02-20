## 응용문제 13 -1

import random

def find_product(list,find_product):

    position=-1
    start=0
    end=len(list)-1

    while(start<=end):
        mid=(start+end)//2
        if find_product==list[mid]:
            return mid
        elif find_product > list[mid]:
            start = mid + 1
        else:
            end=mid-1

    return position



products=['cake','milk','pizza','orange juice','candy','ice cream']
sells = random.choices(products, k=10)

print(f'오늘 판매된 전체 물건 (중복0,정렬x) ==> {sells}')
sells.sort()                     # 정렬 완 (이진트리 구현 전제조건 충족)
print(f'오늘 판매된 전체 물건 (중복0,정렬0) ==> {sells}')
print(f'오늘 판매된 전체 물건 (중복x,정렬0) ==> {sorted(list(set(sells)))}')  # set 는 중복 x-> 다시 list 타입으로 변환 -> 정렬

products_idx=[]

for product in list(sorted(list(set(sells)))):
    count, pos = 0,0

    while(True):
        pos = find_product(sells, product)
        if pos != -1:
            count += 1
            del(sells[pos])
        else:
            break

    products_idx.append([product, count])


print(f'결산 결과 ==> {products_idx}')





