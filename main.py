from src.utils import setup_logging
from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.anomaly_detection import detect_anomalies
from src.clustering import perform_clustering
from src.visualization import visualize
from src.report import generate_report
from config import CONTAMINATION

def main():
    setup_logging()
    df = load_data()
    df_processed = preprocess_data(df)
    anomalies, anomaly_counts = detect_anomalies(df_processed, contamination=CONTAMINATION)
    clusters = perform_clustering(df_processed)
    visualize(df_processed, anomalies, clusters)
    generate_report(anomaly_counts, clusters)

if __name__ == "__main__":
    main()
