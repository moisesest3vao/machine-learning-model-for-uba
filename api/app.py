from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np
import pandas as pd



# Machine Learning Model

# Carregar dados
df = pd.read_csv('user_behavior_expanded_data_v2.csv')

# Separar variáveis independentes (X) e a variável dependente (y)
X = df.drop('compromised', axis=1)
y = df['compromised']

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







# Fast API
app = FastAPI()

class PredictionRequest(BaseModel):
    feature1: float
    feature2: float

@app.post("/predict/")
async def predict(request: PredictionRequest):

    # Exemplo atualizado de novos dados
    new_data = pd.DataFrame({
        'login_location_diff': [1],
        'login_ip_diff': [1],
        'behavior_anomaly': [0],
        'failed_logins': [4],
        'successful_logins': [25],
        'account_age_days': [1200],
        'password_change_freq': [30],
        'suspicious_activity': [1],
        'login_time_diff': [60],
        'access_device_change': [1],
        'email_change': [1],
        'ip_blacklisted': [1],
        'password_strength': [7],
        'account_locked': [1],
        'multiple_failed_logins': [3],
        'unusual_time_logins': [1],
        'login_frequency': [15],
        'suspicious_ips': [2],
        'device_fingerprint_change': [1],
        'high_risk_location': [1],
        'account_role_change': [1],
        'access_time_hours': [10],
        'unusual_login_location': [1],
        'file_access_frequency': [5],
        'unauthorized_app_access': [1],
        'data_exfiltration_attempts': [2],
        'network_anomalies': [1],
        'login_duration': [20],  # Adicionando coluna ausente
        'high_volume_downloads': [2],  # Adicionando coluna ausente
        'unusual_login_ip_range': [1],  # Adicionando coluna ausente
        'multi_factor_auth_enabled': [1],  # Adicionando coluna ausente
        'account_privilege_changes': [0],  # Ajuste com base em dados de treinamento
        'email_forwarding': [1],  # Ajuste com base em dados de treinamento
        'system_alerts_generated': [2],  # Ajuste com base em dados de treinamento
        'remote_access': [0],  # Ajuste com base em dados de treinamento
        'suspicious_file_modifications': [1],  # Ajuste com base em dados de treinamento
        'unusual_file_uploads': [0],  # Ajuste com base em dados de treinamento
        'compromised_device': [1],  # Ajuste com base em dados de treinamento
        'access_to_restricted_areas': [0],  # Ajuste com base em dados de treinamento
        'unusual_account_activity': [1],  # Ajuste com base em dados de treinamento
        'external_links_in_emails': [1],  # Ajuste com base em dados de treinamento
        'data_access_by_role': [2],  # Ajuste com base em dados de treinamento
    })


    try:
        # Realizar a predição
        prediction = clf.predict(new_data)

        # Mostrar a predição
        prediction_proba = clf.predict_proba(new_data)

        # Retornar os resultados
        return {
            "prediction": True if prediction[0] == 1 else False,
            "compromised_probability": f"{prediction_proba[0][1]:.2f}",
            "uncompromised_probability": f"{prediction_proba[0][0]:.2f}"
        }

    except Exception as e:
        # Levantar uma exceção HTTP se estiver usando um framework como FastAPI
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
def read_root():
    return {"message": "Welcome to the LinearSVC model API!"}
