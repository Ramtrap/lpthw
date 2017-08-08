from sys import argv

print "ex16.py\n"

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

# print "Type the filename again:"
# file_again = raw_input("> ")
#
# txt_again = open(file_again)
#
# print txt_again.read()

txt.close
# txt_again.close

# print "Your files, %r and %r, have been closed." % (filename, file_again)
