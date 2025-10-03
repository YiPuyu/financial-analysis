import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. 定义要下载的ETF代码
# SPY: 美国标普500 ETF
# EWJ: 日本iShares MSCI日本ETF
# USDJPY=X: 美元/日元汇率
tickers = ['SPY', 'EWJ', 'USDJPY=X']

# 2. 下载2023年至今的数据
data = yf.download(tickers, start='2023-01-01', end='2024-03-31')['Close'] # 获取复权收盘价
data.columns = ['SPY', 'EWJ', 'USDJPY'] # 给列重新命名

# 3. 查看一下前几行数据，确保下载成功
print(data.head())

# 4. 检查是否有缺失值，如果有就删除
data = data.dropna()

# 5. 计算每日收益率 (今天的价格 / 昨天的价格 - 1)
returns = data.pct_change().dropna() # .pct_change()计算百分比变化，.dropna()删除第一行NaN值

# 6. 重命名收益率列，更清晰
returns.columns = ['SPY_Return', 'EWJ_Return', 'USDJPY_Return']
print(returns.head())

# 7. 计算SPY和EWJ收益率之间的相关系数
correlation = returns['SPY_Return'].corr(returns['EWJ_Return'])
print(f"SPY和EWJ日收益率的相关系数为: {correlation:.4f}")


import statsmodels.api as sm

# 回归1：SPY -> EWJ
X = returns['SPY_Return']
y = returns['EWJ_Return']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())


# 8. 绘制收益率散点图，直观展示联动性
plt.figure(figsize=(10, 6))
plt.scatter(returns['SPY_Return'], returns['EWJ_Return'], alpha=0.5) # alpha设置点透明度
plt.title('SPY vs EWJ Daily Returns (2023-2024)')
plt.xlabel('SPY Daily Return')
plt.ylabel('EWJ Daily Return')

# 添加相关系数作为文本注释
plt.text(0.05, 0.95, f'Correlation: {correlation:.4f}', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')

# 添加网格线让图更清晰
plt.grid(True)
plt.savefig('spy_ewj_scatter.png') # 保存图片，可以放在你的报告或简历里
plt.show()

# 9. 绘制价格趋势图，看大方向是否一致
# 计算60日滚动相关性（可以改成30、90日）
rolling_corr = returns['SPY_Return'].rolling(60).corr(returns['EWJ_Return'])

# ------------------- 插入汇率回归 -------------------
X2 = returns[['SPY_Return', 'USDJPY_Return']]
y = returns['EWJ_Return']
X2 = sm.add_constant(X2)
model2 = sm.OLS(y, X2).fit()
print(model2.summary())
# ----------------------------------------------------

plt.figure(figsize=(12,6))
plt.plot(rolling_corr, label='60-day Rolling Correlation (SPY vs EWJ)')
plt.axhline(y=0, color='red', linestyle='--', linewidth=1)  # 零轴参考线
plt.title('Rolling Correlation between SPY and EWJ')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.legend()
plt.grid(True)
plt.savefig('rolling_correlation.png')
plt.show()
