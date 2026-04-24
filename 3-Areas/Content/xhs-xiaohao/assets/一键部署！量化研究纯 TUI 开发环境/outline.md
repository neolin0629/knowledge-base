---
type: flowchart
density: per-section
style: blueprint
image_count: 5
custom_palette: dark + purple
---

## Illustration 1
**Position**: After "我把工具按用途分了几类"
**Purpose**: Show the full tool ecosystem organized by category
**Visual Content**: Framework diagram — 6 tool categories radiating from central "TUI Quant Dev" node: Terminal (Ghostty+Zellij), Search (fzf+fd+rg+eza+zoxide), Data (DuckDB+pgcli), Files (yazi), Git (lazygit+delta), Python (uv)
**Filename**: 01-flowchart-tool-ecosystem.png

## Illustration 2
**Position**: After search tools section (after "rgf 搜内容直接跳到对应行")
**Purpose**: Visualize how the 5 search tools chain together
**Visual Content**: Flowchart — fd (find files) → fzf (fuzzy select) → action; rg (search content) → fzf → jump to line; zoxide (smart cd); eza (ls replacement). Show keyboard shortcuts: Ctrl+T, Alt+C, Ctrl+R
**Filename**: 02-flowchart-search-pipeline.png

## Illustration 3
**Position**: After data tools section (after "光标悬停 parquet 文件还能自动预览表格数据")
**Purpose**: Show the data inspection quick commands
**Visual Content**: Flowchart — .parquet/.csv file → pqs (schema) / pqh (preview) / csvh (CSV preview) → DuckDB CLI / pgcli. Show yazi preview integration
**Filename**: 03-flowchart-data-tools.png

## Illustration 4
**Position**: After "为什么全用终端？" section (after "终端是唯一选择")
**Purpose**: Compare terminal workflow vs GUI workflow for quant research
**Visual Content**: Comparison — Left: Terminal (composable pipes, remote SSH, keyboard-driven, unified config) vs Right: GUI (window switching, mouse clicking, separate apps, different configs per machine)
**Filename**: 04-flowchart-terminal-vs-gui.png

## Illustration 5
**Position**: After "主题统一" section (after "视觉上很整体")
**Purpose**: Show Catppuccin Macchiato unifying all tools
**Visual Content**: Framework — Central "Catppuccin Macchiato" theme node connecting to: Ghostty, starship, bat, lazygit, yazi, delta. Show the blue-gray base with accent colors
**Filename**: 05-flowchart-theme-unity.png
