import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv('D:\\历史复盘\\2014\\sh_index_2014.csv')
df['日期'] = pd.to_datetime(df['日期'])

# 创建图表
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10), gridspec_kw={'height_ratios': [3, 1]})

# 绘制K线图
colors = ['#e74c3c' if close >= open else '#27ae60' for open, close in zip(df['开盘'], df['收盘'])]
ax1.vlines(df['日期'], df['最低'], df['最高'], color=colors, linewidth=0.8)
ax1.scatter(df['日期'], df['收盘'], c=colors, s=8, zorder=5)

# 标注关键点位
max_idx = df['收盘'].idxmax()
min_idx = df['收盘'].idxmin()
ax1.annotate(f'年末高点: {df.loc[max_idx, "收盘"]:.0f}', 
             xy=(df.loc[max_idx, '日期'], df.loc[max_idx, '收盘']),
             xytext=(10, 20), textcoords='offset points',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#e74c3c', alpha=0.7),
             arrowprops=dict(arrowstyle='->', color='#e74c3c'),
             fontsize=10, color='white', fontweight='bold')

ax1.annotate(f'年内低点: {df.loc[min_idx, "收盘"]:.0f}', 
             xy=(df.loc[min_idx, '日期'], df.loc[min_idx, '收盘']),
             xytext=(10, -30), textcoords='offset points',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#27ae60', alpha=0.7),
             arrowprops=dict(arrowstyle='->', color='#27ae60'),
             fontsize=10, color='white', fontweight='bold')

# 标注关键事件
events = [
    ('2014-03-12', 1974, '年内低点\n1974', '#27ae60'),
    ('2014-05-09', 2011, '定向降准\n开始宽松', '#3498db'),
    ('2014-07-24', 2126, '牛市启动\n突破年线', '#e74c3c'),
    ('2014-09-30', 2363, '四季度\n加速上涨', '#f39c12'),
    ('2014-11-21', 2486, '央行降息\n全面宽松', '#e74c3c'),
    ('2014-12-31', 3234, '年末高点\n+53%', '#e74c3c'),
]

for date, y, text, color in events:
    d = pd.to_datetime(date)
    ax1.annotate(text, xy=(d, y), xytext=(0, 30), textcoords='offset points',
                ha='center', fontsize=8, color=color, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=color, lw=1))

ax1.set_title('2014年上证指数全年走势图 - 牛市的起点', fontsize=18, fontweight='bold', pad=20)
ax1.set_ylabel('指数点位', fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m月'))
ax1.xaxis.set_major_locator(mdates.MonthLocator())

# 成交量图
colors_vol = ['#e74c3c' if close >= open else '#27ae60' for open, close in zip(df['开盘'], df['收盘'])]
ax2.bar(df['日期'], df['成交量']/1e8, color=colors_vol, alpha=0.7, width=1)
ax2.set_ylabel('成交量(亿股)', fontsize=12)
ax2.set_xlabel('日期', fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m月'))
ax2.xaxis.set_major_locator(mdates.MonthLocator())

plt.tight_layout()
plt.savefig('D:\\历史复盘\\2014\\chart_2014_index.png', dpi=150, bbox_inches='tight', facecolor='white')
print('走势图已保存: chart_2014_index.png')

# 生成月度涨跌幅图
df_monthly = pd.read_csv('D:\\历史复盘\\2014\\monthly_2014.csv')
df_monthly['年月'] = pd.to_datetime(df_monthly['年月'])

fig, ax = plt.subplots(figsize=(14, 6))
colors = ['#e74c3c' if x >= 0 else '#27ae60' for x in df_monthly['涨跌幅']]
bars = ax.bar(df_monthly['年月'].dt.strftime('%m月'), df_monthly['涨跌幅'], color=colors, alpha=0.8, edgecolor='white', linewidth=1)

# 添加数值标签
for bar, val in zip(bars, df_monthly['涨跌幅']):
    height = bar.get_height()
    ax.annotate(f'{val:+.1f}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3 if height >= 0 else -15),
                textcoords="offset points",
                ha='center', va='bottom' if height >= 0 else 'top',
                fontsize=10, fontweight='bold')

ax.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
ax.set_title('2014年上证指数月度涨跌幅', fontsize=16, fontweight='bold', pad=15)
ax.set_ylabel('涨跌幅(%)', fontsize=12)
ax.set_xlabel('月份', fontsize=12)
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('D:\\历史复盘\\2014\\chart_2014_monthly.png', dpi=150, bbox_inches='tight', facecolor='white')
print('月度涨跌幅图已保存: chart_2014_monthly.png')

# 生成市场情绪温度计图
months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
sentiment = [35, 40, 30, 35, 40, 45, 55, 60, 70, 80, 90, 95]

fig, ax = plt.subplots(figsize=(14, 6))

# 绘制温度计效果
for i, (month, val) in enumerate(zip(months, sentiment)):
    color = '#e74c3c' if val >= 60 else ('#f39c12' if val >= 40 else '#27ae60')
    ax.barh(i, val, color=color, alpha=0.8, height=0.6)
    ax.text(val + 2, i, f'{val}', va='center', fontsize=11, fontweight='bold')

# 添加情绪区间标注
ax.axvline(x=20, color='#27ae60', linestyle='--', alpha=0.5)
ax.axvline(x=40, color='#f39c12', linestyle='--', alpha=0.5)
ax.axvline(x=60, color='#e74c3c', linestyle='--', alpha=0.5)
ax.axvline(x=80, color='#c0392b', linestyle='--', alpha=0.5)

ax.text(10, -1.2, '极度恐慌', ha='center', fontsize=9, color='#27ae60')
ax.text(30, -1.2, '谨慎', ha='center', fontsize=9, color='#f39c12')
ax.text(50, -1.2, '乐观', ha='center', fontsize=9, color='#e74c3c')
ax.text(70, -1.2, '狂热', ha='center', fontsize=9, color='#e74c3c')
ax.text(90, -1.2, '极度狂热', ha='center', fontsize=9, color='#c0392b')

ax.set_yticks(range(len(months)))
ax.set_yticklabels(months)
ax.set_xlim(0, 105)
ax.set_title('2014年A股市场情绪温度计 - 从低迷到狂热', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('情绪指数', fontsize=12)
ax.grid(True, alpha=0.3, axis='x')

plt.tight_layout()
plt.savefig('D:\\历史复盘\\2014\\chart_2014_sentiment.png', dpi=150, bbox_inches='tight', facecolor='white')
print('情绪温度计图已保存: chart_2014_sentiment.png')

print('所有图表生成完成!')
