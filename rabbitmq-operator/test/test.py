import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
sieve_root = os.path.dirname(os.path.dirname(os.path.dirname(current)))
sys.path.append(sieve_root)

from sieve_test_driver.test_framework import new_built_in_workload
from sieve_common.common import RUNNING, TERMINATED

test_cases = {
    "recreate": new_built_in_workload()
    .cmd("kubectl apply -f examples/rabbitmq-operator/test/rmqc-1.yaml")
    .wait_for_pod_status("rabbitmq-cluster-server-0", RUNNING)
    .cmd("kubectl delete RabbitmqCluster rabbitmq-cluster")
    .wait_for_pod_status("rabbitmq-cluster-server-0", TERMINATED)
    .cmd("kubectl apply -f examples/rabbitmq-operator/test/rmqc-1.yaml")
    .wait_for_pod_status("rabbitmq-cluster-server-0", RUNNING),
}

test_cases[sys.argv[1]].run(sys.argv[2])
