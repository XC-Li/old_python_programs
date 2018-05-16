# Write to CSV
# Designed By Xc.Li @ Mar.2016
import time
import os


def write(dirname, filename, content):
    if filename == "default":
        filename = time.ctime()[4:7]+time.ctime()[8:10]
    file_name = "D:\OneDrive\Python\\data\%s\%s.csv" % (dirname, filename)
    dir_name = "D:\OneDrive\Python\\data\%s" % dirname
    try:
        tf = open(file_name, 'a')
    except:
        os.system("mkdir "+dir_name)
        tf = open(file_name, 'a')
    tf.write(content)
    tf.write('\n')
    tf.close()
