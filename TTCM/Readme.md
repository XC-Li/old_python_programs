# 首位交易循环机制(TTCM)的Python实现 #
> Xc.Li  
> Feb.2015

## 算法原理 ##
首位交易循环机制的算法，略。
## Python实现 ##
### 学校和学生的数据结构 ###
- 学校 class School
    - counter:计数器
    - pointer：指向
    - preference:偏好向量
    - available:学校是未满员
    - 函数：refresh  
    用于每次刷新学校的指向和偏好向量

- 学生 class Student
    - preference:偏好向量
    - pointer：指向
    - available：学生是否已经找到学校
    - result：保存学生最终去的学校
    - 函数：refresh  
    用于每次刷新学生的指向和偏好向量
    
#### 学校 ####
    class School(object):
    def __init__(self, quantity, preference):
        self.counter = quantity
        self.pointer = preference[0]
        self.preference = preference
        self.available = True
        print self.counter, self.pointer, preference
#### 学生 ####
    class Student(object):
    def __init__(self, preference):
        self.preference = preference
        self.pointer = preference[0]
        self.available = True
        self.result = None
### 学校和学生的刷新 ###
#### 学校 ####
class School 里的函数：

    def refresh(self):
    original_preference = self.preference
    self.preference = []
    for item in original_preference:
        if student_list[item].available is True:
            self.preference.append(item)
    try:
        self.pointer = self.preference[0]
    except:
        print 'ok'
#### 学生 ####
class Student 里的函数：

    def refresh(self):
    original_preference = self.preference
    self.preference = []
    for item in original_preference:
        if school_list[item].available is True:
            self.preference.append(item)
    self.pointer = self.preference[0]

### 穷举构环 ###
从学校出发，根据学校和学生的指向向circle列表中添加元素。  
判断方式：  
1. 如果某元素和起始元素相同则终止程序，找到一个完整的环  
处理方式是调用School.refresh和Student.refresh刷新状态，调用Handle(circle)处理环。  
2. 如果环的长度大于10（仅举例），则认为是死循环（例如s2-i1-s1-i1-s1-....)，也终止程序。

    while True:

    count = 0
    for j in range(1, student_num + 1, 1):  #careful
        if student_list['i' + str(j)].available is False:
            count += 1
    if count == student_num:
        break

    i = 1
    circle = []
    while i <= school_num:
        school_name = 's' + str(i)
        if school_list[school_name].available is False:
            continue
        # circle.append(school_name)
        while True:
            student_name = school_list[school_name].pointer
            circle.append(student_name)
            school_name = student_list[student_name].pointer
            circle.append(school_name)
            if school_name == 's' + str(i):
                flag = 1
                break
            if len(circle) > 10:
                flag = 0
                circle = 'Error'
                break
        if flag == 1:
            handle(circle)
            for j in range(1, school_num + 1, 1):  # careful
                school_list['s' + str(j)].refresh()
            for j in range(1, student_num + 1, 1):  # careful
                student_list['i' + str(j)].refresh()
        print circle
        circle = []
        i += 1
### 环的处理 ###
对于每个环内的学生i，将目前指向pointer赋值给结果result保存，把available赋值为False，以示退出。  
对于每个环内的学校s，counter减1。判断counter是否为0，如果是则把available赋值为False，以示退出。

    def handle(circle):
    for item in circle:
        if item[0] == 'i':
            student_list[item].available = False
            student_list[item].result = student_list[item].pointer
        if item[0] == 's':
            school_list[item].counter -= 1
            if school_list[item].counter == 0:
                school_list[item].available = False
                print 'school out!'

## 运行 ##
### 测试 ###
number of schools:*输入0*  
演示：

    C:\Python27\python.exe D:/OneDrive/Python/TTCM.py
    number of schools:0 #这里输入0
    test
    2 i1 ['i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8']
    2 i3 ['i3', 'i5', 'i4', 'i8', 'i7', 'i2', 'i1', 'i6']
    3 i5 ['i5', 'i3', 'i1', 'i7', 'i2', 'i8', 'i6', 'i4']
    3 i6 ['i6', 'i8', 'i7', 'i4', 'i2', 'i3', 'i5', 'i1']
    ['i1', 's2', 'i3', 's3', 'i5', 's1']
    Error #表示找不到环
    Error
    ['i6', 's4']
    school out!
    ['i2', 's1']
    school out!
    ['i4', 's3', 'i7', 's2']
    Error
    ok #学校满员
    ok
    ok
    ok
    ['i8', 's4']
    1 s2
    2 s1
    3 s3
    4 s3
    5 s1
    6 s4
    7 s2
    8 s4

    
### 数据输入 ###
number of schools：学校个数（整数）  
number of students:学生个数（整数）  
quantity of school:学校招生人数（整数）  
enter the preference of school:学校偏好，例如*i1,i2,i3*  
enter the preference of student:学生偏好，例如*s1,s2,s3*  
## 完整代码 ##
基于Python2.7

    # -*- encoding:utf-8 -*-
    # 首位交易循环机制
    # Designed By Xc.Li @ Feb.2015
    
    
    class School(object):
        def __init__(self, quantity, preference):
            self.counter = quantity
            self.pointer = preference[0]
            self.preference = preference
            self.available = True
            print self.counter, self.pointer, preference
    
        def refresh(self):
            original_preference = self.preference
            self.preference = []
            for item in original_preference:
                if student_list[item].available is True:
                    self.preference.append(item)
            try:
                self.pointer = self.preference[0]
            except:
                print 'ok'
    
    
    class Student(object):
        def __init__(self, preference):
            self.preference = preference
            self.pointer = preference[0]
            self.available = True
            self.result = None
    
        def refresh(self):
            original_preference = self.preference
            self.preference = []
            for item in original_preference:
                if school_list[item].available is True:
                    self.preference.append(item)
            self.pointer = self.preference[0]
    
    # input and initialize
    
    school_num = int(raw_input("number of schools:"))
    if school_num == 0:
        print 'test'
        school_num = 4
        school_list = {
            's1': School(2, ['i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8']),
            's2': School(2, ['i3', 'i5', 'i4', 'i8', 'i7', 'i2', 'i1', 'i6']),
            's3': School(3, ['i5', 'i3', 'i1', 'i7', 'i2', 'i8', 'i6', 'i4']),
            's4': School(3, ['i6', 'i8', 'i7', 'i4', 'i2', 'i3', 'i5', 'i1'])
        }
        student_num = 8
        student_list = {
            'i1': Student(['s2', 's1', 's3', 's4']),
            'i2': Student(['s1', 's2', 's3', 's4']),
            'i3': Student(['s3', 's2', 's1', 's4']),
            'i4': Student(['s3', 's4', 's1', 's2']),
            'i5': Student(['s1', 's3', 's4', 's2']),
            'i6': Student(['s4', 's1', 's2', 's3']),
            'i7': Student(['s1', 's2', 's3', 's4']),
            'i8': Student(['s1', 's2', 's4', 's3'])
        }
    
    else:
        student_num = int(raw_input("number of students:"))
        # school initialize
        i = 1
        school_list = {}
        while i <= school_num:
            school_name = 's' + str(i)
            print school_name
            quantity = int(raw_input("quantity of school:"))
            preference = raw_input("enter the preference of school:")
            preference = preference.split(",")
            school_list[school_name] = School(quantity, preference)
            i += 1
    
        # student initialize
        i = 1
        student_list = {}
        while i <= student_num:
            student_name = 'i' + str(i)
            print student_name
            preference = raw_input("enter the preference of student:")
            preference = preference.split(",")
            student_list[student_name] = Student(preference)
            i += 1
    
    
    def handle(circle):
        for item in circle:
            if item[0] == 'i':
                student_list[item].available = False
                student_list[item].result = student_list[item].pointer
            if item[0] == 's':
                school_list[item].counter -= 1
                if school_list[item].counter == 0:
                    school_list[item].available = False
                    print 'school out!'
    k = 0
    while True:
    
        count = 0
        for j in range(1, student_num + 1, 1):  # fuck it!
            if student_list['i' + str(j)].available is False:
                count += 1
        if count == student_num:
            break
    
        i = 1
        circle = []
        while i <= school_num:
            school_name = 's' + str(i)
            if school_list[school_name].available is False:
                continue
            # circle.append(school_name)
            while True:
                student_name = school_list[school_name].pointer
                circle.append(student_name)
                school_name = student_list[student_name].pointer
                circle.append(school_name)
                if school_name == 's' + str(i):
                    flag = 1
                    break
                if len(circle) > 10:
                    flag = 0
                    circle = 'Error'
                    break
            if flag == 1:
                handle(circle)
                for j in range(1, school_num + 1, 1):  # careful
                    school_list['s' + str(j)].refresh()
                for j in range(1, student_num + 1, 1):  # careful
                    student_list['i' + str(j)].refresh()
            print circle
            circle = []
            i += 1
    for k in range(1, student_num + 1, 1):
        print k, student_list['i' + str(k)].result
