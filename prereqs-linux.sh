#!/bin/bash
sudo apt-get install -y coreutils
curDir=`pwd`
cd /tmp
wget https://raw.githubusercontent.com/vmware-tanzu/carvel-kapp-controller/83fffcfe99a65031b4170813acf94f8d5058b346/hack/dependencies.yml
wget https://raw.githubusercontent.com/vmware-tanzu/carvel-kapp-controller/83fffcfe99a65031b4170813acf94f8d5058b346/hack/install-deps.sh
chmod a+x ./install-deps.sh
./install-deps.sh
cd $curDir
