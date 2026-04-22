# CHANGELOG

> 记录 vault 结构、CLAUDE.md 规则、关键工作流的演进历史。
> 这是给未来的我看的——3 个月后忘了"为什么当时这么改"时来这里查。
> 也是给 Claude 看的——它可以基于历史决策理解上下文。

格式：[类型] 简短描述 + 详细说明 + 受影响文件

类型说明：
- `STRUCTURE` - 目录结构变动
- `RULE` - CLAUDE.md 规则变动
- `WORKFLOW` - 工作流/指令变动
- `MIGRATION` - 历史内容迁移
- `EXPERIMENT` - 试验性变动（可能回滚）
- `REVERT` - 回滚某个之前的变动

---

## 2026-04-21

### [RULE] Content CLAUDE.md 群更新：大号字数上调 + 大号/公众号学术文献联网搜索

- **改动 1**：`xhs-dahao/CLAUDE.md` Section 3 写作结构字数从 300-500 字调整为 500-700 字；各小节区间同步放大（钩子 25-50→50-80，核心结论 50-80→80-120，论证数量 3→3-4 且每点 50-80→80-120，延伸思考 30-50→50-80）
- **改动 2**：`wechat/CLAUDE.md` Section 8"写作时"新增：联网搜索国内学术文献（知网、万方、金融研究、管理科学学报等）+ 引用格式规范；将原"数据来源"和新学术引用合并为"数据与文献来源"一块
- **改动 3**：`Content/CLAUDE.md` Section 4.3 `draft` 指令输出清单补充：dahao/wechat 草稿须附学术文献搜索摘要
- **理由**：大号定位是专业金融内容，300-500 字太短，难以呈现数据论证；公众号长文引用学术文献是严谨性信号，读者期待，与大号保持一致
- **影响文件**：`3-Areas/Content/xhs-dahao/CLAUDE.md`（v1→v2）、`3-Areas/Content/wechat/CLAUDE.md`（v1→v2）、`3-Areas/Content/CLAUDE.md`（v1→v2）

---

## 2026-04-16

### [RULE] CLAUDE.md v5.3 → v5.4：新增"何时更新本文档"小节
- **改动**：根 CLAUDE.md 第 10 节新增「本文档何时更新」「目录漂移自动提醒」「CHANGELOG 同步」三个子节
- **理由**：之前没说清楚什么时候改 CLAUDE.md，每次新建目录都要纠结。给出明确判断标准。
- **配套**：新建 `CHANGELOG.md`（本文件）
- **影响文件**：`CLAUDE.md`、`CHANGELOG.md`（新建）

### [RULE] CLAUDE.md v5.2 → v5.3：新增第 0 节"扫描与效率原则"
- **改动**：CLAUDE.md 最前面加了第 0 节，定义每条指令的扫描边界（status/lint/search/link 等）
- **理由**：跑 `status` 时 Claude 自动扫了全 vault（10+ 条 bash），太重。需要明确边界。
- **典型问题**：之前 status 会跑 `for dir in 3-Areas/*/; do find ...; done` 这种全量统计，应该用 Dataview 而不是 bash。
- **影响文件**：`CLAUDE.md`

---

## 模板：未来添加 changelog 时用

```markdown
## YYYY-MM-DD

### [TYPE] 简短描述
- **改动**：具体改了什么
- **理由**：为什么这么改（最重要，未来的自己会感谢你写了这个）
- **配套**：相关联的其他改动
- **影响文件**：列出修改的文件
- **回滚方法**（可选）：如果发现错了怎么撤回
```
