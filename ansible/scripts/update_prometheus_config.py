#!/usr/bin/env python

from argparse import ArgumentParser, Namespace
from copy import deepcopy
from typing import Dict
import yaml


JOB_NAME = "pi-sensors"

DEFAULT_HOSTNAME = "localhost"
DEFAULT_PORT = 3000


def parse_args() -> Namespace:
    """Parse command line arguments."""
    parser = ArgumentParser()
    parser.add_argument(
        "--source",
        type=str,
        required=True,
        help="Filename for Prometheus configuration file",
    )
    parser.add_argument(
        "--hostname",
        type=str,
        required=False,
        default=DEFAULT_HOSTNAME,
        help=f"Hostname for {JOB_NAME} scrape target, default: {DEFAULT_HOSTNAME}",
    )
    parser.add_argument(
        "--port",
        type=int,
        required=False,
        default=DEFAULT_PORT,
        help=f"Port for {JOB_NAME} scrape target, default: {DEFAULT_PORT}",
    )

    return parser.parse_known_args()[0]


def read_config(source: str) -> Dict:
    with open(source, "r") as f:
        config = yaml.load(f, Loader=yaml.CLoader)
    return config


def update_config(config: Dict, hostname: str, port: int) -> Dict:
    job_config = job_config_dict(hostname, port)
    job_indices = [
        index
        for index in range(len(config["scrape_configs"]))
        if config["scrape_configs"][index]["job_name"] == JOB_NAME
    ]

    new_config = deepcopy(config)
    if len(job_indices) > 0:
        index = job_indices[0]
        new_config["scrape_configs"][index] = job_config
    else:
        new_config["scrape_configs"].append(job_config)

    return new_config


def job_config_dict(hostname: str, port: int) -> Dict:
    return {
        "job_name": JOB_NAME,
        "static_configs": [
            {
                "targets": [
                    f"{hostname}:{port}",
                ],
            },
        ],
    }


def write_config(config: Dict, source: str) -> None:
    with open(source, "w") as f:
        yaml.dump(config, f)


if __name__ == "__main__":
    args = parse_args()
    config = read_config(args.source)
    updated_config = update_config(config, args.hostname, args.port)
    if updated_config != config:
        write_config(updated_config, args.source)
