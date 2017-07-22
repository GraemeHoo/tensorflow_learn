#2017/7/22 by Graeme
import tensorflow as tf
import numpy as np

#creat data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

###creat tensorflow structure start###
weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([1]))

y = weights*x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))

optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()
###creat tensorflow structure end ###

sess = tf.Session()
sess.run(init)   #very important 激活整个网络

for step in range(201):
	sess.run(train)
	if step % 20 ==0:
		print(step, sess.run(weights),sess.run(biases))