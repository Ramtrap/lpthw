print "ex13.py\n"
# from sys import argv
#
# "sys" is a module, aka library
# modules give you features!
#
# script, first, second, third = argv
#
# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third

from sys import argv

script, first, second, third = argv
fourth = raw_input("What is your fourth variable called?: ")

print "The script is called::", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable, if you forgot, was called: ", fourth
