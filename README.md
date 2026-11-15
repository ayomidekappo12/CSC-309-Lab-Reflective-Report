# CSC 309 – Artificial Intelligence: Lab Part 5

**Mini Project: Building a Basic Chatbot**

A simple Python chatbot that:

1. Asks the user for their name.
2. Responds with a personalised greeting.
3. Displays the current date in a readable format (e.g. "Today's date is November 14, 2024").

## Requirements

- Python 3.x
- No external packages (uses only the built-in `input()` function and the `datetime` module)

## Project structure

```
.
├── README.md
└── part5_chatbot/
    ├── chatbot.py          # The chatbot program
    └── output/
        └── sample_run.txt  # Output captured from running the program
```

## How to run

```bash
cd part5_chatbot
python chatbot.py
```

## Sample output

```
Hello! What is your name?
> Alex
Nice to meet you, Alex!
Today's date is November 14, 2026.
```

The full captured run is in [`part5_chatbot/output/sample_run.txt`](part5_chatbot/output/sample_run.txt).

## How it works

| Step | Code used |
| --- | --- |
| Read the user's name | `input()`, with `.strip()` to remove spaces and a loop that asks again if the name is blank |
| Personalised greeting | f-string: `f"Nice to meet you, {name}!"`, with `.title()` to capitalise the name |
| Current date | `datetime.now()`, formatted with `strftime('%B')` for the month name |
