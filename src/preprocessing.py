import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    """Eksik değer doldurma ve ölçekleme."""
    imputer = SimpleImputer(strategy='median')
    features = df.drop('Potability', axis=1)
    target = df['Potability']
    features_imputed = pd.DataFrame(imputer.fit_transform(features), columns=features.columns)
    scaler = StandardScaler()
    features_scaled = pd.DataFrame(scaler.fit_transform(features_imputed), columns=features.columns)
    features_scaled['Potability'] = target.values
    return features_scaled
