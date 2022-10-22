##202210222
##문자열 연산하기
##1. 문자열 더해서 연산
head = "python"
tail = "is fun"
print(head + tail)
##2 문자열 곱하기
a = "python"
print(a * 2)
##3 문자열 곱하기 응용
print("=" * 50)
print("my program")
print("=" * 50)


##문자열과 인덱싱과 슬라이싱
##1 문자열 인덱싱
print("문자열 인덱싱")
a = "Life is too short, You need Python"
print(a[3])
print("파이썬은 0부터 숫자를 센다")
##2 문자열 인덱싱 활용
print(a[12])
print(a[-0])
##3 문자열 슬라이싱
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:4])
print(a[19:])
print(a[:17])
print(a[:])
print(a[19:-7])
##4 슬라이싱으로 문자열 나누기
c = "20010331Rainy"
date = c[:8]
weather = c[8:]
year = c[:4]
day = c[4:8]
print(date)
print(weather)
print("연도", year)
print("날짜", day)
##5문자열 교체
e = "Pithon"
print(e[1])
print(e[:1] + "y" + e[2:])

##문자열 포맷팅
##1. 숫자바로 대입
print("I eat %d apples" % 3)
##2. 문자열 바로 대입
print("I eat %s apples" % "five")
##3. 숫자값을 난타내는 변수 대입
number = 10
print("I eat %d apples" % number)
##4. 2개이상의 값 넣기
number = 8
day = "four"
print("I ate %d apples. so I was sick for %s days" % (number, day))

##포맷코드와 숫자함께 사용
##1. 정렬과 공백
print("%10s" % "hi")
##2. 소수점 공백
print("%0.4f" % 3.42134324)
print("%10.4f" % 3.42134234)

# format함수를 사용한 포맷팅
##1. 숫자 바로 대입
print("I eat {0} apples".format(11))
##2. 문자열 바로 대입
print("I eat {0} apples".format("six"))
##3. 숫자값으 가진 변수로 대입
number = 4
print("I eat {0} apples".format(number))
##4. 2개 이상의 값 넣기
number = 3
day = "two"
print("I ate {0} apples. so I was hungry for {1} days".format(number, day))
##5. 이름으로 넣기
print("I ate {number} apples. so I was hungry for {day} days".format(number=10, day=3))
##6. 인덱스와 이름 혼용해서 넣기
print("I ate {0} apples. so I was hungry for {day} days.".format(15, day=5))
