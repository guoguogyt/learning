# 第4章实例

import pandas as pd

dtype_dict = {"id":"str","chain":"str","dept":"str","category":"str","company":"str","brand":"str"}
data = pd.read_csv('transaction.csv', nrows=999999, dtype=dtype_dict)
data['date'] = pd.to_datetime(data['date'])
data.head(5)

