import numpy as np
from AShare import *


# 获取数据
data = get_price('sh688235',frequency='1d',count=140)

# 计算移动平均线
data['SMA'] = data['close'].rolling(window=14).mean()

# 创建信号
data['Signal'] = 0.0
data['Signal'][data['close'] > data['SMA']] = 1.0

# 计算策略收益
data['Return'] = data['close'].pct_change()
data['Strategy_Return'] = data['Return'] * data['Signal'].shift()

# 计算累积收益
data['Cumulative_Strategy_Returns'] = (1 + data['Strategy_Return']).cumprod()

data.to_excel('data.xlsx')