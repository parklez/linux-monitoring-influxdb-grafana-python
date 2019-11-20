# linux-monitoring-influxdb-grafana-python
This is a program that fetches a lot of information from the linux virtual filesystem, such as cpu temperature, ram usage, network traffic, as well as calling a few bash commands such as 'who' and 'ps'. Then writes all information into InfluxDB so that Grafana can render some nice graphics with all that.

<p align="center">
    <img src="https://github.com/parklez/linux-monitoring-influxdb-grafana-python/blob/master/screenshot.png" height="400"/>
</p>

## Dependencies
- Python 3
- influxdb-python [Github link](https://github.com/influxdata/influxdb-python)
- InfluxDB [Offical website](https://www.influxdata.com/get-influxdb/)
- Grafana [Official website](https://grafana.com/get)

## Installation

1. Install all above dependencies.
2. Enable InfluxDB and Grafana services

## Usage
1. Run medidas.py

```bash
python3 medidas.py
```

2. By default, Grafana can be accessed by a browser under 'localhost:3000'.
3. There you may import the layout available in this repository.

## TODO
- A lot of performance improvements, such as creation of threads.
- Some coding changes.

## Contributing
You really don't want to

## License
???
