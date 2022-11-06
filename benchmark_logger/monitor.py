#!/usr/bin/env python3

# Import classes and files
from benchmark_logger.logger_config import setup_logger

# Libs
import psutil


class Monitor:
    def __init__(self, fname=None) -> None:
        self.logger = setup_logger(__name__, filename=fname)
        numcores = psutil.cpu_count()
        tempr_col = "CPUtmp; " * numcores
        freq_col = "CPUfreq; " * numcores
        self.logger.info(f"{tempr_col}{freq_col}CPUusage; RAMusage; Swapusage;")

    def log_all_stats(self, interval= 0.5):
        # Get CPU temp
        temps = psutil.sensors_temperatures()["coretemp"]
        temp_cels = str([cores[1] for cores in temps])

        # Get CPU freq
        freqs = psutil.cpu_freq(percpu=True)
        freq_ghz = str([float("{:.2f}".format(cores[0] / 1000)) for cores in freqs])

        # Get CPU usage
        cpu_perc = str(psutil.cpu_percent(interval=interval, percpu=True))

        # Get RAM usage
        ram_perc = psutil.virtual_memory()[2]
        swap_perc = psutil.swap_memory()[3]

        # Log stats
        self.logger.info(
            f"{temp_cels[1:-1]};{freq_ghz[1:-1]};{cpu_perc[1:-1]};{ram_perc};{swap_perc};"
        )

