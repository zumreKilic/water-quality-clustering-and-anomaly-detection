import pandas as pd
import logging
from config import DATA_PATH

def load_data():
    """Veriyi yükler ve temel bilgileri gösterir."""
    df = pd.read_csv(DATA_PATH)
    logging.info(f"Veri yüklendi: {df.shape}")
    logging.info(f"Sütunlar: {list(df.columns)}")
    logging.info(f"Eksik değerler:\n{df.isnull().sum()}")
    return df
