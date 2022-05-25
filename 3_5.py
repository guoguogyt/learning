# 热启动

from sklearn import datasets
from sklearn .linear_model import LogisticRegression

iris = datasets.load_iris()
X,y = iris.data[:,1:3], iris.target

lr1 =LogisticRegression(solver="lbfgs", multi_class='multinomial', random_state=1, warm_start=True, max_iter=80)
clf1 = lr1.fit(X,y)
print("Iteration:"+str(clf1.n_iter_))
clf1 = lr1.fit(X,y)
print("Iteration:"+str(clf1.n_iter_))

Iteration:[39]
Iteration:[2]