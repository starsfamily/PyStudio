import pandas as pd
import numpy as np
import tushare as ts



#设置token
token = '505b8931caa230ee0e09aa84f4e7715b8dd28ede75af1021d7b39ede'
ts.set_token(token)
pro = ts.pro_api()

df = pro.stock_basic(exchange='SSE',list_status='L',fields='ts_code,name,list_date')
df = df[df['list_date'].apply(int).values<20180101]
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


def cal_ret(nf, D=5):
    nf = nf/nf.shift(D)-1
    return nf.iloc[D: , : ].fillna(0)


ret5 = cal_ret(data,D=5)


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

rps5= all_RPS(ret5)

def data_write(file_path, datas):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    #创建sheet #将数据写入第 i 行，第 j 列
    i = 0
    for data in datas:
        for j in range(len(data)):
            sheet1.write(i,j,data[j])
            i = i + 1
    f.save(file_path)

data_write('rpstop10.xls',rps5['RPS'].values>87)
'''
dates=['20190402','20190401','20190329']
df_new=pd.DataFrame()
for date in dates:
    df_new[date]=rps5[date].index[:10]
print(df_new)
#df_new.to_csv('每日RPS.csv',encoding='utf-8',mode='A')
'''