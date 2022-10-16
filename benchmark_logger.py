#!/usr/bin/env python3

"""
IMPORTANT:
This script will not be installed. Run from directory.
"""

# Import local files
from benchmark_logger.monitor import Monitor

# Import python libs
import argparse
from datetime import datetime


def main(args):
    """
    Entrypoint of the CLI interface
    """
    monitor_instance = Monitor(fname=args.name)
    monitor_instance.log_all_stats()


if __name__ == "__main__":
    # Create parser
    client_arguments = argparse.ArgumentParser(
        prog="benchmark_logger",
        description="This lets you log the current system info",
        prefix_chars="--",
        add_help=False,
    )

    # Required arguments

    # Optional arguments
    optional_client_arguments = client_arguments.add_argument_group(
        "optional arguments"
    )
    optional_client_arguments.add_argument(
        "-h",
        "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="show this help message and exit",
    )
    # current date and time
    curDT = datetime.now()
    optional_client_arguments.add_argument(
        "--name",
        default=curDT.strftime("%d-%m-%Y-%H-%M-%S"),
        action="store",
        help="Name of the benchmark you are performing",
    )

    # Parse arguments
    args = client_arguments.parse_args()
    main(args)
