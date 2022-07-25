# 投票决定最终成果 - 软投票

from sklearn import datasets
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier

iris = datasets.load_iris()
X,y = iris.data[:,1:3], iris.target

clf1 = LogisticRegression(solver='lbfgs', multi_class='multinomial',random_state=1)
clf2 = RandomForestClassifier(n_estimators=50,random_state=1)
clf3 = GaussianNB()

#每个方法预先的权值，默认各方法权值相同.
eclf = VotingClassifier(estimators=[('lr',clf1),('rf',clf2),('gnb',clf3)],voting='soft', weights=[1,1,5])

for clf,label in zip([clf1,clf2,clf3,eclf],['Logistic Regression','Random Forest','native Bayes','Ensemble']):
    scores = cross_val_score(clf,X,y,cv=5,scoring='accuracy')
    print("Accuracy:%0.2f (+/-%0.2f)[%s]"%(scores.mean(),scores.std(), label))