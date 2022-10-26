## 4 튜플 자료형

##4.1 튜플 요소 값 삭제할때
t1 = (1, 2, "a", "b")

##4.2 인덱싱
print(t1[0])

##4.3 슬라이싱
print(t1[1:])

##4.4 튜플 더하기
t2 = (3, 4)
print(t1 + t2)

##4.5 튜플 곱하기
print(t2 * 3)

##4.6 튜플 길이 구하기
print(len(t1))

##5 딕셔너리 자료형
##5.1 딕셔너리 정의
a = {1: "hi"}
print(a)

##5.2 딕셔너리 쌍 추가
a = {1: "a"}
a[2] = "b"
print(a)
a["name"] = "pey"
print(a)
a[3] = [1, 2, 3]
print(a)

##5.3 딕셔너리 요소 제거
del a[1]
print(a)


##5.4 딕셔너리에서 key 사용해 value 얻기
grade = {"pey": 10, "juliet": 90}
print(grade["pey"])

##5.5 딕셔너리 관련함수
##5.5.1 key리스트 만들기
a = {"name": "pey", "phone": "0123456789", "birth": "1119"}
print(a.keys())
for k in a.keys():
    print(k)
print(list(a.keys()))
##5.5.2 key, value 쌍 얻기
print(a.items())
##5.5.3 key, value 쌍 모두 지우기
a.clear()
print(a)
##5.5.4 key로 value 얻기
a = {"name": "pey", "phone": "0123456789", "birth": "1119"}
print(a.get("name"))
print(a.get("phone"))
##5.5.5 해당 key가 딕셔너리 안에 있는지 조사
a = {"name": "pey", "phone": "0123456789", "birth": "1119"}
print("name" in a)
