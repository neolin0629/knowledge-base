# CLAUDE.md — Vault 根规则

> Neo 的个人知识库。PARA 风格。
> Claude 角色：**仓库管理员**——帮我建双链、基于笔记写文章、跨目录搜索、一致性检查。
> 我是笔记作者，你不代我写知识，你让我的笔记产生复利。

---

## 0. 扫描与效率原则（⭐ 非常重要，必须遵守）

**默认不扫全库。** 每条指令都有明确的扫描边界，不得超出。

### 0.1 成本意识
- 能用一条 `ls` 解决的不要用 `find`；能用 `grep -l` 筛文件名的不要逐个读内容。
- 如果一个指令需要 > 5 条 bash 或需要读多个文件内容，**必须先告诉我计划并等我 approve**。
- 任何 `find . -type f` 或类似全库扫描都是昂贵操作，不要默认做。

### 0.2 优先级：Dataview > frontmatter > grep > 读全文
- 需要统计数据？**告诉我"去看 dashboard.md"**，不要自己数。Dataview 已经实时计算好了。
- 需要按字段筛选？用 `grep -l "account: dahao" -r <目录>` 而不是读每个文件 frontmatter。
- 需要关键词匹配？用 `grep -rli "关键词"` 先筛文件，再决定读哪些。
- 读全文是最后手段，只对少数目标文件做。

### 0.3 每条指令的扫描边界（硬性约束）

| 指令                | 允许扫描范围                                           | 允许的操作              | 禁止              |
| ----------------- | ------------------------------------------------ | ------------------ | --------------- |
| `status`          | 根目录 `ls`（非递归）+ 关键目录文件数                           | `ls`、`wc -l`       | 读任何文件内容、递归 find |
| `content-status`  | `3-Areas/Content/*/` 下一级的 topic-pool/drafts/     | `ls` + 文件名列表       | 读文件内容           |
| `lint`            | 必要时全库，但**必须先说计划让我 approve**                      | 先说明"我要扫 X 个目录 Y 秒" | 未 approve 就扫    |
| `search [Q]`      | 先 `grep -rli` 筛候选，再只读命中的                         | grep + 读命中文件       | 全库读内容           |
| `link [目标]`       | 仅目标文件/目录 + 关键词反向搜索                               | grep 反向找           | 扫无关区域           |
| `from-inbox [文件]` | 仅该文件                                             | 读该文件               | 扫其他 inbox 文件    |
| `promote [文件]`    | 仅该文件                                             | 读该文件               | 扫 Areas 全部      |
| `journal *`       | 仅 `3-Areas/Investing/Journal/<对应子目录>`            |                    | 扫 Areas 其他部分    |
| `project *`       | 仅 `4-Projects/<具体项目>` 或 `4-Projects/*/README.md` |                    | 进入项目内文件递归       |

**遇到越界需求时**：停下来问我，不要自作主张扩大范围。

---

## 1. 关于我

量化研究投资经理（GoldMine 平台，Python + ClickHouse + DuckDB，股票/期货/期权）。
同时运营三个内容渠道（详见 `3-Areas/Content/CLAUDE.md`）。

---

## 2. 目录结构

```
0-Inbox/         临时收件箱。硬上限 15 篇。
1-Notes/         已整理但未归主题的笔记（跨多 Area、通用思考）
2-Assets/        图片、音频、视频等资产
3-Areas/         ⭐ 按主题长期组织
4-Projects/      ⭐ 有明确目标和终点的项目
5-Resources/     验证过、长期有用的外部参考资料
6-Archive/       已结束的项目（⭐ 保留 frontmatter，参与 Dataview）
7-Templates/     所有模板
8-Raw/           原始资料（未加工）
9-Excalidraw/    可视化图表（excalidraw 格式，由 Obsidian 插件管理）
```

### 2.1 `1-Notes/` 定位

介于 `0-Inbox`（临时）和 `3-Areas`（已归主题）之间：

| 对比  | 0-Inbox | 1-Notes  | 3-Areas |
| --- | ------- | -------- | ------- |
| 状态  | 未整理     | 已整理但未归主题 | 已归主题    |
| 上限  | 15      | 无        | 无       |
| 内容  | 碎片      | 完整笔记     | 主题维护    |

**放 Notes**：跨多主题的笔记（读书会议含宏观+量化+心理）、通用思考、访谈纪要
**放 Areas**：明确单一主题的内容
**放 Areas/xxx/Journal**：明确属于某主题的时间记录

### 2.2 `3-Areas/` 子结构

```
3-Areas/
├── Investing/
│   ├── Quant/ (含 Journal/)
│   ├── Macro/ (含 Journal/)
│   ├── Commodities/ (含 Journal/)
│   ├── AI-Investing/
│   ├── Risk/
│   └── Journal/         ⭐ 量化复盘（daily/weekly/monthly/event）
├── Content/             内容运营（详见该目录 CLAUDE.md）
│   ├── xhs-dahao/
│   ├── xhs-xiaohao/
│   └── wechat/
├── AI-Workflow/
├── Health/
├── Writing/
├── Personal-Systems/
├── Person/              人物研究（投资人、量化先驱、历史人物等）
└── History/             历史文化笔记
```

### 2.3 `4-Projects/` 示例

```
4-Projects/
├── CTA因子重构/
│   ├── progress/
│   ├── docs/
│   └── README.md
├── xhs-100-posts-quant/   (系列作为项目)
└── client-A-strategy-report/
```

### 2.4 `8-Raw/` 子目录

```
8-Raw/
├── x-clippings/
├── research-reports/
├── papers/
├── books/
├── podcasts/
├── articles/
└── videos/
```

### 2.5 `6-Archive/` 契约

归档是**保留数据**，不是**丢弃数据**。

**铁律：**
1. 归档文章的 frontmatter **绝对不改**（account/status/views 等保持原值）
2. 改的只是**项目 README** 的 frontmatter：加 `status: archived`、`archived_at`、`archive_reason`、`originally_started`
3. 目录重命名：`6-Archive/<原名>-<reason>-<YYYY-MM>/`（reason = completed | dropped | paused-long）
4. Dataview 查询必须 `FROM "3-Areas/Content" OR "6-Archive"` + frontmatter 过滤

---

## 3. 边界规则

| 纠结点 | 规则 |
|---|---|
| `0-Inbox` vs `1-Notes` | Inbox 未整理碎片（有上限）；Notes 已整理但未归主题。 |
| `1-Notes` vs `3-Areas` | Notes 跨主题/未归主题；Areas 明确单主题。 |
| `3-Areas` vs `4-Projects` | Areas 无限期；Projects 有 deadline。 |
| `5-Resources` vs `8-Raw` | Raw 未加工；Resources 已认可精选。 |
| 归档后改文章 | **永不改**（见 2.5）。 |

---

## 4. Frontmatter 规范

### 4.1 通用笔记（0-Inbox、1-Notes、3-Areas）

```yaml
---
title: 
created: 2026-04-16
updated: 2026-04-16
tags: []
area:                       # Areas 相对路径（1-Notes 可留空）
status: draft | done
links: []
---
```

### 4.2 其他类型
- 内容文章 → `3-Areas/Content/CLAUDE.md`
- 量化复盘 → `3-Areas/Investing/Journal/README.md`
- 项目 → 第 7 节

### 4.3 链接一律 `[[双链]]`

---

## 5. 全局指令

### `status` — vault 概览（⚡ 轻量）

**扫描边界**：
```bash
ls -1 .                                          # 根目录
ls 0-Inbox | wc -l                              # Inbox 数
ls 1-Notes | wc -l                              # Notes 数
ls -1d 4-Projects/*/                            # Active 项目名（一级）
ls -1 3-Areas/Investing/Journal/daily/ | tail -5 # 最近 5 篇 daily
```

**输出格式**（不超过 20 行）：
```
📁 一级目录：0-Inbox / 1-Notes / 2-Assets / ...（确认齐全）

📥 Inbox：X 篇（上限 15）
📝 Notes：X 篇
🚀 Active 项目：N 个
  - project-a
  - project-b
  - ...
📔 最近 5 次复盘：
  - 2026-04-15
  - 2026-04-14
  - ...

详细数据看 dashboard.md。
```

**禁止**：读任何 frontmatter、统计文章数、扫 Content、进 Archive、跑 find。

### `link [文件/目录]` — 补双链
**扫描边界**：
1. 读目标文件（一次）
2. 提取关键词（概念、人名、主题）
3. 对每个关键词 `grep -rli "关键词" 3-Areas/ 1-Notes/`（grep 本身快）
4. 给候选清单让我 approve
**禁止**：读所有候选文件的全文再判断相关性——用关键词匹配信号即可。

### `search [问题]` — 跨目录搜索
**扫描边界**：
1. 从问题里提关键词
2. `grep -rli "关键词" 3-Areas/ 1-Notes/ 4-Projects/ 6-Archive/`
3. 候选 > 10 篇时，先列清单让我挑重点再读
4. 只读命中文件的相关段落（用 grep -A/-B 取上下文），不读全文

### `lint` — 仓库体检（⚠️ 重操作，先报计划）

**调用前必须先说**：
> 我将扫 X 个目录（列出），跑 Y 条 bash，预计 Z 秒。继续吗？

用户 approve 后才扫。

**检查项**：
- 0-Inbox 超 15
- 1-Notes 超 60 天且无反向链接
- Projects 超 deadline 或 90 天没动
- Archive 契约违规
- （用 grep 和 Dataview 能查到的都不要重新扫）

### `from-inbox [文件]` — inbox 归位
只读该文件，提议归属，等我 approve 再移动。

### `promote [1-Notes 文件]` — notes 升级到 Area
只读该文件，提议目标 Area，等我 approve。

### `scratch [描述]`
存到 `0-Inbox/` 带日期文件名，tag `scratch`。

---

## 6. 量化复盘

详见 `3-Areas/Investing/Journal/README.md`。

| 我说                     | 你做                | 扫描边界                                              |
| ---------------------- | ----------------- | ------------------------------------------------- |
| `journal daily`        | 在 daily/ 生成今日草稿   | 仅 daily/                                          |
| `journal weekly`       | 聚合本周 daily + 反哺检查 | 仅 daily/ 最近 7 天                                   |
| `journal monthly`      | 月度复盘 + Areas 观点复核 | daily/ 最近 30 天 + Investing/Quant \|Macro 等 README |
| `journal event <slug>` | 事件复盘 10 问         | 仅新建文件                                             |

---

## 7. 项目规范

```yaml
---
type: project
status: active | paused | done | archived
started: 2026-04-01
deadline: 2026-06-30
owner: Neo
tags: []
---
```

| 我说 | 你做 |
|---|---|
| `project new <名>` | 创建项目骨架 |
| `project status [名]` | 项目状态 |
| `project archive <名>` | 按 2.5 契约归档 |

---

## 8. 行为准则

**该做的：**
- 遵守第 0 节扫描约束
- 补双链必须我确认
- 写文章必须溯源
- 归档遵守 2.5 契约
- 说人话

**不该做的：**
- **默认全库扫描**
- **不经 approve 跑 > 5 条 bash**
- **自己统计 Dataview 已经有的数据**
- 改 `8-Raw/` 和 `6-Archive/` 文章的 frontmatter
- 一次改 >10 个文件
- 不经我同意搬家
- 在没有笔记来源时凭空写内容
- 自动归类 inbox 或升级 notes

---

## 9. 指令速查

| 指令 | 说明 | 重量级 |
|---|---|---|
| `status` | vault 概览 | ⚡ |
| `link [X]` | 补双链 | ⚡ |
| `search [Q]` | 跨目录搜索 | 🟡 |
| `from-inbox [文件]` | inbox 归位 | ⚡ |
| `promote [文件]` | notes 升级 | ⚡ |
| `scratch [描述]` | 即兴想法 | ⚡ |
| `lint` | 体检（需 approve） | 🔴 |
| `journal daily/weekly/...` | 量化复盘 | 🟡 |
| `project new/status/archive` | 项目管理 | ⚡ |

内容相关指令详见 `3-Areas/Content/CLAUDE.md`。

---

## 10. 元规则

- 本文档会进化。
- 工作流是默认值，我可随时覆盖。
- 冲突时以当次指令为准，告诉我哪条规则不一致。
- **目录结构同步规则**：当你发现 vault 实际目录结构和 CLAUDE.md 第 2 节描述明显不一致时（比如新增了一级目录或 Areas 一级子主题），主动提醒我："目前 vault 里有 X 目录但 CLAUDE.md 里没记录，要不要更新？"——但不要自动改，让我决定。
- **发现你正在超出扫描边界时，立刻停下来问我。**

### 本文档何时更新

判断标准：**新建/改动会改变 Claude 工作流吗？**

| 改动 | 是否更新 CLAUDE.md |
|---|---|
| 一级目录新增/删除/改名 | ✅ 必须更新 |
| 3-Areas 一级子主题新增（如 Crypto） | 🟡 建议更新（可攒 2-3 个批量改） |
| 全局指令新增/废弃/改行为 | ✅ 必须更新 |
| 边界规则、扫描约束变化 | ✅ 必须更新 |
| 子 CLAUDE.md（Content/dahao 等）改动 | 🟡 不影响根，但 CHANGELOG 要记 |
| 4-Projects 下新增项目目录 | ❌ 不用（项目自己有 README） |
| 项目内部子目录（progress/docs/experiments） | ❌ 不用 |
| 8-Raw 下新增分类子目录 | ❌ 不用 |
| Areas 主题下新增子文件夹（如 Quant/factors-library/） | ❌ 不用 |

判断口诀：**会改变 Claude 决策路径的 → 改；只是组织文件的 → 不改。**

### 目录漂移自动提醒

当你（Claude）发现 vault 实际结构和本文档第 2 节明显不一致时（如新增了一级目录或 Areas 一级子主题），主动提醒我：

> "检测到 vault 里有 X 但 CLAUDE.md 没记录，要不要更新本文档？"

**不要自动改 CLAUDE.md**，让我决定。每次跑 `status` 或 `lint` 时顺便检查一次即可，不要专门为此扫描。

### CHANGELOG 同步

每次更新 CLAUDE.md（任意层级），同步在 `CHANGELOG.md` 加一条记录。你（Claude）可以主动建议 changelog 文案，但**实际写入需要我 approve**。
