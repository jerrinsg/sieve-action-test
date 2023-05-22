#!/bin/bash
set -x
sudo apt-get install -y coreutils
curDir=`pwd`
cd /tmp
wget https://raw.githubusercontent.com/vmware-tanzu/carvel-kapp-controller/83fffcfe99a65031b4170813acf94f8d5058b346/hack/dependencies.yml
wget https://raw.githubusercontent.com/vmware-tanzu/carvel-kapp-controller/83fffcfe99a65031b4170813acf94f8d5058b346/hack/install-deps.sh
chmod a+x ./install-deps.sh
./install-deps.sh
cd $curDir
echo "# sieve.client v0.0.0
## explicit; go 1.19
sieve.client" >> vendor/modules.txt
ytt -f config/ | kbld -f-
old_tag=$(docker images | grep kbld | awk '{print $2}')
echo $old_tag
docker tag kbld:$old_tag kapp-controller:latest
docker rmi kbld:$old_tag
