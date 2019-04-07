import tushare as ts

X=input("请输入股票代码")
df = ts.get_sina_dd(X, date='2019-04-03')
XF=ts.get_hist_data(X)
print(df)
print(XF)