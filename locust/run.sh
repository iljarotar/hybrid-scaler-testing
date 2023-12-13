#! /bin/bash

echo "starting locust"

locust --headless --users 10 --spawn-rate 1 -H $1 -t 60s
