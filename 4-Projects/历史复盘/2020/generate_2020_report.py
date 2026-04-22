# -*- coding: utf-8 -*-
"""
2020年A股年度复盘报告生成脚本 - 深度版
主题：疫情V型反转
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
with open('stats_2020.json', 'r', encoding='utf-8') as f:
    stats = json.load(f)

df_daily = pd.read_csv('sh_index_2020.csv')
df_daily.columns = ['date', 'code', 'open', 'high', 'low', 'close', 'volume', 'amount', 'turnover', 'change_pct']
df_daily['date'] = pd.to_datetime(df_daily['date'])

df_monthly = pd.read_csv('monthly_2020.csv')
df_monthly.columns = ['month_str', 'open', 'close', 'high', 'low', 'volume', 'change_percent']
df_monthly['month'] = range(1, 13)

# 生成全年走势图
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10), gridspec_kw={'height_ratios': [3, 1]})

# 绘制K线
for idx, row in df_daily.iterrows():
    color = '#d62728' if row['close'] >= row['open'] else '#2ca02c'
    ax1.plot([row['date'], row['date']], [row['low'], row['high']], color=color, linewidth=0.5)
    ax1.plot([row['date'], row['date']], [row['open'], row['close']], color=color, linewidth=1.5)

ax1.fill_between(df_daily['date'], df_daily['close'], alpha=0.2, color='#d62728')

# 标注关键点位
max_idx = df_daily['close'].idxmax()
min_idx = df_daily['close'].idxmin()
ax1.annotate(f'最高点: {df_daily.loc[max_idx, "close"]:.0f}', 
             xy=(df_daily.loc[max_idx, 'date'], df_daily.loc[max_idx, 'close']),
             xytext=(10, 20), textcoords='offset points',
             bbox=dict(boxstyle='round,pad=0.5', fc='green', alpha=0.7),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
ax1.annotate(f'最低点: {df_daily.loc[min_idx, "close"]:.0f}', 
             xy=(df_daily.loc[min_idx, 'date'], df_daily.loc[min_idx, 'close']),
             xytext=(10, -30), textcoords='offset points',
             bbox=dict(boxstyle='round,pad=0.5', fc='red', alpha=0.7),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

# 先计算Y轴范围
y_min = df_daily['low'].min() * 0.98
y_max = df_daily['high'].max() * 1.02

# 标注重大事件
events = [
    ('2020-01-23', '武汉\n封城', 'red'),
    ('2020-02-03', '千股跌停\n-7.72%', 'red'),
    ('2020-03-19', '2646\n全球底', 'purple'),
    ('2020-03-23', '美联储\n无限QE', 'blue'),
    ('2020-07-06', '暴涨5.71%\n牛市呼声', 'green'),
    ('2020-08-24', '创业板\n注册制', 'orange'),
    ('2020-11-03', '拜登\n胜选', 'blue'),
    ('2020-12-31', '3474\n新高收官', 'green'),
]

for date_str, label, color in events:
    date = pd.to_datetime(date_str)
    ax1.axvline(date, color=color, linestyle='--', alpha=0.6, linewidth=1.5)
    ax1.text(date, y_max * 0.98, label, rotation=90, 
             verticalalignment='top', fontsize=9, color=color, fontweight='bold')

# 设置Y轴范围
ax1.set_ylim(y_min, y_max)

ax1.set_title('2020年上证指数全年走势：疫情V型反转的奇迹之年', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('指数点位', fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m月'))
ax1.xaxis.set_major_locator(mdates.MonthLocator())

# 成交量图
colors_vol = ['#d62728' if df_daily.loc[i, 'close'] >= df_daily.loc[i, 'open'] else '#2ca02c' 
              for i in range(len(df_daily))]
ax2.bar(df_daily['date'], df_daily['volume']/1e8, color=colors_vol, alpha=0.7, width=1)
ax2.set_ylabel('成交量（亿股）', fontsize=12)
ax2.set_xlabel('日期', fontsize=12)
ax2.grid(True, alpha=0.3, axis='y')
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m月'))
ax2.xaxis.set_major_locator(mdates.MonthLocator())

plt.tight_layout()
plt.savefig('chart_2020_index.png', dpi=150, bbox_inches='tight')
plt.close()
print("[OK] 生成全年走势图: chart_2020_index.png")

# 生成月度涨跌幅图
colors = ['#d62728' if x < 0 else '#2ca02c' for x in df_monthly['change_percent']]
fig, ax = plt.subplots(figsize=(14, 7))
bars = ax.bar(df_monthly['month'], df_monthly['change_percent'], color=colors, edgecolor='black', linewidth=0.5, width=0.7)

for bar, val in zip(bars, df_monthly['change_percent']):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + (0.3 if height > 0 else -0.8),
            f'{val:.2f}%', ha='center', va='bottom' if height > 0 else 'top', fontsize=11, fontweight='bold')

ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
ax.set_title('2020年上证指数月度涨跌幅', fontsize=14, fontweight='bold')
ax.set_xlabel('月份', fontsize=12)
ax.set_ylabel('涨跌幅 (%)', fontsize=12)
ax.set_xticks(range(1, 13))
ax.set_xticklabels([f'{i}月' for i in range(1, 13)])
ax.grid(True, alpha=0.3, axis='y')
ax.set_ylim(-8, 13)

plt.tight_layout()
plt.savefig('chart_2020_monthly.png', dpi=150, bbox_inches='tight')
plt.close()
print("[OK] 生成月度涨跌幅图: chart_2020_monthly.png")

# 生成情绪温度计
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

ax1 = fig.add_subplot(gs[0, :2])
df_daily['month'] = df_daily['date'].dt.month
monthly_volume = df_daily.groupby('month')['volume'].mean() / 1e8
ax1.plot(monthly_volume.index, monthly_volume.values, marker='o', linewidth=2.5, color='#1f77b4', markersize=8)
ax1.fill_between(monthly_volume.index, monthly_volume.values, alpha=0.3, color='#1f77b4')
ax1.set_title('月均成交量变化（亿股）', fontsize=12, fontweight='bold')
ax1.set_xlabel('月份')
ax1.set_xticks(range(1, 13))
ax1.grid(True, alpha=0.3)

ax2 = fig.add_subplot(gs[0, 2])
df_daily['returns'] = df_daily['close'].pct_change()
df_daily['volatility'] = df_daily['returns'].rolling(20).std() * np.sqrt(252) * 100
ax2.plot(df_daily['date'], df_daily['volatility'], color='#ff7f0e', linewidth=1.5)
ax2.axhline(y=df_daily['volatility'].mean(), color='red', linestyle='--', label=f'均值: {df_daily["volatility"].mean():.1f}%')
ax2.set_title('20日滚动波动率', fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend()

ax3 = fig.add_subplot(gs[1, 0])
up_months = sum(df_monthly['change_percent'] > 0)
down_months = sum(df_monthly['change_percent'] < 0)
ax3.pie([up_months, down_months], labels=['上涨', '下跌'], colors=['#2ca02c', '#d62728'], 
        autopct='%1.0f%%', startangle=90, textprops={'fontsize': 11, 'fontweight': 'bold'})
ax3.set_title('月度涨跌分布', fontsize=12, fontweight='bold')

ax4 = fig.add_subplot(gs[1, 1])
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
q_returns = [-4.51, 8.52, 2.18, 7.06]
colors_q = ['#2ca02c' if x > 0 else '#d62728' for x in q_returns]
ax4.bar(quarters, q_returns, color=colors_q, edgecolor='black', width=0.6)
ax4.axhline(y=0, color='black', linestyle='-', linewidth=1)
ax4.set_title('季度涨跌幅 (%)', fontsize=12, fontweight='bold')
for i, v in enumerate(q_returns):
    ax4.text(i, v + (0.3 if v > 0 else -0.5), f'{v:.2f}%', ha='center', 
             va='bottom' if v > 0 else 'top', fontsize=11, fontweight='bold')

ax5 = fig.add_subplot(gs[1, 2])
bins = [2600, 2800, 3000, 3200, 3400, 3600]
ax5.hist(df_daily['close'], bins=bins, color='#9467bd', edgecolor='black', alpha=0.7)
ax5.axvline(x=df_daily['close'].mean(), color='red', linestyle='--', linewidth=2, label=f'均值: {df_daily["close"].mean():.0f}')
ax5.set_title('指数点位分布', fontsize=12, fontweight='bold')
ax5.legend()

ax6 = fig.add_subplot(gs[2, 0])
daily_changes = df_daily['change_pct'].dropna()
ax6.hist(daily_changes, bins=30, color='#8c564b', edgecolor='black', alpha=0.7)
ax6.axvline(x=0, color='red', linestyle='--', linewidth=2)
ax6.axvline(x=daily_changes.mean(), color='green', linestyle='--', linewidth=2)
ax6.set_title('日涨跌幅分布', fontsize=12, fontweight='bold')

ax7 = fig.add_subplot(gs[2, 1:])
monthly_amount = df_daily.groupby('month')['amount'].mean() / 1e8
ax7.bar(monthly_amount.index, monthly_amount.values, color='#e377c2', edgecolor='black', alpha=0.8)
ax7.plot(monthly_amount.index, monthly_amount.values, marker='o', color='red', linewidth=2, markersize=8)
ax7.set_title('月均成交额变化（亿元）', fontsize=12, fontweight='bold')
ax7.set_xlabel('月份')
ax7.set_xticks(range(1, 13))
ax7.grid(True, alpha=0.3, axis='y')

plt.suptitle('2020年市场情绪温度计：从恐慌到复苏', fontsize=16, fontweight='bold', y=0.98)
plt.savefig('chart_2020_sentiment.png', dpi=150, bbox_inches='tight')
plt.close()
print("[OK] 生成情绪温度计: chart_2020_sentiment.png")

print("\n=== 2020年复盘报告图表生成完成 ===")
