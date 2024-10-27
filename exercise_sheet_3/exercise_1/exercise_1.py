# Import der benötigten Bibliotheken
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.datasets import fetch_openml

# Dataset laden
fashion_mnist = fetch_openml('Fashion-MNIST', version=1, parser='auto')


X, y = fashion_mnist['data'], fashion_mnist['target']

# (a) Beschreibung des Datensatzes anzeigen
print(fashion_mnist.DESCR)

# (b) Anzahl der Bilder anzeigen
print(f"Anzahl der Bilder im Datensatz: {X.shape[0]}")

# (c) Größe jedes Bildes anzeigen
print(f"Größe jedes Bildes: {X.shape[1]} Pixel (28x28)")

# (d) Einzelne Instanz anzeigen und Klassifizierung als Text hinzufügen
def plot_single_instance(index):
    image = X.iloc[index].to_numpy().reshape(28, 28)
    label = y.iloc[index]
    plt.imshow(image, cmap="gray")
    plt.title(f"Klassifikation: {label}")
    plt.axis('off')
    plt.show()

# Beispiel: Einzelnes Bild an Index 0 anzeigen
plot_single_instance(0)

# (e) 10x10 Matrix von Bildern darstellen
def plot_image_grid(images, labels, grid_size=10):
    fig, axes = plt.subplots(grid_size, grid_size, figsize=(10, 10))
    axes = axes.flatten()
    for i, ax in enumerate(axes):
        img = images.iloc[i].to_numpy().reshape(28, 28)
        ax.imshow(img, cmap='gray')
        ax.axis('off')
        ax.set_title(labels.iloc[i])
    plt.tight_layout()
    plt.show()

# 10x10 Bildmatrix plotten
plot_image_grid(X, y)

# (f) Erstellen eines 80:20 Train-Test-Splits
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# (g) Sicherstellen, dass der Trainingssatz gemischt wird
X_train, y_train = shuffle(X_train, y_train, random_state=42)

print(f"Trainingsset: {X_train.shape[0]} Bilder")
print(f"Testset: {X_test.shape[0]} Bilder")
