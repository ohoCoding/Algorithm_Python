# 3.리스트 자료형
##1. 리스트 생성
odd = [1, 3, 5, 7, 9]
print(odd)


##2. 리스트 인덱싱과 슬라이싱
a = [1, 2, 3]
print(a)
print(a[0])
print(a[0] + a[1])


##3. 리스트
a = [1, 2, 3, ["a", "b", "c"]]
print(a)
print(a[-1])
print(a[3])
print(a[-1][0])
print(a[-1][1])

##3.1 리스트 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])
a = "12345"
print(a[0:2])

a = [1, 2, 3, 4, 5]
print(a[:2])
print(a[2:])

##3.2 리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

##3.3 리스트 반복
a = [1, 2, 3]
print(a * 3)

##3.4 리스트 길이 구하기
a = [1, 2, 3]
print(len(a))

##3.5 리스트의 수정과 삭제
a = [1, 2, 3]
print(a[2])

##3.6 리스트에서 값 수정
a = [1, 2, 3]
a[2] = 4
print(a)

##3.7 del 함수 사용해 리스트 요소 삭제
a = [1, 2, 3]
del a[1]
print(a)
a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

##3.8 리스트 관련 함수
a = [1, 2, 3]
a.append(4)
print(a)

a = [1, 6, 2, 4]
print(a)
a.sort()
print(a)

##3.9 리스트 뒤집기
a = ["a", "c", "b"]
print(a)
a.reverse()
print(a)

##3.10 위치 반환
a = [1, 2, 3]
print(a.index(3))

##3.11 리스트에 요소 삽입
a = [1, 2, 3]
print(a)
a.insert(0, 4)
print(a)
a.insert(3, 5)
print(a)


##3.12 리스트 요소 제거
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

##3.13 리스트 요소 끄집어내기(pop)

