---
illustration_id: 03
type: flowchart
style: editorial
palette: warm
---

最小量化闭环 — 流程图

Flat vector flowchart with bold arrows and geometric step containers. Editorial style — clear, professional, warm.
PALETTE OVERRIDE (warm): Warm-only color palette, no cool colors.

STEPS (top → bottom, 垂直流程):
1. 原始数据 — 工具: Tushare / AkShare，标注"免费中国市场数据"
2. 信号生成 — 你的条件清单 → Python 判断，标注"从阶段一的条件清单来"
3. 回测 — 工具: vectorbt，标注"比backtrader简单"
4. 统计验证 — 多重比较校正 + Alpha回归，工具: statsmodels，标注"防过拟合"
5. 模拟盘 — 标注"不是实盘，至少跑3个月"
6. 实盘（小仓位）— 标注"从小开始"

CONNECTIONS: 粗箭头连接每一步，箭头旁可加简短注释。步骤4到步骤3有一条反馈箭头，标注"不通过则回退修改"
COLORS: Soft Peach background (#FFECD2), steps alternate between Warm Orange (#ED8936) and Golden Yellow (#F6AD55) containers, Terracotta (#C05621) for arrows and connectors, Deep Brown (#744210) for text and outlines
ELEMENTS: Rounded rectangles for steps, thick downward arrows between steps, small tool icons (database, code, chart, checkmark, monitor, coin), feedback loop arrow on the side

Clean composition with generous white space. Simple or no background. Main elements centered or positioned by content needs.
Color values (#hex) and color names are rendering guidance only — do NOT display color names, hex codes, or palette labels as visible text in the image.
Text should be large and prominent with handwritten-style fonts. Keep minimal, focus on keywords. All text in Chinese.

ASPECT: 9:16 (vertical flowchart, 适合公众号长图)
