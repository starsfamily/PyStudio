import tushare as ts
import pandas as pd
# 换手率选股：
# 1.关注换手率高于6%、量比大于2的个股，
# 2.选择流通股本小于3亿的中小板
# 3.选择换手率突然放大3倍以上进入此区域 或者 连续多日平均换手率维持在此区域的个股。
# 4.第二日开盘阶段量比排行前列个股,换手率大于5%的个股。
token = '505b8931caa230ee0e09aa84f4e7715b8dd28ede75af1021d7b39ede'
ts.set_token(token)
pro = ts.pro_api()

df = pro.query('daily_basic',ts_code='', trade_date='20190419',fields='ts_code,trade_date,turnover_rate,volume_ratio')
mf = pd.DataFrame()

for i in range(len(df)):
    if 20>df.turnover_rate[i]>6 and df.volume_ratio[i]>2:
               mf=mf.append(df.iloc[i],ignore_index=True)

print(mf.sort_values(by=['turnover_rate'],ascending=False))

