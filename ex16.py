from sys import argv

print "ex16.py\n"

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
# Above is too long, this is truncated below
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "Now let's take a look at what it says!"
raw_input("Press ENTER to continue:")

print "Here's your file %r:" % filename
print "\n"
target = open(filename, 'r')
print target.read()


print "And finally, we close it."
target.close()

# print "Type the filename again:"
# file_again = raw_input("> ")
#
# txt_again = open(file_again)
#
# print txt_again.read()

# txt.close
# txt_again.close

# print "Your files, %r and %r, have been closed." % (filename, file_again)
