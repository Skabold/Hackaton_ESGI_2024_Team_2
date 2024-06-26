"""
This module contains the main functions and logic for processing input data.
(You are encouraged to create more intermediate files for processing)
"""

import numpy as np
import os
from dotenv import load_dotenv
import csv
from datetime import datetime

load_dotenv()


def calculate_delay_rate(interval, delayed_date, current_date):
    """
    Calculate the delay rate based on input parameters.

    Args:
        interval (int or float): The time interval in seconds.
        delayed_date (int or float): Date of the delay (timestamp).
        current_date (int or float): Current date (timestamp).

    Returns:
        float: The delay rate
    """
    delayed_date = float(delayed_date)
    current_date = float(current_date)
    if (current_date - delayed_date) >= interval:
        raise RuntimeError("Exception occurred : Wrong refined data")

    delay_rate = 1 - ((current_date - delayed_date) / interval)

    return delay_rate


def train_delay_rate(pathtofile):
    """
    Function to calculate the delay rate for trains based on a CSV file.
    Returns an array with trainId and the corresponding average delay for that train.
    """
    # Load interval from environment variable
    interval = float(os.getenv("INTERVAL"))

    # Get current date and time
    current_date = float(os.getenv("DATE_REF"))

    # Dictionary to store delay sum and number of trips for each train
    train_delays = {}

    # Read CSV file
    with open(pathtofile, "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        next(csvreader)
        for row in csvreader:
            train_id, delayed_date = row
            # Calculate delay rate for this row
            delay_rate = calculate_delay_rate(interval, delayed_date, current_date)
            # Add delay rate to dictionary
            if train_id in train_delays:
                train_delays[train_id].append(delay_rate)
            else:
                train_delays[train_id] = [delay_rate]

    # Calculate average delay for each train
    average_delays = []
    for train_id, rates in train_delays.items():
        average_delay = np.mean(rates) if rates else 0
        average_delays.append((train_id, average_delay))

    return average_delays


def export_train_delay(dr, pathtossave):
    # Specify the output CSV file path
    output_file = pathtossave

    # Write delay rates to CSV
    with open(output_file, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write header
        csvwriter.writerow(["Train ID", "Average Delay"])
        # Write data rows
        for train_id, average_delay in dr:
            csvwriter.writerow([train_id, average_delay])


def one_train_delay_indicator(average_delays, idtrain):
    """
    Function to retrieve the delay indicator for a specific train.
    """
    for train_id, delay in average_delays:
        if train_id == idtrain:
            return delay
    return None


def satisfaction_returns(pathtofile):
    """
    Function to calculate the satisfaction rate for trains based on a CSV file.
    """
    # Load interval from environment variable
    interval = float(os.getenv("INTERVAL"))

    # Get current date and time
    current_date = float(os.getenv("DATE_REF"))

    train_satisfaction = {}

    with open(pathtofile, "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        next(csvreader)
        for row in csvreader:
            train_id, date_satisfaction, satisfaction = row
            if train_id not in train_satisfaction:
                train_satisfaction[train_id] = [0, 0]

            # Calculate delay rate for this row
            train_satisfaction[train_id][0] += int(satisfaction) * (
                1 - ((current_date - float(date_satisfaction)) / interval)
            )
            train_satisfaction[train_id][1] += 1

    satisfactions = []

    for keys in train_satisfaction:
        train_satisfaction[keys][0] = train_satisfaction[keys][0] / (
            train_satisfaction[keys][1] * 3
        )
        satisfactions.append(train_satisfaction[keys][0])

    np.mean(satisfactions)

    return train_satisfaction


def get_satisaction(data, id_str):
    if id_str in data:
        return data[id_str][0]
    else:
        return None


def calculate_train_sum(idTrain, delay_rate, satisfaction_rate):
    tx_r_weight = float(os.getenv("TX_R_WEIGHT"))
    tx_q_weight = float(os.getenv("TX_Q_WEIGHT"))
    tx_s_weight = float(os.getenv("TX_S_WEIGHT"))

    tx_retard = delay_rate
    tx_q = np.random.random()
    tx_s = satisfaction_rate

    if tx_s == 0:
        tx_s = 1

    score = (tx_r_weight * tx_retard) + (tx_q_weight * tx_q)
    score = score / ((tx_r_weight + tx_q_weight) * (tx_s * tx_s_weight))

    print(f"ID Train : {idTrain} \t\t\t SCORE  : {score}")

    print("Computing DONE")
