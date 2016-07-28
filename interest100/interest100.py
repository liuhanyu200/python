# coding=utf-8
# 求 0~9这十个数字可以组成多少不重复的3位数
# a:1-9 b:0-9 c:0-9
def count_no_r():
	l = range(10)
	count = 0

	for a in l[1:]:
		for b in l:
			if a == b: continue # 过滤 a == b
			for c in l:
				if c != a and c != b:
					print a,b,c
					count += 1
	print 'count:', count

# count_no_r() # 648


# 求 水仙花数
def  isArmstrongNumber(n):
	a = []
	t = n
	while t > 0:
		a.append(t % 10)
		t /= 10
	k = len(a)
	return sum([x ** k for x in a]) == n

# for x in range(100,1000):
# 	if isArmstrongNumber(x):
# 		print x

def isPerfectNumber(n):
	a = 1
	


