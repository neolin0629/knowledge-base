# Vault 仪表盘

> 位置建议：vault 根目录。
> 所有查询由 Dataview 动态渲染。
>
> ⚠️ **设计原则**：所有跨时间段的统计同时扫 `3-Areas/Content` 和 `6-Archive`，用 frontmatter 过滤。详见根 CLAUDE.md 2.5 节。

---

## 📊 一、内容运营（跨 Content + Archive）

### 1.1 近 30 天大号表现
```dataview
TABLE 
  views AS 曝光,
  likes AS 点赞,
  saves AS 收藏,
  round((likes + saves + comments) * 100 / views, 2) + "%" AS ER,
  round(saves * 100 / views, 2) + "%" AS 收藏率,
  category
FROM "3-Areas/Content" OR "6-Archive"
WHERE account = "dahao" AND status = "published" 
  AND views > 0 AND publish_date >= date(today) - dur(30 days)
SORT (likes + saves + comments) / views DESC
```

### 1.2 哪些笔记产出的内容最值钱（全时段）
```dataview
TABLE WITHOUT ID
  N AS 来源笔记,
  length(rows) AS 产出文章数,
  sum(rows.views) AS 总曝光,
  sum(rows.followers_gained) AS 总涨粉
FROM "3-Areas/Content" OR "6-Archive"
FLATTEN source_notes AS N
WHERE N AND status = "published" AND views > 0
GROUP BY N
SORT sum(rows.followers_gained) DESC
LIMIT 20
```

### 1.3 小号引流效率
```dataview
TABLE 
  drives_to AS 引流到,
  views AS 小号曝光,
  followers_gained AS 小号涨粉,
  publish_date AS 发布
FROM "3-Areas/Content" OR "6-Archive"
WHERE account = "xiaohao" AND status = "published" AND drives_to
SORT publish_date DESC
LIMIT 20
```

### 1.4 跨账号发布对比（近 90 天）
```dataview
TABLE WITHOUT ID
  account AS 账号,
  length(rows) AS 发文数,
  round(sum(rows.views) / length(rows), 0) AS 平均曝光,
  sum(rows.followers_gained) AS 总涨粉
FROM "3-Areas/Content" OR "6-Archive"
WHERE status = "published" AND publish_date >= date(today) - dur(90 days)
GROUP BY account
SORT sum(rows.followers_gained) DESC
```

### 1.5 Origin 对比（全时段）
```dataview
TABLE WITHOUT ID
  origin,
  length(rows) AS 篇数,
  round(sum(rows.views) / length(rows), 0) AS 平均曝光,
  round(sum(rows.likes + rows.saves + rows.comments) / sum(rows.views) * 100, 2) + "%" AS 平均ER
FROM "3-Areas/Content" OR "6-Archive"
WHERE origin AND status = "published" AND views > 0
GROUP BY origin
SORT sum(rows.views) / length(rows) DESC
```

### 1.6 草稿积压（超 14 天的僵尸草稿）
```dataview
LIST 
FROM "3-Areas/Content" OR "4-Projects"
WHERE status = "draft" AND created_date <= date(today) - dur(14 days)
SORT created_date ASC
```

### 1.7 Topic-Pool 积压（超 30 天未动）
```dataview
TABLE 
  target_account AS 目标账号,
  priority,
  estimated_value AS 预估价值,
  created
FROM "3-Areas/Content"
WHERE type = "topic" AND status != "dropped" AND created <= date(today) - dur(30 days)
SORT created ASC
```

### 1.8 小号爆款待改写（收藏 > 50 且未改写）
```dataview
TABLE views, saves, category, publish_date
FROM "3-Areas/Content" OR "6-Archive"
WHERE account = "xiaohao" AND status = "published" AND saves > 50
SORT saves DESC
LIMIT 10
```

### 1.9 Hook 类型效果（大号全时段）
```dataview
TABLE WITHOUT ID
  hook_type AS 钩子类型,
  length(rows) AS 使用次数,
  round(sum(rows.views) / length(rows), 0) AS 平均曝光,
  round(sum(rows.likes + rows.saves + rows.comments) / sum(rows.views) * 100, 2) + "%" AS 平均ER
FROM "3-Areas/Content" OR "6-Archive"
WHERE account = "dahao" AND status = "published" AND views > 0
GROUP BY hook_type
SORT sum(rows.views) / length(rows) DESC
```

### 1.10 年度产出总览
```dataview
TABLE WITHOUT ID
  account AS 账号,
  length(rows) AS 篇数,
  sum(rows.views) AS 总曝光,
  sum(rows.likes + rows.saves + rows.comments) AS 总互动,
  sum(rows.followers_gained) AS 总涨粉
FROM "3-Areas/Content" OR "6-Archive"
WHERE status = "published" AND publish_date >= date("2026-01-01")
GROUP BY account
```

---

## 📔 二、量化复盘

### 2.1 近 30 天复盘完成度
```dataview
TABLE WITHOUT ID
  date,
  type,
  market_regime AS Regime,
  pnl AS PnL
FROM "3-Areas/Investing/Journal"
WHERE type AND date >= date(today) - dur(30 days)
SORT date DESC
```

### 2.2 月度策略表现（历史 12 个月）
```dataview
TABLE date, pnl AS PnL, market_regime AS Regime
FROM "3-Areas/Investing/Journal/monthly"
SORT date DESC
LIMIT 12
```

### 2.3 新观察待反哺到 Areas
```dataview
TABLE WITHOUT ID
  file.link AS 复盘,
  new_observations AS 新观察
FROM "3-Areas/Investing/Journal"
WHERE length(new_observations) > 0 AND date >= date(today) - dur(14 days)
SORT date DESC
```

### 2.4 事件复盘清单（近 6 个月）
```dataview
TABLE date, market_regime AS Regime
FROM "3-Areas/Investing/Journal/event"
WHERE date >= date(today) - dur(180 days)
SORT date DESC
```

---

## 🚀 三、项目管理

### 3.1 Active 项目
```dataview
TABLE
  status,
  started AS 开始,
  deadline AS 截止,
  (deadline - date(today)).day AS 剩余天数
FROM "4-Projects"
WHERE type = "project" AND status = "active"
SORT deadline ASC
```

### 3.2 过期或卡住的项目（建议归档）
```dataview
TABLE status, started, deadline, file.mtime AS 最后修改
FROM "4-Projects"
WHERE type = "project" 
  AND (status = "active" OR status = "paused")
  AND (deadline < date(today) OR file.mtime < date(today) - dur(90 days))
SORT file.mtime ASC
```

---

## 📦 四、归档项目回顾

### 4.1 所有已归档项目
```dataview
TABLE
  archive_reason AS 归档原因,
  originally_started AS 起始,
  archived_at AS 归档于,
  (date(archived_at) - date(originally_started)).day AS 持续天数
FROM "6-Archive"
WHERE type = "project" AND status = "archived"
SORT archived_at DESC
```

### 4.2 按归档原因统计
```dataview
TABLE WITHOUT ID
  archive_reason AS 原因,
  length(rows) AS 项目数
FROM "6-Archive"
WHERE type = "project" AND status = "archived"
GROUP BY archive_reason
SORT length(rows) DESC
```

### 4.3 已归档系列的总产出
```dataview
TABLE WITHOUT ID
  file.folder AS 系列,
  length(rows) AS 篇数,
  sum(rows.views) AS 总曝光,
  sum(rows.likes + rows.saves + rows.comments) AS 总互动,
  sum(rows.followers_gained) AS 总涨粉
FROM "6-Archive"
WHERE account AND status = "published"
GROUP BY file.folder
SORT sum(rows.followers_gained) DESC
```

### 4.4 Dropped 项目回顾（避免重蹈覆辙）
```dataview
LIST
FROM "6-Archive"
WHERE type = "project" AND archive_reason = "dropped"
SORT archived_at DESC
```

---

## 📝 五、1-Notes 状态

### 5.1 近期 Notes
```dataview
TABLE created, tags, length(file.outlinks) AS 外链数
FROM "1-Notes"
WHERE created >= date(today) - dur(30 days)
SORT created DESC
```

### 5.2 ⭐ Notes 积压（超 60 天且无人引用，建议 promote 或归档）
```dataview
LIST
FROM "1-Notes"
WHERE created <= date(today) - dur(60 days)
  AND length(file.inlinks) = 0
SORT created ASC
LIMIT 20
```

### 5.3 热门 Notes（被引用多的，值得升级到 Area）
```dataview
TABLE 
  length(file.inlinks) AS 被引用,
  created,
  tags
FROM "1-Notes"
WHERE length(file.inlinks) >= 2
SORT length(file.inlinks) DESC
LIMIT 10
```
<!-- 被引用多说明是跨主题的"枢纽笔记"，这种其实更应该留在 1-Notes，或者考虑升级为 Area 的概念页 -->

### 5.4 跨主题 Notes（tags 含多个主题）
```dataview
TABLE tags, length(file.inlinks) AS 被引用
FROM "1-Notes"
WHERE length(tags) >= 2
SORT length(file.inlinks) DESC
```

---

## 🗂️ 六、仓库健康

### 6.1 0-Inbox 积压（超 15 篇预警）
```dataview
TABLE created AS 创建, tags
FROM "0-Inbox"
SORT created ASC
```

### 6.2 超 90 天未更新的 Areas（排除 Journal）
```dataview
LIST
FROM "3-Areas"
WHERE updated <= date(today) - dur(90 days) AND !contains(file.path, "Journal")
SORT updated ASC
LIMIT 15
```

### 6.3 最近新增笔记（全 vault）
```dataview
TABLE created, area, tags
FROM "1-Notes" OR "3-Areas" OR "0-Inbox"
WHERE created >= date(today) - dur(7 days) AND !contains(file.path, "Content")
SORT created DESC
```

### 6.4 孤立笔记（Areas 下没任何反向链接的）
```dataview
LIST
FROM "3-Areas"
WHERE length(file.inlinks) = 0 
  AND !contains(file.path, "Journal")
  AND !contains(file.path, "Content")
LIMIT 15
```

### 6.5 Archive 契约违规检查
> 正常此查询应返回空。有结果说明归档时违反了 2.5 契约
```dataview
LIST
FROM "6-Archive"
WHERE account AND status != "published" AND status != null
LIMIT 20
```

---

_dashboard v2.1 - 2026-04-16_
_v2.1 变更：新增第五部分「1-Notes 状态」（4 个查询）；第六部分加入 1-Notes 的跨 vault 统计。_
_v2.0 变更：所有 Content 查询跨 Archive；新增「归档项目回顾」部分。_
