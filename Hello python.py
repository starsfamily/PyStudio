# 可以自己import我们平台支持的第三方python模块，比如pandas、numpy等。

# 比较简单的根据市盈率做的策略，只选取排名前几的进行轮动调仓。
# 使用前注意补充好300样本股历史数据及专业财务数据
# 推荐使用000001上证指数做基准合约

import time
import os
import csv
import numpy as np



# 在这个方法中编写任何的初始化逻辑。context对象将会在你的算法策略的任何方法之间做传递。
def init(context):
    # 买入的股票数
    context.num = 10
    context.code = []


# before_trading此函数会在每天策略交易开始前被调用，当天只会被调用一次
def before_trading(context):
    # 选取300成份样本股作为股票池
    try:
        context.code = get_blocks("沪深300样本股", 1)
    except:
        pass


# 你选择的证券的数据更新将会触发此段逻辑，例如日或分钟历史数据切片或者是实时数据切片更新
def handle_bar(context):
    # 开始编写你的主要的算法逻辑
    try:
        pe = []
        code = []
        # 筛选非停牌且eps大于0的票
        for i in context.code:
            close = history_bars(i, 1, '1d', 'close')
            temp = fin_indicator(i, 'EPS', 1, 0, 0)
            if len(close) > 0 and temp[-1] > 0:
                code.append(i)
        # 转换成市盈率
        for j in code:
            close = history_bars(j, 1, '1d', 'close')
            temp = fin_indicator(j, 'EPS', 1, 0, 0)
            pe.append(close[-1] / temp[-1])
        pe_ra = np.array(pe)
        # 对pe进行排序，buy_list是排名前几的股票列表
        sort = np.argsort(pe_ra)
        code = np.array(code)
        buy_list = code[[sort[:context.num]]]
        sell_num = 0
        # 获得持仓品种信息
        ho = get_portfolio_book(0)
        if len(ho) > 0:
            for k in ho:
                if not (k in buy_list):
                    sell_close(k, 'Market', 0, 100, 0)
                    sell_num = sell_num + 1
        for kk in buy_list[:context.num]:
            if not (kk in ho):
                buy_open(kk, 'Market', 0, 100, 0)
    except:
        pass


# after_trading函数会在每天交易结束后被调用，当天只会被调用一次
def after_trading(context):
    pass

