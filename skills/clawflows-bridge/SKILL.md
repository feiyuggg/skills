---
name: clawflows-bridge
description: Bridge capability declarations for clawflows automation compatibility in this workspace.
provides:
  - capability: file_system
  - capability: notifications
  - capability: web_fetch
  - capability: shell
  - capability: http
  - capability: web-search
  - capability: rss-reader
  - capability: llm-analysis
---

# ClawFlows Bridge

This local skill provides capability mapping metadata so `clawflows` can validate and run automations in this workspace.

It is a compatibility shim and does not add new executable tools by itself.
