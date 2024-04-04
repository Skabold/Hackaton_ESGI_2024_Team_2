"""
This module contains the main functions and logic for processing input data.
(You are encouraged to create more intermediate files for processing)
"""

import numpy as np
import os
import csv
import datetime


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

    if (current_date - delayed_date) >= interval:
        print(current_date - delayed_date)
        raise RuntimeError("Exception occurred : Wrong refined data")

    delay_rate = 1 - ((delayed_date - current_date) / interval)

    return delay_rate


def train_delay_rate(pathtofile):
    """
    Function to calculate the delay rate for trains based on a CSV file.
    """
    # Load interval from environment variable
    interval = float(os.getenv("INTERVAL"))

    # Get current date and time
    current_date = datetime.now().timestamp()

    # Initialize variables
    delay_sum = 0
    num_trips = 0

    # Dictionary to store delay rates for each train
    delay_rates = {}

    # Read CSV file
    with open(pathtofile, "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        for row in csvreader:
            train_id, delayed_date = row
            # Calculate delay rate for this row
            delay_rate = calculate_delay_rate(interval, delayed_date, current_date)
            # Add delay rate to dictionary
            if train_id in delay_rates:
                delay_rates[train_id].append(delay_rate)
            else:
                delay_rates[train_id] = [delay_rate]

    # Calculate total delay sum and number of trips
    for train_id, rates in delay_rates.items():
        delay_sum += np.sum(rates)
        num_trips += len(rates)

    # Calculate average delay rate
    if num_trips > 0:
        average_delay_rate = delay_sum / num_trips
    else:
        average_delay_rate = 0

    return average_delay_rate
