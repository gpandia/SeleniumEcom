import logging

def test_loggingDemo():
    logger=logging.getLogger(__name__)

    fileHandler=logging.FileHandler("logfile.log")
    formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("A warning statement is executed")
    logger.error("A major error has happened")
    logger.critical("A critical statement is executed")