import logging
import os
from datetime import datetime

PROJECT_ROOT_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')

if not os.path.exists(os.path.join(PROJECT_ROOT_DIR, 'logs')):
    os.makedirs(os.path.join(PROJECT_ROOT_DIR, 'logs'))

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
LOG_FILE_PATH = os.path.join(PROJECT_ROOT_DIR, "logs", LOG_FILE)

logging.basicConfig(
    # filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)