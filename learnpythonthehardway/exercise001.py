import re

def pp(pwd):
	pattern = r"^[a-zA-Z][A-Za-z0-9_]{4,10}[a-zA-Z0-9]$"
	p = re.compile(pattern)
	m = p.match(pwd)
	if m:
		print m.group()
	else:
		print 'Not Match'

def valid_password(pwd):
	# pattern2 = "\w[\\w\\d_]{2,10}[\\w\\d]"
	# pattern1 = r"^a"
	# pattern = re.compile(pattern2)
	# test = re.match(pattern, pwd)
	# test1 = re.match(pattern1, pwd)
	pattern = r"a\w{0,3}b"
	# pattern = r"\d{2,5}"
	pt = re.compile(pattern)
	test = re.match(pt,pwd)
	test1 = re.findall(pt,pwd)
	print test1
	# print test1.group()
	# print test.group()
	# print test.start()
	# print test.end()
	# print test1.span()

# if(valid_password('ahi_23ha')):
# 	print "Yes"
# else:
# 	print "No"
def prime_numbers():
	for i in range(2,101):
		fg = 0
		for j in range(2,i/2):
			if i%j == 0:
				fg=1
				continue
		if (fg == 0):
			print i

def cap_string(str):
    print str.split(', 'or' ')

def cap_string_new(str1):
	pattern = r"\w+"
	p = re.compile(pattern)
	m = re.findall(p,str1)
	# print len(m)
	i = 0
	ss = []
	for i in range(len(m)):
		# m[i][0].upper()
		ss.append(m[i].capitalize())
		# i = i + 1
	print m
	print ss

# valid_password('r221asdb4safgb1lab_jadbafbhbabuabab')
pp('a121a1')
prime_numbers()
cap_string('hello world, my name is liuhanyu, nice too meet you!')
cap_string_new('hello wor1ld, my name is liuha1nyu, nice too meet you!')