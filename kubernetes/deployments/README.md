# Introduction
This python code waits until all replicas in of all deployments in a namespace are satisfied.

The ``run-test.sh`` script:
- Create a KinD cluster.
- Deploy two nginx:
  - The first will be deployed successfully. 
  - The second deployment will never finish because it use a nodeSelector to a node that not exists.
- Run the python application that will wait until all deployments are ready.
- After 30 seconds patch the second deployment to fix it.
- Python app detect the change and finish.
- Destroy KinD cluster.

# Help
```
% python3 -m app.main -h 
usage: wait_deployments [-h] [--namespace NAMESPACE] [--interval INTERVAL] [--timeout TIMEOUT] [--kubeconfig KUBECONFIG] [--deployment-name DEPLOYMENT_NAME]

Wait for deployments to have all replicas ready or exist.

options:
  -h, --help            show this help message and exit
  --namespace NAMESPACE, -n NAMESPACE
                        Namespace to monitor. Default 'default'.
  --interval INTERVAL, -i INTERVAL
                        Verification interval. Default 10 seconds.
  --timeout TIMEOUT, -t TIMEOUT
                        Timeout waiting for all deployments to be completed. Default 300 seconds.
  --kubeconfig KUBECONFIG, -k KUBECONFIG
                        Kubeconfig file. Default '~/.kube/config'.
  --deployment-name DEPLOYMENT_NAME, -dn DEPLOYMENT_NAME
                        Deployment name to wait until it exists. When not provided wait for all deployments to be ready.

By Emmerson
```

## wait_all_replicas
Wait until all deployments are working in a given namespace.
```bash
python3 -m app.main -i 3 -t 300
```

## wait_for_deployment
Wait one given deployment is available (e.g. deployment name nginx-pending).
```bash
python3 -m app.main -i 3 -t 300 -dn nginx-pending
```


## log
The execution log:

```
% make run 
./run-test.sh
Creating cluster "test-cluster" ...
...
------------------------------------------------
deployment.apps/nginx-success created
deployment.apps/nginx-pending created
NAME            READY   UP-TO-DATE   AVAILABLE   AGE
nginx-pending   0/1     0            0           0s
nginx-success   0/1     0            0           0s
------------------------------------------------
2024-03-09 16:46:35,755 <module> : Arguments: Namespace(namespace='default', interval=3, timeout=300, kubeconfig='~/.kube/config', deployment_name='')
2024-03-09 16:46:35,755 wait_all_replicas : Starting
2024-03-09 16:46:35,777 wait_all_replicas : Pending deployments 2: loop 1 - ['nginx-pending(None)', 'nginx-success(None)']
2024-03-09 16:46:35,856 <module> : Arguments: Namespace(namespace='default', interval=3, timeout=300, kubeconfig='~/.kube/config', deployment_name='nginx-pending')
2024-03-09 16:46:35,856 wait_for_deployment : Starting
2024-03-09 16:46:35,877 wait_for_deployment : Found deployment nginx-pending: loop 1 - has None replicas available
2024-03-09 16:46:35,877 wait_for_deployment : Waiting for nginx-pending: loop 1
2024-03-09 16:46:38,785 wait_all_replicas : Pending deployments 2: loop 2 - ['nginx-pending(None)', 'nginx-success(None)']
2024-03-09 16:46:38,887 wait_for_deployment : Found deployment nginx-pending: loop 2 - has None replicas available
2024-03-09 16:46:38,887 wait_for_deployment : Waiting for nginx-pending: loop 2
2024-03-09 16:46:41,795 wait_all_replicas : Pending deployments 2: loop 3 - ['nginx-pending(None)', 'nginx-success(None)']
2024-03-09 16:46:41,897 wait_for_deployment : Found deployment nginx-pending: loop 3 - has None replicas available
2024-03-09 16:46:41,898 wait_for_deployment : Waiting for nginx-pending: loop 3
2024-03-09 16:46:44,803 wait_all_replicas : Pending deployments 2: loop 4 - ['nginx-pending(None)', 'nginx-success(None)']
2024-03-09 16:46:44,909 wait_for_deployment : Found deployment nginx-pending: loop 4 - has None replicas available
2024-03-09 16:46:44,909 wait_for_deployment : Waiting for nginx-pending: loop 4
2024-03-09 16:46:47,813 wait_all_replicas : Pending deployments 2: loop 5 - ['nginx-pending(4)', 'nginx-success(1)']
2024-03-09 16:46:47,917 wait_for_deployment : Found deployment nginx-pending: loop 5 - has None replicas available
2024-03-09 16:46:47,918 wait_for_deployment : Waiting for nginx-pending: loop 5
2024-03-09 16:46:50,824 wait_all_replicas : Pending deployments 2: loop 6 - ['nginx-pending(4)', 'nginx-success(1)']
2024-03-09 16:46:50,927 wait_for_deployment : Found deployment nginx-pending: loop 6 - has None replicas available
2024-03-09 16:46:50,927 wait_for_deployment : Waiting for nginx-pending: loop 6
2024-03-09 16:46:53,835 wait_all_replicas : Pending deployments 2: loop 7 - ['nginx-pending(4)', 'nginx-success(1)']
2024-03-09 16:46:53,935 wait_for_deployment : Found deployment nginx-pending: loop 7 - has None replicas available
2024-03-09 16:46:53,935 wait_for_deployment : Waiting for nginx-pending: loop 7
2024-03-09 16:46:56,844 wait_all_replicas : Pending deployments 2: loop 8 - ['nginx-pending(4)', 'nginx-success(1)']
2024-03-09 16:46:56,944 wait_for_deployment : Found deployment nginx-pending: loop 8 - has None replicas available
2024-03-09 16:46:56,944 wait_for_deployment : Waiting for nginx-pending: loop 8
2024-03-09 16:46:59,853 wait_all_replicas : Pending deployments 2: loop 9 - ['nginx-pending(4)', 'nginx-success(1)']
2024-03-09 16:46:59,953 wait_for_deployment : Found deployment nginx-pending: loop 9 - has None replicas available
2024-03-09 16:46:59,953 wait_for_deployment : Waiting for nginx-pending: loop 9
2024-03-09 16:47:02,862 wait_all_replicas : Pending deployments 1: loop 10 - ['nginx-pending(2)']
2024-03-09 16:47:02,961 wait_for_deployment : Found deployment nginx-pending: loop 10 - has 2 replicas available
2024-03-09 16:47:02,961 wait_for_deployment : Finished (time spend 0:00:27.104677)
2024-03-09 16:47:08,877 wait_all_replicas : Finished (time spend 0:00:33.122158)
NAME            READY   UP-TO-DATE   AVAILABLE   AGE
nginx-pending   4/4     4            4           38s
nginx-success   1/1     1            1           38s
Deleting cluster "test-cluster" ...
Deleted nodes: ["test-cluster-control-plane"]
```
