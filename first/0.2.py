# -*- coding: UTF-8 -*-


# about 'break' and 'continue'
print("---------this is %s test---------" % 'break')
# while True:
#     a = input()
#     if a == "break":
#         break

print("---------this is %s test---------" % 'continue')

for i in range(1, 10):
    if i == 5:
        continue
    print(i)

print("---------this is %s test---------" % 'Exception')

try:
    file = open('test.txt')
    print('file is opend')
    file.close()
except:
    print('file is not found')
print('finish')

print("---------this is %s test---------" % 'dictionary')

dic = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40
}
# delete dictionary
del dic['b']
# add dictionary
dic['e'] = 50
for key in dic:
    print(dic[key])

