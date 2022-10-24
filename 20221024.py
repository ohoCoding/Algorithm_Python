##왼쪽 정렬
print("{0:<10}".format("hi"))
## 오른쪽 정렬
print("{0:>10}".format("hi"))
## 가운데 정렬
print("{0:^10}".format("hi"))
## 공백채우기
print("{0:=^10}".format("hi"))
## 소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y))
## 문자 표현하기
print("{{and}}".format())
## f 문자열 포맷팅
name = "홍길동"
age = 30
print(f"나의 이름은{name}입니다. 나이는 {age} 입니다.")
print(f"나는 내년이면 {age+1}살이 된다!")

# 딕셔너리 f문자열 포매팅
d = {"name": "홍길동", "age": 30}
print(f'나의 이름은 {d["name"]} 입니다. 나이는 {d["age"]} 입니다.')

##문자열 관련 함수
# 1. 문자 개수 세기
a = "hobby"
print(a.count("b"))

# 2.1 위치 알려주기
a = "Python is the best choice"
print(a.find("b"))

# 2.2 위치 알려주기
a = "Life is too short"
print(a.index("t"))

# 3. 문자열 삽입
print(",".join("abcd"))
print(",".join(["a", "b", "c", "d"]))

# 4. 소문자를 대문자로 바꾸기
a = "hi"
print(a.upper())

# 5. 대문자를 소문자로 바꾸기 
a ="HI"
print(a.lower())