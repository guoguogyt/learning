# 继续4_1之后的数据转换
# 需要按照“客户”+“连锁店”+“日期”3个主键来构建一个交易事件：给定日期下客户在连锁店购买了一系列的产品
import numpy as np
import pandas as pd

dtype_dict = {"id":"str","chain":"str","dept":"str","category":"str","company":"str","brand":"str"}
data = pd.read_csv('transactions.csv', nrows=999999, dtype=dtype_dict)
data['date'] = pd.to_datetime(data['date'])
data.head(5)

transaction_ids = np.random.randint(100000,data.shape[0],size=data.shape[0])

grouped = data.groupby(['date','id','chain'])

transaction_index = 0
id,chain,date,transaction,items = [],[],[],[],[]
for name,group in grouped:
    transaction_id = transaction_ids[transaction_index]
    id.append(group['id'].unique()[0])
    chain.append(group['chain'].unique()[0])
    date.append(group['date'].unique()[0])
    transaction.append(transaction_id)
    items.append(' '.join(group['category'].sort_values().values))

trans_data = pd.DataFrame({'id':id,'chian':chain,'date':date,'transaction':transaction,'items':items})
trans_data.head(5)