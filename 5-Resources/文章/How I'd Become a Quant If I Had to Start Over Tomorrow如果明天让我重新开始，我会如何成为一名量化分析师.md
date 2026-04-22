---
title: "How I'd Become a Quant If I Had to Start Over Tomorrow如果明天让我重新开始，我会如何成为一名量化分析师"
source: "https://x.com/gemchange_ltd/article/2028904166895112617"
author:
  - "[[gemchanger (@gemchange_ltd)]]"
published: 2026-03-04
created: 2026-04-02
updated: 2026-04-21
area: Investing/Quant
status: done
description: "成为专业 Quant 的完整学习路径（18 个月：概率 → 统计 → 线代 → 微积分 → 随机微积分 → Black-Scholes）。目标受众是 Jane Street / Citadel 级投行量化岗，非普通散户。作为「专业量化 vs 普通人量化」对照的反参考素材，引用于 `3-Areas/Content/xhs-xiaohao/drafts/普通人如何入门量化.md` 和 `3-Areas/Content/xhs-dahao/topic-pool/真正的普通人量化路径.md`。"
tags:
  - "quant"
  - "trading"
  - "reference"
  - "career-path"
---
In 2025, entry-level quants at top firms pulled $300K-$500K total comp.到 2025 年，顶尖公司入门级量化分析师的总薪酬将达到 30 万至 50 万美元。

AI/ML hiring in finance grew 88% year-over-year.金融行业人工智能/机器学习领域的招聘人数同比增长了 88%。

This article is everything I wish someone had handed me when i started my path laid out in the exact order you should learn it.这篇文章包含了当初我入门时希望有人能给我的所有内容，而且学习顺序也完全正确。

The path is like layers of a video game, where you can't skip levels.这条路径就像电子游戏中的关卡一样，你不能跳过任何关卡。

Every concept builds on the last. But if you put in real work, not watching some lame ahh YouTube videos about finance, that's just wasting your time, actual problem-solving work - you can go from knowing nothing to being something in about 18 months. **Disclaimer: Not Financial Advice & Do Your Own Research & Markets involve risk. My own project -** [@coldvisionXYZ](https://x.com/@coldvisionXYZ)每个概念都建立在前一个概念的基础上。但如果你投入真正的精力，而不是去看那些无聊的 YouTube 金融视频（那纯粹是浪费时间），而是真正去解决问题——你可以在大约 18 个月内从一无所知变成有所成就。 **免责声明：** 非财务建议，请自行研究，市场存在风险。 我自己的项目—— [@coldvisionXYZ](https://x.com/@coldvisionXYZ)

## Forget everything you think you know about trading忘记你自以为了解的所有交易知识。

Most people think quantitative trading is about picking stocks. Having opinions on Tesla. Predicting earnings.大多数人认为量化交易就是挑选股票，对特斯拉发表看法，预测盈利。

Quant trading is about math.量化交易本质上是数学。

You are mostly working with statistical relationships, pricing inefficiencies, and structural edges that exist because markets are complex systems run by humans who make systematic errors.你主要处理的是统计关系、定价效率低下以及结构性优势，这些都是因为市场是由人类运行的复杂系统而存在的，而人类会犯系统性错误。

## Part I: Probability is the Language of Uncertainty第一部分 ：概率是不确定性的语言

Everything in quantitative finance reduces kinda to 1 question:量化金融领域的一切都可以归结为一个问题：

What are the odds, and are the odds in my favor?胜算有多大？胜算在我这边吗？

That's probability. If you don't understand probability at a deep level, nothing else in this article matters.这就是概率。如果你对概率没有深刻的理解，这篇文章的其他内容就毫无意义。

**Conditional thinking条件思维**

Most people think in absolutes. Something is true or it isn't. Quants think in conditionals. Given what I know, how likely is this?大多数人的思维方式是绝对的。某件事要么是真的，要么就不是。 量化分析师用条件句思考问题。根据我已知的信息，这件事发生的可能性有多大？

![图像](https://pbs.twimg.com/media/HCei_w7XcAAjMwU?format=png&name=large)

The probability of A given B equals the probability of both happening divided by the probability of B. Profound implications.在已知事件 B 的条件下，事件 A 发生的概率等于事件 A 和事件 B 同时发生的概率除以事件 B 发生的概率。这其中蕴含着深刻的意义。

A stock goes up 60% of days - that's the base rate. But on days when volume is above average, it goes up 75% of the time.股票上涨的概率为60%——这是基本概率。但在成交量高于平均水平的日子里，上涨的概率会达到75%。

That conditional probability is a NOT BS. The raw 60% is NOISY BS.那个条件概率绝对不是胡扯。原始的60%概率是胡扯，而且误差很大。

**Bayes' theorem贝叶斯定理**

![图像](https://pbs.twimg.com/media/HCejMkSbgAAeuXv?format=png&name=large)

Your updated belief equals你更新后的信念等于

(how likely you'd see this data if your hypothesis were true) \* (your prior belief) / (the total probability of seeing this data under any hypothesis).（如果你的假设成立，你看到这些数据的可能性有多大）\*（你的先验信念）/（在任何假设下看到这些数据的总概率）。

The denominator sums over all hypotheses.分母是对所有假设求和。

In practice, you compute this with Monte Carlo sampling.实际上，您可以使用蒙特卡罗抽样来计算此值。

But the logic is the same. Bayes is how you update your conviction in real time.但逻辑是一样的。贝叶斯方法就是让你实时更新你的判断。

A model says a stock should be worth $50. Earnings come out, revenue is 3% above estimate. The Bayesian posterior shifts upward. The traders who update fastest and most accurately win bread.模型预测某股票价值 50 美元。财报发布，营收超出预期 3%。贝叶斯后验概率向上移动。更新速度最快、准确率最高的交易员最终获利。

**Expected value and variance your two best friends期望值和方差是你的两个好朋友**

![图像](https://pbs.twimg.com/media/HCejtL7XsAA5vQ7?format=png&name=large)

![图像](https://pbs.twimg.com/media/HCejv0UXIAACqgx?format=png&name=large)

Expected value is your conviction. Variance is your risk.预期价值就是你的信念。 波动就是风险。

If your strategy has positive expected value and you can survive the variance, you likely will make money.如果你的策略具有正的预期价值，并且你能承受波动，那么你很可能会赚钱。

**Level 1 homework (3-4 weeks at 2 hours/day):** 1\. Read Blitzstein & Hwang, Introduction to Probability (free PDF from Harvard). Every problem in Chapters 1-6. 2. Code Simulate 10,000 coin flips, verify the law of large numbers visually. 3. Code 2 Implement a Bayesian updater takes a prior and likelihood, returns a posterior.一级作业（3-4周，每天2小时）： 1. 阅读 Blitzstein & Hwang， 《概率论导论》 （哈佛大学免费 PDF 版）。第 1-6 章所有习题。 2. 代码 模拟 10,000 次抛硬币，用直观的方式验证大数定律。 3. 代码 2 实现一个贝叶斯更新器，接受先验分布和似然分布，并返回后验分布。

```python
import numpy as np
import matplotlib.pyplot as plt

# Law of large numbers: running average converges to true probability
np.random.seed(42)
flips = np.random.choice([0, 1], size=10000, p=[0.5, 0.5])
running_avg = np.cumsum(flips) / np.arange(1, 10001)

plt.figure(figsize=(10, 4))
plt.plot(running_avg, linewidth=0.7)
plt.axhline(y=0.5, color='r', linestyle='--', label='True probability')
plt.xlabel('Number of flips')
plt.ylabel('Running average')
plt.title('Law of Large Numbers in Action')
plt.legend()
plt.savefig('lln.png', dpi=150)
print(f"After 10,000 flips: {running_avg[-1]:.4f} (true: 0.5000)")
```

## Part II: Statistics第二部分 ：统计学

Once you speak probability, you need to learn to listen to data. 一旦你开始谈论概率，你就需要学会倾听数据。

![图像](https://pbs.twimg.com/media/HCgQBaXXYAEaXBx?format=png&name=large)

That's statistics and the #1 lesson statistics teaches is "most of what looks like NOT A BS is actually NOISY BS"这就是统计学，而统计学教导我们的第一课就是“大多数看起来不像胡说八道的东西，实际上都是嘈杂的胡说八道”。

Hypothesis testing is the BS detector假设检验是 BS 检测器。

You build a model. It backtests at 15% annual return. Is it real?你建立了一个模型。回测结果显示年化收益率为15%。这真实吗？

Set up H\_0: "this strategy has zero expected return." Compute a test statistic. Calculate a p-value - the probability of seeing results this good if H\_0 were true.设定 H\_0：“该策略的预期收益为零。” 计算检验统计量。 计算 p 值——如果 H\_0 为真，则看到如此好结果的概率。

BUT If you test 1,000 random strategies, 50 of them will show p-values below 0.05 purely by chance.但是，如果你测试 1000 个随机策略，其中 50 个策略的 p 值会纯属偶然地低于 0.05。

That's the multiple comparisons problem. Ur fix is Bonferroni correction divide your significance threshold by the number of tests Or use Benjamini-Hochberg for false discovery rate control.这就是多重​​比较问题。 你的解决方法是使用 Bonferroni 校正，将显著性阈值除以检验次数。 或者使用 Benjamini-Hochberg 方法控制错误发现率。

Every single beginner massively overestimates how much NOT A BS they've found. Your first 10 strategies will all be NOISY BS. Accept this now and save yourself a lot of money.每个新手都会严重高估自己找到的真正有用的信息数量。你最初的十个策略可能全是些华而不实的废话。现在就接受这个事实，可以帮你省下很多钱。

**Regression decomposing returns回归分解收益率**

Linear regression y=Xβ+ϵ is the workhorse. In finance, you regress your strategy's returns against known risk factors:线性回归 y=Xβ+ϵ 是主要方法。 在金融领域，你需要对策略收益与已知的风险因素进行回归分析：

![图像](https://pbs.twimg.com/media/HCgDDAkaEAEvrzK?format=png&name=large)

The intercept α is your **alpha** the return that can't be explained by known factors. If α is zero after accounting for factors, your "edge" is just disguised market exposure.截距 α 就是你的 alpha 值。 无法用已知因素解释的回报。如果考虑所有因素后α仍为零，那么你的“优势”只不过是伪装的市场风险敞口。

The OLS estimator:普通最小二乘法估计量：

![图像](https://pbs.twimg.com/media/HCgDMxxXIAA4zDW?format=png&name=large)

The most important number is α. Use **Newey-West standard errors** financial data has autocorrelation and heteroskedasticity, so default OLS standard errors are wrong. Using them is like driving with a cracked windshield.最重要的数字是α。 由于金融数据存在自相关性和异方差性，因此使用 **Newey-West 标准误差**是不准确的。使用默认的 OLS 标准误差就像驾驶挡风玻璃有裂纹的汽车一样危险。

**Maximum Likelihood Estimation最大似然估计**

Given data x\_1,…,x\_n,​ from a model with parameter θ:给定来自参数为θ的模型的数据 x\_1,…,x\_n,​：

![图像](https://pbs.twimg.com/media/HCgQ6rLXUAAaw9F?format=png&name=large)

Set the derivative to zero and solve. (or it's over gng)令导数为零并求解。（或者它是在 gng 上求解）

MLE is how you calibrate every model in finance fit a GARCH model to volatility, estimate jump-diffusion parameters, calibrate option pricing to market quotes.MLE 是校准金融中每个模型的方法，例如将 GARCH 模型拟合到波动率、估计跳跃扩散参数、将期权定价校准到市场报价。

It's asymptotically efficient no other consistent estimator has lower variance for large samples (the Cramér-Rao lower bound).它渐近有效，没有其他一致估计量在大样本情况下具有更低的方差（克拉默-拉奥下界）。

When someone at a firm says they're "calibrating" a model, they almost, like always mean MLE.当公司里有人说他们在“校准”模型时，他们几乎总是指最大似然估计（MLE）。

**Level 2 homework (4-5 weeks):** 1\. Read Wasserman, All of Statistics, Chapters 1-13. 2. Code Download real stock returns with yfinance. Test normality (they'll fail). Fit a t-distribution via MLE. Compare. 3. Code Run a Fama-French 3-factor regression on a stock portfolio using statsmodels. 4. Code Implement a permutation test shuffle dates 10,000 times, compare shuffled performance to actual.第二阶段作业（4-5周）： 1. 阅读 Wasserman， 《统计学大全》 ，第 1-13 章。 2. 代码 使用 yfinance 下载真实股票收益率数据。检验正态性（结果会不成立）。使用最大似然估计法拟合 t 分布。进行比较。 3. 代码 使用 statsmodels 对股票投资组合运行 Fama-French 三因子回归。 4. 代码 进行置换测试，将日期打乱 10,000 次，比较打乱后的性能与实际性能。

```python
import numpy as np
from scipy import optimize, stats

# Demonstrate fat tails: MLE fit of Student-t to return data
np.random.seed(42)

# Simulate "realistic" returns (fat tails, slight positive drift)
true_df = 4
returns = stats.t.rvs(df=true_df, loc=0.0005, scale=0.015, size=1000)

def neg_log_likelihood(params, data):
    df, loc, scale = params
    if df <= 2 or scale <= 0:
        return 1e10
    return -np.sum(stats.t.logpdf(data, df=df, loc=loc, scale=scale))

result = optimize.minimize(
    neg_log_likelihood, x0=[5, 0, 0.01], args=(returns,),
    method='Nelder-Mead'
)
fitted_df, fitted_loc, fitted_scale = result.x

print(f"MLE degrees of freedom: {fitted_df:.2f} (true: {true_df})")
print(f"MLE location:           {fitted_loc:.6f}")
print(f"MLE scale:              {fitted_scale:.6f}")

# Normality test
_, p_normal = stats.normaltest(returns)
print(f"\nNormality test p-value: {p_normal:.2e}")
print(f"Reject normality? {'YES  fat tails confirmed' if p_normal < 0.05 else 'NO'}")
```

## Part III: Linear Algebra第三部分 ：线性代数

Linear algebra sounds boring. It's the machinery that runs everything: portfolio construction, PCA, neural networks, covariance estimation, factor models. You cannot be a quant without being fluent in matrices.线性代数听起来很枯燥，但它却是支撑一切的基础：投资组合构建、主成分分析、神经网络、协方差估计、因子模型等等。如果你不精通矩阵，就无法成为一名合格的量化分析师。

![图像](https://pbs.twimg.com/media/HCgSDNfawAUriXT?format=jpg&name=large)

(if u skipped Algebra in school school doing that, it's over)（如果你在学校因为这样做而跳过了代数课，那就完了）

**Thinking in matrices矩阵思维**

A covariance matrix Σ captures how every asset moves relative to every other asset. For 500 stocks, Σ is 500×500 with 125,250 unique entries. Portfolio variance collapses to a single expression协方差矩阵 Σ 描述了每项资产相对于其他所有资产的变动情况。对于 500 只股票，Σ 为 500×500，包含 125,250 个唯一元素。投资组合的方差可以简化为一个单一表达式。

![图像](https://pbs.twimg.com/media/HCgEBHmWkAIWTsh?format=png&name=large)

This quadratic form is the core of Markowitz portfolio theory, of risk management, of everything.这种二次方程形式是马科维茨投资组合理论、风险管理以及一切事物的核心。

**Eigenvalues is what actually matters in a universe of stocks在股票市场中，真正重要的是特征值。**

Look at a 500-stock universe and the first 5 eigenvectors explain 70% of all variance. Everything else is NOISY BS.观察一个包含500只股票的股票池，前5个特征向量就能解释70%的方差。其余的都是无意义的噪声。

The first time eigendecomposition u use it the whole world changes. Look at a 500-stock universe and the first 5 eigenvectors explain 70% of all variance. Dimensionality reduction, and it's the foundation of factor investing.当你第一次使用特征值分解时，整个世界都会改变。以一个包含500只股票的股票池为例，前5个特征向量就能解释70%的方差。这就是降维，也是因子投资的基础。

**Level 3 homework (4-6 weeks):** 1\. Watch Gilbert Strang's MIT 18.06 lectures all of them. Non-negotiable. 2. Read Strang, Introduction to Linear Algebra. Do the problems. 3. Code PCA decomposition of S&P 500 returns. Plot eigenvalue spectrum. Identify top 3 components. 4. Code Markowitz mean-variance optimization from scratch.三年级作业（4-6周）： 1. 观看 吉尔伯特·斯特朗在麻省理工学院18.06学期的讲座涵盖了所有这些内容。没有商量的余地。 2. 阅读 斯特朗， 《线性代数导论》 。做题。 3. 代码 对标普 500 指数收益率进行主成分分析（PCA）。绘制特征值谱。找出前三个主成分。 4. 代码 从零开始实现马科维茨均值-方差优化。

```python
import numpy as np
import cvxpy as cp

# ============================================
# Markowitz optimization with cvxpy
# ============================================
np.random.seed(42)
n_assets = 10
mu = np.random.uniform(0.04, 0.15, n_assets)
A = np.random.randn(n_assets, n_assets) * 0.1
cov = A @ A.T + np.eye(n_assets) * 0.01

w = cp.Variable(n_assets)
objective = cp.Minimize(cp.quad_form(w, cov))
constraints = [
    mu @ w >= 0.08,      # minimum return
    cp.sum(w) == 1,       # fully invested
    w >= -0.1,            # max 10% short
    w <= 0.3              # max 30% long
]

prob = cp.Problem(objective, constraints)
prob.solve()

ret = mu @ w.value
vol = np.sqrt(w.value @ cov @ w.value)
sharpe = (ret - 0.03) / vol

print(f"Portfolio return:  {ret:.4f}")
print(f"Portfolio vol:     {vol:.4f}")
print(f"Sharpe ratio:      {sharpe:.4f}")
print(f"Weights: {np.round(w.value, 4)}")
```

## Part IV: Calculus & Optimization第四部分 ：微积分与优化

Calculus is the language of change. In finance, everything changes: prices, volatilities, correlations, the entire probability distribution shifts second by second. Calculus describes and exploits those changes.微积分是变化的语言。在金融领域，一切都在变化：价格、波动性、相关性，整个概率分布每时每刻都在变化。微积分描述并利用了这些变化。

**Derivatives** (the math kind): appears in every neural network backpropagation and every Greek calculation.**导数** （数学上的导数）：出现在每个神经网络反向传播和每个希腊字母计算中。

**Taylor expansion**:**泰勒展开式** ：

![图像](https://pbs.twimg.com/media/HCgE6k4boAA07fr?format=png&name=large)

Delta hedging is the first-order approximation. Gamma hedging adds the second-order correction. And the reason Itô calculus differs from ordinary calculus is precisely because the second-order Taylor term doesn't vanish for random processes. **Just** **Remember it**Delta 对冲是初步近似。 Gamma 对冲增加了二阶修正。 伊藤微积分与普通微积分的不同之处恰恰在于，对于随机过程，二阶泰勒项并不**为零** 。 **记住它**

**Level 4 homework (4-5 weeks):** 1\. Read Boyd & Vandenberghe, Convex Optimization (free PDF from Stanford), Chapters 1-5. 2. Code Implement gradient descent from scratch. Minimize the Rosenbrock function. 3. Code Solve a portfolio optimization problem with cvxpy including transaction cost constraints.4级作业（4-5周）： 1. 阅读 Boyd & Vandenberghe， 《凸优化》 （斯坦福大学免费 PDF），第 1-5 章。 2. 代码 从头开始实现梯度下降法。最小化 Rosenbrock 函数。 3. 代码 使用 cvxpy 解决包含交易成本约束的投资组合优化问题。

## Part V: Stochastic Calculus第五部分 ：随机微积分

Before stochastic calculus, you're a data scientist who likes finance.在学习随机微积分之前，你是一位喜欢金融的数据科学家。

After it, you're a quant. QUANTATIVE FINANCE EXPERT, you heard? 之后，你就是个量化分析师了。量化金融专家，你听说过吗？

![图像](https://pbs.twimg.com/media/HCgU9xXW8AAmAc_?format=png&name=large)

that's you那就是你。

This is where you learn to model randomness in continuous time, derive the Black-Scholes equation from first principles, and understand why the trillion-dollar derivatives market works the way it does.在这里，你将学习如何在连续时间中对随机性进行建模，从第一性原理推导出布莱克-斯科尔斯方程，并了解万亿美元的衍生品市场为何以这种方式运作。

**Brownian motion pure randomness, formalized布朗运动是纯粹的随机性，已形式化。**

A Brownian motion (Wiener process) W\_t is a continuous-time random walk:布朗运动（维纳过程）W\_t 是一个连续时间随机游走：

- W\_0 = 0
- Increments W\_t - W\_s ~ N(0, t - s) for t > s对于 t > s，W\_t - W\_s ~ N(0, t - s) 递增
- Non-overlapping increments are independent非重叠增量是独立的
- Paths are continuous but nowhere differentiable路径是连续的，但处处不可微

The critical insight that everything else depends on: dW\_t has "size" dt, which means (dW\_t)^2 = dt. This sounds like a technicality, but its the single most important fact in quantitative finance.所有其他结论都依赖于一个关键洞见：dW\_t 的“大小”为 dt，这意味着 (dW\_t)^2 = dt。这听起来像是一个技术细节，但它却是量化金融中最重要的事实。

**Geometric Brownian Motion** models stock prices:**几何布朗运动**模型股票价格：

![图像](https://pbs.twimg.com/media/HCgHgzZWIAAmud7?format=png&name=large)

**Itô's lemma伊藤引理**

In normal calculus, df = f'(x)dx. You Taylor-expand, and the (dx)^2 term is infinitesimally small you drop it.在普通微积分中，df = f'(x)dx。进行泰勒展开，(dx)^2 项非常小，可以忽略不计。

But when x is a stochastic process, (dW\_t)^2 = dt is first order. You can't drop it.但是当 x 是一个随机过程时，(dW\_t)^2 = dt 是一阶项 ，不能省略。

**Itô's lemma**:**伊藤引理** ：

![图像](https://pbs.twimg.com/media/HCgHxPzawAE8TWR?format=png&name=large)

Apply it to an option price and you get Black-Scholes. Formula is the engine behind the entire derivatives industry.将其应用于期权价格，即可得到布莱克-斯科尔斯模型。该模型是整个衍生品行业的引擎。

**Deriving Black-Scholes from scratch从零开始推导布莱克-斯科尔斯模型**

Follow along with pen and paper.请用笔和纸边做边记。

**Step 1**: Let V(S,t) be an option price. Apply Itô's lemma:**步骤 1** ：设 V(S,t) 为期权价格。应用伊藤引理：

![图像](https://pbs.twimg.com/media/HCgH4u8W8AAi9NX?format=png&name=large)

**Step 2**: Construct a delta-hedged portfolio Π=V−∂S/∂V​⋅S. Compute dΠ:**步骤 2** ：构建 delta 对冲投资组合 Π=V−∂S/∂V​⋅S。计算 dΠ：

![图像](https://pbs.twimg.com/media/HCgIDXgXoAA_PP_?format=png&name=large)

The dW\_t​ terms cancel perfectly. The portfolio is locally riskless.dW\_t 项完全抵消。该投资组合局部无风险。

**Step 3**: A riskless portfolio must earn the risk-free rate: dΠ=rΠ dtd\\Pi = r\\Pi \\, dt dΠ=rΠdt.**步骤 3** ：无风险投资组合必须获得无风险利率：dΠ=rΠ dtd\\Pi = r\\Pi \\, dt dΠ=rΠdt。

**Step 4**: Substitute and rearrange:**步骤 4** ：替换和重新排列：

![图像](https://pbs.twimg.com/media/HCgIfdGWYAEfPl8?format=png&name=large)

This is the **Black-Scholes PDE**.这是**布莱克-斯科尔斯偏微分方程** 。

Notice what happened - the drift μ vanished. The option price doesn't depend on the expected return of the stock. Risk preferences don't matter. You can price options as if everyone is risk-neutral. The first time this sinks in genuinely mind-bending.注意发生了什么——漂移系数μ消失了。期权价格不再取决于股票的预期收益。风险偏好无关紧要。你可以假设每个人都是风险中性者来定价期权。第一次理解这一点时，确实令人震惊。

Solving this PDE for a European call with strike K and expiry T gives:求解行权价为 K、到期日为 T 的欧式看涨期权的偏微分方程，得到：

![图像](https://pbs.twimg.com/media/HCgIq17boAAZdI7?format=png&name=large)

![图像](https://pbs.twimg.com/media/HCgIyuuawAAEWtg?format=png&name=large)

where d\_1=其中 d\_1=

![图像](https://pbs.twimg.com/media/HCgI4E5WoAAzATN?format=png&name=large)

d\_2 =

The Greeks希腊人

- **Delta** Δ is How much the option moves per $1 stock move. Your hedge ratio.**Delta** Δ 表示股票价格每变动 1 美元，期权价格变动的幅度。它是你的对冲比率。
- **Gamma** Γ​: How fast delta changes. Your convexity exposure.**Gamma** Γ：delta 变化的速度。你的凸性暴露程度。
- **Theta** Θ: Time decay. Typically negative for long options.**Theta** Θ：时间衰减。对于多头期权，通常为负值。
- **Vega** V: Sensitivity to volatility. Where most derivatives money is made.**Vega** V：对波动性的敏感度。衍生品交易中最赚钱的部分就在这里。
- **Rho** ρ: Sensitivity to interest rates.**Rho** ρ：对利率的敏感度。

Delta tells you your hedge ratio. Gamma tells you how often to re-hedge. Theta is the cost of holding. Vega is the bread and butter of vol trading desks.Delta 值告诉你对冲比率。Gamma 值告诉你多久需要重新对冲一次。Theta 值是持有成本。Vega 值是波动率交易部门的命脉。

**Level 5 homework (6-8 weeks - the hardest level):** 1\. Read Shreve, Stochastic Calculus for Finance II. The gold standard. 2. Alternative Arguin, A First Course in Stochastic Calculus (newer, more accessible). 3. Derive Apply Itô's lemma to f(S)=ln⁡(S) where S follows GBM. Get the −σ^2/2. 4. Derive The full Black-Scholes equation from the delta-hedging argument. 5. Code Black-Scholes from scratch. Compare to Monte Carlo. Verify convergence.5级作业（6-8周 - 最难的级别）： 1. 阅读 Shreve， 《金融随机微积分 II》 。黄金标准。 2. 替代方案 Arguin， 《随机微积分入门教程》 （较新、更易于理解）。 3. 推导 将伊藤引理应用于 f(S)=ln⁡(S)，其中 S 服从 GBM 分布。得到 −σ^2/2。 4. 推导 从 delta 对冲论证出发，得到完整的 Black-Scholes 方程。 5. 代码 从头开始构建 Black-Scholes 方程。与蒙特卡罗模拟结果进行比较。验证收敛性。

```python
import numpy as np
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    if option_type == 'call':
        return S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    else:
        return K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)

def monte_carlo_option(S0, K, T, r, sigma, n_sims=500_000):
    """Price via risk-neutral simulation (drift = r, not mu)"""
    Z = np.random.standard_normal(n_sims)
    ST = S0 * np.exp((r - sigma**2/2)*T + sigma*np.sqrt(T)*Z)
    payoffs = np.maximum(ST - K, 0)
    price = np.exp(-r*T) * np.mean(payoffs)
    stderr = np.exp(-r*T) * np.std(payoffs) / np.sqrt(n_sims)
    return price, stderr

def greeks(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return {
        'delta': norm.cdf(d1),
        'gamma': norm.pdf(d1) / (S * sigma * np.sqrt(T)),
        'theta': -(S*norm.pdf(d1)*sigma)/(2*np.sqrt(T)) - r*K*np.exp(-r*T)*norm.cdf(d2),
        'vega':  S * np.sqrt(T) * norm.pdf(d1),
        'rho':   K * T * np.exp(-r*T) * norm.cdf(d2),
    }

# Verify: Monte Carlo converges to Black-Scholes
S, K, T, r, sigma = 100, 105, 1.0, 0.05, 0.2

bs = black_scholes(S, K, T, r, sigma)
mc, err = monte_carlo_option(S, K, T, r, sigma)
g = greeks(S, K, T, r, sigma)

print(f"Black-Scholes: ${bs:.4f}")
print(f"Monte Carlo:   ${mc:.4f} ± {err:.4f}")
print(f"Difference:    ${abs(bs - mc):.4f}\n")
for name, val in g.items():
    print(f"  {name:>6}: {val:.6f}")
```

## Polymarket宝利市场

This is the most interesting market in the world right now and the math behind it connects everything in this article: probability, information theory, convex optimization, integer programming这是目前世界上最有趣的市场，而其背后的数学原理贯穿本文的所有内容：概率论、信息论、凸优化、整数规划

**How LMSR prices beliefsLMSR 如何为信念定价**

The **Logarithmic Market Scoring Rule (LMSR)**, invented by Robin Hanson, powers automated prediction markets. The cost function for n outcomes:由 Robin Hanson 发明的**对数市场评分规则 (LMSR)** 为自动化预测市场提供了动力。n 个结果的成本函数如下：

![图像](https://pbs.twimg.com/media/HCgK1C4X0AAdWZK?format=png&name=large)

where q\_i​ tracks outstanding shares of outcome i and b is the liquidity parameter. The price of outcome i:其中 q\_i 表示结果 i 的流通股数量，b 为流动性参数。结果 i 的价格：

![图像](https://pbs.twimg.com/media/HCgK60sXYAEqP3I?format=png&name=large)

That's the **softmax function** - function powering every neural network classifier.这就是 **softmax 函数** ——每个神经网络分类器的核心函数。

Prices always sum to 1, always lie in (0,1), and always exist providing infinite liquidity. The market maker's maximum loss is bounded at b \* ln(n)价格之和始终为 1，始终位于 (0,1) 区间，且始终存在，流动性无限。做市商的最大损失上限为 b \* ln(n)。

## The Quant Career Landscape量化分析师职业发展前景

**4 archetypes:** **Quant Researcher** The most-cracked guy who finds patterns in petabytes, builds predictive models, designs strategies. Needs PhD-level math/stats/ML, or exceptional undergraduate achievement. At firms like Jane Street, QRs work with tens of thousands of GPUs.**4 种原型：** 量化研究员 最厉害的数据分析专家，能从 PB 级数据中发现规律，构建预测模型，制定策略。需要拥有数学/统计学/机器学习博士水平，或者本科阶段的优异成绩。在像 Jane Street 这样的公司，QR（量子计算专家）要操作数万个 GPU。

**Quant Developer/Engineer** The mid-cracked guy, mostly the builder. Trading platforms, execution engines, real-time data pipelines. Makes the researcher's model actually trade. Needs production C++/Rust/Python, low-latency systems.量化开发人员/工程师 这位中层人员，主要负责搭建平台。他负责交易平台、执行引擎和实时数据管道的开发，让研究人员的模型能够真正投入交易。他需要生产环境的 C++/Rust/Python 代码，以及低延迟的系统。

**Quant Trader** Either the biggest degen or the most-cracked guy, mostly the decision-maker. Runs capital, manages risk, makes real-time calls. Highest compensation variance - eight figures in exceptional years.量化交易员 要么是最大的赌徒，要么是最疯癫的人，通常是决策者。负责资金运作、风险管理，并能实时做出决策。薪酬波动幅度最大——在业绩极佳的年份可达八位数。

**Risk Quant** The most-cracked guy or just insanely experienced corporate guy, mostly the guardian. Model validation, VaR, stress testing, regulatory compliance. Steadier career, lower ceiling. The emerging AI/ML Quant role signal generation with deep learning is the fastest-growing, with hiring up 88% year-over-year in 2025.风险量化 最厉害的分析师，或者经验极其丰富的企业高管，通常是负责模型验证、风险价值 (VaR)、压力测试和监管合规的专家。职业发展较为稳定，但上限较低。新兴的人工智能/机器学习量化分析师角色，即利用深度学习进行信号生成，增长最为迅速，预计到 2025 年，招聘人数将同比增长 88%。

**What it pays:薪酬待遇：**

**Level Top Tier (Jane Street, Citadel, HRT)** New grad $300K-$500K+ total comp Mid career (3-7yr)$550K-$950K Senior (8+yr)$1M-$3M+ Star trader/PM $3M-$30M+ **Mid Tier (Two Sigma, DE Shaw)** New grad $250K–$350K Mid career (3-7yr) $350K–$625K Senior (8+yr) $575K–$1.2M Star trader/PM idk**顶级级别（简街、城堡、HRT）** 应届毕业生总收入 30 万至 50 万美元以上 职业生涯中期（3-7年经验）年薪55万至95万美元 资深员工（8年以上经验）年薪100万至300万美元以上 明星交易员/PM，交易额 300 万至 3000 万美元以上 中端（Two Sigma、DE Shaw） 应届毕业生年薪 25 万至 35 万美元 职业生涯中期（3-7年）年薪35万至62.5万美元 资深员工（8年以上经验）年薪57.5万美元至120万美元 星际贸易员/PM 不知道

Jane Street's average employee compensation was reported at $1.4 million/year in H1 2025. That's the average though据报道，Jane Street 2025 年上半年的员工平均薪酬为每年 140 万美元。但这只是平均值。

**The interview gauntlet面试的艰辛**

**Resume screen** -> **Online assessment** (mental math via Zetamac - target 50+, logic puzzles) -> **Phone screen** (probability problems, betting games) -> **Superday** (3-5 back-to-back interviews, mock trading, coding, whiteboard derivations).**恢复屏幕** \-> **在线评估** （通过 Zetamac 进行心算测试 - 目标 50 分以上，逻辑谜题）-> **手机屏幕** （概率问题、博彩游戏）-> **超级日** （3-5 场连续面试、模拟交易、编程、白板推导）。

Jane Street gives problems intentionally too hard to solve alone - they test how you use hints and collaborate.Jane Street 故意设置一些难度过高的问题，让玩家无法独自解决——他们旨在测试玩家如何利用提示以及如何与他人合作。

Over two-thirds of their recent intern class studied CS; over a third studied math. Finance knowledge generally not required.他们最近一批实习生中，超过三分之二是计算机科学专业的；超过三分之一是数学专业的。通常不需要金融知识。

**The #1 prep resource** Xinfeng Zhou's Green Book (A Practical Guide to Quantitative Finance Interviews) - 200+ real problems. Supplement with [QuantGuide.io](https://quantguide.io/) ("LeetCode for quants") Brainstellar Jane Street's Figgie card game**排名第一的备考资源** 周新峰的绿皮书 （ 量化金融面试实用指南 ）——200+个真实问题。 补充 [QuantGuide.io](https://quantguide.io/) （“量化分析师的 LeetCode”） 大脑之星 Jane Street 的 Figgie 纸牌游戏

## The Complete Toolbox完整工具箱

**Python stack** Data: pandas, polars (Polars is 10-50x faster on large datasets) Numerics: numpy, scipy ML (tabular): xgboost, lightgbm, catboost ML (deep): pytorch Optimization: cvxpy Derivatives: QuantLib (Industry-grade, C++ backend) Stats: statsmodels Backtesting: NautilusTrader Backtesting (simpler): backtrader, vectorbt (Easier starting point) Quant research: Microsoft Qlib (17K+ stars, AI-oriented) RL for trading: FinRL (10K+ stars)Python 技术栈 数据： pandas、polars（在大数据集上，polars 的速度比 pandas 快 10-50 倍） 数值库： numpy、scipy 机器学习（表格）： xgboost、lightgbm、catboost 机器学习（深度）： PyTorch 优化： cvxpy 衍生品： QuantLib（工业级 C++ 后端） 统计： 统计模型 回测： NautilusTrader 回测（简易版）： backtrader、vectorbt（更容易上手） 量化研究： 微软 Qlib（17000+ 星，面向人工智能） 用于交易的 RL： FinRL（10K+ 星）

**C++ and Rust** Tbh i don't know anything about this. This is what I've found: C++ libraries: QuantLib, Eigen, Boost. Rust: RustQuant for option pricing, NautilusTrader as the Rust+Python paradigm (Rust core for speed, Python API for research).**C++ 和 Rust** 说实话，我对这方面一窍不通。以下是我找到的信息： C++ 库： QuantLib、Eigen、Boost。 Rust： RustQuant 用于期权定价，NautilusTrader 作为 Rust+Python 范式（Rust 核心用于提高速度，Python API 用于研究）。

**Data sources** Free: yfinance, Finnhub (60 calls/min), Alpha Vantage. Mid-range: [Polygon.io](https://polygon.io/) ($199/mo, sub-20ms latency), Tiingo. Enterprise: Bloomberg Terminal (~$32K/yr), Refinitiv, FactSet. Blockchain: Alchemy (free tier with archive access).**数据来源** 免费 ：yfinance、Finnhub（每分钟 60 次通话）、Alpha Vantage。 中档 ： [Polygon.io](https://polygon.io/) （每月 199 美元，延迟低于 20 毫秒），Tiingo。 企业级： 彭博终端（约 3.2 万美元/年）、Refinitiv、FactSet。 区块链： 炼金术（免费层级，可访问存档）。

**Solvers** Gurobi: Fastest commercial MIP solver, free academic license. Essential for combinatorial arbitrage. Google OR-Tools: Strongest free solver. PuLP/Pyomo: Python modeling interfaces.**求解器** Gurobi： 速度最快的商业混合整数规划求解器，提供免费学术许可。是组合套利的必备工具。 Google OR-Tools ：最强大的免费求解器。 PuLP/Pyomo： Python 建模接口。

## The Reading List (In Order)阅读清单（按顺序）

**Mathematics数学**

1. Blitzstein & Hwang - Introduction to Probability (free PDF from Harvard)Blitzstein & Hwang - 概率论导论 （哈佛大学免费 PDF 版）
2. Strang - Introduction to Linear Algebra + MIT 18.06 lecturesStrang - 线性代数导论 + MIT 18.06 课程
3. Wasserman - All of Statistics沃瑟曼—— 所有统计数据
4. Boyd & Vandenberghe - Convex Optimization (free PDF from Stanford)Boyd & Vandenberghe - 凸优化 （斯坦福大学提供的免费 PDF）
5. Shreve - Stochastic Calculus for Finance I & IIShreve - 金融随机微积分 I & II

**Quant finance量化金融**

1. Hull - Options, Futures, and Other Derivatives赫尔 - 期权、期货及其他衍生品
2. Natenberg - Option Volatility and Pricing纳滕贝格 - 期权波动率和定价
3. López de Prado - Advances in Financial Machine LearningLópez de Prado - 金融机器学习的进展
4. Ernest Chan - Quantitative Trading陈恩斯特 - 量化交易
5. Zuckerman - The Man Who Solved the Market扎克曼—— 破解市场难题的人

Interview prep面试准备

1. Zhou - Practical Guide to Quantitative Finance Interviews (Green Book #1)周著 - 《量化金融面试实用指南》 （绿皮书#1）
2. Crack -Heard on the Street街头传闻
3. Joshi - Quant Job Interview QuestionsJoshi - 量化分析师面试题

**Competitions比赛**

- Jane Street Kaggle ($100K prize)Jane Street Kaggle（奖金 10 万美元）
- WorldQuant BRAIN (100K+ users, pays for alpha signals)WorldQuant BRAIN（10 万+用户，付费获取 alpha 信号）
- Citadel Datathon (fast-track to employment)Citadel Datathon（快速就业途径）
- Jane Street monthly puzzles (above interview difficulty)Jane Street 每月谜题（难度高于面试难度）

## Three things I wish I'd known earlier三件我希望早点知道的事

**Estimation error is the real enemy.** Full Kelly betting, unconstrained Markowitz, ML models with too many features - they all fail for the same reason: overfitting NOISY BS in parameter estimates.估算误差才是真正的敌人。 完全 Kelly 投注、无约束 Markowitz、特征过多的 ML 模型——它们都因为同一个原因而失败：参数估计中存在过拟合的噪声。

The math works perfectly with true parameters. You never have true parameters. The gap between theory and practice is always estimation error, and the best quants are the ones who respect it.这套数学方法在参数真实的情况下完美适用。但你永远无法拥有真实参数。理论与实践之间的差距永远在于估计误差，而最优秀的量化分析师正是那些尊重估计误差的人。

**Tools have democratized. Conviction hasn't.** Anyone can access QuantLib, [Polygon.io](https://polygon.io/), and PyTorch. Technology is necessary but not sufficient. Edge lives in unique data, unique models, or unique execution - not better pip installs.工具已经普及，但信念却没有。 任何人都可以访问 QuantLib， [Polygon.io](https://polygon.io/) 以及 PyTorch。技术固然必要，但并非充分条件。边缘计算存在于独特的数据、独特的模型或独特的执行方式中，而非更高效的 p​​ip 安装。

**The math is the moat** AI can write code and suggest strategies. But the ability to derive why Itô's lemma has an extra term, to prove that discounted prices are martingales under the risk-neutral measure, to know when a convex relaxation is tight versus loose in a combinatorial market that mathematical fluency separates quants who build edge from quants who borrow it. And borrowed edge expires.数学就是护城河 人工智能可以编写代码并提出策略建议。但是，能够推导出伊藤引理为何多出一个项、证明贴现价格在风险中性测度下是鞅、判断组合市场中凸松弛是紧的还是松的，这些数学上的娴熟运用才能，才能将构建优势的量化分析师与借用优势的量化分析师区分开来。而借来的优势终会过期。

## What comes in Part 2第二部分包含什么内容？

Part 2 covers: exotic derivatives (barriers, Asians, lookbacks), stochastic volatility (Heston model calibration), jump-diffusion (Merton), advanced measure theory (martingale representation, optional stopping), stochastic control for optimal execution (Almgren-Chriss), reinforcement learning for market making, transformer architectures for financial time series, FPGA trading infrastructure, WebSocket feeds, parallel execution, Frank-Wolfe with Gurobi for combinatorial arbitrage across thousands of conditions.第二部分涵盖：奇异衍生品（障碍期权、亚式期权、回溯期权）、随机波动率（Heston 模型校准）、跳跃扩散（Merton）、高级测度理论（鞅表示、可选停止）、用于最优执行的随机控制（Almgren-Chriss）、用于做市的强化学习、用于金融时间序列的 Transformer 架构、FPGA 交易基础设施、WebSocket 馈送、并行执行、Frank-Wolfe 与 Gurobi 结合，用于在数千种条件下进行组合套利。

The math gets harder. The paycheck gets longer数学越来越难，工资发放周期也越来越长。

<video preload="auto" tabindex="-1" playsinline="" aria-label="嵌入式视频" poster="https://pbs.twimg.com/tweet_video_thumb/HCgdbVvXQAAE_fz.jpg" src="https://video.twimg.com/tweet_video/HCgdbVvXQAAE_fz.mp4" type="video/mp4" style="width: 100%; height: 100%; position: absolute; background-color: black; top: 0%; left: 0%; transform: rotate(0deg) scale(1.005);"></video>

GIF