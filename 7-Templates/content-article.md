<%*
const today = tp.date.now("YYYY-MM-DD");
const account = await tp.system.suggester(
  ["大号 搞钱最重要", "小号 11点半收盘吃饭", "公众号 11点半收盘吃饭"],
  ["dahao", "xiaohao", "wechat"]
);
const typeOptions = account === "wechat" ? ["longform"] : ["image-text", "video"];
const type = await tp.system.suggester(typeOptions, typeOptions);
const categoryOptions = account === "xiaohao"
  ? ["量化", "宏观", "商品", "AI投资", "方法论", "生活随笔", "交易日记", "避坑", "人设", "软件"]
  : ["量化", "宏观", "商品", "AI投资", "方法论", "市场结构", "深度思考", "季度复盘", "事件复盘", "系统工程"];
const category = await tp.system.suggester(categoryOptions, categoryOptions);
const hookOptions = account === "xiaohao"
  ? ["人设", "故事", "金句", "反常识", "数据冲击", "干货清单"]
  : ["数据冲击", "反常识", "金句", "故事", "干货清单"];
const hook = await tp.system.suggester(hookOptions, hookOptions);
const origin = await tp.system.suggester(
  ["从 topic-pool 来", "基于笔记", "临时灵感", "旧内容改写"],
  ["from-topic-pool", "from-notes", "scratch", "repurposed"]
);
-%>
---
account: <% account %>
type: <% type %>
status: draft

category: <% category %>
hook_type: <% hook %>
origin: <% origin %>

source_topic: 
source_notes: []
source_raw: []

drives_to: 
repurposed_from: 

created_date: <% today %>
publish_date: 

views: 0
likes: 0
saves: 0
comments: 0
shares: 0
followers_gained: 0

---

# <% tp.file.title %>

## 钩子


## 主体


## 结尾


---

## 发布备忘
- 标题候选：
  1. 
  2. 
  3. 
- 配图思路：
- 预估字数：
- 发布时机：
