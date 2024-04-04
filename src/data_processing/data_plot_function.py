import matplotlib.pyplot as plt

def plot_tx_retard(data_list):
    # Filtrer les valeurs en fonction de la condition y > 0.35 et < 0.4 pour rendre la lecture plus digeste
    filtered_list = [y for _, y in data_list if 0.40 < y < 0.9]

    # Créer des intervalles de valeurs
    intervals = [(round(x * 0.01, 2), round((x + 1) * 0.01, 2)) for x in range(40, 90)]

    # Cumuler les valeurs pour chaque intervalle
    cumul_values = [sum(1 for val in filtered_list if interval[0] <= val < interval[1]) for interval in intervals]

    # Créer les étiquettes des intervalles pour l'axe X
    labels = [f'{interval[0]} - {interval[1]}' for interval in intervals]

    # Tracer l'histogramme
    plt.bar(labels, cumul_values, color='skyblue')

    # Titres et étiquettes
    plt.title('Histogramme des valeurs cumulées (0.4 < y < 0.9)')
    plt.xlabel('Intervalles de valeurs')
    plt.ylabel('Nombre de valeurs')

    # Afficher le graphique
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
