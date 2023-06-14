import logging

from aerosense_tools.queries import BigQuery
from octue.log_handlers import apply_log_handler


apply_log_handler()
logger = logging.getLogger(__name__)


def extract_and_add_new_measurement_sessions(request):
    """Extract new measurement sessions from the sensor data table and add them to the sessions table.

    :param dict event: Google Cloud event
    :param google.cloud.functions.Context context: metadata for the event
    :return None:
    """
    BigQuery().extract_and_add_new_measurement_sessions()
    return "ok"
