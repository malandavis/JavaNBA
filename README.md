# NBA Spread and Over/Under Outcome Predictor

## Overview

This project is designed to predict NBA (National Basketball Association) game outcomes, specifically focusing on predicting point spreads and Over/Under totals. It utilizes an HTML parser to gather data on the current day's games and odds from a designated source. The application then performs calculations based on this data and generates predictions, which are saved to a text file. Additionally, the project offers an option to read in an entire season's games and results from a CSV file, enabling simulation and testing of different strategies.

## Features

- **HTML Parsing:** The project scrapes data from an HTML source to retrieve up-to-date information on NBA games and odds.

- **Prediction Generation:** The application utilizes collected data to generate predictions for point spreads and Over/Under totals.

- **Output to Text File:** Predictions are saved to a text file, making them easily accessible and reviewable.

- **Season Simulation:** You can input an entire season's games and results from a CSV file, allowing for the simulation of entire NBA seasons.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/) (version X.X.X)
- Libraries listed in `requirements.txt`

### Installation

1. Clone the repository to your local machine.

```bash
git clone https://github.com/yourusername/nba-predictor.git
cd nba-predictor
