x = "There are %d kind of people." % 10
binary = "binary"
do_not = "don't"

y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y


hilarious = False
joke_evaluation = "Isn't this joke funny?! %r"

print joke_evaluation % hilarious

w = "My name is....."
e = "Iron man"

print w + e
