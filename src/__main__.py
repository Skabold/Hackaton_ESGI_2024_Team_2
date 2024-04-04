"""
File: __main__.py

This script serves as the entry point for the project.
It reads input data, performs data processing, and potentially outputs results.
"""

from data_processing.data_processing_function import calculate_delay_rate


def main():
    # Sample data for testing
    interval = 30 * 3600 * 24
    delayed_date = 1712217600
    current_date = 1712244726
    num_trips = 5

    # Call the function
    try:
        delay_rate = calculate_delay_rate(
            interval, delayed_date, current_date, num_trips
        )
        print("Delay Rate:", delay_rate)
    except RuntimeError as e:
        print("Error occurred:", e)


if __name__ == "__main__":
    main()
