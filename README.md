# Trivia Quiz Bot

A Telegram bot that runs a 5-question casino-themed trivia quiz. Users answer via inline buttons (A–D), get scored at the end, and receive a bonus code link if they answer every question correctly.

Built with [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) v20+ (async `Application` API).

## Features

- **`/start`** — Welcome message and question 1
- **5 multiple-choice questions** — Blackjack, poker, roulette, and card-game trivia
- **Inline keyboards** — Tap A, B, C, or D to answer; the bot edits the message for the next question
- **Scoring** — Tracks correct answers across the quiz
- **Perfect score reward** — 5/5 correct shows a bonus code (`BIGQUIZ`) and deposit link
- **Retry or quit** — After the quiz, users can restart or end the conversation

## Requirements

- Python 3.10+
- A Telegram bot token from [@BotFather](https://t.me/BotFather)

## Installation

```bash
# Clone or copy this folder, then:
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install "python-telegram-bot>=20.0"
```

## Configuration

Set your bot token before running. **Do not hardcode it in source** if you plan to share or publish the code.

**Option A — environment variable (recommended)**

```bash
# Windows (PowerShell)
$env:TELEGRAM_BOT_TOKEN="your-token-here"

# macOS / Linux
export TELEGRAM_BOT_TOKEN="your-token-here"
```

In `bot.py`, replace the empty token with:

```python
import os

application = Application.builder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()
```

**Option B — inline (local dev only)**

```python
application = Application.builder().token("your-token-here").build()
```

## Usage

```bash
python bot.py
```

The bot uses **long polling** (not webhooks). Keep the process running while you test.

### Commands

| Command | Description |
|---------|-------------|
| `/start` | Begin (or restart) the quiz |

### Flow

1. User sends `/start`
2. Bot sends welcome text, then question 1 with A/B/C/D buttons
3. Each answer advances to the next question (same message is edited)
4. After question 5, bot shows score and restart/end buttons
5. **5/5 correct** — bonus message with code `BIGQUIZ` and link
6. **Fewer than 5** — score summary and option to try again

## Project layout

```
trivia-quiz-bot/
├── bot.py          # Main bot script (handlers + main)
└── README.md
```

## How it works

- **Conversation states:** `QUESTION1` … `QUESTION5`, then `RESULT`
- **Callback data:** Numeric constants for answers A–D, plus `RESTART` and `END`
- **`user_answers`:** Module-level dict recording whether each question was answered correctly (reset on each `/start`)
- **`ConversationHandler`:** Routes callback queries to the right question handler by state and button pattern

## Customization

| What to change | Where |
|----------------|--------|
| Questions & answers | `questions` and `correct_answers` dicts in `bot.py` |
| Welcome / result text | `start()` and `question_five()` |
| Bonus code & URL | `result_text` in `question_five()` when `correct_count == 5` |
| Number of questions | Add states, handlers, and entries in `questions` / `correct_answers` / `conv_handler` |

## Logging

Logging is enabled at `INFO` level. You’ll see lines when users start the quiz and other handler activity in the console.

## Production notes

- This bot is designed for **polling** (`application.run_polling()`). For production at scale, consider webhooks behind HTTPS.
- Store `TELEGRAM_BOT_TOKEN` in environment variables or a secrets manager.
- The perfect-score flow links to an external gambling site — ensure that matches your compliance and terms of use for your region and audience.

## License

MIT License — you may copy and modify this project if you include the original copyright notice and license text.

```
MIT License

Copyright (c) 2026 Aaron

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
