#The research on "probability weighting function"
#Designed By Xiaochi Li
#Oct. 2015
#coding:utf-8
import os
import time
#初始参数设定
n = 1      #上升级数
r = 5      #最大上升级数
a = 40431.25
pa = 0.8
b = 40431.25
pb =0.2
count = 0 #一共做了几题
print u"这是一个行为经济学实验"
# os.system('pause')
def hypo1(n):
    pi = 32000 - 800 * n 
    return p1

def hypo2(n):
    pi = 8000 + 100 * n 
    # pi = b * pb / (k * (1+n*m) + 1) #曾经的想法
    return pi
os.system('pause') 
start_time = time.time()           #记录实验开始的时间
p_time = time.time()
print p_time
flag1 = False 
flag2 = False
c_1 = 0
c_2 = 0
print a*pa,b*pb
for n in range(r+1):
    print n, hypo1(n),hypo2(n)
    
for n in range(r+1):
    if flag1 is False:
        os.system('cls')
        print u'第',2*n+1,u'题'
        print u"如果你有两个选择："
        print u"选择1:你有",int(pa*100),u"%的几率获取",a,u"元，  ",int(100-pa*100),u"%的几率获得0" 
        print u"选择2:你有100%的几率获取",hypo1(n)                 
        print u"你会选择：(输入1或者2后按回车)"
        p_time = time.time()             #开始计时
        count = count + 1
        choice = raw_input()
        if choice == '1':
            if a * pa > hypo1(n):
                print 'rational1'
                c_1 = a*pa
                c_11 = hypo1(n)
                flag1 = True
                time_1 = time.time()-p_time
                comment_1 = 'r_1' #rational choice
        if choice == '2':
            if a*pa < hypo1(n):
                print 'irrational1'
                c_1 = hypo1(n)
                c_11 = a*pa
                flag1 = True
                time_1 = time.time()-p_time
                comment_1 = 'i_1' #irrational choice
    if flag2 is False:
        os.system('cls')
        print u'第',2*(n+1),u'题'
        print u"如果你有两个选择："
        print u"选择1:你有",int(pb*100),u"%的几率盈利",b,u"元，  ",int(100-pb*100),u"%的几率盈利0"
        print u"选择2:你有100%的几率盈利",hypo2(n)                 
        print u"你会选择：（输入1或者2后按回车）"
        p_time = time.time()    #开始计时
        count = count + 1
        choice = raw_input()
        if choice == '1':
            if b * pb > hypo2(n):
                print 'rational2'
                c_2 = b*pb
                c_22 = hypo2(n)
                flag2 = True
                time_2 = time.time()-p_time
                comment_2 = 'r_2'
        if choice == '2':
            if b*pb < hypo2(n):      #here was a bug orz...
                print 'irrational2'
                c_2 = hypo2(n)
                c_22 = b*pb
                flag2 = True
                time_2 = time.time()-p_time
                comment_2 = 'i_2'

rec = [c_1,c_11,c_2,c_22,time_1,time_2,time.time()-start_time,count,comment_1,comment_2]
print u'实验完成 谢谢',rec
tf = open('80-20.csv','a')   #文件名
for r in rec:
    rr = str(r)
    tf.write(rr)
    tf.write(',')
tf.write('\n')
tf.close()