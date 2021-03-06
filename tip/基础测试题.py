# 题 1
# 检查密码规则合法性
# 考察基本编码能力和字符串处理
# 参考 python 文档的字符串库

# 给定一个字符串，用以下规则检查合法性
# 完全符合返回 True，否则返回 False
# 1，第一位是字母
# 2，只能包含字母、数字、下划线
# 3，只能字母或数字结尾
# 4，最小长度2
# 5，最大长度10
import re

def valid_password(pwd):
	pattern = r"^[a-zA-Z][A-Za-z0-9_]{0,8}[a-zA-Z0-9]$"
	test = re.match(pattern, pwd)
	print test    

# valid_password('hi_23ha')

# 题 2
# 返回 100 内的素数列表
# 考察基本的循环和选择概念、列表的使用

def prime_numbers():
	for i in range(2,101):
		fg = 0
		for j in range(2,i/2):
			if i%j == 0:
				fg=1
				continue
		if (fg == 0):
			print i

# 题 3
# 给定一个只包含字母的字符串，返回单个字母出现的次数
# 考察字典的概念和使用
# 返回值为包含元组的列表，格式如下（对列表中元组的顺序不做要求）
# 参数 "hello"
# 返回值 [('h', 1), ('e', 1), ('l', 2), ('o', 1)]

def letter_count(str):




# 题 4
# 给定一个英文句子（一个只有字母的字符串），将句中所有单词变为有且只有首字母大写的形式

def cap_string(str1):
    pattern = r"[a-zA-Z]+"
    p = re.compile(pattern)
    m = re.findall(p,str1)
    ss = []
    for i in range(len(m)):
    	ss.append(m[i].capitalize())
    return ss



# 题 5
# 写一个 Queue 类，它有两个方法，用法如下

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue()) # 1
print(q.dequeue()) # 2
print(q.dequeue()) # 3