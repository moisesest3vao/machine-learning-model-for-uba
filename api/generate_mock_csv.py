import pandas as pd
import numpy as np
import random
from faker import Faker

# Initialize Faker for generating realistic data
fake = Faker()

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define the number of records
num_records = 100

# Generate features
def generate_data(num_records):
    data = []
    for _ in range(num_records):
        # Randomly decide if the account is compromised
        compromised = random.choices([0, 1], weights=[0.8, 0.2])[0]  # 80% non-compromised, 20% compromised
        
        # Generate features based on the compromised status
        if compromised:
            failed_login_attempts = np.random.poisson(10)
            last_login_time = fake.date_time_this_year()
            login_location_changes = np.random.poisson(5)
            num_transactions = np.random.poisson(20)
            transaction_amounts = np.random.normal(500, 300, num_transactions).tolist()
            device_fingerprint_changes = np.random.poisson(5)
            ip_addresses = fake.ipv4()
            account_age = np.random.randint(1, 5)  # 1 to 5 years
            password_changes = np.random.poisson(5)
            two_factor_auth = 0
            suspicious_activity_alerts = np.random.poisson(5)
            account_balance_changes = np.random.normal(1000, 500)
        else:
            failed_login_attempts = np.random.poisson(2)
            last_login_time = fake.date_time_this_year()
            login_location_changes = np.random.poisson(1)
            num_transactions = np.random.poisson(5)
            transaction_amounts = np.random.normal(200, 100, num_transactions).tolist()
            device_fingerprint_changes = np.random.poisson(1)
            ip_addresses = fake.ipv4()
            account_age = np.random.randint(1, 10)  # 1 to 10 years
            password_changes = np.random.poisson(1)
            two_factor_auth = 1
            suspicious_activity_alerts = np.random.poisson(1)
            account_balance_changes = np.random.normal(2000, 300)

        # Append the generated row to the data list
        data.append([
            failed_login_attempts,
            last_login_time,
            login_location_changes,
            num_transactions,
            np.mean(transaction_amounts) if transaction_amounts else 0,
            device_fingerprint_changes,
            ip_addresses,
            account_age,
            password_changes,
            two_factor_auth,
            suspicious_activity_alerts,
            account_balance_changes,
            compromised
        ])
    
    return data

# Create DataFrame
columns = [
    'Failed_Login_Attempts', 'Last_Login_Time', 'Login_Location_Changes',
    'Number_of_Transactions', 'Average_Transaction_Amount',
    'Device_Fingerprint_Changes', 'IP_Address', 'Account_Age',
    'Password_Changes', '2FA_Status', 'Suspicious_Activity_Alerts',
    'Account_Balance_Changes', 'Compromised'
]

data = generate_data(num_records)
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('banking_account_compromise_data.csv', index=False)

print("CSV file 'banking_account_compromise_data.csv' has been created.")
