import pandas as pd
import numpy as np
import tushare as ts

#设置token
token = '505b8931caa230ee0e09aa84f4e7715b8dd28ede75af1021d7b39ede'
ts.set_token(token)
pro = ts.pro_api()

#选出大单净流入为正的股票代码
df = pro.moneyflow(trade_date='20190419', fields='ts_code, buy_elg_amount, sell_elg_amount, net_mf_vol')
mf = pro.daily_basic(trade_date='20190419',  fields='ts_code, volume_ratio, pe, pe_ttm')
codes=set()
xcodes=set()
ucodes=set()
zcodes=set()
#选取净流入量大于500手，大单净买入量大于500手的股票
for i in range(len(df)):
  if df.net_mf_vol[i]> 500 and  df.buy_elg_amount[i] > df.sell_elg_amount[i]:
    net_elg_change= int(df.buy_elg_amount[i] -df.sell_elg_amount[i])
    if net_elg_change>500:
       codes.add( df.ts_code[i])

#选取量比大于1,静态市盈率高于动态市盈率的股票
for j in range(len(mf)):
    if mf.volume_ratio[j] > 1 and  mf.pe[j] > mf.pe_ttm[j]:
        xcodes.add( mf.ts_code[j])

ucodes = codes.intersection(xcodes)

# 在以上结果内选取经营活动现金流量净额、 企业自由现金流量、净利润为正的股票
data = pd.DataFrame()
for code in ucodes:
    df = pro.cashflow(ts_code=code,report_type='1', period='20181231',fields='im_net_cashflow_oper_act, free_cashflow, net_profit')
    for i in range(len(df)):
        if df.im_net_cashflow_oper_act[i]>0 and df.free_cashflow[i]>0 and df.net_profit[i]>0:
            data[code]=code

#在以上结果内选取最近两个交易日交易量放大2倍以上的股票
for code in data:
    df=pro.query('daily', ts_code=code, start_date='20190418', end_date='20190419',fields='ts_code,trade_date, vol')
    if df.vol[0]>=df.vol[1]*1.5:
        zcodes.add(code)

print(zcodes)

