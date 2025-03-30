# Fortnite Power Ranking Calculator

## Overview

The Power Ranking Calculator is a simple GUI application that calculates the PR (Power Ranking) gained based on a player's placement in various Fortnite tournaments. The program allows users to select an event, input their ranking, and receive a PR estimate.

Ideally, an accuracy of at least 95% is to be achieved in all cups. Note that regular linear interpolation models seem to achieve this already.

## Features

- User-Friendly Interface
- Event-Specific PR Calculations
- Modular Design

## Instructions

1. Select an event from the dropdown menu.
2. Enter your rank for the event.
3. Click "Calculate" to see the PR gained.

## Future Plans

- More accurate calculation models beyond linear interpolation 
- Support all PR events, finals/opens clearly distinguished

## Tech Stack

- Python 3.x
- Tkinter (built-in with Python)
- PIL

## Supported Events

- Solo Cash Cup Opens
- Solo Cash Cup Finals
- Performance Evaluation Finals
- FNCS Divisionals (1, 2, 3) - All opens.

## Contribute/Run

1. Clone or download the repository.
2. Run `main.py` using Python:

   ```bash
   python main.py