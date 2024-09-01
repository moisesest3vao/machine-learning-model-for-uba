import config.config as config
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

clf = None

def initialize_model():
    global clf  # Declare clf as global to modify it within the function

    # Carregar dados
    df = pd.read_csv(config.get_training_csv_path())

    # Separar variáveis independentes (X) e a variável dependente (y)
    X = df.drop(config.get_y(), axis=1)
    y = df[config.get_y()]

    # Dividir os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Criar o modelo
    clf = DecisionTreeClassifier()

    # Treinar o modelo
    clf.fit(X_train, y_train)

    # Fazer previsões
    y_pred = clf.predict(X_test)

    # Avaliar o modelo
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)
