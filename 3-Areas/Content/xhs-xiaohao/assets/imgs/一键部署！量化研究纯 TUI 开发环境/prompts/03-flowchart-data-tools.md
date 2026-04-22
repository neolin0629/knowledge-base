---
illustration_id: 03
type: flowchart
style: blueprint
---

Data Inspection Workflow - Quick Commands

Layout: left-to-right flowchart with parallel paths

STEPS:
1. "数据文件" (Data Files) — Starting node with file icons
2. Branch into file types:
   - ".parquet" file → "pqs" (查看 Schema) → schema output display
   - ".parquet" file → "pqh" (预览前 20 行) → table preview display
   - ".csv" file → "csvh" (预览 CSV) → table preview display
3. All paths can feed into → "DuckDB CLI" (交互式查询)
4. Auxiliary path: "yazi 文件管理器" → hover on .parquet → "自动预览表格数据"
5. Side node: "pgcli" (PostgreSQL 交互)

CONNECTIONS: Straight arrows from file types through commands to output. Dashed line from yazi showing the preview integration. DuckDB as a larger destination node.

LABELS: Command names as monospace code badges: pqs, pqh, csvh. File extensions: .parquet, .csv. Chinese descriptions for each action. "前 20 行" as specific data point.

COLORS:
- Background: Deep purple-black (#0F0A1A)
- Grid overlay: Faint purple grid lines (#1A1030, opacity 0.3)
- File nodes: Deep violet (#6D28D9)
- Command badges: Electric purple (#8B5CF6) with monospace text
- Output displays: Dark navy (#1E1B4B) with cyan (#06B6D4) borders showing mini table grids
- DuckDB node: Amber (#F59E0B) accent (duck icon)
- yazi path: Muted lavender (#A78BFA), dashed connection
- Arrows: Cyan (#06B6D4)
- Text: Pure white (#FFFFFF)

STYLE: Dark blueprint technical schematic. Precise geometric shapes with grid alignment. 90-degree connections. Mini table/grid representations inside output nodes to suggest data. Engineering drawing quality on dark background. Clean composition with generous spacing.

ASPECT: 3:4
