#!/bin/bash

# creating cluster
kind create cluster --config misc/test-cluster.yaml

# setting the environment with a deployment that always will be pending
echo "------------------------------------------------"
kubectl apply -f misc/nginx-deployment-success.yaml
kubectl apply -f misc/nginx-deployment-pending.yaml
kubectl get deploy

# running python
echo "------------------------------------------------"
python3 -m app.main -i 3 -t 300 &

# fixing deployment to make deploy
kubectl apply -f misc/nginx-deployment-pending-fixed.yaml > /dev/null
python3 -m app.main -i 3 -t 300 -dn nginx-pending

# finishing
sleep 10
kubectl get deploy
kind delete cluster --name test-cluster

#kubectl wait po -l app=nginx-success --for=condition=Ready --timeout=60s
#kubectl wait deploy/nginx-pending --for='jsonpath={.status.conditions[?(@.type=="Available")].status}=True' --timeout=60s
