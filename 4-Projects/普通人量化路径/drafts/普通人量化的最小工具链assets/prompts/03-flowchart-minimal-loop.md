---
illustration_id: 03
type: flowchart
style: minimal-flat
palette: tech-blue
aspect: "9:16"
position: 6 步代码块之后
filename: 03-flowchart-minimal-loop.png
---

Tall portrait vertical flowchart for "完整闭环". 6 steps connected by downward arrows. The 9:16 tall portrait ratio gives each step generous height and makes the top-to-bottom flow natural and readable.

LAYOUT: White background. Header at top, 6 step nodes in a centered column with arrows between them, small footer at bottom. Generous white margins on left and right.

ZONES:

- HEADER ZONE (top 8%): Bold centered text "完整闭环" in dark slate (#0F172A). Medium-large font. Thin horizontal divider line below (#E2E8F0).

- FLOW ZONE (center 84%): 6 step nodes stacked vertically in a centered column (column width ~70% of canvas). Between each node, a downward arrow.

  NODE STRUCTURE (each of 6):
  - Shape: Rounded rectangle (border-radius ~8px), light border (#E2E8F0), white or very light gray bg (#F8FAFC)
  - Left side: A filled circle with the step number (① ② ③ ④ ⑤ ⑥). Circle fill: steel blue (#2563EB). Number text: white. Circle size: matches row height.
  - Right side of circle: Two text lines inside the node
    - Line 1 (step name): Bold, dark slate (#0F172A), medium font
    - Line 2 (tool/annotation): Monospace font, slate-gray (#64748B), smaller font
  
  STEP 1: ① 原始数据 / Tushare / AkShare
  STEP 2: ② 信号生成 / 条件清单 → Python
  STEP 3: ③ 回测 / vectorbt
  STEP 4: ④ 统计验证 / 多重比较校正 + Alpha 回归
  STEP 5: ⑤ 模拟盘 / 至少 3 个月再上实盘
  STEP 6: ⑥ 实盘 / 小仓位

  ARROWS: Between each consecutive node, a centered downward-pointing arrow. Thin stroke, steel blue (#2563EB), clean arrowhead.

- FOOTER ZONE (bottom 8%): Small centered text "适合普通人的量化路径 · 第 3 篇" in light gray (#94A3B8).

LABELS:
- Header: 完整闭环
- Step 1: 原始数据 | Tushare / AkShare
- Step 2: 信号生成 | 条件清单 → Python
- Step 3: 回测 | vectorbt
- Step 4: 统计验证 | 多重比较校正 + Alpha 回归
- Step 5: 模拟盘 | 至少 3 个月再上实盘
- Step 6: 实盘 | 小仓位
- Footer: 适合普通人的量化路径 · 第 3 篇

COLORS:
- Background: #FFFFFF
- Header text: #0F172A
- Header divider: #E2E8F0
- Step node bg: #F8FAFC
- Step node border: #E2E8F0
- Step number circle: #2563EB fill, #FFFFFF text
- Step name: #0F172A bold
- Tool label: #64748B monospace
- Arrow: #2563EB
- Footer: #94A3B8

STYLE: Minimal flat flowchart. Each step is a clean rounded rectangle. Number circles prominently on the left of each box. Straight thin arrows between boxes — no curves, no bends. Plenty of vertical whitespace between steps. No decorative elements. The focus is on the 6-step sequence and readability on mobile.

ASPECT: 9:16 tall portrait. Six vertical steps need height to be legible and well-spaced.
