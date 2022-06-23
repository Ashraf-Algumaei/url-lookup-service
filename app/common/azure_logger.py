import logging

from opencensus.ext.azure.log_exporter import AzureLogHandler
from constants import Constants


def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = AzureLogHandler(connection_string=str(Constants.APP_INSIGHTS_CONNECTION_STRING))
    logger.addHandler(handler)
    return logger
