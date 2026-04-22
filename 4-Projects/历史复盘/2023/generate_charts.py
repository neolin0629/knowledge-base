import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import json

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv('sh_index_2023.csv')
df['日期'] = pd.to_datetime(df['日期'])

# 读取统计数据
with open('stats_2023.json', 'r', encoding='utf-8') as f:
    stats = json.load(f)

# 读取月度数据
monthly_df = pd.read_csv('monthly_2023.csv')
monthly_df['年月'] = pd.to_datetime(monthly_df['年月'])

# ===== 图1: 全年走势图（K线+成交量+关键事件标注） =====
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10), gridspec_kw={'height_ratios': [3, 1]})

# 绘制K线
for i, row in df.iterrows():
    color = '#ff4d4d' if row['收盘'] >= row['开盘'] else '#00c853'
    ax1.plot([row['日期'], row['日期']], [row['最低'], row['最高']], color=color, linewidth=0.8)
    ax1.plot([row['日期'], row['日期']], [row['开盘'], row['收盘']], color=color, linewidth=3)

# 标注关键点位
# 最高点
max_idx = df['最高'].idxmax()
max_row = df.loc[max_idx]
ax1.annotate(f'全年最高点: {max_row["最高"]:.2f}\n{max_row["日期"].strftime("%Y-%m-%d")}', 
             xy=(max_row['日期'], max_row['最高']), 
             xytext=(max_row['日期'], max_row['最高'] + 100),
             arrowprops=dict(arrowstyle='->', color='#ff1744'),
             fontsize=10, ha='center', color='#ff1744', fontweight='bold')

# 最低点
min_idx = df['最低'].idxmin()
min_row = df.loc[min_idx]
ax1.annotate(f'全年最低点: {min_row["最低"]:.2f}\n{min_row["日期"].strftime("%Y-%m-%d")}', 
             xy=(min_row['日期'], min_row['最低']), 
             xytext=(min_row['日期'], min_row['最低'] - 100),
             arrowprops=dict(arrowstyle='->', color='#00c853'),
             fontsize=10, ha='center', color='#00c853', fontweight='bold')

# 标注关键事件
events = [
    ('2023-01-30', '春节后高开', 3310),
    ('2023-05-09', '全年最高点', 3420),
    ('2023-07-25', '政治局会议', 3230),
    ('2023-08-11', '信托风波', 3190),
    ('2023-08-28', '降印花税', 3220),
    ('2023-10-23', '跌破3000', 2920),
    ('2023-12-21', '全年最低点', 2880),
]

for date_str, event, y_pos in events:
    date = pd.to_datetime(date_str)
    if date >= df['日期'].min() and date <= df['日期'].max():
        ax1.axvline(x=date, color='gray', linestyle='--', alpha=0.5)
        ax1.text(date, y_pos, event, rotation=90, fontsize=8, va='bottom', ha='right', alpha=0.8)

ax1.set_ylabel('指数点位', fontsize=12)
ax1.set_title('2023年上证指数全年走势图', fontsize=16, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(df['日期'].min(), df['日期'].max())

# 成交量
ax2.bar(df['日期'], df['成交量']/1e8, color=['#ff4d4d' if c >= o else '#00c853' for c, o in zip(df['收盘'], df['开盘'])], alpha=0.7)
ax2.set_ylabel('成交量(亿股)', fontsize=12)
ax2.set_xlabel('日期', fontsize=12)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('chart_2023_index.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print("图1: 全年走势图已生成")

# ===== 图2: 月度涨跌幅图 =====
fig, ax = plt.subplots(figsize=(14, 6))

colors = ['#ff4d4d' if x >= 0 else '#00c853' for x in monthly_df['涨跌幅']]
bars = ax.bar(range(len(monthly_df)), monthly_df['涨跌幅'], color=colors, alpha=0.8, edgecolor='white', linewidth=1)

# 添加数值标签
for i, (bar, val) in enumerate(zip(bars, monthly_df['涨跌幅'])):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + (0.1 if height >= 0 else -0.3),
            f'{val:.2f}%', ha='center', va='bottom' if height >= 0 else 'top', fontsize=10, fontweight='bold')

ax.set_xticks(range(len(monthly_df)))
ax.set_xticklabels([d.strftime('%Y-%m') for d in monthly_df['年月']], rotation=45, ha='right')
ax.set_ylabel('涨跌幅 (%)', fontsize=12)
ax.set_title('2023年月度涨跌幅', fontsize=16, fontweight='bold')
ax.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('chart_2023_monthly.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print("图2: 月度涨跌幅图已生成")

# ===== 图3: 情绪温度计 =====
# 基于涨跌幅计算情绪指数
fig, ax = plt.subplots(figsize=(16, 4))

# 计算20日滚动涨跌幅作为情绪指标
df['情绪指数'] = df['涨跌幅'].rolling(window=20).mean() * 10
df['情绪指数'] = df['情绪指数'].clip(-10, 10)

# 绘制情绪曲线
ax.fill_between(df['日期'], -10, 10, color='gray', alpha=0.1)
ax.fill_between(df['日期'], df['情绪指数'], 0, 
                where=(df['情绪指数'] >= 0), color='#ff4d4d', alpha=0.6, label='乐观')
ax.fill_between(df['日期'], df['情绪指数'], 0, 
                where=(df['情绪指数'] < 0), color='#00c853', alpha=0.6, label='悲观')
ax.plot(df['日期'], df['情绪指数'], color='white', linewidth=1.5)

# 添加情绪区域标注
ax.axhline(y=7, color='#ff1744', linestyle='--', alpha=0.5)
ax.axhline(y=3, color='#ff9800', linestyle='--', alpha=0.5)
ax.axhline(y=-3, color='#4caf50', linestyle='--', alpha=0.5)
ax.axhline(y=-7, color='#00c853', linestyle='--', alpha=0.5)

ax.text(df['日期'].max(), 8.5, '极度贪婪', fontsize=10, color='#ff1744', fontweight='bold')
ax.text(df['日期'].max(), 4, '贪婪', fontsize=10, color='#ff9800', fontweight='bold')
ax.text(df['日期'].max(), -2, '中性', fontsize=10, color='gray', fontweight='bold')
ax.text(df['日期'].max(), -6, '恐惧', fontsize=10, color='#4caf50', fontweight='bold')
ax.text(df['日期'].max(), -9.5, '极度恐惧', fontsize=10, color='#00c853', fontweight='bold')

ax.set_ylim(-10, 10)
ax.set_ylabel('情绪指数', fontsize=12)
ax.set_title('2023年市场情绪温度计', fontsize=16, fontweight='bold')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('chart_2023_sentiment.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print("图3: 情绪温度计图已生成")
print("所有图表生成完成！")
