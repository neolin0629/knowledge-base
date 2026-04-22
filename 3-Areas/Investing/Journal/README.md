---
type: spec
updated: 2026-04-21
---

# Investing/Journal 规范

> 位置：`3-Areas/Investing/Journal/README.md`
> 作用：量化复盘系统的主规范。Claude 执行 `journal *` 前必读。

---

## 1. 为什么复盘放在 Areas 而不是 Projects

复盘是**无限期持续**的活动，属于 Area。
某个项目（如 `CTA因子重构`）的迭代记录才放 Projects 下。

---

## 2. 目录结构

```
3-Areas/Investing/Journal/
├── README.md       本文件（系统规范）
├── CLAUDE.md       Claude 写作模板与生成规则
├── daily/          每日盘后（30-45 分钟）
├── weekly/         每周日（必须有迭代成果）
├── monthly/        每月末（触发 Areas 观点复核）
└── event/          事件驱动（48h 内完成）
```

---

## 3. 日常执行结构（每日 4 小时）

来源：`4-Projects/量化研究数据库/Quant-research-README.md`

| 时段 | 任务 | 时长 | 输出要求 |
|---|---|---|---|
| 深度研究 | 新增因子/调参/regime 评估 | 120 min | 记录"策略变化点" + 下一步迭代方向 |
| 大周期思考 | 阅读/市场结构/资金逻辑 | 60 min | 今天学到的规律 → 如何量化 → 能否转策略 |
| 盘后检查 | 实盘记录/回测偏差/成本分析 | 60 min | 本日执行问题 + 改善计划 |
| 每日复盘 | 落地输出（即 daily journal） | 30-45 min | 见 5.1 节 |

**铁律**：每天必须留一份复盘。一天没有痕迹 = 没真正变强。

---

## 4. 五个核心原则

### 4.1 每日留痕
每天必须生成一份 daily，哪怕只有 3 行。

### 4.2 写完冻结
某期复盘完成后进入 `frozen` 状态，**正文不得修改**，只能在末尾 `## 补注（YYYY-MM-DD）` 追加。
理由：3 年后回看必须看到当时的原貌，不能被后来的自己美化。

### 4.3 反哺强制
- weekly 必须问我："本周 new_observations 里哪些要沉淀到 3-Areas/Investing/ 对应子主题？"
- monthly 必须对 Investing 下所有 active 观点执行复核
- event 的 `challenges_thesis` 非空时**立刻**更新对应 Areas 笔记

### 4.4 不给投资建议
复盘是思考工具，不需要"本文不构成投资建议"套话。

### 4.5 数据溯源
具体数字必须标注来源（`8-Raw/` 或笔记链接）。不得编造、不得猜。

---

## 5. 各类型说明

### 5.1 daily（每日盘后，30-45 分钟）

**命名**：`YYYY-MM-DD.md`

**核心四问**：
1. 今天做了什么（策略/研究/执行）
2. 得到了什么结论
3. 明天怎么延续
4. 三个可操作的下一步

**每日必记**（不解读，只记录，5 分钟）：
- 资金大方向
- 波动率水平（高/低）
- 政策或流动性变化

### 5.2 weekly（周日晚）

**命名**：`YYYY-WW.md`（如 `2026-W17.md`）

**必答项**：
- 本周聚合 PnL、最大回撤、换手率
- 实盘 vs 回测偏差分析
- 本周"可验证成果"（至少一项：新因子/新回测/研究总结/偏差分析）
- 本周五问（任选其一深入）：
  1. 为什么赚钱？
  2. 为什么亏损？
  3. 逻辑是否在不同 regime 下成立？
  4. 是否有更简单的实现？
  5. 这个策略是否真正"可执行"（成本/滑点/流动性）？
- **反哺清单**：本周 new_observations 哪些要沉淀到 Areas

### 5.3 monthly（月末）

**命名**：`YYYY-MM.md`

**必答项**：
- 本月 market regime 判断，对比上月变化
- 策略池整体表现（胜率/盈亏比/回撤）
- Investing 下所有 active 观点复核（状态是否该调整）
- 一句话月度 lesson

### 5.4 event（事件驱动，48h 硬截止）

**命名**：`YYYY-MM-DD-<slug>.md`

**强制 10 问**：
1. 事件是什么（事实）
2. 事前预期 vs 实际
3. 有无预警信号
4. 决策时效性
5. 情绪影响
6. 哪些观点被验证
7. 哪些观点被挑战（**必须**立刻反哺 Areas）
8. 可复用的教训
9. 风控是否按预期触发
10. 下次类似事件怎么做

---

## 6. Frontmatter 规范

```yaml
---
type: daily-review | weekly-review | monthly-review | event-review
date: 2026-04-21
status: draft | frozen
market_regime: 震荡 | 趋势 | 单边 | 低波
hs300_change: -0.82
vix_proxy: 18.3
strategies_active: []
pnl:
new_observations: []
challenges_thesis: []
reviewed_areas: []         # weekly/monthly 专用：本期反哺了哪些 Areas
tags: [复盘]
---
```

---

## 7. 指令速查

| 指令 | 动作 |
|---|---|
| `journal daily` | 按模板在 daily/ 下生成今日复盘草稿 |
| `journal weekly` | 聚合本周 daily，生成 weekly + 反哺检查 |
| `journal monthly` | 月度复盘 + Investing 观点复核 |
| `journal event <slug>` | 事件复盘，强制 10 问 |
| `journal freeze <path>` | 将指定文件 status 改为 frozen |

完整生成模板见 `CLAUDE.md`。

---

_v2 - 2026-04-21_
