import pandas as pd
d = {'col1': [1, 5], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
print(df)
xf=df.shift(1)
print(xf)
df=df/xf-1
print(df)
print(df.iloc[0:,:].fillna(0))
'''
for date in df.index:
    #ff.loc[date]=df.loc[date])
    print(df.index[date],df.loc[date].values)
'''



