import tushare as ts
import talib


#通过tushare获取股票信息
df = ts.get_k_data('300580', start='2019-03-12', end='2019-03-26')
    #提取收盘价
closed = df['close'].values
    #获取均线的数据，通过timeperiod参数来分别获取 5,10,20 日均线的数据。
ma5 = talib.SMA(closed, timeperiod=5)
ma10 = talib.SMA(closed, timeperiod=10)
ma20 = talib.SMA(closed, timeperiod=20)

    #打印出来每一个数据
print(closed)
print(ma5)
print(ma10)
print(ma20)

    # #通过plog函数可以很方便的绘制出每一条均线
    # plt.plot(closed)
    # plt.plot(ma5)
    # plt.plot(ma10)
    # plt.plot(ma20)
    # #添加网格，可有可无，只是让图像好看点
    # plt.grid()
    # #记得加这一句，不然不会显示图像
    # plt.show()