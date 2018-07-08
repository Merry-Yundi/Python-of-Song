'''
描述
凯撒密码是古罗马恺撒大帝用来对军事情报进行加解密的算法
它采用了替换方法对信息中的每一个英文字符循环替换为字母表序列中该字符后面的第三个字符
即字母表的对应关系如下
原文：A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
密文：D E F G H I J K L M N O P Q R S T U V W X Y Z A B C 
对于原文字符P，其密文C满足如下条件： C=(P+3) mod 26
上述是凯撒密码的加密方法，其解密方法反之，即:P=(C-3) mod 26
假设用户可能使用的输入仅包含西文字母，即英文大小写字母a-zA-Z和特殊字符
请编写一个程序，对输入字符串进行凯撒密码加密，直接输出结果，其中特殊字符不进行加密处理

此题目是AutoOJ(自动评阅)类型，请注意：
1.输入使用input(''),不要加提示信息
2.输出与要求一致
3.不考虑异常输入情况

输入
示例1: python is GOOD!

输出
示例1：sbwkrq lv JRRG!
'''

# 恺撒密码 Caesar_cipher.py
import string
s = string.ascii_lowercase
S = string.ascii_uppercase
seq = s + s[0:3] + S + S[0:3]
a = input()
b = ''
for i in a:
    n = seq.find(i)
    if n > -1:
        b = b + seq[n+3]
    else:
        b = b + i

print(b)
