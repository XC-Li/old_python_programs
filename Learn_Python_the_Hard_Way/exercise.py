# -*-  coding: utf-8 -*-

print "test" #中文注释
print u"为了巩固记忆，手打代码，不要偷懒（也不怎么费时间吧\n"
#ex1~ex4 省略了
#ex5 格式化字符

# my_name = 'Zed'
# my_age = 35;my_height = 74;my_weight = 180
# my_eyes = 'blue'
# my_teeth = 'white'
# my_hair = 'brown'
# print "let's talk about %s \nHe's %d inches tall"  %(my_name,my_height)
# print "if i add %d, %d and %d, I get %d" %(my_age, my_height, my_weight, my_age + my_height + my_weight)

#ex6
# x = "there are %d types of people" %(10+1)
# binary = "binary"
# do_not = "don't"
# y = "Those who know %s and those who %s." %(binary, do_not) #%s后面可以直接接字符
# print x
# print y
# print "I said : %r." %x
# print "I also said : %s." %y
# hilarious = False
# joke_evaluation = "Isn't that joke so funny?! %s"
# print joke_evaluation %hilarious
# w = "Left" ; e = "Right"
# print w + " " + e

#ex7
# print "\n"
# print "." *10
# end1 = "C"; end2 = "h"; end3 = "e"
# end4 = "e"; end5 = "s"; end6 = "e"
# print end1 + end2 + end3,
# print end4 + end5 + end6

#ex8
# formatter = "%s %r %r %r"
# print formatter %(1,2,3,4)
# print formatter %(u"一", "two\n", "three", "four")
# print formatter %(True, False, False, True)
# print formatter %(
    # "I had this thing",
    # "That you could type up right",
    # "But it didn't sing",
    # "So i said goodnight.")
    
#ex10
# print " "
# print "\' \" \r dfe"
# print "abc"

#ex11
print "This is an example:",
a= raw_input("input a:")
print type(a)
print "a is %s" %a
