"""
File: __main__.py

This script serves as the entry point for the project.
It reads input data, performs data processing, and potentially outputs results.
"""

import sys
from data_import.data_import_function import (
    import_train_trajet,
    import_train_satisfaction,
)
from data_processing.data_processing_function import (
    export_train_delay,
    one_train_delay_indicator,
    train_delay_rate,
)

from data_processing.data_plot_function import plot_tx_retard


def main():
    # Vérification des arguments de la ligne de commande
    if len(sys.argv) == 2 and sys.argv[1] == "import":
        import_train_trajet()
        import_train_satisfaction()
    else:
        # Call the function
        delay_rate = train_delay_rate("data/input/refined/data_filtre.csv")

        # Print the result or do whatever you want with it
        # print("Average delay rate:", delay_rate)

        # graph, uncomment if you need it$
        # plot_tx_retard(delay_rate, "taux de retards")

        # check for a single train
        # print()
        # print(one_train_delay_indicator(delay_rate, "859660"))

        # export for apo in case we do an ia :
        # export_train_delay(delay_rate, "data/output/train_delay_indicator.csv")


if __name__ == "__main__":
    main()
