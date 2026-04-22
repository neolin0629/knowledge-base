---
created: 2024-06-20
tags:
  - 量化研究/统计指标
aliases:
  - 信息比率
updated: 2026-04-19
area: Investing/Quant
status: done
---
量化研究中的 IC（Information Coefficient）计算方法有两种：

1. **皮尔逊相关系数（Pearson Correlation Coefficient）**：计算股票池中所有股票的因子值与下期收益率的线性相关度（Correlation）。该方法假设两组随机变量近似服从正态分布。

2. **斯皮尔曼相关系数（Spearman Rank Correlation Coefficient）**：计算股票池中所有股票的因子值排名与下期收益率排名的截面相关系数。该方法不需要假设两组随机变量的分布，且受离群值影响较小。

IC 的计算公式为：

$$IC = \frac{\sum{(x_i - \bar{x})(y_i - \bar{y})}}{\sqrt{\sum{(x_i - \bar{x})^2}\sum{(y_i - \bar{y})^2}}}$$

其中，$x_i$ 为股票池中第 $i$ 只股票的因子值，$y_i$ 为股票池中第 $i$ 只股票的下期收益率，$\bar{x}$ 和 $\bar{y}$ 分别为因子值和收益率的均值。

IC 的值越大，表明该因子对股票收益的预测能力越强。IC 的理论最大值为 1，表示该因子选股 100%准确。

Citations:
[1] https://www.ricequant.com/doc/quant/factor-system.html
[2] https://blog.csdn.net/fengchi863/article/details/101203639
[3] https://blog.csdn.net/m0_37876745/article/details/89326308
[4] https://xueqiu.com/4441758114/207793248
[5] https://bigquant.com/wiki/doc/pingjia-yinzi-xiaoguo-kfpX06DGWI
[6] https://xueqiu.com/1652627245/108835836
[7] https://guorn.com/forum/post/p.3.91894639944815
[8] https://maverickpeter.github.io/2022/02/02/Quant-1/