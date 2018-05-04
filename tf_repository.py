'''功能是预先存放张量计算和用于tf计算的初始化过程'''


import tensorflow as tf


initial_RUL = tf.constant([initial_RUL], name="initial_RUL", dtype=tf.float32)

weights = tf.Variable(tf.random_normal([n, m],stddev=2))
'''权重初始化'''
init_op = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init_op)
'''自动初始化所有系数'''


x = tf.placeholder(tf.float32, shape=(t, n), name='input')