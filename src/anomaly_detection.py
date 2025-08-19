import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM

def detect_anomalies(df, contamination=0.1):
    """Isolation Forest, LOF ve One-Class SVM ile anomali tespiti."""
    X = df.drop('Potability', axis=1)
    results = {}

    iso = IsolationForest(contamination=contamination, random_state=42)
    results['isolation_forest'] = iso.fit_predict(X)

    lof = LocalOutlierFactor(contamination=contamination)
    results['lof'] = lof.fit_predict(X)

    svm = OneClassSVM(gamma='scale', nu=contamination)
    results['one_class_svm'] = svm.fit_predict(X)

    counts = {k: int(np.sum(v == -1)) for k, v in results.items()}
    return results, counts
