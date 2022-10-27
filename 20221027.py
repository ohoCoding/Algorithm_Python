##6. 집합 자료형
s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello")
print(s2)

l1 = list(s1)
print(l1)

print(l1[0])

t1 = tuple(s1)
print(t1)
print(t1[0])


s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

## 교집합
print(s1 & s2)
print(s1.intersection(s2))

## 합집합
print(s1 | s2)
print(s1.union(s2))

## 차집합
print(s1 - s2)
print(s2 - s1)

print(s1.difference(s2))
print(s2.difference(s1))

## 값 1개 추가하기
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

## 값 여러개 추가하기
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

## 특정 값 제거하기
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)
