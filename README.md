# learning
增强型分析学习code

文件2.1.已经废弃，直接使用主目录下的文件即可

有一个数据集很大，无法上传，自行下载，下载地址：https://www.kaggle.com/competitions/acquire-valued-shoppers-challenge/data?select=transactions.csv.gz

运行代码前需要安装搭建相关的环境
搭建环境(这里所有都是使用pip安装，有条件可以下载anaconda进行安装(更便捷))：
1、python
2、pip --default-timeout=1000 install sklearn
3、pip --default-timeout=1000 install pandas
4、pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xgboost

第6章程序再一个kaggle网址运(网页运行优点：因为需要训练，可能会对机器性能有一定的需求，再网页上运行可以避免自己本机性能带来的问题)
网址地址：https://www.kaggle.com/code/sdd456/minst/edit/run/97630433
进入之后新建项目，然后导入文件(文件是后缀名为.ipynb的文件)运行即可(需等待约10min)
结果分析：
1、训练误差值
2、评估误差值
3、每个epoch的学习率
4、每个step的学习率
