import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import FancyBboxPatch
import numpy as np
from datetime import datetime
import json
import sys
import io

# 修复Windows控制台编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# 设置中文字体和高质量渲染
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 150

# 读取数据
df = pd.read_csv('sh_index_2024.csv')
df['日期'] = pd.to_datetime(df['日期'])

with open('stats_2024.json', 'r', encoding='utf-8') as f:
    stats = json.load(f)

monthly_df = pd.read_csv('monthly_2024.csv')
monthly_df['年月'] = pd.to_datetime(monthly_df['年月'])

# ===== 颜色方案（A股惯例：红涨绿跌）=====
COLOR_UP = '#E53935'       # 涨：中国红
COLOR_DOWN = '#43A047'     # 跌：绿色
BG_COLOR = '#FAFAFA'       # 背景色
TEXT_COLOR = '#212121'     # 主文字色
GRID_COLOR = '#E0E0E0'     # 网格线
ACCENT_COLOR = '#1E88E5'   # 强调色（蓝色）

# ============================================================
# 图1: 全年走势图 - 更清晰美观版本
# ============================================================
fig = plt.figure(figsize=(18, 10))
fig.patch.set_facecolor('white')

# 创建GridSpec布局
gs = fig.add_gridspec(3, 1, height_ratios=[4, 1.2, 0.8], hspace=0.08)

ax_price = fig.add_subplot(gs[0])
ax_volume = fig.add_subplot(gs[1], sharex=ax_price)
ax_info = fig.add_subplot(gs[2])

# ---- 价格区域 ----
for i, row in df.iterrows():
    color = COLOR_UP if row['收盘'] >= row['开盘'] else COLOR_DOWN
    # 绘制K线实体（粗线）
    body_bottom = min(row['开盘'], row['收盘'])
    body_top = max(row['开盘'], row['收盘'])
    body_height = body_top - body_bottom if body_top > body_bottom else 2  # 最小高度
    
    ax_price.bar(row['日期'], body_height, bottom=body_bottom, 
                  width=0.6, color=color, edgecolor=color, linewidth=0.5, alpha=0.9)
    
    # 绘制影线（细线）
    ax_price.plot([row['日期'], row['日期']], [row['最低'], body_bottom], 
                   color=color, linewidth=0.8, alpha=0.9)
    ax_price.plot([row['日期'], row['日期']], [body_top, row['最高']], 
                   color=color, linewidth=0.8, alpha=0.9)

# 标注关键点位
# 最高点
max_date = pd.Timestamp(stats['全年最高点日期'])
max_val = stats['全年最高点']
ax_price.annotate(f'[UP] 年内最高: {max_val:.2f}\n{max_date.strftime("%Y-%m-%d")}', 
             xy=(max_date, max_val), xytext=(max_date + pd.Timedelta(days=30), max_val - 50),
             fontsize=11, fontweight='bold', color=COLOR_UP,
             arrowprops=dict(arrowstyle='->', color=COLOR_UP, lw=2),
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFEBEE', edgecolor=COLOR_UP, alpha=0.9),
             zorder=100)

# 最低点  
min_date = pd.Timestamp(stats['全年最低点日期'])
min_val = stats['全年最低点']
ax_price.annotate(f'[DOWN] 年内最低: {min_val:.2f}\n{min_date.strftime("%Y-%m-%d")}', 
             xy=(min_date, min_val), xytext=(min_date + pd.Timedelta(days=25), min_val + 80),
             fontsize=11, fontweight='bold', color=COLOR_DOWN,
             arrowprops=dict(arrowstyle='->', color=COLOR_DOWN, lw=2),
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#E8F5E9', edgecolor=COLOR_DOWN, alpha=0.9),
             zorder=100)

# 标注关键事件
events_2024 = [
    ('2024-02-05', '雪球敲入\n2635低点', 2750, '#FF9800'),
    ('2024-04-12', '新"国九条"\n出台', 3100, ACCENT_COLOR),
    ('2024-09-24', '央行组合拳\n救市启动', 2800, COLOR_UP),
    ('2024-09-30', '史诗级暴涨\n+8.06%', 3300, '#FF1744'),
    ('2024-10-08', '3674高点\n开盘即巅峰', 3550, '#D32F2F'),
    ('2024-10-09', '单日暴跌\n-6.62%', 3380, COLOR_DOWN),
]

for date_str, event, y_pos, ecolor in events_2024:
    date = pd.Timestamp(date_str)
    if date >= df['日期'].min() and date <= df['日期'].max():
        ax_price.axvline(x=date, color=ecolor, linestyle='--', alpha=0.4, linewidth=1)
        ax_price.text(date, y_pos, event, fontsize=8, rotation=90, va='bottom', ha='right',
                     color=ecolor, alpha=0.85, fontweight='bold',
                     bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=ecolor, alpha=0.8))

# 年初年末标注
start_val = stats['年初开盘']
end_val = stats['年末收盘']
ax_price.axhline(y=start_val, color='#9E9E9E', linestyle=':', alpha=0.5, linewidth=1)
ax_price.text(df['日期'].min() - pd.Timedelta(days=5), start_val, f'年初:{start_val}', 
              fontsize=9, color='#757575', va='center')
ax_price.text(df['日期'].max(), end_val, f'年末:{end_val} (+{stats["全年涨跌幅"]:.2f}%)', 
              fontsize=10, color=COLOR_UP, va='center', fontweight='bold')

ax_price.set_ylabel('上证指数 (点位)', fontsize=13, fontweight='bold', labelpad=10)
ax_price.set_title('2024年上证指数全年走势图 — 红利低波与小微盘', 
                    fontsize=18, fontweight='bold', pad=15, color=TEXT_COLOR,
                    loc='left',
                    bbox=dict(boxstyle='round,pad=0.5', facecolor='#E3EEFF', edgecolor=ACCENT_COLOR, alpha=0.8))
ax_price.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
ax_price.set_xlim(df['日期'].min() - pd.Timedelta(days=5), df['日期'].max() + pd.Timedelta(days=5))
ax_price.tick_params(labelsize=10)
ax_price.spines['top'].set_visible(False)
ax_price.spines['right'].set_visible(False)

# ---- 成交量区域 ----
colors_vol = [COLOR_UP if c >= o else COLOR_DOWN for c, o in zip(df['收盘'], df['开盘'])]
bars = ax_volume.bar(df['日期'], df['成交量']/1e8, color=colors_vol, alpha=0.75, width=0.8)
ax_volume.set_ylabel('成交量\n(亿股)', fontsize=11, labelpad=8)
ax_volume.grid(True, alpha=0.3, axis='y', linestyle='-', linewidth=0.5)
ax_volume.tick_params(labelsize=10)
ax_volume.spines['top'].set_visible(False)
ax_volume.spines['right'].set_visible(False)

# 标注成交量异常高的日子（9/30、10/08）
vol_highlights = [(pd.Timestamp('2024-09-30'), 1100), (pd.Timestamp('2024-10-08'), 1310)]
for vdate, vval in vol_highlights:
    idx = (df['日期'] == vdate).argmax()
    actual_vol = df.loc[df['日期'] == vdate, '成交量'].values[0]/1e8
    ax_volume.annotate(f'{actual_vol:.0f}亿', xy=(vdate, actual_vol), fontsize=9, 
                      color='#D32F2F', fontweight='bold', ha='center')

# ---- 信息栏区域 ----
ax_info.axis('off')
info_text = (
    f"[DATA] 全年涨跌: {stats['全年涨跌幅']:+.2f}%  |  "
    f"振幅: {stats['全年振幅']}%  |  "
    f"最大回撤: {stats['最大回撤']}%\n"
    f"[UP] 最大单日涨幅: +{stats['最大单日涨幅']}% ({stats['最大单日涨幅日期']})  |  "
    f"[DOWN] 最大单日跌幅: {stats['最大单日跌幅']}% ({stats['最大单日跌幅日期']})"
)
ax_info.text(0.5, 0.5, info_text, transform=ax_info.transAxes, fontsize=11,
            verticalalignment='center', horizontalalignment='center',
            fontfamily='monospace',
            bbox=dict(boxstyle='round,pad=0.8', facecolor='#F5F5F5', edgecolor='#BDBDBD', alpha=0.95))

plt.tight_layout()
plt.savefig('chart_2024_index.png', dpi=200, bbox_inches='tight', facecolor='white', 
            edgecolor='none', pad_inches=0.3)
plt.close()
print("[OK] 图1: 全年走势图已生成")

# ============================================================
# 图2: 月度涨跌幅图 - 更清晰美观版本
# ============================================================
fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor('white')
ax.set_facecolor('#FAFAFA')

months_cn = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']

# 绘制柱状图
x_pos = np.arange(len(monthly_df))
colors_bar = [COLOR_UP if x >= 0 else COLOR_DOWN for x in monthly_df['涨跌幅']]
bars = ax.bar(x_pos, monthly_df['涨跌幅'], color=colors_bar, width=0.65, 
              edgecolor='white', linewidth=1.5, alpha=0.88, zorder=3)

# 数值标签
for i, (bar, val) in enumerate(zip(bars, monthly_df['涨跌幅'])):
    height = bar.get_height()
    ypos = height + 0.4 if height >= 0 else height - 0.6
    va = 'bottom' if height >= 0 else 'top'
    sign = '+' if height >= 0 else ''
    
    # 特殊高亮极端月份
    if abs(val) > 8:
        fontsize = 12
        weight = 'bold'
        color = '#B71C1C' if val > 0 else '#1B5E20'
    else:
        fontsize = 10.5
        weight = 'normal'
        color = TEXT_COLOR
        
    ax.text(bar.get_x() + bar.get_width()/2., ypos, f'{sign}{val:.2f}%', 
            ha='center', va=va, fontsize=fontsize, fontweight=weight, color=color, zorder=5)

# 零线
ax.axhline(y=0, color=TEXT_COLOR, linestyle='-', linewidth=1.2, zorder=2)

# 平均线
avg_return = monthly_df['涨跌幅'].mean()
ax.axhline(y=avg_return, color=ACCENT_COLOR, linestyle='--', linewidth=1.5, alpha=0.7, zorder=2)
ax.text(len(monthly_df)-0.5, avg_return + 0.15, f'月均: {avg_return:+.2f}%', 
        fontsize=10, color=ACCENT_COLOR, fontweight='bold')

ax.set_xticks(x_pos)
ax.set_xticklabels(months_cn, fontsize=11)
ax.set_ylabel('涨跌幅 (%)', fontsize=13, fontweight='bold', labelpad=10)
ax.set_title('2024年月度涨跌幅一览', fontsize=16, fontweight='bold', pad=15, color=TEXT_COLOR)
ax.set_xlim(-0.5, len(monthly_df) - 0.5)
ax.grid(True, alpha=0.3, axis='y', linestyle='-', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Y轴范围留出空间显示标签
ylim_max = max(monthly_df['涨跌幅']) * 1.25
ylim_min = min(monthly_df['涨跌幅']) * 1.3
ax.set_ylim(ylim_min, ylim_max)

plt.tight_layout()
plt.savefig('chart_2024_monthly.png', dpi=200, bbox_inches='tight', facecolor='white',
            edgecolor='none', pad_inches=0.3)
plt.close()
print("[OK] 图2: 月度涨跌幅图已生成")

# ============================================================
# 图3: 市场情绪温度计 - 更清晰美观版本
# ============================================================
fig, ax = plt.subplots(figsize=(18, 5))
fig.patch.set_facecolor('white')
ax.set_facecolor('#FAFAFA')

# 计算情绪指数（基于20日滚动平均涨跌幅，标准化到-10~10）
rolling_return = df['涨跌幅'].rolling(window=20).mean()
sentiment = (rolling_return / rolling_return.std()) * 5
sentiment = sentiment.clip(-10, 10).fillna(0)

# 绘制背景区域
ax.fill_between(df['日期'], 0, 10, alpha=0.08, color=COLOR_UP, zorder=1)
ax.fill_between(df['日期'], -10, 0, alpha=0.08, color=COLOR_DOWN, zorder=1)

# 绘制情绪曲线填充
ax.fill_between(df['日期'], sentiment, 0, where=(sentiment >= 0), 
                color=COLOR_UP, alpha=0.55, label='乐观区域', zorder=2)
ax.fill_between(df['日期'], sentiment, 0, where=(sentiment < 0), 
                color=COLOR_DOWN, alpha=0.55, label='悲观区域', zorder=2)
ax.plot(df['日期'], sentiment, color='white', linewidth=2.5, alpha=0.95, zorder=4)
ax.plot(df['日期'], sentiment, color=TEXT_COLOR, linewidth=1.2, zorder=4)

# 分界线
levels = [
    (7, '#FF1744', '极度贪婪'),
    (3, '#FF5722', '贪婪'),
    (0, '#FFC107', '中性'),
    (-3, '#4CAF50', '恐惧'),
    (-7, '#00C853', '极度恐惧'),
]

for level, lcolor, lname in levels:
    ax.axhline(y=level, color=lcolor, linestyle='--', alpha=0.4, linewidth=1, zorder=3)
    ax.text(df['日期'].max() + pd.Timedelta(days=8), level, lname, 
            fontsize=10, color=lcolor, fontweight='bold', va='center')

# 关键情绪节点标注
key_sentiment_points = [
    ('2024-02-05', '恐慌冰点\n(雪球危机)', -7),
    ('2024-04-12', '新国九条\n提振信心', 1),
    ('2024-07-31', '情绪低迷\n持续磨底', -3),
    ('2024-09-30', '狂欢巅峰\n(+8.06%)', 8),
    ('2024-10-09', '急转直下\n(-6.62%)', -5),
    ('2024-12-31', '平稳收官', 2),
]

for dstr, desc, _ in key_sentiment_points:
    d = pd.Timestamp(dstr)
    if d in sentiment.index or d <= df['日期'].max():
        # 找最近的日期
        nearest_idx = (df['日期'] - d).abs().idxmin()
        s_val = sentiment.iloc[nearest_idx] if isinstance(sentiment, pd.Series) else sentiment.iloc[nearest_idx]
        actual_date = df['日期'].iloc[nearest_idx]
        
        marker_color = COLOR_UP if s_val >= 0 else COLOR_DOWN
        ax.scatter(actual_date, s_val, color=marker_color, s=120, zorder=6, 
                  edgecolor='white', linewidth=2)

# 设置
ax.set_ylim(-10, 10)
ax.set_ylabel('情绪指数', fontsize=13, fontweight='bold', labelpad=10)
ax.set_xlabel('', fontsize=11)
ax.set_title('2024年市场情绪温度计', fontsize=16, fontweight='bold', pad=15, color=TEXT_COLOR)
ax.set_xlim(df['日期'].min(), df['日期'].max() + pd.Timedelta(days=20))
ax.grid(True, alpha=0.25, linestyle='-', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(1.2)

# X轴格式化
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m月'))
plt.xticks(rotation=0, fontsize=10)

plt.tight_layout()
plt.savefig('chart_2024_sentiment.png', dpi=200, bbox_inches='tight', facecolor='white',
            edgecolor='none', pad_inches=0.3)
plt.close()
print("[OK] 图3: 情绪温度计图已生成")
print("\n[ALL DONE] 2024年全部图表生成完成！")
