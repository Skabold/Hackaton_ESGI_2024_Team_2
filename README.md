# ESGI / SNCF Hackathon 2024 - Team 2

## Project Overview

This project is developed by the Team 2 of "ESGI Hackathon 2024" for SNCF. The aim of this project is to implement a solution to detect spikes in users'tension to take proactive measures and prevent crises (e.g., potential PR disasters).

## Folder Structure

- **data/input**: Contains input data for the project.
- **data/output**: Contains output data for the project.
- **src**: Contains the source code for the project.
  
## How to Run

To launch the project, follow these steps:

1. Ensure you have Python 3.9.2 installed on your system.
2. Clone or download this repository.
3. Navigate to the project directory in your terminal.
4. Install dependencies using `pip install -r requirements.txt`.
5. Run the project using `python3 src/main.py`.

## How to use our project ?

1. First, you need to import your xlsx file into **/data/input/tx_retard.xlsx**. Next, run `python3 src/main.py import`. This command generates a refined CSV file from the xlsx file, which can be found in **/data/input/refined/data_filtre.csv**.
2. After that, you'll need to rerun the script to generate the graph for the refined data using `python3 src/main.py`.

## Update

Feel free to customize this README with additional information or specific instructions as needed for your project.
