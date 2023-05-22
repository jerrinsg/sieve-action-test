#!/bin/bash
set -x

kubectl apply -f https://raw.githubusercontent.com/jerrinsg/sieve-action-test/main/cassandra-operator/crds.yaml
kubectl apply -f //raw.githubusercontent.com/jerrinsg/sieve-action-test/main/cassandra-operator/bundle.yaml
