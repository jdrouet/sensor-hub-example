# Ping monitor

This will allow you to monitor your connection. You can specify your geolocation or it will resolve it with your IP.

## Run it with Docker

```bash
# clone the project
git clone https://github.com/jdrouet/sensor-hub-example.git
cd sensor-hub-example
# build the image
docker build -t sensorhub-ping python-ping
# run the image
docker run -d sensorhub-ping --token PUT_YOUR_TOKEN_HERE
```

## Run it with Python

```bash
# clone the project
git clone https://github.com/jdrouet/sensor-hub-example.git
cd sensor-hub-example
# fetch dependencies
pip install -r requirements.txt
# run the script
python main.py --token PUT_YOUR_TOKEN_HERE
```
