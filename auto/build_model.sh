#!/bin/bash 

cd $(dirname $0)/..

docker-compose run --rm dev build_model.py 
