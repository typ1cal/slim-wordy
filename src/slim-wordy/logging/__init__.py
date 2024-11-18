# Empty file

import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(modeule)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    Level= logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)  # Output to console as well as log file
    ]
)

logger = logging.getLogger("de-eminemllogger")