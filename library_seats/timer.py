# Countdown Timer
# Designed By Xc.Li @ Mar.2016
# coding = utf-8
import time
import os


def func(mode):
    if mode == 5:
        check_point = [00, 05, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
    if mode == 10:
        check_point = [00, 10, 20, 30, 40, 50]
    if mode == 15:
        check_point = [00, 15, 30, 45]
    if mode == "test":
        check_point = [00, 10, 20, 23]
    while True:
        current_minute = time.ctime()[14:-8]
        for item in check_point:
            if str(item) == current_minute or current_minute == '00':
                print "Check Point!"
                time.sleep(5)
                return True
        print "Waiting at mode %d" % mode
        time.sleep(5)
        os.system("cls")

#
# def func1(mode):
#     flag = False
#     previous_minute = time.ctime()[14:-8]
#     while True:
#         time.sleep(5)
#         print "Running at mode %d" % mode
#         current_minute = time.ctime()[14:-8]
#         if flag is True and int(current_minute) - int(previous_minute) == 2 or int(previous_minute) == 59:
#             return True
#         if current_minute == func(mode):
#             flag = True
#             continue
#     return False
