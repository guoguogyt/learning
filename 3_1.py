# XGBoot

from sklearn.datasets import make_hastie_10_2
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier

X,y = make_hastie_10_2(random_state=0)
X_train, X_test = X[:2000],X[2000:]
y_train, y_test = y[:2000],y[2000:]

clf = GradientBoostingClassifier(n_estimators=100,learning_rate=1.0,max_depth=1,random_state=0).fit(X_train,y_train)
print(clf.score(X_test,y_test))

model = XGBClassifier(base_score=0.5, booster='gbtree',colsample_bylevel=1,colsample_bytree=1,gamma=0, learning_rate=0.05, max_delta_step=0,
                      max_depth=1, min_child_weight=1, missing=None, n_estimators=1000, n_jobs=1, nthread=None, objective='reg:linear', random_state=0,
                      reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None, silent=True, subsample=0.5).fit(X_train, y_train)

print(model.score(X_test, y_test))
