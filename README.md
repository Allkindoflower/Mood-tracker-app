Mood Tracker

A simple command-line mood tracking app in Python. It lets you log your mood multiple times per day with timestamps, and review your mood history whenever you want.

How it works:

    When you run it, it asks for commands:

        mood: lets you enter how you’re feeling right now. It saves your mood with the date and time.

        view: shows all the moods you’ve logged so far.

        help: shows the commands you can use.

        clear: clears the screen.

        quit: exits the app.

    Each mood entry is saved to a text file called mood_history.txt in the same folder as the script, so your logs stick around between sessions.

    It stores date, hour, minute, and your mood, so you can track how your feelings change during the day.

Tech notes:

    Uses Python’s datetime module for timestamps.

    Uses simple file reading/writing to store moods.

    Runs in a loop until you type quit.

    Works on Windows, macOS, and Linux (clears screen accordingly).
