# 励志公式
pay = 1.01
gain = 1.01 ** 365
print(gain)
#结果为37.8
pay_ = 0.99
gain_ = pay_ ** 365
print(gain_)
# 结果为0.03
# open(name,mode,encoding)
# namme 这是要打开的目标文件的字符串（可以包含文件所在的具体路径）。
# modr 这是指的文件打开方式：只读，写入，追加。
# encoding ：编码格式（推荐使用utf-8)
# 示例代码：
# f = open('a.txt','w',encoding="UTF-8")
# f.write("你好世界")
# print(type(f))
# f.close()
# # with方法自动关闭文件
# with open('a.txt','w',encoding="UTF-8") as f:
#     f.write("你好世界啊！！！")
# with open('a.txt','a',encoding="UTF-8") as f:
#     f.write(f'\n你好')
# 课后作业
count = 0
with open('D:\做题\word.txt','r') as f:
    for lis in f:
        lis = lis.strip()
        words = lis.split(" ")
        for i in words:
            if "it" in i:
                count += 1
print(count)
# content = f.read()
# count = content.count("it")
# print((count))
