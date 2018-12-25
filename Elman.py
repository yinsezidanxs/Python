import neurolab as nl
import pylab as pl
import numpy as np

def elman(X_train, Y_train, X, nor, num, min_grad, epochs = 500):
    net = nl.net.newelm(np.array(nor), [num, 1], [nl.trans.TanSig(), nl.trans.PureLin()])
    net.layers[0].initf = nl.init.InitRand([-0.1, 0.1], 'wb')
    net.layers[1].initf = nl.init.InitRand([-0.1, 0.1], 'wb')
    net.init()
    net.train(X_train, Y_train, epochs = epochs, goal = min_grad)
    Y = net.sim(X)
    return Y

# Create train samples
i1 = np.sin(np.arange(0, 20))
i2 = np.sin(np.arange(0, 20)) * 2

t1 = np.ones([1, 20])
t2 = np.ones([1, 20]) * 2

input = np.array([i1, i2, i1, i2]).reshape(20 * 4, 1)
target = np.array([t1, t2, t1, t2]).reshape(20 * 4, 1)

a = [[-2, 2]]

output = elman(input, target, input, a, 10, 0.04, 5000)

pl.subplot(111)
pl.plot(target.reshape(80))
pl.plot(output.reshape(80))
pl.legend(['train target', 'net output'])
pl.show()