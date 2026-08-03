from NotebookVideoRenderer.logger import logger
from NotebookVideoRenderer.custom_exception import InvalidURLException

logger.info("This is an info message")

try:
    raise InvalidURLException()
except InvalidURLException as e:
    logger.error(f"Caught an exception: {e}")
