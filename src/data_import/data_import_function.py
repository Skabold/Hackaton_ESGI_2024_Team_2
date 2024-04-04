"""
This module contains the main functions and logic for import of data.
(You are encouraged to create more intermediate files for processing)
"""
import pandas as pd
from datetime import datetime, timedelta
import os

def import_train_trajet():
    # Chemin du fichier Excel
    chemin_fichier_data = os.getcwd() + "/data/input/refined/tx_retard.xlsx"

    # Lecture du fichier Excel en spécifiant l'absence d'en-tête
    df = pd.read_excel(chemin_fichier_data, sheet_name="Feuil1", header=None)

    # Ignorer l'en-tête
    df = df.iloc[1:]

    # Filtrage des lignes
    lignes_filtrees = []
    for index,row in df.iterrows():
        date_excel = row[0]
        heure_debut = row[2]
        
        # Calcul de la date et de l'heure pour la comparaison
        date_et_heure_theorique = date_excel + timedelta(hours=heure_debut.hour, minutes=heure_debut.minute)
        date_actuelle = datetime.now()

        # Calcul des timestamps
        timestamp_theorique = date_et_heure_theorique.timestamp()
        timestamp_actuelle = date_actuelle.timestamp()

        # Filtrage des lignes en fonction des timestamps
        diff_date = timestamp_actuelle - timestamp_theorique
        if diff_date < 365*2 * 3600 * 24 :
            id_objet = row[1]  # Supposant que la colonne de l'id de l'objet est la deuxième colonne
            lignes_filtrees.append([id_objet, timestamp_theorique])

    # Création d'un DataFrame à partir des lignes filtrées
    df_filtre = pd.DataFrame(lignes_filtrees, columns=["id", "delayed_date"])

    # Exporter les données filtrées dans un fichier CSV
    chemin_export_csv = os.getcwd() + "/data/output/data_filtre.csv"
    df_filtre.to_csv(chemin_export_csv, index=False, sep=';')

    print("Fichier CSV exporté avec succès.")