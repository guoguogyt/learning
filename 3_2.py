# 投票决定最终成果 - 硬投票

from sklearn import datasets
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier

# 安德森鸢尾花卉数据集
iris = datasets.load_iris()
X,y = iris.data[:,1:3], iris.target

#逻辑回归模型
clf1 = LogisticRegression(solver='lbfgs', multi_class='multinomial',random_state=1)
#随机森林模型
clf2 = RandomForestClassifier(n_estimators=50,random_state=1)
#高斯朴素贝叶斯  无参数不需要调整
clf3 = GaussianNB()

# 投票器
eclf = VotingClassifier(estimators=[('lr',clf1),('rf',clf2),('gnb',clf3)],voting='hard')

for clf,label in zip([clf1,clf2,clf3,eclf],['Logistic Regression','Random Forest','native Bayes','Ensemble']):
    # 交叉验证   数据分成5分   逐个取出运行5次  取平均  误差范围
    scores = cross_val_score(clf,X,y,cv=5,scoring='accuracy')
    print("Accuracy:%0.2f (+/-%0.2f)[%s]"%(scores.mean(),scores.std(), label))