import matplotlib.pyplot as plt

def plot_tx_retard(list):

    # Séparer les données en X et Y
    id = [item[0] for item in list]
    val = [item[1] for item in list]

    # Tracer l'histogramme
    plt.bar(id, val, color='skyblue')

    # Titres et étiquettes
    plt.title('Histogramme des valeurs')
    plt.xlabel('Id')
    plt.ylabel('Valeurs')

    # Afficher le graphique
    plt.show()