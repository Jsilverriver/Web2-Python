a = ["a", 12, 77, "b"]
s = [1, "four", 9, 16, 25]
print(s)  # [1, "four", 9, 16, 25]
print(s[1])  # "four"
print(len(s))  # 5
s[1] = 4
print(s)  # [1, 4, 9, 16, 25]

a.remove(77)
print("a = {value}".format(value=a))  # a = ["a", 12, "b"]

del s[0]
print("s = {value}".format(value=s))  # s = ["four", 9, 16, 25]
del s[0:1]
print("s = {value}".format(value=s))  # s = [9, 16, 25]
del s[:]
print("s = {value}".format(value=s))  # s = []

a.append(1)
print(a)  # ['a', 12, 'b', 1]

a.insert(len(a), "new")
print(a)  # ['a', 12, 'b', 1, 'new']

