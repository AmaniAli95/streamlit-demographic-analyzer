# streamlit-demographic-analyzer

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites) 
   - [Installation](#installation)
   - [Usage](#usage)
- [Features](#features)
- [Application Structure](#application-structure)
- [File Structure](#file-structure)

## Overview
The Streamlit Demographic Analyzer is a powerful tool for analyzing demographic data and forecasting registered voter statistics across different categories such as ethnicity and age groups within parliamentary districts. This application empowers users to customize parameters and visualize the impact of various factors on voter turnout and party support.

## Getting Started
### Prerequisites
Before running the application, please ensure that you meet the following prerequisites:
- Python 3.x installed on your system.
- Required Python packages installed (you can install them using `pip install -r requirements.txt`).

### Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/AmaniAli95/streamlit-demographic-analyzer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd streamlit-demographic-analyzer
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
To run the Streamlit application, execute the following command in your terminal within the project directory:
```bash
streamlit run main.py
```

This will start the Streamlit development server, and you can access the application in your web browser at `http://localhost:8501`. Follow the on-screen instructions to select the Parliament, District, and other options for analysis. Customize the sliders for voter turnout and support forecasts to observe their impact on election results.

Follow the on-screen instructions to select the Parliament, District, and other options for analysis. You can customize the sliders for voter turnout and support forecasts to see their impact on the election results.

## Features
- Interactive data visualization powered by Plotly Express.
- Forecast voter statistics segmented by age groups and ethnicities.
- Seamlessly save and update data to Google Sheets for collaborative work.
- Flexibility to select different Parliament and District regions for in-depth analysis.
- Real-time updates based on user input.

## Application Structure
The application is structured into three main Python files:

- `main.py`: Orchestrates the Streamlit app, imports the `ethnic` and age sections, and handles common functionalities.
- `ethnic.py`: Contains code specific to the "Ethnic" section of the application.
- `age.py`: Contains code specific to the "Age" section of the application.

The common functionalities, Google Sheets setup, and other utility functions are defined in `main.py`. The specific section code is kept in `ethnic.py` and `age.py` for modularity

## File Structure
```plaintext
streamlit-demographic-analyzer/
│
├── main.py
├── ethnic.py
├── age.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── parliament_data.csv (store your parliament data in csv)
│   ├── district_data.csv (store your district data in csv)
│   └── ...
│
├── tests/
    ├── test_ethnic.py
    ├── test_age.py
    └── ...
```
