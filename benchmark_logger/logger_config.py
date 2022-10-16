import logging
import os

EXTENSION = ".csv"
DAT_DUMP_DIR = "benchmark_data"

### Setup Logging ###


def create_datadump_dir():
    os.chdir(os.path.dirname(__file__))
    os.chdir("../")
    benchmark_dir = os.path.join(os.getcwd(), DAT_DUMP_DIR)
    return benchmark_dir


def setup_logger(name, filename=None):
    """!
    Returns a logger object for the file.
    @param name Pass the __name__ of the file you desire to setup logging on
    @param filename Name of the logfile you wish to have

    @return logger object
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("""%(message)s""")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    if isinstance(filename, str):
        benchmark_dir = create_datadump_dir()
        filename = filename + EXTENSION
        benchmark_dir = os.path.join(benchmark_dir, filename)
        file_handler = logging.FileHandler(benchmark_dir)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger
