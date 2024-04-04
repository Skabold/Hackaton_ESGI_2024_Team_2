"""
This module contains the main functions and logic for processing input data.
(You are encouraged to create more intermediate files for processing)
"""

import numpy as np


def calculate_delay_rate(interval, delayed_date, current_date, num_trips):
    """
    Calculate the delay rate based on input parameters.

    Args:
        interval (int or float): The time interval in seconds.
        delayed_date (int or float): Date of the delay (timestamp).
        current_date (int or float): Current date (timestamp).
        num_trips (int): Number of trips.

    Returns:
        float: The delay rate?

    Testing with sample data:
        # Sample data for testing
        interval = 30 * 3600 * 24
        delayed_date = 1712217600
        current_date = 1712244726
        num_trips = 5
    """

    if (current_date - delayed_date) >= interval:
        print(current_date - delayed_date)
        raise RuntimeError("Exception occurred : Wrong refined data")

    delay_rate = np.sum(1 - ((delayed_date - current_date) / interval)) / num_trips

    return delay_rate
