# Research Agent

## Overview
This project implements a research agent using LangChain. The agent can:
- search the web,
- read page content,
- synthesize findings into a structured Markdown report,
- save the report to a file.

The agent works in an interactive CLI mode and supports multi-turn conversation memory within a session.

## Project Structure
```text
research-agent/
├── main.py
├── agent.py
├── tools.py
├── config.py
├── requirements.txt
├── example_output/
│   └── report.md
├── output/
└── README.md
Features

web_search(query: str) — searches the web using DuckDuckGo (ddgs)

read_url(url: str) — extracts main page content using trafilatura, with httpx fallback

write_report(filename: str, content: str) — saves Markdown reports into the output/ directory

interactive CLI via python main.py

memory support with MemorySaver

externalized config and system prompt in config.py

context control by truncating search snippets and page content

Requirements

Install dependencies:

pip install -r requirements.txt
Environment Variables

Create a .env file in the project root:

OPENAI_API_KEY=your_openai_api_key_here

You can also create .env based on .env.example.

Run

Start the interactive agent:

python main.py

Then enter a research query, for example:

Compare naive RAG and parent-child retrieval in a short structured summary.

Type exit or quit to stop the program.

Architecture
config.py

Contains:

settings loaded from .env

model name

limits for search results and page content

system prompt

tools.py

Contains three main tools:

web_search

read_url

write_report

agent.py

Creates:

the OpenAI chat model

the tool list

memory via MemorySaver

the LangChain agent

main.py

Runs the interactive CLI loop, sends user messages to the agent, and prints only the final answer.
Example Output

An example generated report should be placed in:

example_output/report.md

During runtime, generated reports are saved into:

output/
Notes

Some websites may block automatic page extraction and return HTTP 403.

The agent handles such failures gracefully and continues using other sources.

This project uses a practical research workflow suitable for course homework.
