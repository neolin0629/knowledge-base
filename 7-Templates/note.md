<%*
const today = tp.date.now("YYYY-MM-DD");
const area = await tp.system.prompt("归属（如 Investing/Quant，可留空）", "");
-%>
---
title: <% tp.file.title %>
created: <% today %>
updated: <% today %>
tags: []
area: <% area %>
status: draft
links: []

---

# <% tp.file.title %>


