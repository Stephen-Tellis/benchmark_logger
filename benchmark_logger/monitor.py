# Import classes and files
from benchmark_logger.logger_config import setup_logger

# Libs
import psutil


class Monitor:
    def __init__(self, fname=None) -> None:
        self.logger = setup_logger(__name__, filename=fname)
        self.logger.info("CPUtmp; CPUfreq; CPUusage; RAMusage; Swapusage;")

    def log_all_stats(self):

        # Get CPU temp
        temps = psutil.sensors_temperatures()["coretemp"]
        temp_cels = [cores[1] for cores in temps]

        # Get CPU freq
        freqs = psutil.cpu_freq(percpu=True)
        freq_ghz = [float("{:.2f}".format(cores[0] / 1000)) for cores in freqs]

        # Get CPU usage
        cpu_perc = psutil.cpu_percent(interval=0.5, percpu=True)

        # Get RAM usage
        ram_perc = psutil.virtual_memory()[2]
        swap_perc = psutil.swap_memory()[3]
        self.logger.info(f"{temp_cels};{freq_ghz};{cpu_perc};{ram_perc};{swap_perc};")
