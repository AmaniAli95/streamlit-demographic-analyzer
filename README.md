# streamlit-demographic-analyzer

This Streamlit application analyzes demographic data and provides forecasts for registered voters in different categories (ethnicity and age groups) for parliamentary districts. It allows users to adjust parameters and visualize the impact of various factors on the voter turnout and support for a specific party.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Application Structure](#application-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

This Streamlit application is designed to analyze demographic data and provide insights into registered voters' demographics and voting behavior in parliamentary districts. It includes two main sections: Ethnic and Age groups. Users can select a category and a specific district to analyze. The application offers the following features:

- Selection of Parliament and District to analyze.
- Visualization of registered voters by ethnicity or age group.
- Customizable sliders for voter turnout and support forecasts.
- Real-time forecasts of voter support for a specific party.
- Data saving and updating to Google Sheets for future reference.

## Prerequisites

Before running the application, make sure you have the following prerequisites:

- Python 3.x installed on your system.
- Required Python packages installed (you can install them using `pip install -r requirements.txt`).

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/AmaniAli95/streamlit-GPS-ethnic.git
   ```
2. Navigate to the project directory:
   ```bash
   cd streamlit-GPS-ethnic
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the Streamlit application, execute the following command in your terminal within the project directory:
```bash
streamlit run main.py
```

This will start the Streamlit development server, and you can access the application in your web browser at `http://localhost:8501`.

Follow the on-screen instructions to select the Parliament, District, and other options for analysis. You can customize the sliders for voter turnout and support forecasts to see their impact on the election results.

## Application Structure
The application is structured into three main Python files:

- `main.py`: Orchestrates the Streamlit app, imports the `ethnic` and age sections, and handles common functionalities.
- `ethnic.py`: Contains code specific to the "Ethnic" section of the application.
- `age.py`: Contains code specific to the "Age" section of the application.
The common functionalities, Google Sheets setup, and other utility functions are defined in `main.py`. The specific section code is kept in `ethnic.py` and `age.py` for modularity.

## Contributing
Contributions are welcome! If you would like to improve this application or add new features, please open an issue or create a pull request.
