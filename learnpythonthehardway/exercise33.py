#-*-coding=utf-8-*-
# while 练习

def opnum(index):
	i = 0
	numbers = []

	while i < index:
		print "At the top i is %d" % i
		numbers.append(i)
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

# 没读懂题目
def opnum_new(index, line):
	i = 0
	numbers = []

	while i < index:
		print "At the top i is %d" % i
		numbers.append(i)
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

if __name__ == '__main__':
	opnum(5)