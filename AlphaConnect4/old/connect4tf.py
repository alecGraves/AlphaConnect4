'''
tensorflow implementation of connect4 board object
This was abandoned in favor of just using the python version that works fine.
Perhaps in the future I may try to complete this.
'''
import tensorflow as tf
import numpy as np

# winVecs, computed in connect4.py
# with open("winVecs.npy", "r") as vecFile:
#     winVecs = np.load(vecFile)
from connect4 import BoardExplorer
winVecs = BoardExplorer().getWinPatterns()

tf_winVecs = tf.Variable(winVecs, name="winVecs")

class Connect4BoardTF(object):
    '''structure to hold board object'''
    def __init__(self, name):# pass in a name
        self.name = str(name)
        self.grid = tf.Variable(tf.zeros([6, 7], dtype=tf.int8), name="grid"+self.name)
        self.height = tf.Variable(tf.zeros(7, dtype=tf.int8), name="height"+self.name)
        self.player = tf.Variable(1, name="player"+self.name, dtype=tf.int8)
        self.complete = tf.Variable(-2, name="complete"+self.name, dtype=np.int8)
    def move(self, desire):#  desire = the softmax desire where each slot is where you want to move.
        slot = tf.cast(tf.argmax(tf.multiply(desire, tf.cast(tf.less(self.height, tf.constant(6, dtype=tf.int8)), tf.float32))), tf.int32)
        height = tf.cast(tf.gather(self.height, slot), tf.int32)
        # print(tf.shape(height))
        # print(tf.shape(slot))
        # print(type(tf.stack([slot, height], 0)));exit()
        self.grid = tf.scatter_nd_add(self.grid, tf.expand_dims(tf.stack([height, slot], 0), 0), tf.expand_dims(self.player, -1))
        tf.scatter_add(self.height, slot, tf.constant(1, dtype=tf.int8))
        tf.initialize_all_variables()
        sess = tf.Session()
        init = tf.global_variables_initializer()
        sess.run(init)
        print(sess.run(self.grid))
        # tf.Print()

if __name__ == "__main__":
    board = Connect4BoardTF("0")
    board.move(tf.Variable([0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.001], dtype=tf.float32))
