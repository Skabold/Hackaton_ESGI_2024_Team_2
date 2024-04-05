import matplotlib.pyplot as plt

def plot_tx_retard(data_list):
    # Filtrer les valeurs en fonction de la condition y > 0 et < 1 pour rendre la lecture plus digeste
    filtered_list = [y for _, y in data_list if 0 < y < 100]

    

    # Créer des intervalles de valeurs
    intervals = [(round(x * 0.01, 2), round((x + 1) * 0.01, 2)) for x in range(0, 100)]

    # Cumuler les valeurs pour chaque intervalle
    cumul_values = [sum(1 for val in filtered_list if interval[0] <= val < interval[1]) for interval in intervals]

    # Créer les étiquettes des intervalles pour l'axe X
    labels = [f'{interval[0]} - {interval[1]}' for interval in intervals]

    # Trouver l'indice de l'histogramme le plus grand
    max_index = cumul_values.index(max(cumul_values))

    # Ajuster les limites de l'axe des X pour centrer sur l'histogramme le plus grand
    start_index = max(0, max_index - 15)  # Garder 15 intervalles avant l'histogramme le plus grand
    end_index = min(len(labels), max_index + 15)  # Garder 15 intervalles après l'histogramme le plus grand

    # Extraire les valeurs correspondantes à start_index et end_index
    min_val = intervals[start_index][0]
    max_val = intervals[end_index - 1][1]

    # Tracer l'histogramme
    plt.bar(labels[start_index:end_index], cumul_values[start_index:end_index], color='skyblue')

    # Titres et étiquettes
    plt.title(f'Histogramme des valeurs cumulées ({min_val} < y < {max_val})')
    plt.xlabel('Intervalles de valeurs')
    plt.ylabel('Nombre de valeurs')

    # Afficher le graphique
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
