---
account: dahao
type: image-text
status: draft
category: 量化
hook_type: 数据冲击
origin: from-topic-pool
source_topic: "[[3-Areas/Content/xhs-dahao/topic-pool/专业Quant学习路径]]"
source_notes: []
source_raw:
  - "[[How I'd Become a Quant If I Had to Start Over Tomorrow如果明天让我重新开始，我会如何成为一名量化分析师]]"
  - "[[2026年，普通人如何量化交易]]"
drives_to:
repurposed_from:
created_date: 2026-04-22
publish_date:
views: 0
followers_gained: 0
likes: 0
comments: 0
saves: 0
shares: 0
---

## 写前备忘

**定位**：深度长文，内容优先，不压缩
**发布时机**：工作日 21:00–22:30；建议《真正的普通人量化路径》发布后 5–7 天跟进
**配图建议**（后续用 /baoyu-article-illustrator 生成）：
- 封面：深色底 + 大字「进顶级量化机构的 5 关卡」+ 副标题「18个月，关卡制，不可跳级」
- 图 1：5 关卡时间轴（横轴时间，纵轴数学深度，每关标注书名 + 过关验证）
- 图 2：四岗位能力雷达图（QR / QD / QT / Risk，数学 / 编程 / 金融 / 风险维度）
- 图 3：薪资分层表（顶层 / 次顶层，按经验年限）
- 图 4：面试流程图（Resume → OA → Phone Screen → Superday）

---

## 标题候选（三个）

**A · 数据冲击型**
Jane Street 员工平均年薪 $140 万，进去需要过这 5 关数学

**B · 反常识型**
AI 时代，顶尖 Quant 的数学门槛反而更高了——完整路径和原因

**C · 提问型**
进顶级量化机构要过 5 关数学，每关的过关标准是什么？

---

## 正文

2025 年，Jane Street 员工平均年薪 **$140 万**。

这是平均值，不是顶点。顶尖交易员和 PM 的年收入在 $300 万到 $3000 万之间。

同年，金融行业 AI/ML 岗位招聘同比增长 **88%**。

更反常识的是：Jane Street 在招聘时，**不要求金融知识**。他们最近一届实习生，超过 2/3 是 CS 专业，超过 1/3 是数学专业。他们考察的不是你懂不懂市场，是你懂不懂数学。

---

这篇不是给散户的。

给的是有理工科基础、明确要进入顶级量化机构的人——Jane Street、Citadel、HRT、DE Shaw、Two Sigma。一张 **18 个月的真实地图**，附每一关的过关验证标准。

前 Jane Street 量化研究员 gemchanger 把这条路描述得非常准确：

> "The path is like layers of a video game, where you can't skip levels. Every concept builds on the last. But if you put in real work — not watching YouTube videos, actual problem-solving work — you can go from knowing nothing to being something in about 18 months."
>
> 这条路像电子游戏的关卡，不能跳级。每个概念都建立在上一个的基础上。但如果你投入真正的精力——不是看 YouTube 视频，是真正解题——你可以在 18 个月内从零开始变成那个人。

过关标准永远不是"读完这本书"。是**能写出这段代码，能推导出这个公式**。

---

### Level 1 · 概率论 ｜ 3–4 周

**教材**：Blitzstein & Hwang《Introduction to Probability》前 6 章（Harvard 免费 PDF，probabilitybook.net）

量化金融里所有的问题，最终都可以归结为一个问题：

> "What are the odds, and are the odds in my favor?"
> 赔率是多少，这个赔率对我有利吗？

这就是概率。如果你对概率没有深刻的理解，后面所有的内容都是空架子。

**条件思维**

普通人用绝对的对错思考：某件事要么发生，要么不发生。Quant 用条件句思考：在已知某些信息的情况下，这件事发生的可能性有多大？

具体的例子：一只资产每天上涨的基础概率是 60%。但在成交量高于历史均值的交易日，它上涨的概率是 75%。

那个 75% 的条件概率才是信号。孤立的 60% 只是充满噪声的背景数据。

**贝叶斯更新**

你对某个市场的判断是 50%。突然出了一条数据，经济数据比预期好 3%。通过贝叶斯公式，你精确计算出你的新判断是 58%。你以 58% 的价格参与定价。

在市场上，谁能最快、最准确地完成这种概率更新，谁就赚走大部分的钱。这是量化团队花几百万美元建低延迟系统的原因——不是因为喜欢快，是因为快 0.1 秒意味着多赚几万美元。

**期望值 × 方差**

期望值是你的信念。方差是你的风险。两者都要看，只看期望值会死。

期望每笔赚 $2，标准差 $50，本金 $200——正期望策略，但三连亏就可能爆仓出局，"长期"还没到来就已经出局了。

**凯利公式**

给定胜率和赔率，你该把多少资金押进去才能让资金增速最快、同时不破产？凯利公式给出答案。

实战规则：计算结果打半折（半凯利）。原因是胜率估计永远有误差，全凯利和全仓梭哈在参数误差下同样危险。

**过关验证**
- [ ] 能用 Python 实现贝叶斯更新器：输入先验概率 + 似然函数，输出后验概率
- [ ] 能用凯利公式算仓位，并向任何人清楚解释为什么要打半折

---

### Level 2 · 统计学 ｜ 4–5 周

**教材**：Wasserman《All of Statistics》第 1–13 章（CMU 免费 PDF）

概率是建立模型的语言。统计学是听懂数据说话的工具。

统计学教给你的第一课：

> "Most of what looks like signal is actually noisy noise."
> 大多数看起来像信号的东西，实际上是嘈杂的噪声。

**假设检验：BS 探测器**

你建了一个模型，回测显示年化 15%。这是真实的 Alpha 还是统计噪声？

步骤：设定 H₀ = "该策略预期收益为零"，计算检验统计量，得到 p 值——p 值是"如果策略真的没有 Alpha，看到这么好结果的概率"。

但这里有一个新手最容易掉进去的陷阱——

**多重比较陷阱（关键）**

如果你随机生成 1000 个策略，其中 **50 个**会纯靠运气显示 p < 0.05。你的前 10 个"盈利"策略，大概率就是那群运气好的猴子里的一批。

gemchanger 原话：

> "Every single beginner massively overestimates how much real signal they've found. Your first 10 strategies will all be noise. Accept this now and save yourself a lot of money."
> 每个新手都严重高估了自己找到的真实信号量。你最初的 10 个策略全是噪声。现在就接受这个事实，能省很多钱。

修正方法：Bonferroni 校正——测试了 N 个策略时，显著性门槛从 0.05 改为 0.05/N。或者使用 Benjamini-Hochberg 方法控制错误发现率。

**回归分解 Alpha**

线性回归 y = Xβ + ε 是金融研究的主力工具。在金融里，你把策略收益对已知风险因子做回归：

截距 α 是你的 Alpha——所有已知因子都无法解释的那部分收益。如果在控制市场、规模、价值因子之后，α 依然为零，那你的"优势"只是伪装的市场风险敞口，不是真正的 Alpha。

重要提醒：金融数据有自相关性和异方差，默认的 OLS 标准误差是错的。必须用 **Newey-West 标准误差**修正。用错误的标准误差做统计检验，就像驾驶一辆挡风玻璃有裂纹的汽车。

**最大似然估计 (MLE)**

金融里所有模型的校准手段。GARCH 拟合波动率、跳跃扩散参数估计、期权定价校准到市场报价——用的都是 MLE。

当机构里有人说"我们在校准模型"，几乎总是在说 MLE。

**过关验证**
- [ ] 用 yfinance 下载真实股票收益率 → 正态检验（结果必然失败）→ MLE 拟合 t 分布 → 对比两者
- [ ] 对一个股票组合跑 Fama-French 三因子回归，用 Newey-West 标准误差，读出截距 α 是否显著

---

### Level 3 · 线性代数 ｜ 4–6 周

**教材**：Strang《Introduction to Linear Algebra》+ MIT 18.06 全套讲座（不可跳过，非协商性要求）

线性代数是支撑一切的机器：投资组合构建、PCA、神经网络、协方差估计、因子模型。不精通矩阵，就无法成为量化分析师。

**矩阵思维**

一个协方差矩阵 Σ 描述每项资产相对于其他所有资产的运动方式。对于 500 只股票，Σ 是 500×500 的矩阵，包含 **125,250 个独立元素**。投资组合方差折叠成一个二次型表达式 w'Σw，这是 Markowitz 投资组合理论、风险管理所有内容的核心。

**特征值：才是真正重要的东西**

观察 500 只股票的宇宙，前 5 个特征向量就能解释 **70% 的总方差**。其余 495 个维度基本都是噪声。

特征值分解第一次真正用起来的时候，整个世界会改变。这也是因子投资的数学基础——你不是在做 500 个独立决策，而是在管理少数几个真正重要的维度。

**过关验证**
- [ ] 对 A 股或 S&P 500 收益率做 PCA，画出特征值谱，识别解释方差最大的前 3 个主成分
- [ ] 用 cvxpy 从零实现 Markowitz 均值-方差优化，加入做空约束和交易成本约束

---

### Level 4 · 微积分 & 凸优化 ｜ 4–5 周

**教材**：Boyd & Vandenberghe《Convex Optimization》第 1–5 章（Stanford 免费 PDF）

微积分是变化的语言。金融里一切都在变：价格、波动率、相关性，整个概率分布每秒都在位移。微积分描述并利用这些变化。

**泰勒展开**

Delta 对冲是一阶近似——你对冲了期权价格对标的价格的线性敏感度。Gamma 对冲加入了二阶修正——对冲了 Delta 本身的变化。

这里有一个关键点，为下一关铺垫：在普通微积分里，泰勒展开到二阶项 (dx)² 是无穷小量，可以丢弃。但当 x 是一个随机过程时，(dW)² = dt 是一阶项，**不能丢弃**。这正是随机微积分与普通微积分产生本质差异的地方。

**过关验证**
- [ ] 从零实现梯度下降，最小化 Rosenbrock 函数（一个经典的非凸测试函数）
- [ ] 用 cvxpy 解含交易成本约束的投资组合优化问题

---

### Level 5 · 随机微积分 ｜ 6–8 周，最难

**教材**：Shreve《Stochastic Calculus for Finance I & II》（行业黄金标准）；入门替代：Arguin《A First Course in Stochastic Calculus》

> "Before stochastic calculus, you're a data scientist who likes finance. After it, you're a quant."
> 随机微积分之前，你是个喜欢金融的数据科学家。之后，你才是量化分析师。

**布朗运动**

布朗运动（维纳过程）W_t 是连续时间的随机游走：路径连续，处处不可微，增量独立且服从正态分布。

整个随机微积分的核心洞见是：dW_t 的"大小"为 dt，因此 (dW_t)² = dt。这听起来像技术细节，但它是量化金融中最重要的单一事实。

**伊藤引理**

普通微积分：df = f'(x)dx。泰勒展开，(dx)² 是无穷小量，丢弃。

随机过程：x = W_t 时，(dW_t)² = dt 是一阶项，不能丢弃。伊藤引理因此多出一项（"伊藤修正项"），这就是随机微积分和普通微积分的根本区别。

**从 Delta 对冲到 Black-Scholes**

以下是 gemchanger 给出的从第一原理推导 Black-Scholes 的路径，建议用笔和纸跟着推一遍：

**Step 1**：设 V(S,t) 为期权价格，对 V 应用伊藤引理，展开 dV。

**Step 2**：构建 Delta 对冲组合 Π = V − (∂V/∂S)·S，计算 dΠ。Delta 对冲的关键：dW_t 项完全相消，组合变成局部无风险。

**Step 3**：无风险组合必须获得无风险利率，即 dΠ = rΠ dt。

**Step 4**：代入整理，得到 Black-Scholes 偏微分方程。

注意发生了什么：**漂移项 μ 消失了**。期权价格不依赖股票的预期收益率。风险偏好不重要。你可以假设所有人都是风险中性的来定价期权。

第一次真正看懂这个，会真的震惊。这也是为什么 Black-Scholes 在 1997 年拿到诺贝尔经济学奖的根本原因——不是公式本身，是"定价不需要知道漂移项"这个反直觉洞见。

**Greeks**

- **Delta** (Δ)：期权价格对标的价格的一阶敏感度，你的对冲比率
- **Gamma** (Γ)：Delta 变化的速度，你的凸性风险敞口
- **Theta** (Θ)：时间衰减，持有期权的成本
- **Vega** (V)：对波动率的敏感度——波动率交易台的命脉，大部分衍生品利润来自这里
- **Rho** (ρ)：对利率的敏感度

**过关验证**
- [ ] 不看书，用笔和纸手写推导 Black-Scholes PDE 的完整推导过程
- [ ] Python 实现 Black-Scholes 定价器，与蒙特卡罗模拟对比验证收敛
- [ ] 对 f(S) = ln(S)（S 服从 GBM）应用伊藤引理，推导出 −σ²/2 项

---

### 过了这 5 关，选你要进的方向

量化机构里有四类核心岗位，技能要求有实质差异：

| 岗位 | 核心职责 | 数学深度 | 编程要求 | 薪酬弹性 |
|---|---|---|---|---|
| Quant Researcher (QR) | 发现 Alpha，建预测模型，设计策略 | 最高，PhD 级数学 / ML | 生产级 Python + 科研能力 | 高且稳定 |
| Quant Developer (QD) | 交易平台、执行引擎、实时数据管道 | 中（理解 > 推导） | 生产级 C++ / Rust / Python，低延迟 | 中 |
| Quant Trader (QT) | 运营资本，管理风险，实时决策 | 中（直觉 > 推导） | 交易工具为主 | 最高，波动最大（顶尖年份 8 位数）|
| Risk Quant | VaR、压力测试、监管合规、模型验证 | 中（验证 > 创造） | Python + 统计工具 | 稳定，上限较低 |

还有一个增速最快的新方向：**AI/ML Quant**——用深度学习做信号生成，2025 年招聘增速 +88%，是增长最快的岗位。

**薪酬数据（2025 年，来源：gemchanger 原文）**

| 层级 | 机构 | 应届 Total Comp | 中期 3–7 年 | 资深 8 年+ |
|---|---|---|---|---|
| 顶层 | Jane Street / Citadel / HRT | $300K–$500K+ | $550K–$950K | $1M–$3M+ |
| 次顶 | Two Sigma / DE Shaw | $250K–$350K | $350K–$625K | $575K–$1.2M |

Jane Street 2025 年 H1 全员平均薪酬：**$1.4M/年**。这是平均值。

---

### 面试是另一套关卡

过了这 5 关数学，进入实际的招聘流程：

**标准流程**（海外顶级机构）

```
① 简历筛选
      ↓
② Online Assessment
   Zetamac 心算测试（目标 50 分以上）+ 逻辑谜题
      ↓
③ Phone Screen
   概率问题 + 博弈 / 投注问题
      ↓
④ Superday
   3–5 轮连续面试：模拟交易 + 编程 + 白板推导
```

**Jane Street 的特殊性**：他们故意设置难度高到无法独立解决的题，考察你**如何使用提示、如何在压力下协作**，而不是你能否单独答出来。

**备考资源清单**

- Zhou《Practical Guide to Quantitative Finance Interviews》（绿皮书）——200+ 真实面试题，必备
- QuantGuide.io——被称为"Quant 版 LeetCode"，专项训练概率和博弈问题
- Jane Street 每月谜题——难度高于面试，做了就是降维打击
- Jane Street Figgie 纸牌游戏——训练做市商思维的最好工具之一

**加分赛道：竞赛**

想在简历上有"公开背书"，这几个竞赛是最有价值的路径：

- **Jane Street Kaggle**（奖金 $10 万）——直接进入 Jane Street 的视野
- **WorldQuant BRAIN**（10 万+ 用户，付费购买 Alpha 信号）——做出来的 Alpha 被机构购买，相当于公开验证你的研究能力
- **Citadel Datathon**——拿奖可以快速进入面试通道

---

### AI 时代，数学反而是护城河

这是整篇文章最重要的一个反常识结论，也是 gemchanger 原文的核心论点。

现在任何人都能 pip install QuantLib、Polygon.io、PyTorch。技术工具已经完全民主化。但：

> "The math is the moat. AI can write code and suggest strategies. But the ability to derive why Itô's lemma has an extra term, to prove that discounted prices are martingales under the risk-neutral measure, to know when a convex relaxation is tight versus loose in a combinatorial market — that mathematical fluency separates quants who build edge from quants who borrow it. And borrowed edge expires."
>
> 数学是护城河。AI 能写代码、能提策略。但能推导出伊藤引理为何多出那一项、能证明在风险中性测度下贴现价格是鞅、能判断组合市场里凸松弛是紧的还是松的——这种数学流利度，才能把"构建优势"的 Quant 和"借用优势"的 Quant 区分开来。借来的优势会过期。

还有另一条同样重要的洞见：

> "Estimation error is the real enemy. Full Kelly betting, unconstrained Markowitz, ML models with too many features — they all fail for the same reason: overfitting noisy parameter estimates. The math works perfectly with true parameters. You never have true parameters. The gap between theory and practice is always estimation error, and the best quants are the ones who respect it."
>
> 估计误差才是真正的敌人。全凯利投注、无约束 Markowitz、特征过多的 ML 模型——它们都因为同一个原因失败：对含噪声的参数估计过拟合。数学在参数真实时完美运作。但你永远没有真实的参数。理论与实践之间的差距永远是估计误差，最优秀的 Quant 是那些真正尊重这一点的人。

优势不在于比别人有更好的工具。优势在于独特的数据、独特的模型、独特的执行。工具已经民主化，信念没有。

---

### 完整书单（按学习顺序）

**数学基础（18 个月主线）**

| 优先级 | 书目 | 对应关卡 | 获取方式 |
|---|---|---|---|
| ★★★★★ | Blitzstein & Hwang《Introduction to Probability》| Level 1 | 哈佛免费 PDF |
| ★★★★★ | Wasserman《All of Statistics》| Level 2 | CMU 免费 PDF |
| ★★★★★ | Strang《Introduction to Linear Algebra》+ MIT 18.06 | Level 3 | 免费讲座 |
| ★★★★☆ | Boyd & Vandenberghe《Convex Optimization》| Level 4 | Stanford 免费 PDF |
| ★★★★★ | Shreve《Stochastic Calculus for Finance I & II》| Level 5 | 购买 |

**量化金融**

| 优先级 | 书目 | 用途 |
|---|---|---|
| ★★★★★ | Hull《Options, Futures, and Other Derivatives》| 衍生品全貌，Greeks 深度理解 |
| ★★★★☆ | Natenberg《Option Volatility and Pricing》| 期权波动率交易实战 |
| ★★★★★ | López de Prado《Advances in Financial Machine Learning》| 多重测试、回测过拟合的最深入分析 |
| ★★★★☆ | Ernest Chan《Quantitative Trading》| 散户向量化入门，理解策略构建基础 |
| ★★★☆☆ | Zuckerman《The Man Who Solved the Market》| 文艺复兴传奇，了解行业天花板 |

**面试备考**

| 优先级 | 书目 | 说明 |
|---|---|---|
| ★★★★★ | Zhou《Practical Guide to Quantitative Finance Interviews》| 绿皮书，必备 |
| ★★★★☆ | Crack《Heard on the Street》| 经典面试题集 |
| ★★★☆☆ | Joshi《Quant Job Interview Questions》| 补充题库 |

---

### 国内机构版本（幻方 / 九坤 / 明汯）

以上路径是海外 HFT 和顶级投行的标准框架。

国内顶量化私募的校招逻辑和考察重点与海外有差异——数学深度、侧重方向、A 股特有的市场结构理解，都不完全一样。

---

## 引用

- gemchanger (@gemchange_ltd). *How I'd Become a Quant If I Had to Start Over Tomorrow*. X Platform, 2026-03-04.
- Mr.RC (@MrRyanChi). *2026年，普通人如何量化交易*. X Platform, 2026-04-01.
- Blitzstein, J. & Hwang, J. *Introduction to Probability*. Harvard University. probabilitybook.net.
- Wasserman, L. *All of Statistics: A Concise Course in Statistical Inference*. Springer, 2004.
- Strang, G. *Introduction to Linear Algebra*, 5th ed. Wellesley-Cambridge Press, 2016. + MIT 18.06 OCW.
- Boyd, S. & Vandenberghe, L. *Convex Optimization*. Cambridge University Press, 2004.（
- Shreve, S. *Stochastic Calculus for Finance I & II*. Springer, 2004.
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed. Pearson, 2021.
- López de Prado, M. *Advances in Financial Machine Learning*. Wiley, 2018.
