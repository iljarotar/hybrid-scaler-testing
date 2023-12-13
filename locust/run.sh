#! /bin/bash

host=$1

if [ -z "$host" ]; then
  host="http://localhost:8080"
fi

echo "starting locust at $host"

locust --headless --users 10 --spawn-rate 1 -H $host -t 60s
