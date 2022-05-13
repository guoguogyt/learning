# 投票决定最终成果 - 硬投票

from sklearn import datasets
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.native_bayes import GaussianNB
from sklearn.ensemble import RandomForesetClassifier
from sklearn.ensemble import VotingClassifier

iris = datasets.load_iris()
X,y = iris.data[:,1:3], iris.target

clf1 = LogisticRegression(solver='lbfgs', multi_class='multinomial',random_state=1)
clf2 = RandomForesetClassifier(n_estimators=50,random_state=1)
clf3 = GaussianNB()

eclf = VotingClassifier(estimators=[('lr',clf1),('rf',clf2),('gnb',clf3)],voting='hard')

for clf,label in zip([clf1,clf2,clf3,eclf],['Logistic Regression','Random Forest','native Bayes','Ensemble']):
    scores = cross_val_score(clf,X,y,cv=5,scoring='accuracy')
    print("Accuracy:%0.2f (+/-%0.2f)[%s]"%(scores.mean(),scores.std(), label))