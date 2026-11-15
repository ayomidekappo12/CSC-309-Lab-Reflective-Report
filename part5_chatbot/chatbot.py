"""
CSC 309 - Artificial Intelligence
Part 5 Mini Project: A Basic Chatbot

The chatbot:
  1. Asks the user for their name.
  2. Greets the user by name.
  3. Shows today's date in a readable format.
"""

from datetime import datetime


def get_name():
    """Ask for the user's name and keep asking until something is typed."""
    print("Hello! What is your name?")
    name = input("> ").strip()
    while not name:
        print("Sorry, I didn't catch that. What is your name?")
        name = input("> ").strip()
    return name.title()  # e.g. "alex" -> "Alex"


def today_as_text():
    """Return today's date like 'November 14, 2024'."""
    today = datetime.now()
    return f"{today.strftime('%B')} {today.day}, {today.year}"


def main():
    name = get_name()
    print(f"Nice to meet you, {name}!")
    print(f"Today's date is {today_as_text()}.")


if __name__ == "__main__":
    main()
