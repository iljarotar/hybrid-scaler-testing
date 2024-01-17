#! /bin/bash

host=$1
headless=$2

if [ -z "$host" ]; then
  host="http://localhost:8080"
fi

echo "starting locust at $host"

locust $headless -H $host -f locustfile.py,combined_load.py
