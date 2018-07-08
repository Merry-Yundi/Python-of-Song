'''
描述
给定括号的个数，编写一个程序生成所有格式正确的括号组合。
输入格式
输入一个整数
输出格式
输出一个列表，每个元素是一个字符串，表示一个可能的括号组合。
输入输出示例
示例1   输入   输出
       3     ['((()))','(()()','(())()','()(())']
'''
# 合法括号组合的生成 Legal_bracket.py 
def foo(output,open,close,pairs):
    if open == pairs and close == pairs:
        ls.append(output)
    else:
        if open < pairs:
            foo(output+'(',open+1,close,pairs)
        if close < open:
            foo(output+')',open,close+1,pairs)
n = eval(input())
ls = []
foo('',0,0,n)
print(ls)
