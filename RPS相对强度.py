import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tushare as ts


#正常显示画图时出现的中文和负号
'''
from pylab import mpl
mpl.rcParams['font.sans-serif']=['Noto Sans CJK TC']
mpl.rcParams['axes.unicode_minus']=False
'''
#设置token
token = '505b8931caa230ee0e09aa84f4e7715b8dd28ede75af1021d7b39ede'
ts.set_token(token)
pro = ts.pro_api()

df = pro.stock_basic(exchange='SSE',list_status='L',fields='ts_code,name,list_date')
df = df[df['list_date'].apply(int).values<20170101]
codes = df.ts_code.values
names = df.name.values
code_name = dict(zip(names, codes))


def get_data(code, start= '20180301', end = '20190402'):
    df = pro.daily(ts_code=code, start_date=start, end_date=end, field='trade_date, close')
    df.index = pd.to_datetime(df.trade_date)
    df = df.sort_index()
    return df.close

data = pd.DataFrame()
for name, code in code_name.items():
    data[name]=get_data(code)

data.to_excel('dailyData.xls',sheet_name='每日收盘价',encoding='gbk')
data=pd.read_excel('dailyData.xls',encoding='gbk',index_col='trade_date')
data.index=(pd.to_datetime(data.index)).strftime('%Y%m%d')

def cal_ret(df, D=20):
    df = df/df.shift(D)-1
    return df.iloc[D: , : ].fillna(0)#从行[D]开始用0填补空缺
#计算收益率

ret30 = cal_ret(data, D=20)

def get_RPS(ser):
    df = pd.DataFrame(ser.sort_values(ascending=False))
    df['n'] = range(1, len(df)+1)
    df['rps'] = (1+df['n']/len(df))*100
    return df


def all_RPS(data):
    dates = (pd.to_datetime(data.index)).strftime('%Y%m%d')
    RPS={}
    for i in range(len(data)):
        RPS[dates[i]]=pd.DataFrame(get_RPS(data.iloc[i]).values, columns=['收益率','排名','RPS'],index=get_RPS(data.iloc[i]).index)
    return RPS


rps30 = all_RPS(ret30)


def all_data(rps, ret):
    df = pd.DataFrame(np.NaN, columns=ret.columns, index=ret.index)
    for date in ret.index:
        date = date.strftime('%Y%m%d')
        d=rps[date]
        for c in d.index:
            df.loc[date,c] = d.loc[c,'RPS']
    return df


df_new=pd.DataFrame(np.NaN, columns=ret30.columns, index=ret30.index)


for date in df_new.index:
    d = rps30[date]
    for c in d.index:
        df_new.loc[date, c] = d.loc[c, 'RPS']#loc[] 来按索引（标签名）引用这一行,加上RPS数值

df_new.to_excel('dailyData1.xls',sheet_name='Sheet2',encoding='utf-8')

def plot_rps(stock):
 plt.subplot(211)
 data[stock][20:].plot(figsize=(16,16),color='r')
 plt.title(stock+'Price Trends',fontsize=15)
 plt.yticks(fontsize=12)
 plt.xticks([])
 ax=plt.gca()
 ax.spines['right'].set_color('None')
 ax.spines['top'].set_color('none')

 plt.subplot(212)
 df_new[stock].plot(figsize=(16,8),color='b')
 plt.title(stock+'RPS corelative force',fontsize=15)
 my_ticks=pd.date_range('2018-03-01','2019-04-02',freq='m')
 plt.xticks(my_ticks,fontsize=12)
 plt.yticks(fontsize=12)
 ax=plt.gca()
 ax.spines['right'].set_color('none')
 ax.spines['top'].set_color('none')
 plt.show()
 plt.savefig('RPS.png')#保存图片

plot_rps('方正科技')

