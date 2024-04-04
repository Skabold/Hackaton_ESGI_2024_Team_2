"""
File: __main__.py

This script serves as the entry point for the project.
It reads input data, performs data processing, and potentially outputs results.
"""

from data_processing.data_processing_function import train_delay_rate


def main():
    # Call the function
    delay_rate = train_delay_rate("data/input/raw.csv")

    # Print the result or do whatever you want with it
    print("Average delay rate:", delay_rate)


if __name__ == "__main__":
    main()
