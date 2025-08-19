import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def visualize(df, anomalies, clusters):
    """PCA ile 2D görselleştirme."""
    X = df.drop('Potability', axis=1)
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    plt.figure(figsize=(10,5))
    plt.scatter(X_pca[:,0], X_pca[:,1], c=df['Potability'], cmap='coolwarm', alpha=0.6)
    plt.title('Potability Dağılımı')
    plt.show()
