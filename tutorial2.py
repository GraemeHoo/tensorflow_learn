import tensorflow as tf

matrix1 = tf.constant([[3,3]])  #one row,two column
matrix2 = tf.constant([[2],[2]]) #two row,one column

product = tf.matmul(matrix1,matrix2)  #matrix multiply

#method 1
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()  #可不要

#method 2
with tf.Session() as sess:#以sess命名并执行至结束
    result2 = sess.run(product)
    print(result2)
    #至此被close
