---
type: topic
status: ready-to-draft
priority: high
source_notes: []
source_raw:
  - "[[How I'd Become a Quant If I Had to Start Over Tomorrow如果明天让我重新开始，我会如何成为一名量化分析师]]"
  - "[[2026年，普通人如何量化交易]]"
source_inspiration: 《真正的普通人量化路径》的配套篇——那篇劝退普通散户，这篇给真正想进机构的人一张完整地图
target_account: dahao
target_hook: 数据冲击
estimated_value: 高
created: 2026-04-22
related_topic: "[[适合普通人的量化路径]]"
---

## 一、读者画像（精确锁定）

**目标读者**：有一定数理基础（本科理工科），明确想进入专业量化机构的人。
- 海外方向：Jane Street / Citadel / HRT / DE Shaw / Two Sigma
- 国内方向：幻方 / 九坤 / 明汯 / 国信（量化研究员方向）
- 不是"对量化感兴趣的散户"，是"手里有子弹但不知道怎么系统走完这条路"的人

**与《真正的普通人量化路径》的分工**：
- 普通人篇 = 你不需要走这条路，这里是你真正需要的路
- 本篇 = 你确认要走这条路，这是18个月的真实地图

---

## 二、核心立意（refined）

**原文 gemchanger 原话（核心锚点）**：
> "Before stochastic calculus, you're a data scientist who likes finance. After it, you're a quant."
> 「随机微积分之前，你是个喜欢金融的数据科学家；之后，你才是量化分析师。」

**本文立意**：
专业 Quant 的学习路径不是"数学书单"，是**关卡制游戏**——每一关有明确的过关条件，跳关必死。大多数人失败不是因为不努力，是因为不知道"每一关我到底需要证明自己会什么"。

这篇文章要给出的不是书单，而是：
1. 每个阶段的**可验证 go/no-go 标准**（能写出什么代码、能推导什么公式）
2. 四种岗位方向（QR / QD / QT / Risk Quant）所需技能的**真实差异**
3. "AI 时代数学还重要吗"这个问题的**反常识答案**

---

## 三、关键数据点（直接来自 source_raw，可引用）

### 薪资数据（2025年，gemchanger 原文）

| 层级 | 机构 | 应届 Total Comp | 中期 (3–7年) | 资深 (8年+) |
|---|---|---|---|---|
| 顶层 | Jane Street / Citadel / HRT | $300K–$500K+ | $550K–$950K | $1M–$3M+ |
| 次顶 | Two Sigma / DE Shaw | $250K–$350K | $350K–$625K | $575K–$1.2M |
| 标杆 | Jane Street 全员平均 | **$140万/年**（2025年H1 报告值） | — | — |

> Jane Street 2025年H1 员工平均薪酬 $1.4M/年，这是平均值，不是顶点。

### AI/ML 招聘数据（gemchanger 原文）

> 2025 年金融行业 AI/ML 岗位招聘同比增长 **88%**。

### 关于国内机构（待补充，见第六节）

---

## 四、五关卡路径（核心内容框架）

gemchanger 原文的完整路径是**层层递进的 5 级关卡**，每级有书、有推导、有编程作业作为过关验证：

### Level 1：概率论（3–4周）
**核心转变**：从"这件事发生不发生"→ "在 XX 条件下这件事发生的概率是多少"

**必须掌握的概念**：
- 条件概率（Volume 高时上涨概率从 60% → 75%，后者才是信号）
- 贝叶斯更新（新信息出来，怎么精确调整概率估计）
- 期望值 × 方差（正期望但方差极大 = 本金不够就会在"长期"到来前先爆）
- 凯利公式（最优仓位 = 全凯利的一半，原文明确写"胜率估计有误差时全凯利和全梭哈一样危险"）

**go/no-go 验证**：
- [ ] 能写 Python 实现贝叶斯更新器（输入先验+似然，输出后验）
- [ ] 能用凯利公式算仓位并解释为什么打半折

**教材**：Blitzstein & Hwang《Introduction to Probability》前 6 章（哈佛免费 PDF）

---

### Level 2：统计学（4–5周）
**核心转变**：从"模型回测赚了"→ "这个结果是真信号还是多重比较的运气"

**必须掌握的概念**：
- 假设检验：你的策略 H₀ = "零预期收益"，p < 0.05 不够——你测试了多少个策略？
- **多重比较陷阱（关键）**：随机生成 1000 个策略，50 个会纯靠运气 p < 0.05；你前 10 个策略大概率都是那群运气好的猴子
- Bonferroni 校正（N 个测试时，显著性门槛 = 0.05 / N）
- 线性回归 + Newey-West 标准误差（金融数据有自相关+异方差，默认 OLS 标准误差是错的）
- MLE（最大似然估计）：所有金融模型的校准手段——GARCH、跳跃扩散、期权定价全靠它

**go/no-go 验证**：
- [ ] 用 yfinance 下载真实收益率 → 正态检验（必然失败）→ MLE 拟合 t 分布
- [ ] 对股票组合跑 Fama-French 三因子回归，读懂截距 α 是否显著

**教材**：Wasserman《All of Statistics》第 1–13 章（CMU 免费 PDF）

---

### Level 3：线性代数（4–6周）
**核心转变**：从"我理解了资产"→ "我能同时处理 500 只资产的协方差结构"

**必须掌握的概念**：
- 协方差矩阵 Σ（500只股票 = 500×500矩阵，含 125,250 个独立元素）
- 特征值分解：500只股票的前 5 个特征向量解释 **70%** 的总方差——其余都是噪声
- Markowitz 均值-方差优化（投资组合构建的基础）
- PCA（因子投资的数学基础）

**go/no-go 验证**：
- [ ] 对 A股/S&P 500 收益率做 PCA，画出特征值谱，识别前 3 个主成分
- [ ] 用 cvxpy 从零实现 Markowitz 优化（含交易成本约束）

**教材**：Strang《Introduction to Linear Algebra》+ MIT 18.06 全套讲座（不可跳过）

---

### Level 4：微积分 & 凸优化（4–5周）
**核心转变**：从"会用工具"→ "能推导工具的边界条件"

**必须掌握的概念**：
- 泰勒展开：Delta 对冲是一阶近似，Gamma 对冲是二阶修正
- 为什么伊藤微积分与普通微积分不同：随机过程中 (dW)² = dt 不可忽略（这是下一关的基础）
- 梯度下降 & 凸优化（神经网络和组合优化的共同基础）

**go/no-go 验证**：
- [ ] 从零实现梯度下降，最小化 Rosenbrock 函数
- [ ] 用 cvxpy 解含交易成本约束的组合优化

**教材**：Boyd & Vandenberghe《Convex Optimization》第 1–5 章（斯坦福免费 PDF）

---

### Level 5：随机微积分（6–8周，最难）
**核心转变**：这是关卡终点，也是身份认证

> "Before stochastic calculus, you're a data scientist who likes finance. After it, you're a quant."

**必须掌握的概念**：
- 布朗运动（维纳过程）：路径连续但处处不可微
- 伊藤引理：为什么随机微积分比普通微积分多一项——(dW)² = dt 是一阶项，不可丢
- Black-Scholes PDE 的推导：Delta 对冲消去随机项 → 无风险组合 → 期权定价不依赖 μ（漂移项消失，这个洞见第一次看到会震惊）
- Greeks：Delta（对冲比率）/ Gamma（重新对冲频率）/ Vega（波动率交易的命脉）

**go/no-go 验证**：
- [ ] 手写推导 Black-Scholes PDE（笔+纸，不看书）
- [ ] Python 实现 Black-Scholes 定价，与蒙特卡罗对比验证收敛
- [ ] 对 f(S) = ln(S) 应用伊藤引理，推导出 -σ²/2 项

**教材**：Shreve《Stochastic Calculus for Finance II》（黄金标准）；入门版：Arguin《A First Course in Stochastic Calculus》

---

## 五、四个岗位方向（差异化技能要求）

| 岗位 | 核心技能 | 数学深度 | 编程要求 | 薪酬波动 |
|---|---|---|---|---|
| Quant Researcher (QR) | 发现 Alpha，建预测模型 | 最高（PhD 级数学/ML） | 生产级 Python + 研究能力 | 高且稳定 |
| Quant Developer (QD) | 交易系统、执行引擎、数据管道 | 中（不需要推导，需要理解） | 生产级 C++/Rust/Python，低延迟 | 中 |
| Quant Trader (QT) | 运营资本、实时风险决策 | 中（直觉 > 推导） | 交易工具为主 | 最高，波动最大（顶尖年份 8 位数） |
| Risk Quant | VaR、压力测试、监管合规 | 中（模型验证为主） | Python + 统计工具 | 稳定，上限较低 |

**新增方向**：AI/ML Quant——深度学习信号生成，2025年招聘同比 +88%，增长最快。

---

## 六、面试闯关（来自 gemchanger 原文）

**海外顶级机构标准流程**：
```
简历筛选
  ↓
Online Assessment（Zetamac 心算，目标 50+；逻辑谜题）
  ↓
Phone Screen（概率问题、博弈/投注问题）
  ↓
Superday（3–5 轮连续面试：模拟交易 + 编程 + 白板推导）
```

**Jane Street 特殊性**：
- 故意出难度过高的题，考察"你如何用提示、如何协作"，不是考察"能否独立解出"
- 最近一届实习生：2/3 是 CS 专业，1/3 是数学专业
- **不需要金融知识**——这是反常识点

**主要备考资源**：
- Zhou《Practical Guide to Quantitative Finance Interviews》（绿皮书，200+ 真题，必备）
- [QuantGuide.io](https://quantguide.io/)（"量化版 LeetCode"）
- Jane Street 每月谜题（难度高于面试，但做了就是降维打击）
- Jane Street Figgie 纸牌游戏（训练做市思维）

**加分赛道（竞赛）**：
- Jane Street Kaggle（奖金 $10 万）
- WorldQuant BRAIN（10 万+用户，付费购买 Alpha 信号，做出来相当于公开背书）
- Citadel Datathon（拿奖直通面试）

---

## 七、三个反常识结论（文章立场，每条有原文支撑）

### 1. "AI 时代数学反而更重要"
原文原话：
> "The math is the moat. AI can write code and suggest strategies. But the ability to derive why Itô's lemma has an extra term... that mathematical fluency separates quants who build edge from quants who borrow it. And borrowed edge expires."
> 「数学是护城河。AI 能写代码、能提策略，但能推导出伊藤引理为何多出一项的人……那种数学流利度，才能把"构建优势"的 Quant 和"借用优势"的 Quant 区分开。借来的优势会过期。」

### 2. "估计误差，不是市场，才是你真正的敌人"
原文原话：
> "Estimation error is the real enemy. Full Kelly betting, unconstrained Markowitz, ML models with too many features - they all fail for the same reason: overfitting noisy estimates. The math works perfectly with true parameters. You never have true parameters."
> 「全凯利投注、无约束 Markowitz、特征过多的 ML 模型——它们都因为同一个原因失败：在嘈杂的参数估计上过拟合。数学在参数真实时完美运作。你永远没有真实的参数。」

### 3. "工具已经民主化，信念没有"
原文原话：
> "Tools have democratized. Conviction hasn't. Anyone can access QuantLib, Polygon.io, and PyTorch. Technology is necessary but not sufficient. Edge lives in unique data, unique models, or unique execution — not better pip installs."
> 「任何人都能 pip install。但优势在独特的数据、独特的模型或独特的执行——不在于更好的工具。」

---

## 八、完整书单（按学习顺序）

**数学基础**（Level 1–5 对应）：
1. Blitzstein & Hwang《Introduction to Probability》（哈佛免费 PDF）
2. Wasserman《All of Statistics》（CMU 免费 PDF）
3. Strang《Introduction to Linear Algebra》+ MIT 18.06
4. Boyd & Vandenberghe《Convex Optimization》（斯坦福免费 PDF）
5. Shreve《Stochastic Calculus for Finance I & II》

**量化金融**：
1. Hull《Options, Futures, and Other Derivatives》
2. Natenberg《Option Volatility and Pricing》
3. López de Prado《Advances in Financial Machine Learning》（多重比较/回测过拟合必读）
4. Ernest Chan《Quantitative Trading》

**面试备考**：
1. Zhou《Practical Guide to Quantitative Finance Interviews》（绿皮书）
2. Crack《Heard on the Street》
3. Joshi《Quant Job Interview Questions》

---

## 九、国内机构（需要补充，目前 source 不足）

gemchanger 原文完全面向海外 HFT / 投行语境。国内顶量化私募（幻方/九坤/明汯）的招聘逻辑有差异：

**已知差异（待查验）**：
- 国内量化研究员校招更看重：因子研究能力、A股市场理解、Python 工程化能力
- 数学门槛相似（概率+统计+线代），但随机微积分在国内 CTA / 股票多头岗不是必考点（期权做市岗除外）
- 国内薪酬数据：待查（幻方/九坤 package 传言 600W+，需要可引用来源）

**待查**：
- [ ] 国内顶量化私募校招笔试公开题型（牛客网 / 量化部落）
- [ ] 国内量化研究员薪酬可信数据来源（2024–2025）
- [ ] 是否需要为国内读者单独写一个附录或分开写两篇

---

## 十、结构草案（大号图文，目标 600–700 字 + 配图）

**钩子选项**（三个，待择一）：

A. **数据冲击型**：
> "Jane Street 员工 2025 年平均年薪 $140万。他们招聘时不要求金融知识，只考数学和概率。这条路的入场券是 5 个关卡，跳关必死。"

B. **反常识型**：
> "AI 时代，机构量化 Quant 的数学要求不降反升——因为 AI 能 pip install，但不能推导出为什么你的模型在真实参数下失效。"

C. **提问型**：
> "你知道入门 Jane Street 需要多少数学吗？不是金融知识，是数学。具体是哪 5 门，每门过了才能进下一关。"

**正文结构**：
1. 钩子（薪资数据 + "5关卡不可跳级"定位）
2. 四个岗位方向表（QR/QD/QT/Risk — 找准自己的目标）
3. 5 关卡地图（每关：核心概念 + 过关验证标准，不是书单）
4. 面试闯关（流程 + 备考资源）
5. 三条反常识（AI 时代数学反而是护城河；估计误差是真敌人；工具平权信念不平权）
6. 结尾：这条路存在，但它需要的不是努力，是按顺序过关的清醒

**配图建议**（后续用 /baoyu-article-illustrator）：
- 5关卡时间轴（横轴时间，纵轴数学深度，每关标注书名+过关验证）
- 四岗位雷达图（数学/编程/金融/风险各维度）
- 薪资数据表

---

## 十一、与《真正的普通人量化路径》的对接

- 本篇结尾加一句：「如果看完这篇你觉得这条路不适合你，那篇文章才是给你的 → [[适合普通人的量化路径]]」
- 普通人篇结尾加一句：「如果你确定要走专业机构这条路，完整的 5 关卡地图在这里 → [[专业Quant学习路径]]」
- **移动文件时再改**，不在此提前动

---

## 十二、学术文献（大号强制）

| 文献 | 用途 | 状态 |
|---|---|---|
| Blitzstein & Hwang《Introduction to Probability》哈佛 | Level 1 概率论基础 | ✅ source_raw 中有引用 |
| Wasserman《All of Statistics》CMU | Level 2 统计+多重比较 | ✅ source_raw 中有引用 |
| Strang《Introduction to Linear Algebra》MIT | Level 3 线代基础 | ✅ source_raw 中有引用 |
| Boyd & Vandenberghe《Convex Optimization》Stanford | Level 4 凸优化 | ✅ source_raw 中有引用 |
| Shreve《Stochastic Calculus for Finance I & II》 | Level 5 随机微积分 | ✅ source_raw 中有引用 |
| López de Prado《Advances in Financial Machine Learning》(2018) | 多重测试、回测过拟合 | ✅ 《普通人篇》已用，可复用 |
| Hull《Options, Futures, and Other Derivatives》 | 衍生品 Greeks 解释 | 🟡 需确认版本/出版社 |
