# 热启动

from sklearn import datasets
from sklearn .linear_model import LogisticRegressssion

iris = datasets.load_iris()
X,y = iris.data[:,1:3], iris.target

lr1 =LogisticRegressssion(solver="lbfgs", multi_class='multinomial', random_state=1, warm_state=True, max_iter=40)
clf1 = lr1.fit(X,y)
print("Iteration:"+str(clf1.n_iter_))
clf1 = lr1.fit(X,y)
print("Iteration:"+str(clf1.n_iter_))

Iteration:[39]
Iteration:[2]