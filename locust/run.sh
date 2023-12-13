#! /bin/bash

echo "starting locust"

locust --headless --users 10 --spawn-rate 1 -H http://localhost:8080 -t 60s
