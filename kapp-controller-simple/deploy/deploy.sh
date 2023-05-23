#!/bin/bash
set -x

kapp deploy -y -a kc -f ./release.yml
kapp deploy -y -a default-ns-sa -f https://raw.githubusercontent.com/carvel-dev/kapp-controller/develop/examples/rbac/default-ns.yml
