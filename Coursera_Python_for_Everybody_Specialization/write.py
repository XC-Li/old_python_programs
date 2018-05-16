c_1 = str(1)
c_2 = 2
list = [c_1,c_2]
tf = open('testfile.txt','a')

tf.write(c_1)
tf.write('.')
tf.write(c_2)
tf.write('\n')
tf.close()