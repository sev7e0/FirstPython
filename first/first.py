# -*- coding: UTF-8 -*-
from random import randint

print('hello world')

print(1 + 2 * 3)

print(5 < 50)

# print("who you are?")
# name = input()
# print("oh yes ,you are ")
# print(name)
#
a = True
b = not a
print('this is a %s' % 'demo')
print('---------------------------------')

# num = randint(5, 10)
# print("guess what i think?")
# flag = False
# while not flag:
#     answer = int(input())
#
#     if num > answer:
#         print("%d is too small" % answer)
#
#     if num < answer:
#         print("%d is too big" % answer)
#
#     if num == answer:
#         print("bingo,you answer is %s ,right answer is %s" % (answer, num))
#         flag = True


# 通过调用函数来实现计算
def isEqual(num2, answer2):
    if num2 > answer2:
        print("%d is too small" % answer2)
        return False

    elif num2 < answer2:
        print("%d is too big" % answer2)
        return False

    else:
        print("bingo,you answer is %s ,right answer is %s" % (answer2, num2))
        return True


num = randint(1, 5)
flag2 = False
print("guess what i think?")
while not flag2:
    answer2 = int(input())
    flag2 = isEqual(num, answer2)

print('------------------------------')


a = 0
for i in range(1, 101):
    a = a + i
print(a)

print('--------------------------------------')
# 整数类型 0包括0.0 为false 其他为 true
# 字符串 空串包括“” ‘’为 false其他为 true
print(bool(-122))
print(bool(0))
print(bool(122))
print(bool('abc'))
print(bool(''))
print(bool('False'))
