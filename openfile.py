#打开文件
file=open("filename","mode")
#mode
#1."r" 只读
#2.”w" 写入


#读取文件
content=file.read()
lines=file.readlines()#逐行读取

#写入文件内容
file.write()
file.writelines()

#关闭
file.close()
with open()  as file:#自动关闭

#预防错误
try:
    with open('filename', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('文件未找到')
except IOError:
    print('读取文件时发生错误')

#文件指针
seek(0)
print(file.tell())
