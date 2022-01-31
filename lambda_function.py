import logging
import math

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Define a list of Python lambda functions that are called by this AWS Lambda function.
ACTIONS = {
    "increment": lambda x: x + 1,
}


def lambda_handler(event, context):
    logger.info("Event: %s", event)

    result = ACTIONS[event["action"]](event["number"])
    logger.info("Calculated result of %s", result)

    response = {"result": result}
    return response
