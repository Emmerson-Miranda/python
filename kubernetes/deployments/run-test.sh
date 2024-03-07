#!/bin/bash
#ifconfig | grep "192.168" 

# creating cluster
kind create cluster --config ./test-cluster.yaml

# setting the environment with a deployment that always will be pending
kubectl apply -f nginx-deployment-success.yaml
kubectl apply -f nginx-deployment-pending.yaml
sleep 10

# python configuration
python3 -m venv venv
. ./venv/bin/activate
pip install --upgrade pip > /dev/null
pip3 install -r requirements.txt > /dev/null

# running python
python3 -m app.main &
sleep 30

# fixing pyton deployment to make it deploy
kubectl apply -f nginx-deployment-pending-fixed.yaml
sleep 20

# finishing
echo "Shell Script Finished!"
kind delete cluster --name test-cluster
