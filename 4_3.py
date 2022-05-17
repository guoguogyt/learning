import numpy as np
import pandas as pd

dtype_dict = {"id":"str","chain":"str","dept":"str","category":"str","company":"str","brand":"str"}
data = pd.read_csv('transaction.csv', nrows=999999, dtype=dtype_dict)
data['date'] = pd.to_datetime(data['date'])
data.head(5)

transaction_ids = np.random.randint(100000,data.shape[0],size=data.shape[0])

grouped = data.groupby(['date','id''chain'])

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

grouped = trans_data.groupby(['id'])

sequence_index = 0
sequence_id, sequence_items = [],[]
for name,group in grouped:
    sequence_id.append(name)
    group = group.sort_values(by=['date'],ascending=True)
    seqs = []
    for seq in group['items'].values:
        seq.append(seq+"-1")
    seqs.append("-2")
    sequence_items.append("".join(seqs))

sequence_data = pd.DataFrame({'id':sequence_id,'sequence_items':sequence_items})
sequence_data.head(5)