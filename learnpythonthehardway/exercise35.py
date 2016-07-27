# coding=utf-8
# 访问列表元素

# animals = ['bear', 'tuger', 'penguin', 'zebra']
# bear = animals[0]

from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"

	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you are not greedy, you win!"
		exit(0)
	else:
		dead("You are greedy bastard!")

gold_room()