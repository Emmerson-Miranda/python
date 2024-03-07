from kubernetes import client, config
import time, os, datetime

WAITING_DEPLOYMENTS_NAMESPACE = os.getenv("WAITING_DEPLOYMENTS_NAMESPACE", "default")
WAITING_DEPLOYMENTS_SLEEP_SECS = int(os.getenv("WAITING_DEPLOYMENTS_SLEEP_SECS", "10"))
WAITING_DEPLOYMENTS_CONFIG_FILE = os.getenv("WAITING_DEPLOYMENTS_CONFIG_FILE", "~/.kube/config")

config.load_kube_config(config_file=WAITING_DEPLOYMENTS_CONFIG_FILE)
apis_api = client.AppsV1Api()


def wait_all_deployment_replicas(ns=WAITING_DEPLOYMENTS_NAMESPACE, sleep_secs=WAITING_DEPLOYMENTS_SLEEP_SECS):
    wait_for_all_replicas = True
    loop_counter = 1
    start = datetime.datetime.now()
    while wait_for_all_replicas:
        try:
            resp = apis_api.list_namespaced_deployment(namespace=ns)
            deployments = []
            for n in resp.items:
                if n.status.unavailable_replicas:
                    deployments.append(n.metadata.name)
            if deployments:
                wait_for_all_replicas = True
                print(f"Pending deployments: loop {loop_counter} {deployments}")
                loop_counter = loop_counter + 1
                time.sleep(sleep_secs)
            else:
                wait_for_all_replicas = False
        except:
            time.sleep(sleep_secs)
    time_difference = datetime.datetime.now() - start
    return time_difference


time.sleep(5)
print(f"Finished after {wait_all_deployment_replicas().seconds} seconds")
