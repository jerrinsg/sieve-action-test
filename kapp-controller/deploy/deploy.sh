#!/bin/bash
set -x

kapp deploy -y -a kc -f ./release.yml
kapp deploy -y -a cluster-admin-rbac -f https://raw.githubusercontent.com/carvel-dev/kapp-controller/develop/examples/rbac/cluster-admin.yml
