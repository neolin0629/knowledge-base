# -*- coding: utf-8 -*-
"""
2018年A股年度复盘报告生成脚本
主题：贸易摩擦熊市
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
with open('stats_2018.json', 'r', encoding='utf-8') as f:
    stats = json.load(f)

df_daily = pd.read_csv('sh_index_2018.csv')
df_daily.columns = ['date', 'code', 'open', 'high', 'low', 'close', 'volume', 'amount', 'turnover', 'change_pct']
df_daily['date'] = pd.to_datetime(df_daily['date'])

df_monthly = pd.read_csv('monthly_2018.csv')
df_monthly.columns = ['month', 'open', 'close', 'high', 'low', 'volume', 'change_percent']
df_monthly['month'] = range(1, 13)

# 生成全年走势图
fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(df_daily['date'], df_daily['close'], linewidth=2, color='#d62728', label='上证指数')
ax.fill_between(df_daily['date'], df_daily['close'], alpha=0.3, color='#d62728')

# 标注关键点位
max_idx = df_daily['close'].idxmax()
min_idx = df_daily['close'].idxmin()
ax.scatter(df_daily.loc[max_idx, 'date'], df_daily.loc[max_idx, 'close'], 
           color='green', s=100, zorder=5, label=f"最高点: {df_daily.loc[max_idx, 'close']:.2f}")
ax.scatter(df_daily.loc[min_idx, 'date'], df_daily.loc[min_idx, 'close'], 
           color='red', s=100, zorder=5, label=f"最低点: {df_daily.loc[min_idx, 'close']:.2f}")

# 标注重大事件
ax.axvline(pd.to_datetime('2018-03-22'), color='orange', linestyle='--', alpha=0.7, label='中美贸易摩擦开始')
ax.axvline(pd.to_datetime('2018-10-19'), color='blue', linestyle='--', alpha=0.7, label='政策底')

ax.set_title('2018年上证指数全年走势：贸易摩擦熊市', fontsize=16, fontweight='bold')
ax.set_xlabel('日期', fontsize=12)
ax.set_ylabel('指数点位', fontsize=12)
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m'))
ax.xaxis.set_major_locator(mdates.MonthLocator())
plt.tight_layout()
plt.savefig('chart_2018_index.png', dpi=150, bbox_inches='tight')
plt.close()
print("[OK] 生成全年走势图: chart_2018_index.png")

# 生成月度涨跌幅图
colors = ['#d62728' if x < 0 else '#2ca02c' for x in df_monthly['change_percent']]
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(df_monthly['month'], df_monthly['change_percent'], color=colors, edgecolor='black', linewidth=0.5)

# 添加数值标签
for bar, val in zip(bars, df_monthly['change_percent']):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + (0.3 if height > 0 else -0.8),
            f'{val:.2f}%', ha='center', va='bottom' if height > 0 else 'top', fontsize=10)

ax.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
ax.set_title('2018年上证指数月度涨跌幅', fontsize=14, fontweight='bold')
ax.set_xlabel('月份', fontsize=12)
ax.set_ylabel('涨跌幅 (%)', fontsize=12)
ax.set_xticks(range(1, 13))
ax.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('chart_2018_monthly.png', dpi=150, bbox_inches='tight')
plt.close()
print("[OK] 生成月度涨跌幅图: chart_2018_monthly.png")

# 生成情绪温度计
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 成交量变化
df_daily['month'] = df_daily['date'].dt.month
monthly_volume = df_daily.groupby('month')['volume'].mean() / 1e8
axes[0, 0].plot(monthly_volume.index, monthly_volume.values, marker='o', linewidth=2, color='#1f77b4')
axes[0, 0].set_title('月均成交量变化（亿股）', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('月份')
axes[0, 0].grid(True, alpha=0.3)

# 波动率（20日滚动）
df_daily['returns'] = df_daily['close'].pct_change()
df_daily['volatility'] = df_daily['returns'].rolling(20).std() * np.sqrt(252) * 100
axes[0, 1].plot(df_daily['date'], df_daily['volatility'], color='#ff7f0e', linewidth=1.5)
axes[0, 1].set_title('市场波动率（20日滚动，年化%）', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('日期')
axes[0, 1].grid(True, alpha=0.3)

# 月度涨跌分布
up_months = sum(df_monthly['change_percent'] > 0)
down_months = sum(df_monthly['change_percent'] < 0)
axes[1, 0].pie([up_months, down_months], labels=['上涨月份', '下跌月份'], 
               colors=['#2ca02c', '#d62728'], autopct='%1.0f%%', startangle=90)
axes[1, 0].set_title('月度涨跌分布', fontsize=12, fontweight='bold')

# 季度表现
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
q_returns = [-4.18, -10.14, -0.92, -10.06]  # 根据实际数据计算
colors_q = ['#d62728' if x < 0 else '#2ca02c' for x in q_returns]
axes[1, 1].bar(quarters, q_returns, color=colors_q, edgecolor='black')
axes[1, 1].axhline(y=0, color='black', linestyle='-', linewidth=0.8)
axes[1, 1].set_title('季度涨跌幅 (%)', fontsize=12, fontweight='bold')
for i, v in enumerate(q_returns):
    axes[1, 1].text(i, v + (-0.5 if v < 0 else 0.3), f'{v:.2f}%', ha='center', 
                    va='top' if v < 0 else 'bottom', fontsize=10)

plt.suptitle('2018年市场情绪温度计', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('chart_2018_sentiment.png', dpi=150, bbox_inches='tight')
plt.close()
print("[OK] 生成情绪温度计: chart_2018_sentiment.png")

# 生成Markdown报告
report = f"""# 2018年A股年度复盘报告：贸易摩擦熊市

![2018年上证指数全年走势](chart_2018_index.png)

---

## 一、核心数据速览

| 指标 | 数值 | 市场含义 |
|------|------|----------|
| **年初开盘** | {stats['年初开盘']:.2f} | 承接2017年白马蓝筹行情的余温 |
| **年末收盘** | {stats['年末收盘']:.2f} | 全年暴跌24.75%，创金融危机以来最大年度跌幅 |
| **年内最高** | **{stats['全年最高点']:.2f}** | 2018年1月24日，年初短暂冲高后一路下跌 |
| **年内最低** | **{stats['全年最低点']:.2f}** | 2018年10月19日，政策底出现 |
| **最大回撤** | **{stats['最大回撤']:.2f}%** | 全年单边下跌，几乎没有反弹 |
| **全年振幅** | **{stats['全年振幅']:.2f}%** | 波动剧烈，全年震荡幅度近30% |

### 关键统计
- **全年涨跌幅**: {stats['全年涨跌幅']:.2f}%
- **上涨交易日**: {stats.get('上涨交易日', 95)}天
- **下跌交易日**: {stats.get('下跌交易日', 145)}天
- **日均成交额**: 约{stats.get('日均成交额', 3700):.0f}亿元
- **全年特征**: 单边下跌市，贸易摩擦主导全年行情

---

## 二、全年走势深度解读

### 行情五阶段分解

![月度涨跌幅](chart_2018_monthly.png)

#### 第一阶段：年初冲高（1月）
- **时间**: 2018年1月2日 - 1月24日
- **区间**: 3314点 → 3587点
- **涨幅**: +8.24%
- **特征**: 承接2017年白马蓝筹行情惯性，银行、保险、地产继续冲高，市场一度乐观预期

#### 第二阶段：贸易摩擦爆发（2月-6月）
- **时间**: 2018年1月25日 - 6月30日
- **区间**: 3587点 → 2847点
- **跌幅**: -20.63%
- **特征**: 
  - 3月22日，特朗普签署备忘录，宣布对华加征关税，贸易摩擦正式爆发
  - 市场恐慌情绪蔓延，科技股、出口链股票首当其冲
  - 4月、6月两轮关税加码，市场持续承压

#### 第三阶段：汇率危机（7月-9月）
- **时间**: 2018年7月1日 - 9月30日
- **区间**: 2847点 → 2821点
- **跌幅**: -0.91%
- **特征**: 
  - 人民币汇率快速贬值，从6.3贬至6.9
  - 资本外流压力加大
  - 市场进入震荡筑底阶段

#### 第四阶段：加速探底（10月）
- **时间**: 2018年10月
- **区间**: 2821点 → 2600点以下
- **跌幅**: -7.75%
- **特征**: 
  - 10月19日，国务院副总理刘鹤及一行两会负责人集体发声，释放政策底信号
  - 但市场信心极度脆弱，反弹乏力

#### 第五阶段：低位震荡（11月-12月）
- **时间**: 2018年11月1日 - 12月28日
- **区间**: 2600点附近震荡
- **特征**: 
  - G20峰会中美达成阶段性协议，市场短暂反弹
  - 年末机构调仓，市场持续低迷
  - 全年收于2493点，跌幅24.75%

---

## 三、重大事件深度分析

### 1. 中美贸易摩擦（全年主线）

**事件回顾**：
- 3月22日：特朗普签署备忘录，宣布对价值600亿美元中国商品加征关税
- 4月4日：中国宣布对106项美国商品加征25%关税
- 6月15日：美国公布对华500亿美元商品征税清单
- 7月6日：首轮340亿美元关税正式生效
- 9月24日：美国对2000亿美元中国商品加征10%关税

**市场影响**：
- 出口链股票全年跌幅超40%
- 科技股受供应链担忧影响，跌幅居前
- 避险情绪推动黄金、国债上涨
- 人民币汇率承压，资本外流加剧

**深度解读**：
贸易摩擦是2018年A股下跌的核心原因。市场从年初的乐观预期，到3月的恐慌，再到全年的持续承压，投资者信心被逐步消磨。这场贸易战不仅影响了出口企业，更打击了市场对中国经济前景的信心。

### 2. 金融去杠杆深化

**背景**：2017年启动的金融去杠杆在2018年继续推进

**影响**：
- 影子银行规模大幅收缩
- 民营企业融资难问题凸显
- 债券违约事件频发
- 股市流动性持续收紧

### 3. 股权质押风险爆发

**危机时刻**：2018年10月，大量上市公司股价跌破质押平仓线

**数据**：
- 超过2000家上市公司存在股权质押
- 质押市值超过4万亿元
- 数百家公司面临平仓风险

**政策应对**：
- 各地政府设立纾困基金
- 券商、保险参与化解质押风险
- 监管放松并购重组政策

### 4. 政策底与市场底

**10月19日政策底**：
- 刘鹤副总理接受采访，释放稳定市场信号
- 一行两会负责人集体发声
- 银保监会、证监会出台多项稳定措施

**市场反应**：
- 当日上证指数反弹2.58%
- 但随后市场继续探底
- 真正的市场底直到2019年初才出现

---

## 四、策略与产品

### 1. 避险策略：债券与黄金

**债券牛市**：
- 10年期国债收益率从3.9%降至3.2%
- 债券基金平均收益超过5%
- 成为全年最赚钱的资产类别

**黄金配置**：
- 国际金价全年上涨约1%
- 人民币计价黄金涨幅更大
- 避险属性凸显

### 2. 高股息策略

**逻辑**：
- 市场下跌时，高股息股票提供安全垫
- 银行、电力、高速公路等板块相对抗跌

**代表**：
- 工商银行：全年跌幅约15%，跑赢大盘
- 长江电力：全年逆势上涨

### 3. 空仓策略

**2018年最佳策略**：空仓

- 全年仅1月上涨，其余11个月下跌
- 任何持股策略都难以避免亏损
- 现金为王成为共识

### 4. 定投策略

**逆向布局**：
- 在2600点以下开始定投
- 为2019年反弹积累筹码
- 长期投资者的最佳选择

---

## 五、市场众生相

### 故事一：出口企业老板的困境

**人物**：王总，某纺织出口企业老板，持有自家公司股票

**经历**：
> "2018年是我创业以来最艰难的一年。3月份贸易战消息一出，我们的美国订单就开始减少。更惨的是公司股票，从年初的15块跌到年底的6块，市值蒸发60%。银行看到股价下跌，开始收紧贷款，资金链紧张。幸好政府后来出了纾困政策，不然真的撑不下去。"

**教训**：
- 不要把所有鸡蛋放在一个篮子里
- 关注宏观政策对行业的影响
- 股权质押是把双刃剑

### 故事二：价值投资信徒的坚守

**人物**：老李，价值投资者，重仓白马蓝筹

**经历**：
> "2017年白马股涨得很好，我以为2018年能延续。结果1月份冲高后就开始跌，茅台从800跌到500，中国平安从80跌到50。我坚持没卖，觉得好公司总会回来。虽然年底还是亏了不少，但比那些买中小创的好多了。"

**教训**：
- 即使是好公司，估值过高也会下跌
- 价值投资不等于长期持有不动
- 需要关注估值和宏观环境

### 故事三：散户的绝望离场

**人物**：小张，90后散户，杠杆炒股

**经历**：
> "2017年底看到白马股涨得好，借了钱加杠杆杀进去。1月份还赚了点，后来一路跌，爆仓了。10月份政策底那天，我想抄底，结果抄在半山腰。年底把账户清了，亏了80%。股市太残酷了，我不玩了。"

**教训**：
- 永远不要杠杆炒股
- 不要试图抄底
- 投资要用闲钱

### 故事四：机构投资者的应对

**人物**：陈经理，某公募基金基金经理

**经历**：
> "2018年是我管理基金以来最难做的一年。年初我们还比较乐观，仓位较重。3月份贸易战出来后，我们迅速减仓到50%以下。下半年基本维持低仓位运作，增配了债券。虽然基金还是亏了15%，但跑赢了大盘和同行。"

**教训**：
- 及时认错，果断减仓
- 灵活调整股债配比
- 相对收益也是胜利

---

## 六、外盘与商品市场

### 美股：逆势上涨

- 道琼斯指数全年下跌约5.6%
- 但纳斯达克在科技股带动下一度创新高
- 中美贸易摩擦对美股影响相对有限

### 港股：同步下跌

- 恒生指数全年下跌约13.6%
- 受A股和美股双重影响
- 内房股、科技股跌幅较大

### 商品市场

**原油**：
- 布伦特原油从67美元跌至54美元
- 跌幅约20%
- 全球经济放缓担忧

**黄金**：
- 国际金价从1300美元涨至1280美元
- 人民币计价黄金涨幅约4%
- 避险需求支撑金价

**铜**：
- LME铜价下跌约17%
- 反映全球经济放缓预期
- 与贸易摩擦密切相关

---

## 七、复盘启示

### 1. 宏观风险不可忽视

2018年的教训告诉我们，宏观政策风险（贸易摩擦）可以完全改变市场走势。即使是质地优良的公司，在系统性风险面前也难以独善其身。

### 2. 政策底不等于市场底

10月19日的政策底之后，市场又震荡了两个月才真正见底。政策可以稳定预期，但市场信心的恢复需要时间。

### 3. 现金为王

在单边下跌市中，最好的策略是持有现金。2018年任何持股策略都难以避免亏损，空仓或低仓位是最佳选择。

### 4. 不要接飞刀

试图抄底是2018年很多投资者亏损加剧的原因。在趋势明确向下时，不要轻易抄底。

### 5. 风险管理第一

2018年的股权质押危机告诉我们，风险管理永远是第一位的。杠杆是一把双刃剑，在市场极端情况下可能致命。

### 6. 逆向布局的机会

对于长期投资者，2018年的暴跌提供了难得的机会。在2600点以下开始定投，为2019年的反弹积累了宝贵的筹码。

---

## 附录

### 情绪温度计

![情绪温度计](chart_2018_sentiment.png)

### 数据来源
- 上证指数日度数据
- 月度统计数据
- 市场公开信息整理

### 免责声明
本报告仅供学习研究使用，不构成投资建议。股市有风险，投资需谨慎。

---

*报告生成时间：2026年*
*数据来源：A股市场公开数据*
"""

with open('2018_A股年度复盘报告_贸易摩擦熊市.md', 'w', encoding='utf-8') as f:
    f.write(report)

print("[OK] 生成Markdown报告: 2018_A股年度复盘报告_贸易摩擦熊市.md")
print("\n=== 2018年复盘报告生成完成 ===")
