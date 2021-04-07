# Pi-Sensors

A [Prometheus] exporter for the [Enviro] (or [Enviro+]) PHAT on a [Raspberry Pi
Zero]. The exporter itself is a [FastAPI] app. [Ansible] playbooks are used to
deploy the app, as well as setup Prometheus and [Grafana] on the Raspberry Pi
Zero.

## Setup

#### Prerequisites

+ Raspberry Pi Zero (or similar) with a network connection
+ Enviro (or Enviro+) PHAT attached to a Raspberry Pi
+ Python 3.8+
+ [Pipenv]

#### Initialisation

1. Install all the Python packages, pre-commit libraries and copy
   `ansible/hosts.example.yml` to `ansible/hosts.yml`:
   ```
   make init
   ```
1. Open `ansible/hosts.yml` in your text editor and complete the `hosts` and
   `vars` sections according to your setup,
1. Use Ansible to remotely install Prometheus and Grafana, and setup the Enviro
   PHAT, on the Raspberry Pi Zero:
   ```
   make setup
   ```

#### Notes

The Grafana server installed via the Debian repo is not for the ARMv6 chipset
(on the Raspberry Pi Zero). To install a working binary, carry out the following
steps in a terminal on the Raspberry Pi:

1. Download the ARMv6 binaries for Grafana:
   ```
   wget https://dl.grafana.com/oss/release/grafana-7.5.3.linux-armv6.tar.gz
   ```
1. Check the SHA256 checksum to check that the archive is genuine:
   ```
   diff \
       <(sha256sum grafana-7.5.3.linux-armv6.tar.gz | cut -d ' ' -f 1) \
       <(echo "6934fae31682f278cf5dafab4632dd9bced7011ebe77633b46200f85079fd8f4")
   ```
   If there is no result then the archive is genuine.
1. Unpack the binaries:
   ```
   tar -zxvf grafana-7.5.3.linux-armv6.tar.gz \
       grafana-7.5.3/bin/grafana-cli \
       grafana-7.5.3/bin/grafana-server
   ```
1. Backup the original Grafana binaries:
   ```
   sudo mv /usr/sbin/grafana-server /usr/sbin/grafana-server.bak
   sudo mv /usr/sbin/grafana-cli /usr/sbin/grafana-cli.bak
   ```
1. Copy the Grafana binaries for ARMv6:
   ```
   sudo cp grafana-7.5.3/bin/grafana-server /usr/sbin/
   sudo cp grafana-7.5.3/bin/grafana-cli /usr/sbin/
   ```
1. Restart the Grafana service:
   ```
   sudo systemctl restart grafana-server.service
   ```
1. [Optional] Clean up:
   ```
   rm -rf grafana-7.5.3.linux-armv6.tar.gz grafana-7.5.3
   ```

## Deployment

Run `make deploy` to deploy the app to your Raspberry Pi Zero.

## Development server

Run `make serve` to run the app on your local machine. The Prometheus exporter
will then be available at:

    http://localhost:8000/metrics

A JSON version of the metrics will also be available at:

    http://localhost:8000/json

## License

This software is released under the terms and conditions of [The MIT License].
Please see the `LICENSE` file for more details.

[Ansible]: https://www.ansible.com/ "Ansible"
[Enviro+]: https://shop.pimoroni.com/products/enviro?variant=31155658457171 "Enviro+"
[Enviro]: https://shop.pimoroni.com/products/enviro?variant=31155658489939 "Enviro"
[FastAPI]: https://fastapi.tiangolo.com/ "FastAPI"
[Grafana]: https://grafana.com "Grafana"
[Pipenv]: https://pipenv.pypa.io/en/latest/ "Pipenv"
[Prometheus]: https://prometheus.io/ "Prometheus"
[Raspberry Pi Zero]: https://www.raspberrypi.org/products/raspberry-pi-zero/ "Raspberry Pi Zero"
[The MIT License]: http://www.opensource.org/licenses/mit-license.php "The MIT License"
