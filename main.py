"""

from src.mlProject.utils import logger

import logging

logger.info("This is my first custom log")

"""

# we can directly use src also for import as package
# we copy paste the logging code in __init

from mlProject import logger

logger.info("This is the 2nd custom log")