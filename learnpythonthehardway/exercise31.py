print "You enter a dark room with two doors. Do you go through the door #1 or #2?"

door = raw_input("> ")

if door == '1':
	print "There is a giant bear here eating a cheese cake. What do you do?"
	print "1.Take the cake."
	print "2.Scrime at the bear."

	bear = raw_input("> ")

	if bear == '1':
		print "The bear eats your legs off. Good job!"
	elif bear == '2':
		print "the bear eats your legs off. Good job!"
	else:
		print "well,doing %s is probably better. Bear runs away." % bear

elif bear == '2':
	print "You stare into the endless abyss at Cthu1hu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")