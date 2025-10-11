# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Guidelines for writing code

Please:
- Keep the code as short, minimal, and concise as possible. 
- No comments, except for things that are really important and hard to get otherwise.
- Take as long as you need, iterating to make it really simple and short and cutting out fluff.
- Run ruff checks on your code after every major addition or update.

## Git

Make commits for every major change that you make. Exercise your own judgement on what constitutes a major change, but in general try not to go overboard.

## Package Management Commands

Use these commands:

- Install dependencies: `uv add <package>`
- Remove dependencies: `uv remove <package>`
- Sync dependencies: `uv sync`

## Running Python Code

- Run a Python script with `uv run <script-name>.py`
- Run Python tools like Pytest with `uv run pytest` or `uv run ruff`