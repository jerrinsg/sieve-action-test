import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
sieve_root = os.path.dirname(os.path.dirname(os.path.dirname(current)))
sys.path.append(sieve_root)

from sieve_test_driver.test_framework import new_built_in_workload

test_cases = {
    "scale-up-down": new_built_in_workload(60)
    .cmd("kapp deploy --apply-timeout 45m --wait-timeout 45m -y -a cassandra -f https://raw.githubusercontent.com/jerrinsg/sieve-action-test/main/kapp-controller/test/cassandra.yml")
    .wait_for_pod_number("cassandra", 1)
    .wait(60)
    .cmd("kapp deploy --apply-timeout 45m  --wait-timeout 45m -c -y -a cassandra -f https://raw.githubusercontent.com/jerrinsg/sieve-action-test/main/kapp-controller/test/cassandra-scaleup.yml")
    .wait_for_pod_number("cassandra", 2)
    .wait(60)
    .cmd("kapp deploy --apply-timeout 45m --wait-timeout 45m -c -y -a cassandra -f https://raw.githubusercontent.com/jerrinsg/sieve-action-test/main/kapp-controller/test/cassandra.yml")
    .cmd("kubectl delete persistentvolumeclaims cassandra-data-cassandra-1")
    .wait_for_pod_number("cassandra", 1)
    .wait(60)
}
# delete and recreate
# scale up and down
test_cases[sys.argv[1]].run(sys.argv[2])
