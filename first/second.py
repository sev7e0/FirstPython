
# 字符串拼接
# strs = str(input("please input something"))
# a = []
# # 将输入的字符串按照规则填入元组
# a = strs.split(" ")
# print(a)

#字符串操作
word = "hellopython"
for i in word:
    print(i)
print('--------------------------')
print(word[2])
print('--------------------------')
print(word[:5])
print('--------------------------')
print("hyyd".join(word))
print('--------------------------')

#文件读取
file = open("C:\\Users\lijiaqi-yd\PycharmProjects\FirstPython\\testfile\data.txt")
con = file.read();
print(con)
file.close()
print('--------------------------')

file = open("C:\\Users\lijiaqi-yd\PycharmProjects\FirstPython\\testfile\data.txt")
# 解决换行回车\n问题
row = file.readline().splitlines()
print(row[0])
file.close()
print('--------------------------')

file = open("C:\\Users\lijiaqi-yd\PycharmProjects\FirstPython\\testfile\data.txt")
array = file.readlines()
# 解决回车\n问题
# array = ''.join(array).strip('\n')
print(array)
file.close()
print('--------------------------')
