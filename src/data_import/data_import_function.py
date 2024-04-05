"""
This module contains the main functions and logic for import of data.
(You are encouraged to create more intermediate files for processing)
"""

import pandas as pd
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import csv

load_dotenv()

def import_train_satisfaction():
    chemin_fichier_entree =  os.getcwd() + "/data/input/satisfaction.csv"
    chemin_fichier_sortie =os.getcwd() + "/data/input/refined/satisfaction.csv"

    # Ouvrir le fichier CSV en mode lecture
    with open(chemin_fichier_entree, newline='') as fichier_entree:
        lecteur_csv = csv.reader(fichier_entree)
        
        # Ignorer la première ligne (entête)
        next(lecteur_csv)
        
        # Récupérer et traiter les données
        donnees_sortie = []
        for ligne in lecteur_csv:
            premiere_colonne = ligne[0]
            deuxieme_colonne_timestamp = datetime.strptime(ligne[1], '%d/%m/%Y').timestamp()
            quatrieme_colonne = ligne[3]
            donnees_sortie.append([premiere_colonne, deuxieme_colonne_timestamp, quatrieme_colonne])

    # Écrire les données dans un nouveau fichier CSV avec un délimiteur ";"
    with open(chemin_fichier_sortie, mode='w', newline='') as fichier_sortie:
        writer = csv.writer(fichier_sortie, delimiter=';')
        writer.writerows(donnees_sortie)
    print("Fichier satisfaction CSV exporté avec succès.")
    

def import_train_trajet():
    interval = float(os.getenv("INTERVAL"))
    # Chemin du fichier Excel
    chemin_fichier_data = os.getcwd() + "/data/input/tx_retard.xlsx"

    # Lecture du fichier Excel en spécifiant l'absence d'en-tête
    df = pd.read_excel(chemin_fichier_data, sheet_name="Feuil1", header=None)

    # Ignorer l'en-tête
    df = df.iloc[1:]

    # Filtrage des lignes
    lignes_filtrees = []
    for index, row in df.iterrows():
        date_excel = row[0]
        heure_debut = row[2]

        # Calcul de la date et de l'heure pour la comparaison
        date_et_heure_theorique = date_excel + timedelta(
            hours=heure_debut.hour, minutes=heure_debut.minute
        )
        date_actuelle_str = os.getenv("DATE_REF")
        date_actuelle = datetime.fromtimestamp(float(date_actuelle_str))

        # Calcul des timestamps
        timestamp_theorique = date_et_heure_theorique.timestamp()
        timestamp_actuelle = date_actuelle.timestamp()

        # Filtrage des lignes en fonction des timestamps
        diff_date = timestamp_actuelle - timestamp_theorique
        if diff_date < interval:
            id_objet = row[
                1
            ]  # Supposant que la colonne de l'id de l'objet est la deuxième colonne
            lignes_filtrees.append([id_objet, timestamp_theorique])

    # Création d'un DataFrame à partir des lignes filtrées
    df_filtre = pd.DataFrame(lignes_filtrees, columns=["id", "delayed_date"])

    # Exporter les données filtrées dans un fichier CSV
    chemin_export_csv = os.getcwd() + "/data/input/refined/data_filtre.csv"
    df_filtre.to_csv(chemin_export_csv, index=False, sep=";")

    print("Fichier taux de retard CSV exporté avec succès.")


def get_train_list():
    chemin_fichier_data = os.getcwd() + "/data/input/refined/data_filtre.csv"

    train_list = []
    df = pd.read_csv(chemin_fichier_data, header=None, sep=';')  # Ignore l'en-tête

    for index, row in df.iloc[1:].iterrows():  # Ignorer la première ligne (l'en-tête)
        id_objet = row[0]
        if id_objet not in train_list:
            train_list.append(id_objet)

    return train_list