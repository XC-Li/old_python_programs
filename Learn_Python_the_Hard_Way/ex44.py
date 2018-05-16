class Parent(object):

    def override(self):
        print "Parent override()"

    def implicit(self):
        print "Parent implict()"

    def altered(self):
        print "Parent altered()"


class Child(Parent):

    def override(self):
        print "Child override()"

    def altered(self):
        print "Child, BEFORE PARENT Altered()"
        super(Child, self).altered()
        print "Child, AFTER PARENT Altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
