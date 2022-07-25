# XGBoot  目前还存在问题
'''
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
'''

# XGBoot
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
from xgboost import plot_importance

# 加载手写数字数据集
digits = datasets.load_digits()
print(digits.data.shape)
x_train, x_test, y_train, y_test = train_test_split(digits.data,
                                                    digits.target,
                                                    test_size=0.3,
                                                    random_state=33)
model = XGBClassifier(learning_rate=0.1,
                      # n_estimatores
                      # 含义：总共迭代的次数，即决策树的个数
                      n_estimators=1000,
                      # max_depth
                      # 含义：树的深度，默认值为6，典型值3-10。
                      max_depth=6,
                      # min_child_weight
                      # 调参：值越大，越容易欠拟合；值越小，越容易过拟合
                      # （值较大时，避免模型学习到局部的特殊样本）。
                      min_child_weight=1,
                      # 惩罚项系数，指定节点分裂所需的最小损失函数下降值。
                      gamma=0,
                      # subsample
                      # 含义：训练每棵树时，使用的数据占全部训练集的比例。
                      # 默认值为1，典型值为0.5-1。
                      subsample=0.8,
                      # colsample_bytree
                      # 含义：训练每棵树时，使用的特征占全部特征的比例。默认值为1，典型值为0.5-1。
                      colsample_btree=0.8,
                      # objective 目标函数
                      # multi：softmax num_class=n 返回类别
                      objective='multi:softmax',
                      # scale_pos_weight
                      # 正样本的权重，在二分类任务中，当正负样本比例失衡时，设置正样本的权重，模型效果更好。例如，当正负样本比例为1:10时，scale_pos_weight=10
                      scale_pos_weight=1,
                      random_state=27
                      )

model.fit(x_train,
          y_train,
          eval_set=[(x_test, y_test)],
          eval_metric='mlogloss',
          early_stopping_rounds=10,
          verbose=True)

fig, ax = plt.subplots(figsize=(15, 15))

plot_importance(model,
                height=0.5,
                ax=ax,
                max_num_features=64)
plt.show()

y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print("accuarcy: %.2f%%" % (accuracy * 100.0))




