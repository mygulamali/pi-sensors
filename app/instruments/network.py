from prometheus_client import Gauge

from instruments.constants import METRICS_PREFIX
from models.network import Network as Model


class Network:
    received_bytes: Gauge = Gauge(
        f"{METRICS_PREFIX}_network_received_bytes",
        "Number of bytes received by network [bytes]",
        ["name", "address"],
    )
    sent_bytes: Gauge = Gauge(
        f"{METRICS_PREFIX}_network_sent_bytes",
        "Number of bytes sent by network [bytes]",
        ["name", "address"],
    )

    def __init__(self, model: Model):
        labels = {
            "name": model.name,
            "address": model.address,
        }

        self.received_bytes.labels(**labels).set(model.received_bytes)
        self.sent_bytes.labels(**labels).set(model.sent_bytes)
