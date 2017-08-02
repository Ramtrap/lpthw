name = 'William C. Dutcher'
age = 37 # not a lie
height = 68.75 # inches
cm = 2.54 # centimeters
weight = 235 # lbs
kilo = 0.45359237 # kilos
eyes = 'Green'
teeth = 'White'
hair = 'Black'
print '%f' % kilo
print "Let's talk about %s." % name
print "He's %.2f inches tall." % height
print "That is %.2f centimeters tall." % (height * cm)
print "He's %d pounds heavy." % weight
print "That is %.2f kilos." % (weight * kilo)
print "Actually, that's way too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
#r_kilo = round(kilo)
print round(kilo)
print round(1.7333)
print "The rounded version of %f is: %f" % (kilo, round(kilo))
