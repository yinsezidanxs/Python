import numpy as np
import neurolab as nl
import copy
from sklearn.metrics import mean_squared_error
from scipy import interpolate
import pylab as pl

def elman_seq(seq_all, win, num, min_grad, l, epochs = 500, loc = -1):
    if loc == -1:
        loc = len(seq_all) + 1
    seq = copy.deepcopy(seq_all[0 : loc - 1])
    x_pred = []
    pred = []
    train_x = []
    train_y = []
    nor = []
    i = 0
    while i + win < len(seq):
        train_x.append(seq[i : i + win])
        train_y.append(seq[i + win])
        i += 1
    train_x = np.array(train_x).reshape((len(seq) - win, win))
    train_y = np.array(train_y).reshape((-1, 1))
    for j in range(win):
        nor.append([0, 1])
    net = nl.net.newelm(np.array(nor), [num, 1], [nl.trans.TanSig(), nl.trans.PureLin()])
    net.layers[0].initf = nl.init.InitRand([-0.1, 0.1], 'wb')
    net.layers[1].initf = nl.init.InitRand([-0.1, 0.1], 'wb')
    net.init()
    net.train(train_x, train_y, epochs = epochs, goal = min_grad)
    test = copy.deepcopy(seq[len(seq) - win : len(seq)])
    pred.append(net.sim(np.array(test).reshape((1, -1)))[0, 0])
    for k in range(l - 1):
        test.pop(0)
        test.append(pred[-1])
        pred.append(net.sim(np.array(test).reshape((1, -1)))[0, 0])
    x_pred = [i for i in range(loc - 1, loc + l - 1)]
    return pred, x_pred

cv_ori = [0.9999, 0.8052, 0.6622, 0.52, 0.3878, 0.2849, 0.2144]
f = interpolate.interp1d([0, 20, 40, 60, 80, 100, 120], cv_ori, kind = 'cubic')
cv = list(f([i for i in range(121)]))

win_bot = 12
win_top = 13
num_bot = 15
num_top = 16
mse = 999999
win_best = 999999
num_best = 999999
pred = []
x_pred = []
for ii in range(win_bot, win_top):
    for jj in range(num_bot, num_top):
        mse_temp = 0
        pred_temp = []
        [pred_temp, x_pred] = elman_seq(cv, ii, jj, 1.00e-6, 40, 20000, 82)
        mse_temp = mean_squared_error(np.array(pred_temp), np.array(cv[81 : 121]))
        if mse_temp < mse:
            mse = mse_temp
            win_best = ii
            num_best = jj
            pred = copy.deepcopy(pred_temp)

print('最佳参数组合为：窗口取' + str(win_best) + '，神经元数目取' + str(num_best) + '，此时均方误差为：' + str(mse))

pl.subplot(111)
pl.plot(cv, color = 'k', lw = 1)
pl.plot(x_pred, pred, color = 'r', lw = 1)
pl.legend(['Original', 'Predicted'])
pl.show()