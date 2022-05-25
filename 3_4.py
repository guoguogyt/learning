# 非热启动

from sklearn import datasets
from sklearn .linear_model import LogisticRegression

iris = datasets.load_iris()
X,y = iris.data[:,1:3], iris.target

lr =LogisticRegression(solver="lbfgs", multi_class='multinomial', random_state=1, warm_start=False, max_iter=80)

clf = lr.fit(X,y)
print("Iteration:"+str(clf.n_iter_))

Iteration:[79]


