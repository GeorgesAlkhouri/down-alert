import logging as py_logging

logger = py_logging.getLogger("down-alert")
handler = py_logging.StreamHandler()
formatter = py_logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
