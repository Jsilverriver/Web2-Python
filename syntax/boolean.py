# number, 정확히는 Integer
print(1)
# String
print("Hello Python")
# Boolean
# true, flase 값은 앞에 첫글자가 'T' , 'F' 이렇게 대문자이어야만 하는것 같다?
print(True)
print(False)
# Expression 값을 표현한다는 개념..
print(1 + 1)  # 숫자2를 표현하는 표현식이라 말할수 있다.
print("Hello " + "World")  # 표현식, 결합 연산자, 이항 연산자.
# Comparision operator, 비교 연산자.
print(1 == 1)
print(1 < 2)
print(2 < 1)
print(
    "Hello" in "Hello world"
)  # True. 'in' membership operator 앞에 있는 값이 뒤에있는 값에 들어가 있는지 없는지 불리언으로 나타내주는 연산자.
# 현재 디렉토리에 자기 자신의 파일이 있는지 없는지 알고싶을때?
# python3 check exist file in directory 검색.
import os.path  # 'os' 일종의 명령들을 모아놓은 디렉토리 밑에 패스라는 디렉토리 밑에있는 명령들을 import(가져온다)한다는 명령.

os.path.exists("boolean.py")  # 그 밑에 존재하냐? 존재하면 True를 불리언 값으로 나타내줌.

