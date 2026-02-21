# ClawFlows Bridge Capability Pack

Provides: file_system, notifications, web_fetch, shell, http, web-search, rss-reader, llm-analysis
Skill: clawflows-bridge

## Methods

### fetchRSS
**How to fulfill:**
Use an RSS fetch path (e.g., `web_fetch` tool or compatible RSS source), normalize items to `{title, link, score?}`.

### search
**How to fulfill:**
Use web/news search and return array items shaped like `{title, url}`.

### summarize
**How to fulfill:**
Use an LLM summarizer over provided `input/articles` and return `{summary}` or text.

### GET
**How to fulfill:**
Perform HTTP GET for provided URL and return response body text.

### run
**How to fulfill:**
Execute shell command in configured project path and capture stdout.

### notify
**How to fulfill:**
Send notification text to configured channel/session.
