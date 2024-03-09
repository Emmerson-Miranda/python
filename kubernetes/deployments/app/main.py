import argparse
import datetime
import logging
import time
from kubernetes import client, config

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(funcName)s : %(message)s', handlers=[logging.StreamHandler()])


def wait_for_deployment(namespace, deployment_name, interval_secs, kubeconfig_file, timeout):
    logging.info(f"Starting")
    wait_deployment = True
    loop_counter = 1
    start = datetime.datetime.now()
    config.load_kube_config(config_file=kubeconfig_file)
    apis_api = client.AppsV1Api()
    while wait_deployment:
        try:
            resp = apis_api.read_namespaced_deployment(namespace=namespace, name=deployment_name)
            logging.info(f"Found deployment {deployment_name}: loop {loop_counter} - has {resp.status.available_replicas} replicas available")
            if resp.status.available_replicas:
                wait_deployment = False
                continue
        except client.exceptions.ApiException as ex:
            if ex.status != 404:
                raise ex

        if (interval_secs * loop_counter) > timeout:
            wait_deployment = False
            logging.info(f"Timeout exceed loop {(interval_secs * (loop_counter - 1))} ")
        else:
            logging.info(f"Waiting for {deployment_name}: loop {loop_counter}")
            loop_counter = loop_counter + 1
            time.sleep(interval_secs)
    delta = datetime.datetime.now() - start
    logging.info(f"Finished (time spend {delta})")
    return delta


def wait_all_replicas(namespace, interval_secs, kubeconfig_file, timeout):
    logging.info(f"Starting")
    wait_for_all_replicas = True
    loop_counter = 1
    start = datetime.datetime.now()
    config.load_kube_config(config_file=kubeconfig_file)
    apis_api = client.AppsV1Api()
    while wait_for_all_replicas:
        resp = apis_api.list_namespaced_deployment(namespace=namespace)
        if resp.items:
            deployments = [f"{n.metadata.name}({n.status.unavailable_replicas})" for n in resp.items if n.status.unavailable_replicas or (not n.status.replicas)]
        else:
            deployments = [f"No deployments in namespace {namespace}"]

        if deployments:
            logging.info(f"Pending deployments {len(deployments)}: loop {loop_counter} - {deployments}")
        else:
            wait_for_all_replicas = False

        if (interval_secs * loop_counter) > timeout:
            wait_for_all_replicas = False
            logging.info(f"Timeout loop {(interval_secs * (loop_counter - 1))} ")
            continue
        else:
            loop_counter = loop_counter + 1
            time.sleep(interval_secs)
    delta = datetime.datetime.now() - start
    logging.info(f"Finished (time spend {delta})")
    return delta


def get_cmd_options():
    parser = argparse.ArgumentParser(prog='wait_deployments', description='Wait for deployments to have all replicas ready or exist.', epilog='By Emmerson')
    parser.add_argument("--namespace", "-n", default="default", type=str, help="Namespace to monitor. Default 'default'.")
    parser.add_argument("--interval", "-i", default="10", type=int, help="Verification interval. Default 10 seconds.")
    parser.add_argument("--timeout", "-t", default="300", type=int, help="Timeout waiting for all deployments to be completed. Default 300 seconds.")
    parser.add_argument("--kubeconfig", "-k", default="~/.kube/config", type=str, help="Kubeconfig file. Default '~/.kube/config'.")
    parser.add_argument("--deployment-name", "-dn", default="", type=str, help="Deployment name to wait until it exists. When not provided wait for all deployments to be ready.")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_cmd_options()
    logging.info(f"Arguments: {args}")
    if args.deployment_name:
        res = wait_for_deployment(namespace=args.namespace, interval_secs=args.interval,
                                  timeout=args.timeout, kubeconfig_file=args.kubeconfig,
                                  deployment_name=args.deployment_name)
    else:
        res = wait_all_replicas(namespace=args.namespace, interval_secs=args.interval,
                                timeout=args.timeout, kubeconfig_file=args.kubeconfig)
