# ex38
# Operation on lists

ten_things = "Apple Orange Crows Telephone Light Sugar"
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "corn", "Banana", "Girl", "boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "adding:", next_one
    stuff.append(next_one)
    print "there is %d items now" % len(stuff)

print "There we go:", stuff

print "do some more things."

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(" ".join(stuff))
print('#'.join(stuff[3:5]))
