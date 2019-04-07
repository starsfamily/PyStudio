import tushare as ts
token = '505b8931caa230ee0e09aa84f4e7715b8dd28ede75af1021d7b39ede'
ts.set_token(token)
pro = ts.pro_api()

#X=input("请输入股票代码")
xf = ts.get_fund_info('070009')

#pro.fund_nav(ts_code='070009.OF',fields='ts_code, end_date, unit_nav')
#df = pro.fund_daily(ts_code='150018.SZ', start_date='20190301',end_date='20190402',fields='ts_code,trade_date, open,high,low,close')

print(xf)
