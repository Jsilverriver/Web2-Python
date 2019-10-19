# input("password?")
# python3 conditional.py를 terminal에 입력하면 끝나지 않고 password?라는게 뜨고, 그안에 사용자가 값을 입력하면 끝난다.
# 그리고 이 안에 값은 string값으로 들어간다.
"""user_id = input("ID?")
if user_id == "eungang":
    user_input = input("password?")
    if user_input == "111111":
        print("Hello Host!")
    else:
        print("1 who are you?")
else:
    print("2 who are you?")"""


# Logical Operator
user_id = input("ID?")
user_input = input("password?")

if (user_id == "eungang" and user_input == "111111") or (
    user_id == "megumi" and user_input == "222222"
):
    print("1 Hello Master")
elif user_id == "gyeongja" and user_input == "333333":
    print("2 Hello Master")
else:
    print("who are you?")
