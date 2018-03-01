# -*- coding: UTF-8 -*-
from random import randint as ran
import sys
name = input('please tell me your name')
try:
    file = open('C:\\Users\lijiaqi-yd\PycharmProjects\FirstPython\\testfile\game.txt')
    lines = file.readlines()
    file.close()
except:
    print('open file error')
    sys.exit(0)
    # os.mknod('game.txt')
scores = {}
for line in lines:
    s = line.split()
    scores[s[0]] = s[1:]

score = scores.get(name)
if score is None:
    score = [0, 0, 0]
# print(score[0])

old_times = int(score[0])
min_times = int(score[1])
totle_times = int(score[2])
avg_times = 0

# 判断当前用户是不是第一次玩
if old_times > 0:
    avg_times = float(totle_times / old_times)
else:
    avg_times = 0
print('%s , play %d, min %d, avg %.2f' % (name, old_times, min_times, avg_times))


def isEqual(num2, answer2 = 0):
    if num2 > answer2:
        print("%d is too small" % answer2)
        return False

    elif num2 < answer2:
        print("%d is too big" % answer2)
        return False

    else:
        print("bingo,you answer is %s ,right answer is %s" % (answer2, num2))
        return True


num = ran(1, 5)
flag2 = False
print("guess what i think?")
temp_times = 0
while not flag2:
    # 当输入非数字时 循环继续
    try:
        answer2 = int(input())
    except:
        continue
    flag2 = isEqual(num, answer2)
    temp_times += 1
# 判断当前是第一次 还是最小的一次
if temp_times < min_times or min_times == 0:
    min_times = temp_times
totle_times += min_times
old_times += 1
scores[name] = [str(old_times), str(min_times), str(totle_times)]

result = ''
for n in scores:
    line = n + ' ' + ' '.join(scores[n]) + '\n'
    result += line
new_file = open('C:\\Users\lijiaqi-yd\PycharmProjects\FirstPython\\testfile\game.txt', 'w')
new_file.write(result)
new_file.close()

