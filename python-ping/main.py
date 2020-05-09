import argparse
from ping3 import ping
import requests
from time import sleep

def get_my_ip():
  res = requests.get("https://api.ipify.org?format=json")
  data = res.json()
  return data["ip"]

def get_my_coords(ip):
  res = requests.post("https://www.ipfingerprints.com/scripts/getIPCoordinates.php", data={"ip": ip})
  data = res.json()
  return data["lat"], data["lng"]

def get_headers(args):
  return { "Token": args.token }

def get_tags(args):
  tags = {
    "category": "ping",
    "unit": "second"
  }
  if args.lat is None or args.lng is None:
    ip = get_my_ip()
    tags["lat"], tags["lng"] = get_my_coords(ip)
  else:
    tags["lat"] = args.lat
    tags["lng"] = args.lng
  return tags

def measure(args):
  print("measure")
  return ping(args.target)

def compute(data):
  return {
    "max": max(data),
    "min": min(data),
    "mean": sum(data) / len(data),
  }

def publish(data, tags, headers):
  print("publish", data)
  url = "https://datalab.inyoursaas.io/api/publish"
  body = {
    "tags": tags,
    "fields": data
  }
  requests.post(url, headers=headers, json=body)

def run(args):
  headers = get_headers(args)
  tags = get_tags(args)
  while True:
    measurements = []
    for i in range(round(args.publish_interval / args.ping_interval)):
      measurements.append(measure(args))
      sleep(args.ping_interval)
    publish(compute(measurements), tags, headers)

parser = argparse.ArgumentParser(description='ping monitory')
parser.add_argument('--target', type=str, default="google.com", help='Target of the ping command')
parser.add_argument('--publish-interval', type=int, default=60 * 5, help='interval in second between publishment (min: 5min)')
parser.add_argument('--ping-interval', type=int, default=30, help='interval in second between each ping')
parser.add_argument('--lat', type=float, help='latitude of the sensor')
parser.add_argument('--lng', type=float, help='longitude of the sensor')
parser.add_argument('--token', type=str, required=True, help='token of publisher')

run(parser.parse_args())
