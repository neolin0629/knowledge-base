---
created: 2026-04-19
updated: 2026-04-19
tags:
  - obsidian
area: Personal-Systems
status: done
---
# Obsidian目录结构优化建议

**Created:** 4/16/2026 20:18:27  
**Updated:** 4/19/2026 16:24:03  
**Exported:** 4/19/2026 16:24:21  
**Link:** [https://claude.ai/chat/80ccf639-354a-4a8d-bdff-6fc308777268](https://claude.ai/chat/80ccf639-354a-4a8d-bdff-6fc308777268)  

## Response:
2026/4/19 16:17:35

好问题。我先澄清一件事：你截图里这种属性名（`er`、`ctr`、`nf`）是你之前 Templater 模板的旧版本，和最新 dashboard 已经对不上了。我按最新 dashboard 的查询倒推每类文件该有什么属性，给你一份完整清单。

**核心原则：属性不是越多越好，够用就行**。每个属性要么被 Dataview 查到、要么帮 Claude 做决策，没用的不加。

---

## 一、内容运营类（文章、选题、草稿）

这是属性最多最严格的一类，因为 dashboard 大部分查询都在统计这些。

### 1.1 小红书/公众号已发布文章

位置：`3-Areas/Content/xhs-dahao/published/`、`xiaohao/published/`、`wechat/published/`、以及 `4-Projects/<系列名>/` 下已发布的

```yaml
---
# 身份（必填）
account: dahao              # dahao | xiaohao | wechat
type: image-text            # image-text | video | longform
status: published           # ⭐ 发布后必须是 published

# 分类（必填）
category: 量化              # 大号允许：量化/宏观/商品/AI投资/方法论/市场结构
                           # 小号额外：生活随笔/交易日记/踩坑/人设
hook_type: 数据冲击         # 数据冲击 | 反常识 | 人设 | 金句 | 故事
origin: from-notes          # from-topic-pool | from-notes | scratch | series | repurposed

# 溯源（大号必填，小号可空）
source_notes: [[...]]       # 基于哪些笔记
source_raw: []              # 引用的原始资料

# 引流网络（按需填）
drives_to:                  # 小号专用：引流到哪篇大号
repurposed_from:            # 大号/公号：由哪篇改写

# 系列（系列文章必填）
series: [[量化100问]]        # 若属于某系列
series_index: 001            # 编号

# 时间（必填）
created_date: 2026-04-16
publish_date: 2026-04-16    # ⭐ 发布时填

# 数据（只填原始值，发布后手动回填）
views: 0
likes: 0
saves: 0
comments: 0
shares: 0
followers_gained: 0
---
```

**对比你截图里的旧版**，需要改的地方：

| 旧属性 | 新属性 | 说明 |
|---|---|---|
| `status: 🚀已发布` | `status: published` | 改成纯英文值，Dataview 过滤稳定 |
| `er: 没有值` | ❌ 删掉 | Dataview 算 `(likes+saves+comments)/views`，不手填 |
| `ctr: 没有值` | ❌ 删掉 | 同上 |
| `nf: 没有值` | `followers_gained: 0` | 英文字段名 + 填 0 而不是空（Dataview 才能 SUM） |
| `subtype: with_cover` | 保留 | 有用但不是必填 |
| `source_notes:` | `source_notes: []` | 数组格式 |
| （无）| 加 `hook_type` | dashboard 1.9 要按 hook 分类看 |
| （无）| 加 `origin` | dashboard 1.5 要对比 |
| （无）| 加 `likes / saves / comments / shares` | 只有 views 没法算 ER |

**两个最容易错的地方**：

1. **`views: 0` 而不是 `views:` 空着**。Dataview 的 `WHERE views > 0` 过滤会把空值当 null 过滤掉，但 SUM 空值会出问题。**统一填 0 作为默认值**。
2. **发布前 `status: draft`，发布后改成 `status: published`**。不要用中文、不要加 emoji——dashboard 全部用英文值匹配。

### 1.2 Topic（选题池）

位置：`3-Areas/Content/<各渠道>/topic-pool/`

```yaml
---
type: topic                 # ⭐ 这个字段让 dashboard 1.7 能筛出选题
status: idea                # idea | researching | ready-to-draft | dropped
priority: high              # high | medium | low
source_notes: []
source_raw: []
source_inspiration:         # 看到什么引起的（某篇小号爆款、某条推特）
target_account: dahao       # ⭐ dashboard 1.7 需要
target_hook:                # 预设钩子
estimated_value: 高         # 高 | 中 | 低
created: 2026-04-16
---
```

**关键点**：topic 和 article 用 `type` 字段区分。topic 文件正文是调研笔记，不是成文。`draft` 时会转成 article（移动到 drafts/）。

### 1.3 Draft（草稿）

位置：`3-Areas/Content/<各渠道>/drafts/`

属性**和已发布文章相同**，只是 `status: draft`，`publish_date` 空，数据字段全是 0。

### 1.4 Series 内部文章

位置：`4-Projects/xhs-100-posts-quant/` 下

属性**和已发布文章相同**，额外必填：

```yaml
series: [[量化100问]]
series_index: 001
origin: series               # 固定值
```

---

## 二、Areas 主题笔记

### 2.1 概念页 / 主题笔记（3-Areas/Investing/Quant/ 等下的文件）

```yaml
---
title: 动量因子                # 可选，默认用文件名
created: 2026-04-16
updated: 2026-04-16            # ⭐ dashboard 6.2 查超 90 天未更新要用
tags: [因子, 量化]
area: Investing/Quant          # ⭐ 所在 Area 的相对路径，方便统计
status: done                   # draft | done
links: [[相关笔记1]], [[相关笔记2]]
---
```

**只有 5 个必填字段**：`created`、`updated`、`tags`、`area`、`status`。比内容文章少得多，因为 Areas 笔记是给你自己看的，不是给算法看的。

**什么时候填 `status: draft`**：还没整理好的半成品、只记了几个要点的笔记。整理好了就 `status: done`。

**`area` 字段的值规范**：写**相对路径**而不是目录名。
- ✅ `Investing/Quant`
- ✅ `Investing/Commodities`
- ❌ `Quant`（太笼统，搜不到）
- ❌ `3-Areas/Investing/Quant`（带前缀反而累赘）

### 2.2 量化复盘

位置：`3-Areas/Investing/Journal/daily/`、`weekly/`、`monthly/`、`event/`

```yaml
---
type: daily-review             # ⭐ 必填，daily-review | weekly-review | monthly-review | event-review
date: 2026-04-16               # ⭐ 必填，dashboard 2.x 都按这个排序
status: draft                  # draft | frozen
market_regime: 震荡             # 震荡 | 趋势 | 单边 | 低波 | 高波 | 转折
hs300_change: -0.82            # 数字，不带 %
strategies_active: [因子策略A]
pnl:                           # 期间盈亏（数字或空）
new_observations: []           # ⭐ dashboard 2.3 需要，反哺候选
challenges_thesis: []          # 挑战了 Areas 里哪些观点
tags: [复盘]
---
```

**event 类型额外**：

```yaml
type: event-review
event_category: 黑天鹅          # 黑天鹅 | 策略爆仓 | regime切换 | 政策突变
severity: high                  # low | medium | high
thesis_challenged: []           # 必须立刻反哺
thesis_validated: []
```

**关键点**：
- `new_observations` 是个数组。Claude 跑 weekly/monthly 的反哺检查时会扫这个字段
- 写完冻结后 `status: frozen`，正文不能改

### 2.3 Areas 下的 Journal（主题内事件笔记）

位置：`3-Areas/Investing/Quant/Journal/2026-04-10-读书.md` 这种

```yaml
---
title: 读《Advances in Financial ML》第三章
created: 2026-04-10
updated: 2026-04-10
tags: [读书, 量化方法论]
area: Investing/Quant           # ⭐ 所属 Area
status: done
type: journal-event             # 可选，用于和 2.1 的概念页区分
source_raw: [8-Raw/books/...]
links: []
---
```

**和量化复盘的 Journal 区别**：这种是"某主题下的事件记录"，不参与 PnL/策略统计，属性简单。

---

## 三、1-Notes（跨主题笔记）

```yaml
---
title: 和老张聊策略后的感悟
created: 2026-04-16
updated: 2026-04-16
tags: [思考, 方法论]             # ⭐ 多个 tag 说明是跨主题的
area:                           # ⭐ 留空！这是 1-Notes 的特征
status: done
links: []
---
```

**核心特征**：`area` 字段**留空**。这就是 1-Notes 和 3-Areas 笔记的本质区别——Areas 笔记必有 area 字段。

dashboard 5.2 的"Notes 积压"查询就是找 `1-Notes/` 里 60 天无反向链接的，5.4 找 `length(tags) >= 2` 的跨主题笔记。所以 **tags 要写准**。

---

## 四、0-Inbox（临时碎片）

```yaml
---
title: 
created: 2026-04-16
tags: [scratch]                 # ⭐ 所有临时想法统一打 scratch tag
---
```

**就这么简单**。inbox 是未整理状态，加多了属性反而浪费精力。等走 `from-inbox` 流程时 Claude 帮你补全。

**唯一建议**：`scratch` tag 一定要有，这样 Dataview 能区分"原本就是随手记"和"已整理但未归位"。

---

## 五、Projects（4-Projects/）

### 5.1 项目 README.md

位置：每个 `4-Projects/<项目名>/README.md`

```yaml
---
type: project                   # ⭐ 必填，dashboard 3.x 都靠这个筛选
status: active                  # active | paused | done | archived
started: 2026-04-01             # ⭐ 必填
deadline: 2026-06-30            # ⭐ 必填（无则填个大致的，利于 lint 检查）
owner: kaka
tags: [量化, CTA]
---
```

**归档后改动**（见 Archive 契约）：

```yaml
status: archived
archived_at: 2027-04-16
archive_reason: completed       # completed | dropped | paused-long
originally_started: 2026-04-16
```

### 5.2 项目内部文档

`4-Projects/<项目>/progress/`、`docs/` 下的文件**不需要特殊 frontmatter**，当普通笔记处理：

```yaml
---
title: 
created: 2026-04-16
updated: 2026-04-16
tags: [项目名相关tag]
---
```

---

## 六、Raw / Resources / Archive / Assets / Templates

### 6.1 `8-Raw/` 原始资料

**可选加 frontmatter**，但基本不需要——Raw 是档案，不参与统计。

如果想加，最简就是：

```yaml
---
source_url:                     # 如果是网页剪藏
clipped_at: 2026-04-16
---
```

### 6.2 `5-Resources/` 精选资源

```yaml
---
title: 
type: resource                  # 可选
tags: [分类标签]
added: 2026-04-16               # 加入精选的时间
source_raw:                     # 如果原件在 8-Raw/ 里，链过去
---
```

### 6.3 `6-Archive/` 归档

**不要手动改归档里文章的 frontmatter**。唯一要改的是归档项目的 README（见 5.1）。

### 6.4 `2-Assets/` 和 `7-Templates/`

**不需要 frontmatter**。这些是资源文件，不参与查询。

---

## 最简速查表（打印出来贴墙上）

| 位置 | 必填字段（最小集） |
|---|---|
| `0-Inbox/` | `created`, `tags: [scratch]` |
| `1-Notes/` | `created`, `updated`, `tags`, `status` |
| `3-Areas/<主题>/` | `created`, `updated`, `tags`, `area`, `status` |
| `3-Areas/Investing/Journal/daily/` | `type`, `date`, `status`, `market_regime`, `new_observations` |
| `3-Areas/Content/<渠道>/topic-pool/` | `type: topic`, `target_account`, `status`, `priority`, `created` |
| `3-Areas/Content/<渠道>/drafts/` | 草稿用完整 article 属性，`status: draft` |
| `3-Areas/Content/<渠道>/published/` | 完整 article 属性，`status: published`, `publish_date`, 数据字段 |
| `4-Projects/<项目>/README.md` | `type: project`, `status`, `started`, `deadline` |
| `4-Projects/<项目>/` 系列文章 | 完整 article 属性 + `series` + `series_index` |
| `6-Archive/` | **保持原值不动**；项目 README 加归档元数据 |
| `8-Raw/` / `5-Resources/` / `2-Assets/` | 不需要 |

---

## 现在你截图的那篇文章怎么办

你那篇已发布的图文（category: 投资展望），建议这样改 frontmatter：

```yaml
---
# 改：
account: dahao                   # 加
type: image-text                 # 保持
status: published                # 改（原来的 🚀已发布）
subtype: with_cover              # 保持（可选）
category: 宏观                    # 改（"投资展望"不在允许列表，建议改成"宏观"或"市场结构"）
hook_type: 金句                   # 加（猜的，按实际选）
origin: from-notes               # 加（如果是基于笔记写的）

source_notes: [[某个 Areas 笔记]] # ⭐ 大号必填，追溯到笔记
source_raw: []                   # 加
drives_to:                       # 加（如果有关联小号引流文章）
repurposed_from:                 # 加

created_date: 2026-03-01
publish_date: 2026-03-01         # 保持

# 删：
# er: 没有值         → 删，Dataview 算
# ctr: 没有值        → 删
# nf: 没有值         → 改为 followers_gained: 0

# 加 5 个数据字段：
views: 0                         # 发布后回填真实数据
likes: 0
saves: 0
comments: 0
shares: 0
followers_gained: 0
---
```

---

## 要不要我生成一份迁移脚本思路

如果你已经发布的文章比较多（比如 28 篇在 `00_output/` 或原 published 目录），手动改 frontmatter 会累。可以告诉 Claude Code：

```
你：帮我扫 3-Areas/Content/xhs-dahao/published/ 下所有文件，
    列一个 frontmatter 迁移清单：
    - 哪些缺 account
    - 哪些 status 是中文需要改
    - 哪些需要加 views/likes/saves 等数据字段
    - 不执行，只出清单
```

然后你 approve 后 Claude 帮你批量改。**不要让它自动统计数据——views 等原始值必须你从小红书后台看到再填**，Claude 不能编。