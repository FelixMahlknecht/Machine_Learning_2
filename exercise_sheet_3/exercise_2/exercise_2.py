# Import der benötigten Bibliotheken
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.utils import shuffle

# Dataset laden
fashion_mnist = fetch_openml('Fashion-MNIST', version=1, parser='auto')
X, y = fashion_mnist['data'], fashion_mnist['target']

# Train-Test-Split im Verhältnis 80:20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Sicherstellen, dass das Training-Set gemischt wird
X_train, y_train = shuffle(X_train, y_train, random_state=42)

# (a) Zielset anpassen: "Sandal" als True (1) und alle anderen Klassen als False (0)
y_train_binary = (y_train == '5').astype(int)
y_test_binary = (y_test == '5').astype(int)

# (b) Erstellen und Trainieren des SGD-Klassifikators
sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(X_train, y_train_binary)

# (c) Testen des Modells auf neuen Bildern
sample_indices = [0, 1, 2, 3, 4]  # Beispiel-Indices
sample_images = X_test.iloc[sample_indices]
sample_labels = y_test_binary.iloc[sample_indices]

# Vorhersagen anzeigen
predictions = sgd_clf.predict(sample_images)
print("Vorhersagen:", predictions)
print("Echte Labels:", sample_labels.values)

# Genauigkeit des Modells auf dem gesamten Testset anzeigen
accuracy = accuracy_score(y_test_binary, sgd_clf.predict(X_test))
print(f"Genauigkeit auf dem Testset: {accuracy * 100:.2f}%")
