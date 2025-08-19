from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

def perform_clustering(df):
    """KMeans, DBSCAN ve Hierarchical kümeleme."""
    X = df.drop('Potability', axis=1)
    results = {}

    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    labels_kmeans = kmeans.fit_predict(X)
    results['kmeans'] = {
        'labels': labels_kmeans,
        'silhouette': silhouette_score(X, labels_kmeans),
        'calinski': calinski_harabasz_score(X, labels_kmeans),
        'davies': davies_bouldin_score(X, labels_kmeans)
    }

    dbscan = DBSCAN(eps=0.5, min_samples=5)
    labels_dbscan = dbscan.fit_predict(X)
    results['dbscan'] = {'labels': labels_dbscan}

    hierarchical = AgglomerativeClustering(n_clusters=2)
    labels_h = hierarchical.fit_predict(X)
    results['hierarchical'] = {'labels': labels_h}
    return results
