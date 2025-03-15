# Fortnite Power Ranking Calculator

## Overview

The **Fortnite Power Ranking Calculator** is a simple GUI application that calculates the PR (Power Ranking) gained based on a player's placement in various Fortnite tournaments. The program allows users to select an event, input their ranking, and receive a PR estimate.

## Features

- **User-Friendly Interface**: Built with Tkinter for a simple and interactive experience.
- **Event-Specific PR Calculations**: Adjusts PR gains based on the type of event (e.g., Solo Cash Cup, FNCS Division 1, etc.).
- **Modular Design**: PR calculations are handled separately in `pr_calculation_model.py` to allow for easy future expansion.

## How It Works

1. Select an event from the dropdown menu.
2. Enter your rank for the event.
3. Click "Calculate" to see the PR gained.

## Future Plans

- Implement interpolation for more accurate PR calculations.
- Expand support for additional Fortnite tournaments.
- Improve the UI for better user experience.

## Dependencies

- Python 3.x
- Tkinter (built-in with Python)

## How to Run

1. Clone or download the repository.
2. Run `main.py` using Python:

   ```bash
   python main.py