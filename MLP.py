import numpy as np

def sigmod(z):  
    return 1.0 / (1.0 + np.exp(-z))  

class mlp(object):  
    def __init__(self, lr=0.1, lda=0.0, te=1e-5, epoch=100, size=None):  
        self.learningRate = lr  
        self.lambda_ = lda  
        self.thresholdError = te  
        self.maxEpoch = epoch  
        self.size = size  
        self.W = []  
        self.b = []  
        self.init()  
  
    def init(self):  
        for i in range(len(self.size)-1):  
            self.W.append(np.mat(np.random.uniform(-0.5, 0.5, size=(self.size[i+1], self.size[i]))))  
            self.b.append(np.mat(np.random.uniform(-0.5, 0.5, size=(self.size[i+1], 1))))  
  
    def forwardPropagation(self, item=None):  
        a = [item]  
        for wIndex in range(len(self.W)):  
            a.append(sigmod(self.W[wIndex]*a[-1]+self.b[wIndex]))
        return a  
  
    def backPropagation(self, label=None, a=None):  
        delta = [(a[-1]-label)*a[-1]*(1.0-a[-1])]  
        for i in range(len(self.W)-1):  
            abc = np.multiply(a[-2-i], 1-a[-2-i])  
            cba = np.multiply(self.W[-1-i].T*delta[-1], abc)  
            delta.append(cba)
        for j in range(len(delta)):  
            ads = delta[j]*a[-2-j].T  
            self.W[-1-j] = self.W[-1-j]-self.learningRate*(ads+self.lambda_*self.W[-1-j])  
            self.b[-1-j] = self.b[-1-j]-self.learningRate*delta[j]
        error = 0.5*(a[-1]-label)**2  
        return error  
  
    def train(self, input_=None, target=None, show=10):  
        for ep in range(self.maxEpoch):  
            error = []  
            for itemIndex in range(input_.shape[1]):  
                a = self.forwardPropagation(input_[:, itemIndex])  
                e = self.backPropagation(target[:, itemIndex], a)  
                error.append(e[0, 0])  
            tt = sum(error)/len(error)  
            if tt < self.thresholdError:  
                print("Finish {0}: ".format(ep), tt)
                return  
            elif ep % show == 0:  
                print("epoch {0}: ".format(ep), tt) 
  
    def sim(self, inp=None):  
        return self.forwardPropagation(item=inp)[-1]  

if __name__ == "__main__":
    tt = [[5, 2, 12], [7.8, 1.9, 15], [5.5, 2.5, 11], 
          [0.1, 0.005, 0.1], [0.5, -0.05, 0.15], [-0.2, 0, 0.4], 
          [5.1, 0.01, -0.3], [7, -0.3, 0.02], [4.8, 0.5, 0], 
          [5.7, 2.2, -0.1], [4.95, 1.98, -0.05], [6.2, 2.01, 0.2]]
    tt = np.array(tt)
    tt = np.transpose(tt)
    tt = np.mat(tt)
    labels = [0, 0, 0, 
              1/3, 1/3, 1/3, 
              2/3, 2/3, 2/3, 
              1, 1, 1]
    labels = np.mat(labels)
    model = mlp(lr=1, lda=0.0, te=1e-5, epoch=500, size=[3, 1])
    print(tt.shape, labels.shape)
    print(len(model.W), len(model.b))
    print( )
    model.train(input_=tt, target=labels, show=10)
    t = [[6.72, 2.3, 13.4], [0.1, -0.08, 0.13], [5.1, 0.25, 0], [5.2, 1.8, 0.3]]
    t = np.array(t)
    t = np.transpose(t)
    t = np.mat(t)
    sims = [model.sim(t[:, idx]) for idx in range(t.shape[1])]
#if __name__ == "__main__":
#    tt = np.arange(0, 6.28, 0.01)
#    labels = np.zeros_like(tt)
#    print(tt.shape)
#    tt = np.mat(tt)
#    labels = np.sin(tt)*0.5+0.5
#    labels = np.mat(labels)
#    model = mlp(lr=0.8, lda=0.0, te=1e-5, epoch=500, size=[1, 6, 1])
#    print(tt.shape, labels.shape)
#    print(len(model.W), len(model.b))
#    print( )
#    model.train(input_=tt, target=labels, show=10)
#    sims = [model.sim(tt[:, idx])[0, 0] for idx in range(tt.shape[1])]
#
#    xx = tt.tolist()[0]
#    plt.figure()
#    plt.plot(xx, labels.tolist()[0], xx, sims, 'r')
#    plt.show()