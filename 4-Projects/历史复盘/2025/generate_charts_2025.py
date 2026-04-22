import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import FancyBboxPatch
import numpy as np
from datetime import datetime
import json
import sys
import io

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Set Chinese font and high quality rendering
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 200
plt.rcParams['font.size'] = 10

# Color scheme - A股: Red=Up, Green=DOWN
RED = '#E53935'
GREEN = '#43A047'
BLUE = '#1E88E5'
ACCENT_COLOR = '#FF6F00'
BG_COLOR = '#FAFAFA'
GRID_COLOR = '#E0E0E0'

print("=" * 60)
print("  2025 A-Share Annual Review Chart Generator")
print("=" * 60)

# Load data
stats = json.load(open('stats_2025.json', 'r', encoding='utf-8'))
df = pd.read_csv('sh_index_2025.csv', parse_dates=['日期'])
df_monthly = pd.read_csv('monthly_2025.csv')
# Rename columns for consistency
df.columns = ['date', 'code', 'open', 'high', 'low', 'close', 'volume', 'amount', 'turnover', 'pct_change']
df_monthly.columns = ['month', 'open', 'close', 'high', 'low', 'volume', 'pct_change']
print(f"\n[DATA] Loaded {len(df)} daily records, stats and monthly data")

# ============================================================
# CHART 1: Full Year Trend (K-line + Volume + Event Markers)
# ============================================================
print("\n[CHART 1] Generating full year trend chart...")

fig, (ax_price, ax_vol) = plt.subplots(2, 1, figsize=(16, 9),
                                        gridspec_kw={'height_ratios': [4, 1]},
                                        facecolor='white')
fig.suptitle('2025 Shanghai Composite Index - Full Year Trend',
             fontsize=18, fontweight='bold', y=0.97, color='#212121')

# Price area chart with gradient effect
ax_price.fill_between(df['date'], df['close'], df['close'].min() * 0.96,
                       alpha=0.15, color=RED)
ax_price.plot(df['date'], df['close'], color=RED, linewidth=1.8,
              label='Close Price', zorder=3)

# Moving averages - 20-day and 60-day
df['ma20'] = df['close'].rolling(window=20).mean()
df['ma60'] = df['close'].rolling(window=60).mean()
ax_price.plot(df['date'], df['ma20'], color='#FFA726', linewidth=1.2,
              label='MA20', alpha=0.85, linestyle='-')
ax_price.plot(df['date'], df['ma60'], color='#42A5F5', linewidth=1.2,
              label='MA60', alpha=0.85, linestyle='--')

# Key points annotation
max_date = pd.Timestamp(stats['全年最高点日期'])
max_val = stats['全年最高点']
min_date = pd.Timestamp(stats['全年最低点日期'])
min_val = stats['全年最低点']

ax_price.annotate(f'[UP] Peak: {max_val:.2f}\n{max_date.strftime("%Y-%m-%d")}',
                  xy=(max_date, max_val), xytext=(max_date + pd.Timedelta(days=25), max_val + 50),
                  fontsize=10, fontweight='bold', color=RED,
                  bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFEBEE',
                            edgecolor=RED, alpha=0.9),
                  arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

ax_price.annotate(f'[DOWN] Bottom: {min_val:.2f}\n{min_date.strftime("%Y-%m-%d")}',
                  xy=(min_date, min_val), xytext=(min_date + pd.Timedelta(days=25), min_val - 80),
                  fontsize=10, fontweight='bold', color=GREEN,
                  bbox=dict(boxstyle='round,pad=0.5', facecolor='#E8F5E9',
                            edgecolor=GREEN, alpha=0.9),
                  arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

# Start and end points
start_close = df.iloc[0]['close']
end_close = df.iloc[-1]['close']
ax_price.scatter([df.iloc[0]['date']], [start_close], color=BLUE, s=80, zorder=5, marker='o')
ax_price.scatter([df.iloc[-1]['date']], [end_close], color=BLUE, s=80, zorder=5, marker='s')
ax_price.annotate(f'Open: {start_close:.2f}', xy=(df.iloc[0]['date'], start_close),
                  xytext=(-40, 15), textcoords='offset points', fontsize=9,
                  color=BLUE, fontweight='bold')
ax_price.annotate(f'Close: {end_close:.2f}', xy=(df.iloc[-1]['date'], end_close),
                  xytext=(-50, -25), textcoords='offset points', fontsize=9,
                  color=BLUE, fontweight='bold')

# Volume bars with color based on price direction
colors_vol = [RED if df['close'].iloc[i] >= df['open'].iloc[i] else GREEN
              for i in range(len(df))]
ax_vol.bar(df['date'], df['volume'] / 100000000, color=colors_vol,
            width=0.8, alpha=0.75, edgecolor='none')
ax_vol.set_ylabel('Volume\n(100M shares)', fontsize=10)
ax_vol.set_xlim(ax_price.get_xlim())
ax_vol.grid(axis='y', alpha=0.35, linestyle='--', color=GRID_COLOR)

# Info box
info_text = (
    f"[DATA] YTD Return: {stats['全年涨跌幅']:+.2f}%  |  "
    f"Range: {stats['全年振幅']}%  |  "
    f"Max Drawdown: {stats['最大回撤']}%\n"
    f"[UP] Best Day: +{stats['最大单日涨幅']}% ({stats['最大单日涨幅日期']})  |  "
    f"[DOWN] Worst Day: {stats['最大单日跌幅']}% ({stats['最大单日跌幅日期']})"
)
props = dict(boxstyle='round,pad=0.6', facecolor='#FFF8E1',
             edgecolor=ACCENT_COLOR, alpha=0.95)
ax_price.text(0.02, 0.97, info_text, transform=ax_price.transAxes, fontsize=9.5,
             verticalalignment='top', bbox=props, family='monospace',
              linespacing=1.6)

ax_price.set_ylabel('Index Points', fontsize=11, fontweight='bold')
ax_price.legend(loc='upper left', fontsize=10, framealpha=0.9)
ax_price.grid(True, alpha=0.3, linestyle='-', color=GRID_COLOR)
ax_price.set_xlim(df['date'].iloc[0] - pd.Timedelta(days=3),
                   df['date'].iloc[-1] + pd.Timedelta(days=3))
ax_price.xaxis.set_major_locator(mdates.MonthLocator())
ax_price.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
plt.setp(ax_price.xaxis.get_majorticklabels(), rotation=0, ha='center')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('chart_2025_index.png', dpi=200, bbox_inches='tight', facecolor='white',
            edgecolor='none', pad_inches=0.3)
plt.close()
print("[OK] Chart 1: Full year trend saved as chart_2025_index.png")


# ============================================================
# CHART 2: Monthly Returns Bar Chart
# ============================================================
print("\n[CHART 2] Generating monthly returns chart...")

fig, ax = plt.subplots(figsize=(14, 7), facecolor='white')
fig.suptitle('2025 Monthly Returns Analysis',
             fontsize=17, fontweight='bold', y=0.96, color='#212121')

months = df_monthly['month'].tolist()
returns = df_monthly['pct_change'].tolist()
colors_bar = [RED if r >= 0 else GREEN for r in returns]
abs_max = max(abs(r) for r in returns) * 1.15

bars = ax.bar(months, returns, color=colors_bar, edgecolor='white', linewidth=1.2,
               width=0.72, alpha=0.88, zorder=3)

for i, (bar, ret) in enumerate(zip(bars, returns)):
    height = bar.get_height()
    y_pos = height + abs_max * 0.02 if height >= 0 else height - abs_max * 0.03
    va = 'bottom' if height >= 0 else 'top'
    sign = '+' if ret > 0 else ''
    label_color = RED if ret >= 0 else GREEN
    ax.text(bar.get_x() + bar.get_width()/2, y_pos,
            f'{sign}{ret:.2f}%',
            ha='center', va=va, fontsize=12, fontweight='bold',
            color=label_color, zorder=4)

# Zero line emphasis
ax.axhline(y=0, color='#424242', linewidth=2, zorder=2)
ax.axhline(y=0, color='#FFC107', linewidth=0.8, linestyle='--', zorder=2, alpha=0.6)

# Stats box
ytd_ret = sum(returns)
pos_months = sum(1 for r in returns if r > 0)
neg_months = sum(1 for r in returns if r < 0)
best_m = months[returns.index(max(returns))]
worst_m = months[returns.index(min(returns))]

stats_text = (
    f"[SUMMARY]\n"
    f"YTD: {ytd_ret:+.2f}%\n"
    f"Up/Down: {pos_months}/{neg_months}\n"
    f"Best: {best_m} ({max(returns):+.2f}%)\n"
    f"Worst: {worst_m} ({min(returns):+.2f}%)"
)
props = dict(boxstyle='round,pad=0.55', facecolor='#F3E5F5',
             edgecolor='#8E24AA', alpha=0.95)
ax.text(0.98, 0.97, stats_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='right', bbox=props,
        family='monospace', linespacing=1.5)

ax.set_ylim(-abs_max * 1.18, abs_max * 1.18)
ax.set_ylabel('Return (%)', fontsize=11, fontweight='bold')
ax.set_xlabel('Month', fontsize=11, fontweight='bold')
ax.grid(axis='y', alpha=0.3, linestyle='-', color=GRID_COLOR, zorder=1)
ax.set_axisbelow(True)

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig('chart_2025_monthly.png', dpi=200, bbox_inches='tight', facecolor='white',
            edgecolor='none', pad_inches=0.3)
plt.close()
print("[OK] Chart 2: Monthly returns saved as chart_2025_monthly.png")


# ============================================================
# CHART 3: Market Sentiment Thermometer
# ============================================================
print("\n[CHART 3] Generating sentiment thermometer...")

fig, ax = plt.subplots(figsize=(13, 8), facecolor='white')
fig.suptitle('2025 A-Share Market Sentiment Thermometer',
             fontsize=17, fontweight='bold', y=0.95, color='#212121')

months_s = df_monthly['month'].tolist()
rets = df_monthly['pct_change'].tolist()
vols = [v / max(df_monthly['volume']) for v in df_monthly['volume']]
sentiments = []
window = 3

for i in range(len(rets)):
    start_idx = max(0, i - window + 1)
    recent_rets = rets[start_idx:i+1]
    vol_factor = vols[i]

    momentum_score = sum(recent_rets) / len(recent_rets) / 5
    vol_score = vol_factor

    combined = (momentum_score * 0.65 + vol_score * 0.35) * 45 + 50
    sentiments.append(max(8, min(92, combined)))

x_pos = np.arange(len(months_s))
bar_colors = []
for s in sentiments:
    if s >= 70:
        bar_colors.append('#D32F2F')   # Hot red
    elif s >= 55:
        bar_colors.append('#FF9800')   # Warm orange
    elif s >= 42:
        bar_colors.append('#4CAF50')   # Neutral green
    elif s >= 28:
        bar_colors.append('#2196F3')   # Cool blue
    else:
        bar_colors.append('#1565C0')   # Cold dark blue

bars = ax.bar(x_pos, sentiments, color=bar_colors, edgecolor='white',
               width=0.68, alpha=0.9, linewidth=1.5, zorder=3)

for i, (bar, s) in enumerate(zip(bars, sentiments)):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
            f'{s:.0f}',
            ha='center', va='bottom', fontsize=12, fontweight='bold',
            color='#37474F', zorder=4)

for level in [22, 38, 52, 68, 82]:
    ax.axhline(y=level, color='#ECEFF1', linewidth=1, zorder=1, linestyle='-')
    alpha_val = 0.07 if level not in [38, 68] else 0.12
    ax.axhspan(level - 16, level + 16, facecolor=['#E3F2FD', '#BBDEFB', '#C8E6C9',
                 '#FFF3E0', '#FFEBEE'][[22, 38, 52, 68, 82].index(level)],
               alpha=alpha_val, zorder=0)

zone_labels = [
    (14, 'EXTREME FEAR\n(Panic Zone)', '#1565C0'),
    (30, 'FEAR\n(Cautious)', '#2196F3'),
    (46, 'NEUTRAL\n(Balanced)', '#4CAF50'),
    (62, 'GREED\n(Optimistic)', '#FF9800'),
    (78, 'EXTREME GREED\n(Euphoria)', '#D32F2F'),
]
for y_pos, label, clr in zone_labels:
    ax.text(-0.55, y_pos, label, ha='left', va='center', fontsize=9.5,
            fontweight='bold', color=clr, alpha=0.88)

avg_sentiment = np.mean(sentiments)
ax.axhline(y=avg_sentiment, color='#7B1FA2', linewidth=2.5, linestyle='--',
           zorder=5, alpha=0.85, label=f'Annual Avg: {avg_sentiment:.1f}')
ax.text(len(months_s) - 0.3, avg_sentiment + 2.5,
        f'Avg: {avg_sentiment:.1f}',
        ha='right', va='bottom', fontsize=11, fontweight='bold',
        color='#7B1FA2', zorder=6)

summary_text = (
    f"[SENTIMENT SUMMARY]\n"
    f"Avg Score: {avg_sentiment:.1f}/100\n"
    f"Highest: {max(sentiments):.0f} ({months_s[sentiments.index(max(sentiments))]})\n"
    f"Lowest: {min(sentiments):.0f} ({months_s[sentiments.index(min(sentiments))]})\n"
    f"Volatility: {(np.std(sentiments)):.1f}"
)
props = dict(boxstyle='round,pad=0.55', facecolor='#EDE7F6',
             edgecolor='#7B1FA2', alpha=0.95)
ax.text(0.98, 0.96, summary_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='right', bbox=props,
        family='monospace', linespacing=1.5)

ax.set_xticks(x_pos)
ax.set_xticklabels(months_s, fontsize=11, fontweight='bold')
ax.set_ylim(0, 102)
ax.set_ylabel('Sentiment Index', fontsize=11, fontweight='bold')
ax.set_xlabel('Month', fontsize=11, fontweight='bold')
ax.grid(axis='y', alpha=0.2, linestyle='--', color='#BDBDBD', zorder=1)
ax.set_axisbelow(True)

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

ax.legend(loc='upper left', fontsize=11, framealpha=0.9)

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.savefig('chart_2025_sentiment.png', dpi=200, bbox_inches='tight', facecolor='white',
            edgecolor='none', pad_inches=0.3)
plt.close()
print("[OK] Chart 3: Sentiment thermometer saved as chart_2025_sentiment.png")

# ============================================================
# DONE
# ============================================================
print("\n" + "=" * 60)
print("  [ALL DONE] All 2025 charts generated successfully!")
print("=" * 60)
print(f"\n  Output files:")
print(f"    - chart_2025_index.png      (Full Year Trend)")
print(f"    - chart_2025_monthly.png     (Monthly Returns)")
print(f"    - chart_2025_sentiment.png   (Sentiment Thermometer)")
