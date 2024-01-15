#! /bin/bash

host=$1
headless=$2

if [ -z "$host" ]; then
  host="http://localhost:8080"
fi

echo "starting locust at $host"

locust $headless -H $host -f locustfile.py,irregular_load.py
locust $headless -H $host -f locustfile.py,high_load.py
locust $headless -H $host -f locustfile.py,steady_load.py
