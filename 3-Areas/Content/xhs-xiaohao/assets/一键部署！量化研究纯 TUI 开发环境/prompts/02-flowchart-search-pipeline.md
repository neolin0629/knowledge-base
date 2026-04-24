---
illustration_id: 02
type: flowchart
style: blueprint
---

Search Tool Pipeline - Process Flow

Layout: top-down flowchart with branching paths

STEPS:
1. "输入" (Input) — Starting point: user types a query or shortcut
2. Branch A — "Ctrl+T" → fd (找文件) → fzf (模糊匹配) → "打开文件"
3. Branch B — "Alt+C" → zoxide (智能跳转) → "进入目录"
4. Branch C — "Ctrl+R" → fzf (搜历史命令) → "执行命令"
5. Branch D — "rgf" → ripgrep (搜内容) → fzf (选择结果) → "跳到对应行"
6. Auxiliary — eza: "替代 ls，彩色显示目录"

CONNECTIONS: Thick arrows connecting each step. Decision diamond at "输入" branching into 4 paths. Each path flows downward. Final actions in rounded terminal boxes.

LABELS: Keyboard shortcuts (Ctrl+T, Alt+C, Ctrl+R) displayed as key-cap badges. Tool names: fd, fzf, ripgrep, zoxide, eza. Function descriptions in Chinese.

COLORS:
- Background: Deep purple-black (#0F0A1A)
- Grid overlay: Faint purple grid lines (#1A1030, opacity 0.3)
- Step containers: Deep violet (#6D28D9) with thin purple border
- Decision diamond: Electric purple (#8B5CF6)
- Arrows: Cyan (#06B6D4)
- Key-cap badges: Amber (#F59E0B) background with dark text
- Terminal (end) boxes: Magenta-purple (#A855F7)
- Text: Pure white (#FFFFFF)
- Auxiliary note: Muted lavender (#A78BFA)

STYLE: Dark blueprint technical schematic. Precise geometric shapes, straight and 90-degree angle connections only. Grid-aligned. Engineering drawing quality on dark background. Subtle grid overlay. Clean composition with generous spacing. No decorative flourishes.

ASPECT: 3:4
