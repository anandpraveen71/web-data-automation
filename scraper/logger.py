import logging
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(BASE_DIR, "app.log")

# Create logger
logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

# Prevent duplicate logs
logger.propagate = False

# File handler (writes to file)
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)

# Format
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add handler
if not logger.handlers:
    logger.addHandler(file_handler)