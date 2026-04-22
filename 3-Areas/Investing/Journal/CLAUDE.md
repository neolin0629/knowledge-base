# Journal/CLAUDE.md — Claude 写作规则与模板

> 本文件供 Claude 执行 `journal *` 指令时使用。
> 系统规范见 `README.md`，本文件只放模板和生成行为规则。

---

## 0. 扫描边界（继承根规则）

| 指令 | 允许读取 | 禁止 |
|---|---|---|
| `journal daily` | 仅 `daily/` 最近 1 篇（承接上文） | 读其他子目录 |
| `journal weekly` | `daily/` 最近 7 天文件 | 读 Areas 全部 |
| `journal monthly` | `daily/` 最近 30 天 + `Investing/Quant/`、`Investing/Macro/` 的 README | 进入 Areas 其他目录 |
| `journal event` | 仅新建文件 | 扫任何已有文件 |
| `journal freeze` | 仅目标文件 | 其他 |

超出边界前必须先说明并等用户 approve。

---

## 0.1 生成行为规则

- 生成草稿，**不替用户填写主观判断**（PnL、观点、结论等留空等用户填）
- 数字字段一律留空，不猜不估
- `new_observations` 和 `challenges_thesis` 留空，提示用户填写
- 生成后提示："以下字段需要你填写：xxx"
- 不主动冻结文件，除非用户明确说 `journal freeze`

---

## 1. daily 模板

**触发**：`journal daily`
**文件路径**：`daily/YYYY-MM-DD.md`

```markdown
---
type: daily-review
date: {{YYYY-MM-DD}}
status: draft
market_regime: 
hs300_change: 
vix_proxy: 
strategies_active: []
pnl:
new_observations: []
challenges_thesis: []
tags: [复盘]
---

## 市场速记

- 资金大方向：
- 波动率水平：
- 政策/流动性变化：

---

## 策略研究（今日 120 min）

**做了什么：**

**结论：**

**策略变化点：**

**下一步迭代方向：**

---

## 大周期思考（今日 60 min）

**今天学到的市场规律：**

**如何量化这个规律：**

**是否可能转化为策略逻辑：**

---

## 执行检查（今日 60 min）

**本日执行问题：**

**实盘 vs 回测偏差：**

**下一步改善计划：**

---

## 今日复盘

- 今天做了什么：
- 得到了什么结论：
- 明天怎么延续：
- 三个可操作的下一步：
  1. 
  2. 
  3. 
```

---

## 2. weekly 模板

**触发**：`journal weekly`
**文件路径**：`weekly/YYYY-WW.md`（如 `2026-W17.md`）
**生成步骤**：读本周 daily/ 文件 → 聚合 new_observations → 生成草稿 → 提示反哺清单

```markdown
---
type: weekly-review
date: {{本周周日日期}}
status: draft
week: {{YYYY-WW}}
strategies_active: []
pnl_weekly:
max_drawdown:
turnover:
reviewed_areas: []
new_observations: []
challenges_thesis: []
tags: [复盘]
---

## 本周数据

| 指标 | 本周 | 上周 |
|---|---|---|
| PnL | | |
| 最大回撤 | | |
| 换手率 | | |

---

## 实盘 vs 回测偏差

**偏差点：**

**原因分析：**

---

## 本周可验证成果

> 至少完成一项：新因子验证 / 新回测 / 研究总结 / 偏差分析

- [ ] 

---

## 本周五问（任选其一深入）

> 1. 为什么赚钱？2. 为什么亏损？3. 逻辑在不同 regime 下成立吗？4. 有更简单的实现？5. 策略真正可执行吗？

**选择的问题：**

**回答：**

---

## 本周 new_observations 聚合

> 来自 daily 汇总，需确认哪些沉淀到 Areas

{{聚合本周 daily 的 new_observations 字段}}

**待反哺清单**（请确认后我执行）：
- 
```

---

## 3. monthly 模板

**触发**：`journal monthly`
**文件路径**：`monthly/YYYY-MM.md`
**生成步骤**：读本月 daily/ → 读 Investing/Quant/README、Investing/Macro/README → 生成草稿 → 列出 active 观点请用户复核

```markdown
---
type: monthly-review
date: {{YYYY-MM-末日}}
status: draft
month: {{YYYY-MM}}
market_regime:
pnl_monthly:
max_drawdown:
reviewed_areas: []
tags: [复盘]
---

## 本月市场 Regime

**判断：**

**对比上月变化：**

---

## 策略池整体表现

| 策略 | 胜率 | 盈亏比 | 最大回撤 | 备注 |
|---|---|---|---|---|
| | | | | |

---

## Investing 观点复核

> 以下 active 观点需确认状态是否调整

{{从 Investing/ README 提取 active 观点列表}}

| 观点 | 上月状态 | 本月建议 | 依据 |
|---|---|---|---|
| | | | |

---

## 月度 Lesson

> 一句话：

---

## 下月重点

1. 
2. 
3. 
```

---

## 4. event 模板

**触发**：`journal event <slug>`
**文件路径**：`event/YYYY-MM-DD-<slug>.md`
**硬截止**：48h 内完成，`challenges_thesis` 非空时立刻提示反哺

```markdown
---
type: event-review
date: {{YYYY-MM-DD}}
status: draft
slug: {{slug}}
challenges_thesis: []
tags: [复盘, 事件]
---

## 事件复盘：{{slug}}

**发生时间：**

---

1. **事件是什么（事实）**

2. **事前预期 vs 实际**

3. **有无预警信号**

4. **决策时效性**

5. **情绪影响**

6. **哪些观点被验证**

7. **哪些观点被挑战**
   > ⚠️ 若非空，立刻更新对应 Areas 笔记

8. **可复用的教训**

9. **风控是否按预期触发**

10. **下次类似事件怎么做**
```

---

_v1 - 2026-04-21_
