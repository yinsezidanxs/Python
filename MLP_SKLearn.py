from sklearn.neural_network import MLPClassifier

'''
class MLPClassifier(hidden_layer_sizes=(100,), activation="relu", solver='adam', alpha=0.0001, batch_size='auto', learning_rate="constant", learning_rate_init=0.001, 
    power_t=0.5, max_iter=200, shuffle=True, random_state=None, tol=1e-4, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True, early_stopping=False, 
    validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-8)

Multi-layer Perceptron classifier.

This model optimizes the log-loss function using LBFGS or stochastic gradient descent.

Parameters

hidden_layer_sizes : tuple, length = n_layers - 2, default (100,)
    The ith element represents the number of neurons in the ith hidden layer.  

activation : {'identity', 'logistic', 'tanh', 'relu'}, default 'relu'
    Activation function for the hidden layer.  
    - 'identity', no-op activation, useful to implement linear bottleneck,  
      returns f(x) = x  
    - 'logistic', the logistic sigmoid function,  
      returns f(x) = 1 / (1 + exp(-x)).  
    - 'tanh', the hyperbolic tan function,  
      returns f(x) = tanh(x).  
    - 'relu', the rectified linear unit function,  
      returns f(x) = max(0, x)  

solver : {'lbfgs', 'sgd', 'adam'}, default 'adam'
    The solver for weight optimization.  
    - 'lbfgs' is an optimizer in the family of quasi-Newton methods.  
    - 'sgd' refers to stochastic gradient descent.  
    - 'adam' refers to a stochastic gradient-based optimizer proposed  
      by Kingma, Diederik, and Jimmy Ba  
    Note: The default solver 'adam' works pretty well on relatively large datasets (with thousands of training samples or more) in terms of both training time and validation score.  
    For small datasets, however, 'lbfgs' can converge faster and perform better.  

alpha : float, optional, default 0.0001
    L2 penalty (regularization term) parameter.  

batch_size : int, optional, default 'auto'
    Size of minibatches for stochastic optimizers.  
    If the solver is 'lbfgs', the classifier will not use minibatch.  
    When set to "auto", `batch_size=min(200, n_samples)`  

learning_rate : {'constant', 'invscaling', 'adaptive'}, default 'constant'
    Learning rate schedule for weight updates.  
    - 'constant' is a constant learning rate given by 'learning_rate_init'.  
    - 'invscaling' gradually decreases the learning rate `learning_rate_` at each time step 't' using an inverse scaling exponent of 'power_t'.  
      effective_learning_rate = learning_rate_init / pow(t, power_t)  
    - 'adaptive' keeps the learning rate constant to 'learning_rate_init' as long as training loss keeps decreasing.  
      Each time two consecutive epochs fail to decrease training loss by at least tol, or fail to increase validation score by at least tol if 'early_stopping' is on, 
      the current learning rate is divided by 5.  
      Only used when `solver='sgd'`.  

learning_rate_init : double, optional, default 0.001
    The initial learning rate used. It controls the step-size in updating the weights. Only used when solver='sgd' or 'adam'.  

power_t : double, optional, default 0.5
    The exponent for inverse scaling learning rate.  
    It is used in updating effective learning rate when the learning_rate is set to 'invscaling'. Only used when solver='sgd'.  

max_iter : int, optional, default 200
    Maximum number of iterations. The solver iterates until convergence  
    (determined by 'tol') or this number of iterations. For stochastic  
    solvers ('sgd', 'adam'), note that this determines the number of epochs  
    (how many times each data point will be used), not the number of  
    gradient steps.  

shuffle : bool, optional, default True
    Whether to shuffle samples in each iteration. Only used when solver='sgd' or 'adam'.  

random_state : int, RandomState instance or None, optional, default None
    If int, random_state is the seed used by the random number generator;  
    If RandomState instance, random_state is the random number generator;  
    If None, the random number generator is the RandomState instance used by `np.random`.  

tol : float, optional, default 1e-4
    Tolerance for the optimization. When the loss or score is not improving by at least tol for two consecutive iterations, 
    unless `learning_rate` is set to 'adaptive', convergence is considered to be reached and training stops.  

verbose : bool, optional, default False
    Whether to print progress messages to stdout.  

warm_start : bool, optional, default False
    When set to True, reuse the solution of the previous call to fit as initialization, otherwise, just erase the previous solution.  

momentum : float, default 0.9
    Momentum for gradient descent update. Should be between 0 and 1. Only used when solver='sgd'.  

nesterovs_momentum : boolean, default True
    Whether to use Nesterov's momentum. Only used when solver='sgd' and momentum   0.  

early_stopping : bool, default False
    Whether to use early stopping to terminate training when validation score is not improving. 
    If set to true, 
    it will automatically set aside 10% of training data as validation and terminate training when validation score is not improving by at least tol for two consecutive epochs. 
    Only effective when solver='sgd' or 'adam'  

validation_fraction : float, optional, default 0.1
    The proportion of training data to set aside as validation set for early stopping. Must be between 0 and 1.  
    Only used if early_stopping is True   

beta_1 : float, optional, default 0.9
    Exponential decay rate for estimates of first moment vector in adam, should be in [0, 1). Only used when solver='adam'  

beta_2 : float, optional, default 0.999
    Exponential decay rate for estimates of second moment vector in adam, should be in [0, 1). Only used when solver='adam' 

epsilon : float, optional, default 1e-8
    Value for numerical stability in adam. Only used when solver='adam'  

Attributes

classes_ : array or list of array of shape (n_classes,)
    Class labels for each output.  

loss_ : float
    The current loss computed with the loss function.  

coefs_ : list, length n_layers - 1
    The ith element in the list represents the weight matrix corresponding to layer i.  

intercepts_ : list, length n_layers - 1
    The ith element in the list represents the bias vector corresponding to layer i + 1.  

n_iter_ : int,
    The number of iterations the solver has ran.  

n_layers_ : int
    Number of layers.  

n_outputs_ : int
    Number of outputs.  

out_activation_ : string
    Name of the output activation function.  

Notes

MLPClassifier trains iteratively since at each time step the partial derivatives of the loss function with respect to the model parameters are computed to update the parameters.
It can also have a regularization term added to the loss function that shrinks model parameters to prevent overfitting.
This implementation works with data represented as dense numpy arrays or sparse scipy arrays of floating point values.
'''

tt = [[5, 2, 12], [7.8, 1.9, 15], [5.5, 2.5, 11], 
        [0.1, 0.005, 0.1], [0.5, -0.05, 0.15], [-0.2, 0, 0.4], 
        [5.1, 0.01, -0.3], [7, -0.3, 0.02], [4.8, 0.5, 0], 
        [5.7, 2.2, -0.1], [4.95, 1.98, -0.05], [6.2, 2.01, 0.2]]
labels = [0, 0, 0, 
            1, 1, 1, 
            2, 2, 2, 
            3, 3, 3]
clf = MLPClassifier(activation = 'logistic', tol = 0.000001, hidden_layer_sizes = (4, ), solver = 'lbfgs')
clf.fit(tt, labels)
classes = clf.classes_
loss = clf.loss_
coefs = clf.coefs_
intercepts = clf.intercepts_
n_iter = clf.n_iter_
n_layers = clf.n_layers_
n_outputs = clf.n_outputs_
out_activation = clf.out_activation_
print(clf)
t = [[6.72, 2.3, 13.4], [0.1, -0.08, 0.13], [5.1, 0.25, 0], [5.2, 1.8, 0.3]]
#t = np.array(t)
#t = np.transpose(t)
# t = np.mat(t)
#sims = [clf.predict(t[:, idx]) for idx in range(4)]
sim = clf.predict(t)