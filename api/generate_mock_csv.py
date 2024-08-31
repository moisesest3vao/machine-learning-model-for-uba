import pandas as pd
import numpy as np

# Definindo o número de amostras
n_samples = 1000

# Gerando dados fictícios
np.random.seed(42)  # Para reprodutibilidade

data = {
    'login_location_diff': np.random.randint(0, 2, size=n_samples),
    'login_ip_diff': np.random.randint(0, 2, size=n_samples),
    'behavior_anomaly': np.random.randint(0, 2, size=n_samples),
    'failed_logins': np.random.poisson(2, size=n_samples),
    'successful_logins': np.random.poisson(20, size=n_samples),
    'account_age_days': np.random.randint(0, 3650, size=n_samples),
    'password_change_freq': np.random.randint(30, 365, size=n_samples),
    'suspicious_activity': np.random.randint(0, 2, size=n_samples),
    'login_time_diff': np.random.exponential(30, size=n_samples),
    'access_device_change': np.random.randint(0, 2, size=n_samples),
    'email_change': np.random.randint(0, 2, size=n_samples),
    'ip_blacklisted': np.random.randint(0, 2, size=n_samples),
    'password_strength': np.random.randint(1, 11, size=n_samples),
    'account_locked': np.random.randint(0, 2, size=n_samples),
    'multiple_failed_logins': np.random.poisson(1, size=n_samples),
    'unusual_time_logins': np.random.randint(0, 2, size=n_samples),
    'login_frequency': np.random.poisson(10, size=n_samples),
    'suspicious_ips': np.random.poisson(1, size=n_samples),
    'device_fingerprint_change': np.random.randint(0, 2, size=n_samples),
    'high_risk_location': np.random.randint(0, 2, size=n_samples),
    'account_role_change': np.random.randint(0, 2, size=n_samples),
    'access_time_hours': np.random.poisson(5, size=n_samples),
    'unusual_login_location': np.random.randint(0, 2, size=n_samples),
    'file_access_frequency': np.random.poisson(3, size=n_samples),
    'unauthorized_app_access': np.random.randint(0, 2, size=n_samples),
    'data_exfiltration_attempts': np.random.poisson(1, size=n_samples),
    'network_anomalies': np.random.randint(0, 2, size=n_samples),
    'login_duration': np.random.exponential(20, size=n_samples),
    'high_volume_downloads': np.random.poisson(2, size=n_samples),
    'unusual_login_ip_range': np.random.randint(0, 2, size=n_samples),
    'multi_factor_auth_enabled': np.random.randint(0, 2, size=n_samples),
    'account_privilege_changes': np.random.randint(0, 2, size=n_samples),
    'email_forwarding': np.random.randint(0, 2, size=n_samples),
    'system_alerts_generated': np.random.poisson(2, size=n_samples),
    'remote_access': np.random.randint(0, 2, size=n_samples),
    'suspicious_file_modifications': np.random.poisson(1, size=n_samples),
    'unusual_file_uploads': np.random.randint(0, 2, size=n_samples),
    'compromised_device': np.random.randint(0, 2, size=n_samples),
    'access_to_restricted_areas': np.random.randint(0, 2, size=n_samples),
    'unusual_account_activity': np.random.randint(0, 2, size=n_samples),
    'external_links_in_emails': np.random.poisson(1, size=n_samples),
    'data_access_by_role': np.random.poisson(2, size=n_samples),
    'compromised': np.random.randint(0, 2, size=n_samples)  # Variável alvo
}

df = pd.DataFrame(data)

# Salvando em CSV
df.to_csv('user_behavior_expanded_data_v2.csv', index=False)
