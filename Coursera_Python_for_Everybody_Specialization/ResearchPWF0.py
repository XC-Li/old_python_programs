#The research on "probability weighting function"
#Designed By Xiaochi Li
#Oct. 2015
import os
#初始参数设定
k = 1.0/15 #相对盈利系数
m = 0.3    #相对盈利系数上升速度
a0 = -0.1
b0 = -0.1
n = 1      #相对盈利系数上升级数
r = 5      #最大上升级数
a = 4000
pa = 0.8
b = 4000
pb =0.2
print u"这是一个行为经济学实验"
os.system('pause')
def hypo1(n):
    pi = a * pa *(a0+m*n)
    return pi
def hypo2(n):
    pi = b * pb *(b0+m*n)
    # pi = b * pb / (k * (1+n*m) + 1)
    return pi
flag1 = False 
flag2 = False
c_1 = 0
c_2 = 0
print a*pa,b*pb
for n in range(r+1):
    print n, hypo1(n),hypo2(n)
for n in range(r+1):
    if flag1 is False:
        # os.system('cls')
        print u"如果你有两个选择："
        print u"选择1:你有",int(pa*100),u"%的几率获取",a,u"元，  ",int(100-pa*100),u"%的几率获得0" #理智
        print u"选择2:你有100%的几率获取",hypo1(n)                 #不理智
        print u"你会选择：(输入1或者2后按回车)"
        choice = raw_input()
        if choice == '1':
            if a * pa > hypo1(n):
                print 'yes1'
                c_1 = a*pa
                flag1 = True
        if choice == '2':
            if a*pa < hypo1(n):
                print 'yes2'
                c_1 = hypo1(n)
                flag1 = True
    if flag2 is False:
        # os.system('cls')
        print u"如果你有两个选择："
        print u"选择1:你有",int(pb*100),u"%的几率盈利",b,u"元，  ",int(100-pb*100),u"%的几率盈利0"
        print u"选择2:你有100%的几率盈利",hypo2(n)                 #不理智
        print u"你会选择：（输入1或者2后按回车）"
        choice = raw_input()
        if choice == '1':
            if b * pb > hypo2(n):
                print 'yes3'
                c_2 = b*pb
                flag2 = True
        if choice == '2':
            if b*pa < hypo2(n):
                print 'yes4'
                c_2 = hypo2(n)
                flag2 = True
print 'done',c_1,c_2
c_1 = str(c_1)
c_2 = str(c_2)
tf = open('testfile.txt','a')
tf.write(c_1)
tf.write(',')
tf.write(c_2)
tf.write('\n')
tf.close()