import os
import pandas as pd

def merge_csv_files():
    input_folder = os.getcwd() + "/data/input/merge/"
    output_file = os.getcwd() + "/data/input/refined/merged/merged_train_list.csv"

    # Liste tous les fichiers CSV dans le répertoire d'entrée
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

    # Vérifie s'il y a des fichiers à fusionner
    if not csv_files:
        print("Aucun fichier CSV trouvé dans le répertoire.")
        return

    # Charge le premier fichier CSV pour obtenir les colonnes à conserver
    first_file_path = os.path.join(input_folder, csv_files[0])
    first_df = pd.read_csv(first_file_path, delimiter=';', encoding='latin-1', nrows=1)

    # Colonnes à conserver
    columns_to_keep = first_df.columns

    # Fusionne les données des fichiers CSV en ne conservant que les colonnes présentes dans le premier fichier
    merged_df = pd.DataFrame(columns=columns_to_keep)  # Initialise un DataFrame vide avec les colonnes à conserver
    for csv_file in csv_files:
        file_path = os.path.join(input_folder, csv_file)
        df = pd.read_csv(file_path, delimiter=';', usecols=columns_to_keep, encoding='latin-1', on_bad_lines='skip', low_memory=False)  # Utilise seulement les colonnes à conserver
        merged_df = pd.concat([merged_df, df], ignore_index=True)

    # Supprime les lignes vides
    merged_df = merged_df.dropna(how='all')

    # Exporte le fichier fusionné
    merged_df.to_csv(output_file, index=False, sep=';')
    print("Fusion des fichiers CSV terminée. Fichier exporté:", output_file)
