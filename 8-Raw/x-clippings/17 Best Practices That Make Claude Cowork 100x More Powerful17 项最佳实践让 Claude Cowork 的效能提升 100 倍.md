---
title: "17 Best Practices That Make Claude Cowork 100x More Powerful17 项最佳实践让 Claude Cowork 的效能提升 100 倍"
source: "https://x.com/heynavtoor/article/2028148844891152554"
author:
  - "[[Nav Toor (@heynavtoor)]]"
published: 2026-03-02
created: 2026-04-02
description:
tags:
  - "ai-workflow"
  - "to-process"
---
I’ve been using Claude Cowork since January 12, the day it launched.我从 1 月 12 日 Claude Cowork 上线那天就开始使用它了。

In seven weeks, I’ve run over 400 Cowork sessions. I’ve tested every plugin, every connector, every slash command. I’ve broken it in ways Anthropic probably hasn’t seen. And I’ve figured out the exact practices that separate people who think Cowork is “kind of cool” from people who’ve replaced half their software stack with it.七周内，我运行了超过 400 场 Cowork 会话。我测试了每一个插件、每一个连接器、每一个斜杠命令。我甚至以 Anthropic 可能都没见过的方式破坏了它。而且，我已经弄清楚了究竟是什么让那些觉得 Cowork “还不错”的人和那些用它替换了半数软件的人区分开来。

The gap is enormous. And it has nothing to do with prompting skill.差距巨大。而且这与提示技巧无关。

It’s about setup. Structure. And seventeen specific practices that most users will never discover on their own because Anthropic doesn’t document them.它关乎设置、结构，以及十七项具体的实践，而大多数用户永远不会自己发现这些实践，因为 Anthropic 没有将它们记录下来。

I tested each one. Measured the difference. Here’s the complete list — ranked by impact.我逐一测试了它们，并测量了差异。以下是完整列表——按影响程度排名。

# Part 1: Context architecture (practices 1–5)第一部分：情境架构（实践 1-5）

These five practices alone will transform your Cowork experience. Everything else builds on this foundation.仅这五项实践就能彻底改变你的联合办公体验。其他一切都建立在这个基础之上。

## 1\. Build a \_MANIFEST.md for every working folder1. 为每个工作文件夹创建一个 \_MANIFEST.md 文件

This is the single highest-impact practice nobody talks about.这是影响最大的实践之一，但却鲜为人知。

Here’s the problem. When you point Cowork at a folder, Claude reads everything. Every file. Every subfolder. Every outdated draft and superseded version. A developer on DEV Community documented this after a 462-file consulting folder started producing contradictory output — Claude was pulling context from pricing models that had been replaced three months earlier.问题在于，当您使用 Cowork 指向某个文件夹时，Claude 会读取所有内容。包括每个文件、每个子文件夹，以及所有过时的草稿和已被取代的版本。一位开发者在 DEV 社区记录了这个问题：一个包含 462 个文件的咨询文件夹开始产生自相矛盾的输出——Claude 竟然从三个月前就已经被替换的定价模型中提取上下文信息。

The fix: a \_MANIFEST.md file you drop into any working folder. It tells Claude which documents are the source of truth, which subfolders map to which domains, and what to skip entirely.解决方法：在任意工作文件夹中放置一个 \_MANIFEST.md 文件。该文件会告诉 Claude 哪些文档是权威来源，哪些子文件夹映射到哪些域，以及哪些内容需要完全跳过。

Structure it in three tiers:将其结构分为三个层级：

Tier 1 (Canonical): The source-of-truth documents Claude must read first. Your brand guidelines. Your project brief. Your current strategy document.第一层级（权威文档）：克劳德必须首先阅读的权威文档。您的品牌指南。您的项目简报。您当前的战略文档。

Tier 2 (Domain): Subfolders mapped to specific topics. Claude only loads these when the task touches that domain. “/pricing → pricing models and rate cards” or “/research → competitor analysis.”第二层级（领域）：映射到特定主题的子文件夹。Claude 仅在任务涉及该领域时才会加载这些子文件夹。“/pricing → 定价模型和价目表”或“/research → 竞争对手分析”。

Tier 3 (Archival): Old drafts, superseded versions, reference material. Claude ignores these unless you explicitly ask.第三层级（存档）：旧草稿、已取代版本、参考资料。除非你明确要求，否则克劳德不会理会这些内容。

The underscore prefix keeps it sorted to the top of your folder. Takes five minutes to fill out. Saves hours of confused output. For folders under ten files, you don’t need one. For anything bigger and especially project folders that accumulate files over weeks this is non-negotiable.下划线前缀能确保文件名始终显示在文件夹顶部。填写只需五分钟，却能节省数小时混乱的输出时间。对于少于十个文件的文件夹，无需添加下划线。但对于更大的文件夹，尤其是那些会持续数周积累文件的项目文件夹，添加下划线前缀是必不可少的。

## 2\. Use Global Instructions as your permanent operating system2. 使用 Global Instructions 作为您的永久操作系统

Settings → Cowork → Edit next to Global Instructions.设置 → 协同办公 → 在“全局指令”旁边进行编辑。

Most people leave this blank. That’s like buying a car and never adjusting the mirrors.大多数人都会把这一项留空。这就像买了辆车却从来不调整后视镜一样。

Global Instructions load before everything else before your files, before your prompt, before Claude even looks at your folder. They’re the baseline behavior that applies to every single session.全局指令会在所有其他操作之前加载，甚至在你的文件、提示符甚至 Claude 查看你的文件夹之前就已经加载完毕。它们是适用于每个会话的基本行为。

Mine says: “I’m \[name\], a \[role\]. Before starting any task, look for \_MANIFEST.md and read Tier 1 files first. Always ask clarifying questions before executing. Show a brief plan before taking action. Default output format: .docx. Never use filler language. Never pad outputs. Quality bar: every deliverable should be client-ready without editing. If confidence is low, say so.”

This means even my laziest, most rushed prompt still produces calibrated output. Claude always knows who I am. Always reads the right files first. Always asks before

guessing. The Global Instructions handle the baseline. Your prompt just handles the task.

## 3\. Create three persistent context files

I covered this in depth in my previous article, but it’s too important not to repeat here.

Create a folder called “Claude Context” (or “00\_Context” so it sorts first). Add three files:

about-me.md Your professional identity. Not your resume. What you actually do, who you serve, what your current priorities are, and one or two examples of your best work.

brand-voice.md — Your communication style. Tone descriptors, words you use, words you never use, formatting preferences, and two to three paragraphs of your actual writing as reference.

working-style.md How Claude should behave. Collaboration rules, output format defaults, quality standards, and a list of things to avoid.

These three files eliminate the “generic AI output” problem overnight. Without them, every session starts cold. With them, Claude starts every session already knowing your voice, your standards, and your preferences.

The key insight most people miss: these files compound. Refine them weekly. Every time Claude produces something you don’t like, ask yourself whether it’s a prompt problem or a context problem. Nine times out of ten, it’s context. Add one line to one file. Permanent fix.

## 4\. Use Folder Instructions for project-specific context

Global Instructions are the same for every session. Folder Instructions are specific to whatever folder you’re working in.

When you select a folder in Cowork, Claude can read and update Folder Instructions automatically. But you can also set them manually. This is where you put project-specific rules: client name, project goals, specific terminology, deliverable formats, review deadlines.

The layering matters. Global Instructions set universal behavior. Folder Instructions add project context. Your prompt specifies the task. Three layers, each one more specific than the last. This is how you go from “generic AI” to “this sounds like it came from someone who’s been on my team for six months.”

## 5\. Never let Claude read everything scope your context deliberately

This is the practice that separates power users from everyone else.

Claude’s context window is enormous over a million tokens on Opus 4.6. But bigger context doesn’t mean better output. In fact, the opposite is often true. The more irrelevant files Claude reads, the more noise enters its reasoning, and the worse your output gets.

Tell Claude what to read. In your Global Instructions, add: “When starting any task, look for \_MANIFEST.md first. Load Tier 1 files. Only load Tier 2 files when the task explicitly touches that domain. Never load Tier 3 files unless I specifically ask.”

If you’re using subagents, scope them even tighter: “When decomposing tasks into subagents, give each subagent only the minimum context it needs for its specific subtask.”

Deliberate context management is the single biggest differentiator between Cowork users who get inconsistent results and Cowork users who get reliable, high-quality output every time.

# Part 2: Task design (practices 6–10)

How you frame a task determines whether Cowork delivers a finished product or an expensive rough draft.

## 6\. Define the end state, not the process

This is the mindset shift that changes everything. Cowork isn’t a chatbot. It’s a coworker. You don’t tell a coworker how to do their job step by step. You tell them what “done” looks like.

Bad prompt: “Help me with my files.”

Good prompt: “Organize all files in this folder into subfolders by client name. Use the format YYYY-MM-DD-descriptive-name for all filenames. Create a summary log documenting every change. Don’t delete anything. If a file could belong to multiple clients, put it in /needs-review.”

The second prompt defines the end state (organized folders), the naming convention, the output artifact (summary log), the safety constraint (no deletion), and the uncertainty protocol (needs-review folder). Claude can now execute autonomously and you can walk away.

Every task prompt should answer three questions: What does “done” look like? What are the constraints? What should Claude do when it’s uncertain?

## 7\. Always request a plan before execution

Add this to your Global Instructions: “Show a brief plan before taking action on any task. Wait for my approval before executing.”

This single line prevents 90% of Cowork disasters. Without it, Claude reads your prompt and immediately starts executing. Sometimes it’s exactly right. Sometimes it misinterprets one word and reorganizes three months of files in the wrong direction.

With the plan step, you get a 30-second review window. “I’m going to create these six subfolders, move these files, rename them using this convention, and save a log here. Proceed?” You scan it. It looks right. You approve. Claude executes.

The cost: an extra 30 seconds per task. The benefit: you never have to undo a 20-minute autonomous mistake.

## 8\. Tell Claude what to do with uncertainty

This is the most underrated practice in the entire list.

Most people give Claude clear instructions for the happy path but say nothing about edge cases. What happens when a receipt image is blurry? When a file could belong to two categories? When a data source is incomplete?

Claude will guess. And Claude’s guesses are often wrong not because it’s stupid, but because it doesn’t know your preferences for ambiguous situations.

Build uncertainty handling into every task: “If a date isn’t clear, mark it as VERIFY. If a file could go in multiple folders, put it in /needs-review. If you’re less than 80% confident in a classification, flag it instead of guessing.”

This transforms Cowork from a tool that sometimes produces errors into a tool that tells you exactly where it needs your judgment. That’s a fundamentally different value proposition.

## 9\. Batch related work into single sessions

Every Cowork session has startup cost. Claude reads your files, loads your context, processes your folder structure. That’s compute you’re paying for.

Don’t run five separate sessions for five related tasks. Run one session: “I need to process this month’s expense receipts, update the budget spreadsheet, generate a summary report, draft an email to finance, and save everything to /monthly-reports/february.”

Claude plans all five tasks, shares context across them (the receipt data feeds into the budget which feeds into the report which feeds into the email), and produces five connected deliverables in one run. Faster. Cheaper. Higher quality because the context from each task informs the next.

If you’re hitting usage limits, this is usually the fix. Fewer sessions with more tasks per session is almost always better than many sessions with one task each.

## 10\. Use subagents deliberately by asking for parallel processing

Cowork’s most powerful feature is one most users never trigger.

When you give Cowork a task with independent parts, it can spin up multiple subagents to work on them simultaneously. Each subagent gets fresh context, tackles its piece, and hands results back to the main agent for synthesis.

How to trigger it: include “Spin up subagents to...” or “Work on these in parallel using subagents” in your prompt.

Example: “I’m evaluating four vendors. Spin up subagents to research each one’s pricing, support reputation, and integration options. Give me a comparison table.” Instead of researching sequentially vendor A, then B, then C, then D Cowork launches four parallel agents. The task that used to take 40 minutes takes 10.

Use it for: competitive analysis, multi-source research, processing batches of files, evaluating options from different angles (financial, operational, customer experience), and any task where subtasks don’t depend on each other.

Caveat: subagents work best on Opus 4.6 and consume more tokens. Use them for complex tasks where the time savings justify the cost. Don’t use them to organize your Downloads folder.

# Part 3: Automation and scheduling (practices 11–13)

This is where Cowork goes from productivity tool to autonomous system.

## 11\. Schedule recurring tasks with /schedule

Type /schedule in any Cowork task. Claude walks you through setting up a task that runs automatically daily, weekly, monthly, or on demand.

The best scheduled tasks I’ve set up:

Monday morning briefing: “Every Monday at 7 AM, check my Slack channels and calendar for the week. Summarize what’s coming up, flag anything that needs prep, and save a briefing to /weekly-briefings.”

Friday status report: “Every Friday at 4 PM, pull my completed tasks from Asana, summarize what I shipped this week, draft a status update, and save to /reports.”

Daily competitor tracking: “Every day at 9 AM, research \[competitor names\] for news, product updates, or pricing changes. Save a summary only if there’s something new.”

Critical limitation: scheduled tasks only run when your computer is awake and Claude Desktop is open. If your machine is asleep when a task is due, Cowork catches up when you’re back and notifies you. Plan around this.

## 12\. Build once, run weekly externalize everything to files

Cowork has no memory between sessions. This is simultaneously its biggest limitation and its greatest design feature.

No memory means no context bleed. No hallucinated recollections from three weeks ago. Every session starts clean. But it also means you can’t rely on “Claude remembers how I like this done.”

The solution: externalize everything to files. Your preferences live in context files. Your project plans live in markdown documents. Your standard operating procedures live in skill files. Your decisions and outcomes live in log files.

One power user documented building a weekly review system: 1,500+ lines across five specialized subagent instructions. Built once. Runs weekly. Claude reads the instructions, spins up five parallel agents, each with scoped permissions and defined outputs, and produces a complete weekly review without any new input.

If you want continuity, you have to build it into files. But the upside is massive: a well-documented workflow is portable, shareable, and version-controlled. It doesn’t live in one AI’s memory. It lives in your system.

## 13\. Use the /schedule + connectors combo for real automation

Scheduled tasks become genuinely powerful when combined with connectors.

Connect Gmail, Slack, Google Drive, Notion, Asana, or any of the 50+ available integrations. Then schedule tasks that pull live data:

“Every Monday, pull all unread Slack messages from [#product](https://x.com/search?q=%23product&src=hashtag_click)\-feedback, categorize them by theme, and create a summary in Google Drive.”“每周一，将所有未读的 Slack 消息从 [＃产品](https://x.com/search?q=%23product&src=hashtag_click) \-收集反馈意见，按主题分类，并在 Google 云端硬盘中创建摘要。”

“Every morning, check my Gmail for invoices, extract amounts and dates, and update the expenses spreadsheet in my local /finance folder.”

This is where Cowork stops being a task executor and starts being an autonomous system. The scheduled task runs. The connector pulls live data. Claude processes it. The output appears in your folder or your connected tool. You review when you’re ready.

Settings → Connectors → Browse connectors to see what’s available. Start with Slack and Gmail. Those two alone will save you hours per week.

# Part 4: Plugins and skills (practices 14–16)

Plugins are Cowork’s modular brain. Skills are its playbook. Most users install one plugin and never look back. That’s leaving 80% of the value on the table.

## 14\. Stack plugins for compound capability

Each plugin is a bundle of skills, slash commands, and subagent configurations designed for a specific domain Sales, Legal, Finance, Product Management, Data Analysis, and so on.

But here’s what most people miss: plugins are composable. You can install multiple plugins and use capabilities from all of them in a single task.

Example: Install the Data Analysis plugin and the Sales plugin. Then: “Analyze our Q1 pipeline data (use Data Analysis), identify the three weakest deals, and draft personalized follow-up emails for each (use Sales).” Claude uses capabilities from both plugins in one workflow.

My current stack: Productivity (always on), Data Analysis (always on), Sales (for outreach weeks), and Marketing (for content weeks). Rotate the last two based on what I’m focused on.

Start with the tier list I published install the S-tier and A-tier plugins that match your role. Then experiment with combinations.

## 15\. Build custom skills for your specific workflows

A skill is a markdown file that teaches Claude how to approach a specific, repeatable task. Plugins bundle many skills. But you can also create your own.

Structure of a custom skill file:

\# \[Skill Name\]

\## Purpose: What this skill does.

\## Inputs: What information Claude needs.

\## Process: Step-by-step instructions.

\## Output: What the finished deliverable looks like.

\## Constraints: Rules and guardrails.

Example: I created a “Weekly Article Drafting” skill. Purpose: Draft a 2,000-word article from a topic and outline. Inputs: topic, outline, target audience, key evidence. Process: research using web search, draft sections, match brand-voice.md, generate VISUAL SUGGESTIONS and QUOTABLE LINES. Output: .docx file in /articles/drafts. Constraints: no AI semantic language, no filler phrases, minimum 8 evidence points.

Now I say “Run my article drafting skill on \[topic\]” and get a publication-ready draft. The skill encodes everything I’d normally spend 20 minutes explaining in a prompt.

Save custom skills as .md files in your working folder or upload them through the Customize menu. Claude reads them at the start of every relevant session.

## 16\. Use the Plugin Management plugin to build plugins conversationally

This is the most meta feature in Cowork and the most underused.

Install the Plugin Management plugin. Then say: “Help me create a plugin for \[your workflow\].” Claude walks you through defining skills, slash commands, and

configuration conversationally. No code. No GitHub. No markdown syntax you need to learn.

You describe what you want. Claude builds the plugin. You test it. You refine it. In under an hour, you have a custom plugin that codifies your specific workflow, your specific standards, and your specific terminology.

For teams, this is transformative. One person builds a plugin for your team’s standard processes. Everyone installs it. Suddenly the whole team produces consistent, on-brand, process-compliant output because the standards live in the plugin, not in individual memory.

Enterprise teams: Anthropic launched a private plugin marketplace in February. Admins can create, curate, and distribute custom plugins across the organization. Build once. Deploy to hundreds.

# Part 5: Safety and efficiency (practice 17)

## 17\. Treat Cowork like a powerful employee, not a toy

Cowork has real file system access. It can create, move, rename, and with your permission delete files on your actual computer. It can browse the web. It can interact with connected tools. It can run for hours unsupervised.

That power demands respect. Here are the non-negotiable safety practices:

Back up before experimenting. Especially with file organization tasks. Cowork gets it right most of the time. “Most of the time” isn’t good enough for your client contracts.

Keep sensitive files in separate folders. Financial documents, passwords, personal information put them in folders Cowork never touches. Don’t grant access to your entire Documents directory. Scope tightly.

Always add “Don’t delete anything” unless you specifically want deletions. Even with deletion protection (Claude asks before deleting), it’s better to prevent the request entirely.

Monitor the first few runs of any new workflow. Watch what Claude does. Read the plan. Check the output. Once you trust a workflow, you can step away. But earn that trust first.

Be aware of prompt injection risk. If Claude reads a malicious document or website, hidden instructions could alter its behavior. Don’t point Cowork at untrusted file sources or unfamiliar URLs without reviewing them first.

Track your usage. Cowork consumes significantly more of your allocation than regular chat. Complex, multi-step tasks with subagents are compute-intensive. If you’re hitting limits, batch related work, use “revise section 2 only” instead of “redo everything,” and pre-load context through files instead of re-explaining in chat.

# The pattern behind all 17 practices

If you zoom out, every practice on this list follows the same principle:

Invest in setup. Reduce prompting.

The people struggling with Cowork are writing long, detailed prompts for every task and getting inconsistent results. The people thriving with Cowork spent an afternoon building their context architecture manifest files, global instructions, context files, folder instructions, custom skills and now write ten-word prompts that produce client-ready deliverables.

This is the fundamental shift from ChatGPT-era thinking to Cowork-era thinking. ChatGPT rewarded prompt engineering. Cowork rewards system engineering.

The prompt is the least important part of a Cowork session. The context, the structure, the skills, and the constraints you’ve built around it that’s where the output quality comes from.

As one Substack writer who runs five parallel workflows before breakfast put it: “It feels less like a conversation and more like leaving tasks for a capable coworker.”

That’s the target. Not a chatbot. Not a prompt-and-respond tool. A coworker who already knows your standards, your voice, your projects, and your preferences because you built that knowledge into files it reads every single time.

# Your implementation checklist

Do these in order. Each one compounds on the last.

Today (30 minutes): Create your three context files and set your Global Instructions. This alone puts you ahead of 95% of Cowork users.

This week: Add a \_MANIFEST.md to your most-used project folder. Install two to three plugins that match your role. Set up one scheduled task.

This month: Build your first custom skill for your most repeated workflow. Experiment with subagents on a complex research task. Refine your context files based on output quality.

By the end of month one, you’ll have a Cowork setup that produces higher-quality output in less time than any AI tool you’ve used before.

The difference between Cowork as a toy and Cowork as a system is seventeen practices and about two hours of setup.

The gap between people who know these practices and people who don’t is already massive.

In six months, it’ll be a canyon.