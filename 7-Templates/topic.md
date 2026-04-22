<%*
const today = tp.date.now("YYYY-MM-DD");
const account = await tp.system.suggester(
  ["大号", "小号", "公众号"],
  ["dahao", "xiaohao", "wechat"]
);
const priority = await tp.system.suggester(["高", "中", "低"], ["high", "medium", "low"]);
-%>
---
type: topic
status: idea
priority: <% priority %>
source_notes: []
source_raw: []
source_inspiration: 
target_account: <% account %>
target_hook: 
estimated_value: 
created: <% today %>

---

# <% tp.file.title %>

## 一句话说清楚想写什么


## 核心观点（如果已成形）


## 需要补充的素材
- [ ] 
- [ ] 

## 相关 Areas 笔记


## 相关 Raw 资料

