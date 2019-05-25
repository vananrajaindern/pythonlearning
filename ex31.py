print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There is a giant bear eating a cheesecake. What do you do?"
    print "1. Take the cake"
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "Well done the bear eats off your face!"
    elif bear == "2":
        print "The bear eats off your legs, haha!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck!"

else:
    print "You stumble around and fall on a knife and die. Good job!"
