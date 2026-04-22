---
account: xiaohao
type: image-text
status: published
category: 软件
hook_type: 干货清单
origin: from-notes
source_notes: []
created_date: 2026-04-08
publish_date: 2026-04-09
views: 194
followers_gained: 0
likes: 6
comments: 8
saves: 13
shares: 1
---
## 导语

一直有人问我，现在量化研究用的是什么样的开发环境？如何做才能兼顾性能与效率？

 然后我正好年初换了台新 Mac，之前 Ubuntu 服务器上那套环境要重新搭一遍，光是一个个装软件、调配置、对齐两台机器的体验，就搞得我很烦躁。装到一半想——能不能写个脚本，以后不管换什么机器，一行命令全搞定？

于是就有了这套方案。先说结论：最终我把所有东西收敛成了 **两个脚本文件**

* `install.sh` 负责装软件，macOS 和 Ubuntu 通用，自动检测系统走不同分支。 
* `configs.sh` 负责生成所有配置文件，已有的不会覆盖，幂等可重复跑。

##

放同一个目录下，`chmod +x` 之后一行命令：

```zsh
./install.sh
```

![[tui_setup_0.png]]

##

然后去泡杯咖啡，回来就全好了。

![[tui_setup_1.png]]
## 装了哪些东西？

我把工具按用途分了几类，

### 终端和分屏

Ghostty 做终端，Zellij 做分屏管理。我写了一个 quant 专用布局——左边 65% 是主工作区（跑 Claude Code 或者写代码），右边上下分成运行日志和临时 shell，底部 20% 是系统监控。定义了一个 alias `zq` 命令快捷启动。

### 搜索全家桶

fzf（模糊搜索）+ fd（找文件）+ ripgrep（搜内容）+ eza（看目录）+ zoxide（智能跳转）。这五个配合起来基本取代了 find、grep、ls、cd。

##

我配了很多快捷键——Ctrl+T 搜文件、Alt+C 跳目录、Ctrl+R 搜历史命令，还有两个自定义函数：`fe` 选文件直接打开，`rgf` 搜内容直接跳到对应行。

### 数据工具

DuckDB CLI + pgcli。在 yazi 文件管理器里，光标悬停 parquet 文件自动预览表格数据。
`pqs file.parquet`  看 schema。
`pqh file.parquet` 看前 20 行。
`csvh trades.csv` 看 CSV。

### 文件管理

yazi 是个终端文件管理器，我装了 duckdb 插件、glow 插件、git 插件。选中文件 y 复制 p 粘贴。搜索用 fzf 和 rg 联动，体验很顺滑。

##

**Git** lazygit + delta。lazygit 用 Space 暂存、c 提交、p 拉取、P 推送，还能逐行 stage（部分提交）。delta 给 diff 加了语法高亮和并排对比。

**Python 环境** uv，Rust 写的包管理器，`uv add polars` 加依赖，`uv run backtest.py` 跑脚本，不用手动管虚拟环境。

![[tui_effect_0.png]]

## 为什么全用终端？

不是为了装 x（好吧，有一点点🤓）。

主要原因是 ai 的 cli 辅助编程越来越好用了，且做量化研究的工作流天然适合终端——写代码、跑回测、查数据、看日志、Git 管理，这些全是文本操作。用 GUI 反而要在不同窗口之间 切换，鼠标点来点去。

终端里所有东西都可以组合：fd 找文件 → 管道传给 fzf 选择 → 传给 duckdb 查数据。这种组合的灵活度是 GUI 做不到的。

而且远程连服务器的时候，终端是唯一选择。我 Mac 和 Ubuntu 服务器用同一套配置，体验完全一致。

## 主题统一

所有工具的主题都统一用了 Catppuccin Macchiato——一套很舒服的深色配色，不是纯黑，是带一点蓝调的深灰底色。终端、提示符、bat、lazygit、yazi、delta 全部统一，视觉上很整体。

###  starship 提示符

starship 配置的最终效果是一行 powerline 风格的提示符，从左到右依次显示：OS 图标 → 用户名 → 路径 → Git 分支和状态 → 当前语言版本 → 时间 → 上条命令耗时。

内置了 Catppuccin 四套色板（Latte / Frappé / Macchiato / Mocha），改一行配置就能切换明暗主题。

## 速查手册

我把速查卡和完整手册也写好了，两个 markdown 文件，分别是日常高频操作的一页速查和所有工具的详细说明。终端里 `glow -p quant-env-cheatsheet.md` 就能随时翻。

这套方案我自己在 Mac 和 Ubuntu 上都跑通了，如果你也做量化、也折腾终端，可以直接拿去用。有问题欢迎评论区讨论👇。

如果你需要一键安装的脚本和速查手册，也可以在评论区留言。✍🏼

---

![[tui_cheatsheet_0.png]]

---

![[tui_cheatsheet_1.png]]