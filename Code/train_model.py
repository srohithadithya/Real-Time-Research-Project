import pandas as pd
import numpy as np
import re
import pickle
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def clean_torque(item):
    res = str(item).replace(".", "").replace(",", "")
    temp = [int(s) for s in re.findall(r'\d+', res)]
    return max(temp) if temp else 0

def clean_mil(item):
    temp = []
    try:
        for s in str(item).split(" "):
            try:
                temp.append(float(s))
            except:
                pass
    except:
        pass
    return max(temp) if temp else 0

def clean_engine_power(item):
    temp = re.findall(r'\d+\.?\d*', str(item))
    return float(temp[0]) if temp else 0

def train():
    print("Loading data...")
    csv_path = "Car details.csv"
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    cars = pd.read_csv(csv_path)
    cars = cars.dropna(how='any')

    print("Cleaning data...")
    # Torque
    cars['torque_rpm'] = cars['torque'].map(clean_torque)
    
    # Mileage
    cars['mil_kmpl'] = cars['mileage'].map(clean_mil)
    
    # Engine CC
    cars['engine_cc'] = cars['engine'].map(clean_engine_power)
    
    # Max Power
    cars['max_power_new'] = cars['max_power'].map(clean_engine_power)

    # Transmission
    cars['transmission'] = cars['transmission'].map(lambda x: 1 if x == 'Manual' else 0)
    
    # Seller Type
    cars['seller_type'] = cars['seller_type'].map(lambda x: 1 if x == 'Individual' else (0 if x == 'Dealer' else -1))
    
    # Fuel
    cars['fuel'] = cars['fuel'].map(lambda x: 1 if x == 'Petrol' else (0 if x == 'Diesel' else -1))

    # Owners (One-hot encoding)
    owners = pd.get_dummies(cars['owner'])
    
    # Combine features
    features = ['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 
                'seats', 'torque_rpm', 'mil_kmpl', 'engine_cc', 'max_power_new']
    
    X = pd.concat([cars[features], owners], axis=1)
    y = cars['selling_price']

    # Ensure all required columns for prediction are present
    required_columns = ['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'seats',
                        'torque_rpm', 'mil_kmpl', 'engine_cc', 'max_power_new',
                        'First Owner', 'Fourth & Above Owner', 'Second Owner', 
                        'Test Drive Car', 'Third Owner']
    
    # Reorder/filter columns to match what the view expects
    X = X[required_columns]

    print("Training Random Forest model...")
    # Using a subset or full data as per notebook logic (notebook used X[:3000] but we can use more if we want)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=300, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    
    score = model.score(X_test, y_test)
    print(f"Model R^2 Score: {score:.4f}")

    # Save model
    model_dir = "mysite/polls"
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "CarSelling.pickle")
    
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train()
