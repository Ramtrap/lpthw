from sys import argv

print "ex14.py\n"

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "How old are you, %s?" % user_name
age = raw_input(prompt)
age = int(age)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you are %r years old. Nice.
""" % (likes, lives, age)