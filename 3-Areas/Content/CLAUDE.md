# Content CLAUDE.md — 内容运营总规则

> 位置：`3-Areas/Content/CLAUDE.md`
> 作用域：此目录及以下所有子目录
> 继承：根 `CLAUDE.md`，此文件**叠加**内容运营相关规则，不重复上层内容

---

## 1. 三个渠道

| 渠道 | 短码 | 目录 | 定位 |
|---|---|---|---|
| 小红书「搞钱最重要」(大号) | `dahao` | `xhs-dahao/` | 专业金融、宏观、量化、商品，未来商业化 |
| 小红书「11点半收盘吃饭」(小号) | `xiaohao` | `xhs-xiaohao/` | 人设向、交易日记，为大号引流 |
| 微信公众号「11点半收盘吃饭」 | `wechat` | `wechat/` | 长文深度 1500-3000 字 |

**每个渠道有自己的 CLAUDE.md**，写各自的调性、频率、数据目标。Claude 在对应目录工作时自动继承那一份。

**系列内容不在此目录**——放 `4-Projects/<系列名>/`（参见根 CLAUDE.md 第 7 节）。Content 下只放单篇/非系列内容。

---

## 2. 每个渠道的三段式结构

```
xhs-dahao/
├── CLAUDE.md           大号专属规则
├── topic-pool/         ⭐ 选题库（想写但还没动笔）
├── drafts/             ⭐ 草稿（正在写）
├── published/          ⭐ 已发布归档
└── assets/             该渠道专属素材（配图、封面模板）
```

### 三段流转

```
想法 ──→ topic-pool/ ──→ drafts/ ──→ published/
         (选题研究)      (实际写作)    (发布+数据回填)
```

**不是所有想法都要写**。topic-pool 可以积累 50 个选题，最终只挑 10 个写。这是 PKM 的关键——降低"灵感被浪费"的焦虑，也降低"凑数硬写"的压力。

---

## 3. 三类文件 Frontmatter

### 3.1 Topic（topic-pool/ 下）

```yaml
---
type: topic
status: idea | researching | ready-to-draft | dropped
priority: high | medium | low
source_notes: []            # 灵感来自哪些 Areas 笔记
source_raw: []              # 哪些 Raw 素材支持
source_inspiration:         # 看到什么引起的（小号某爆款、某条推特）
target_account: dahao       # 这个选题准备给哪个账号用
target_hook:                # 预设的钩子类型
estimated_value: 高         # 高 | 中 | 低（预估效果）
created: 2026-04-16
---
```

### 3.2 Draft / Published（drafts/ 和 published/ 下）

```yaml
---
# 身份
account: dahao              # dahao | xiaohao | wechat
type: image-text            # image-text | video | longform
status: draft               # draft | scheduled | published

# 分类
category: 量化              # 见各渠道 CLAUDE.md 的允许列表
hook_type: 数据冲击          # 数据冲击 | 反常识 | 人设 | 金句 | 故事
origin: from-topic-pool     # from-topic-pool | from-notes | scratch | repurposed

# 溯源
source_topic:               # 从 topic-pool 里哪篇来的（如有）
source_notes: []            # 基于哪些笔记
source_raw: []              # 引用的原始资料

# 引流网络
drives_to:                  # xiaohao 专用：引流到哪篇 dahao
repurposed_from:            # dahao/wechat：由哪篇改写

# 时间
created_date: 2026-04-16
publish_date:

# 数据（只录原始值，比率由 Dataview 算）
views: 0
followers_gained: 0
likes: 0
comments: 0
saves: 0
shares: 0
---
```

**不要手填 ER/CTR**。Dataview 算。

---

## 4. 工作流与指令

### 4.1 `topic add <描述> for <账号>` — 选题入库
在对应 `xhs-dahao/topic-pool/` 等下创建 topic 文件，填 frontmatter，不写正文。

### 4.2 `topic refine <文件>` — 选题研究
Claude 扫相关 Areas 笔记和 Raw 资料，补充到 topic 的正文里（不是 drafts，还在 topic-pool）。完成后可以改 status 为 `ready-to-draft`。

### 4.3 `draft <topic文件 或 主题 或 笔记引用> for <账号>`
- 如果是 topic-pool 里的文件：**移动**到对应 drafts/ 下，基于 topic 正文展开
- 如果是笔记引用（`[[...]]`）：从笔记读素材，在 drafts/ 下新建
- 如果是主题描述：先帮我在 topic-pool 建选题，等我确认后再 draft
- `for 全渠道`：生成三版（大号 + 小号 + 公号）

生成的草稿必须含：3 个标题候选、配图建议、预估字数、发布时机建议。使用/content-ai-avoid 去除 ai 味 。使用/chinese-typography-rules 中文排版。
若账号为 `dahao` 或 `wechat`，还须附：学术文献搜索结果摘要（至少查一次）、文末引用清单（哪怕是"未找到相关文献"）。

### 4.4 `publish <drafts 里的文件>` — 发布归档
Claude 做：
1. **不移动目录，仅改 frontmatter**：`status: published`、填 `publish_date`
2. 从 drafts/ **移动**文件到 published/ （同渠道内）
3. **强制反哺检查**（见下）

### 4.5 `publish` 的反哺检查（强制）

每次 publish 必问：

> 这篇文章里有没有新观点/洞察值得回写到 Areas 笔记？
> - 写的时候有没有"突然想通"的新论点？
> - 有没有数据点是这次查来的，值得沉淀？
> - 读者反馈（如果有）揭示了什么？

根据我回答：
- **无新东西** → 结束
- **补充现有 Areas** → 帮我更新
- **全新洞察** → 建议新笔记，等我 approve

### 4.6 `content-status` — 内容运营状态
跨三渠道报告：
- 各渠道最近 14 天发布、数据
- 草稿积压
- topic-pool 积压（超 30 天未动）
- 未被改写的高价值 Areas 笔记
- 小号爆款待改写大号版

### 4.7 跨渠道改写
- `repurpose [[xiaohao 某篇]] for dahao` → 从 xiaohao/published/ 某篇读内容，按大号调性改写，存到 dahao/drafts/，frontmatter 自动填 `repurposed_from`
- `repurpose [[xiaohao 某篇]] for wechat` → 同理，改写成长文

---

## 5. 溯源铁则

任何进入 drafts 或 published 的文章**必须**能回答：

> 这篇写的内容，我的原始笔记在哪？

- 基于某个 Areas 笔记写 → `source_notes` 填 `[[笔记]]`
- 基于 Raw 某篇研报 → `source_raw` 填 Raw 路径
- 临时灵感（`origin: scratch`）→ 可暂时空，但 publish 时必须补充或承认"纯个人经验"

**大号不允许空溯源发布**（商业化账号，数据支撑必须追得到）。

---

## 6. 引流网络维护

- **xiaohao 的 drives_to**：这是引流效果分析的核心字段。写小号时如果有配套大号文章，必填。
- **dahao/wechat 的 repurposed_from**：记录选题复用，用于"哪类小号爆款改写后仍然火"的分析。

---

## 7. 数据回填节奏

发布后：
- 24 小时：回填第一轮数据
- 7 天：回填稳定数据
- 30 天：最终数据

Claude 不主动改 published 的数据字段，除非我明确说"帮我更新 XXX 的数据为..."。

---

## 8. Content 层的 lint 重点

`lint` 在 Content 子目录下时特别关注：
- topic-pool/ 超过 30 天未动的选题（dropped 或 draft？）
- drafts/ 停留超 14 天的草稿（僵尸草稿）
- published/ 无 publish_date 的（发布流程有漏）
- 大号 published 中 source_notes 为空的（违反溯源铁则）

---

_v2 - 2026-04-21_
