import logging

def setup_logging():
    """Logging yapılandırması"""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
