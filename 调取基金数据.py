import pandas as pd
import tushare as ts
token = '505b8931caa230ee0e09aa84f4e7715b8dd28ede75af1021d7b39ede'
ts.set_token(token)
pro = ts.pro_api()

codes={'160142.SZ','161728.SZ','161131.SZ','501188.SH','501186.SH','501189.SH'}
#X=input("请输入股票代码")
xf = pd.DataFrame()
discount=pd.DataFrame(columns=['discount'])
for code in codes:
    df = pro.fund_daily(ts_code=code, trade_date='20190424',fields='ts_code,trade_date, close')
    ef = pro.fund_nav(ts_code=code, end_date='20190423',fields='ts_code, end_date, unit_nav')
    df = df.merge(ef)
    xf = xf.append(df,ignore_index=True)

discount['discount'] = (xf['close']/xf['unit_nav']-1)*100
discount.transpose()

xf = xf.join(discount,how='right')

xf=xf.set_index('ts_code')

xf= xf.sort_values(by='discount', ascending=True)
# # #df = pro.fund_daily(ts_code='150018.SZ', start_date='20190301',end_date='20190402',fields='ts_code,trade_date, open,high,low,close')

xf.to_excel('fund_data.xlsx',sheet_name='sheet_name_1',encoding='utf-8')
print('ok')
