"""
File: __main__.py

This script serves as the entry point for the project.
It reads input data, performs data processing, and potentially outputs results.
"""

import sys
from data_import.data_import_function import import_train_trajet
from data_processing.data_processing_function import (
    one_train_delay_indicator,
    train_delay_rate,
)

from data_processing.data_plot_function import plot_tx_retard


def main():
    # Vérification des arguments de la ligne de commande
    if len(sys.argv) == 2 and sys.argv[1] == "import":
        import_train_trajet()
    else:
        # Call the function
        delay_rate = train_delay_rate("data/input/refined/data_filtre.csv")

        # Print the result or do whatever you want with it
        print("Average delay rate:", delay_rate)

        # graph, uncomment if you need it
        # plot_tx_retard(delay_rate)

        # check for a single train
        print()
        print(one_train_delay_indicator(delay_rate, "859660"))


if __name__ == "__main__":
    main()
